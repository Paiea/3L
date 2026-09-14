import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREPARED_RECORDS = ("001", "002", "003", "004", "005")


class AudioRoutingTests(unittest.TestCase):
    def _assert_record_contract(self, slot):
        from scripts.audio_route import build_plan

        source_path = ROOT / f"manuscript/records/{slot}/current.md"
        config_path = ROOT / f"audio/routing/record-{slot}.json"
        self.assertTrue(config_path.is_file(), f"missing exact routing config for Record {slot}")

        source = source_path.read_text(encoding="utf-8")
        config = json.loads(config_path.read_text(encoding="utf-8"))
        plan = build_plan(source, config)
        segments = plan["segments"]

        self.assertEqual(plan["source_sha256"], hashlib.sha256(source_path.read_bytes()).hexdigest())
        self.assertTrue(segments)
        self.assertEqual("".join(s["transcript"] for s in segments), plan["audio_body"])
        self.assertTrue(all(len(s["transcript"]) <= config.get("max_chars", 480) for s in segments))
        self.assertTrue(all(s["voice_id"] == ("deep" if s["speaker"] == "greg" else "normal") for s in segments))

        for left, right in zip(segments, segments[1:]):
            if left["speaker"] != right["speaker"]:
                self.assertGreaterEqual(left["pause_after_ms"], config["pause_ms"]["speaker_handoff"])

        self.assertEqual(plan["routing_mode"], "exact_quote_locked")
        self.assertFalse(plan["uses_timestamps_for_speaker_assignment"])

    def test_prepared_records_are_quote_locked_and_preview_safe(self):
        for slot in PREPARED_RECORDS:
            with self.subTest(record=slot):
                self._assert_record_contract(slot)

    def test_duplicate_quotes_can_be_locked_by_exact_occurrence(self):
        from scripts.audio_route import build_plan

        source = "## RECORD 999\n\n## TEST\n\n“Hi.”\n\n“Yes.”\n\nI waited.\n\n“Yes.”\n\nDone.\n"
        config = {
            "record": "999",
            "routing_mode": "exact_quote_locked",
            "voices": {"greg": "deep", "ithar": "normal"},
            "max_chars": 480,
            "pause_ms": {"speaker_handoff": 1100},
            "dragon_quotes": [
                {"text": "“Yes.”", "occurrence": 2}
            ],
        }

        plan = build_plan(source, config)
        routed = [(s["speaker"], s["transcript"]) for s in plan["segments"]]
        dragon = "".join(text for speaker, text in routed if speaker == "ithar")
        greg = "".join(text for speaker, text in routed if speaker == "greg")

        self.assertEqual(dragon, "“Yes.”")
        self.assertIn("“Hi.”\n\n“Yes.”", greg)
        self.assertFalse(plan["uses_timestamps_for_speaker_assignment"])


if __name__ == "__main__":
    unittest.main()
