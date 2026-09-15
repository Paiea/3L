import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTING_DIR = ROOT / "audio" / "routing"


class AudioRoutingTests(unittest.TestCase):
    def _assert_record_contract(self, config_path):
        from scripts.audio_route import build_plan

        slot = config_path.stem.removeprefix("record-")
        source_path = ROOT / f"manuscript/records/{slot}/current.md"
        self.assertTrue(source_path.is_file(), f"missing current prose for routing config {config_path.name}")

        source = source_path.read_text(encoding="utf-8")
        config = json.loads(config_path.read_text(encoding="utf-8"))

        self.assertEqual(config.get("record"), slot)
        self.assertEqual(config.get("routing_mode"), "exact_quote_locked")
        self.assertEqual(config.get("voices"), {"greg": "deep", "ithar": "normal"})
        self.assertLessEqual(int(config.get("max_chars", 480)), 480)
        self.assertGreaterEqual(int(config.get("pause_ms", {}).get("speaker_handoff", 0)), 1100)

        forbidden_routing_keys = {
            "timestamp",
            "timestamps",
            "timecode",
            "timecodes",
            "start_time",
            "end_time",
            "start_ms",
            "end_ms",
            "start_seconds",
            "end_seconds",
        }

        def walk_keys(value):
            if isinstance(value, dict):
                for key, child in value.items():
                    yield key
                    yield from walk_keys(child)
            elif isinstance(value, list):
                for child in value:
                    yield from walk_keys(child)

        bad_keys = sorted({key for key in walk_keys(config) if key.lower() in forbidden_routing_keys})
        self.assertEqual(bad_keys, [], f"timestamp-like routing metadata is forbidden: {bad_keys}")

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

    def test_every_prepared_record_is_discovered_and_enforced(self):
        configs = sorted(ROUTING_DIR.glob("record-*.json"))
        self.assertTrue(configs, "at least one audio routing config must exist")
        for config_path in configs:
            with self.subTest(config=config_path.name):
                self._assert_record_contract(config_path)

    def test_project_handshake_points_audio_jobs_to_the_contract(self):
        project = json.loads((ROOT / "PROJECT.json").read_text(encoding="utf-8"))
        production = project.get("production", {})
        self.assertEqual(production.get("audio_contract"), "audio/README.md")
        self.assertEqual(production.get("audio_routing_mode"), "exact_quote_locked")

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

    def test_straight_quotes_can_be_locked_to_ithar(self):
        from scripts.audio_route import build_plan

        source = '## RECORD 999\n\n## TEST\n\nI waited.\n\n"And your shoulder?"\n\n"It improved."\n'
        config = {
            "record": "999",
            "routing_mode": "exact_quote_locked",
            "voices": {"greg": "deep", "ithar": "normal"},
            "max_chars": 480,
            "pause_ms": {"speaker_handoff": 1100},
            "dragon_quotes": [
                {"text": '"And your shoulder?"', "occurrence": 1}
            ],
        }

        plan = build_plan(source, config)
        routed = [(s["speaker"], s["transcript"]) for s in plan["segments"]]
        dragon = "".join(text for speaker, text in routed if speaker == "ithar")
        greg = "".join(text for speaker, text in routed if speaker == "greg")

        self.assertEqual(dragon, '"And your shoulder?"')
        self.assertIn('"It improved."', greg)
        self.assertFalse(plan["uses_timestamps_for_speaker_assignment"])

    def test_record_without_ithar_routes_entire_body_to_greg(self):
        from scripts.audio_route import build_plan

        source = "## RECORD 999\n\n## TEST\n\nI worked.\n\n“Human dialogue.”\n\nThen I went home.\n"
        config = {
            "record": "999",
            "routing_mode": "exact_quote_locked",
            "voices": {"greg": "deep", "ithar": "normal"},
            "max_chars": 480,
            "pause_ms": {"speaker_handoff": 1100},
            "dragon_quotes": [],
        }

        plan = build_plan(source, config)

        self.assertEqual({segment["speaker"] for segment in plan["segments"]}, {"greg"})
        self.assertEqual("".join(segment["transcript"] for segment in plan["segments"]), plan["audio_body"])


if __name__ == "__main__":
    unittest.main()
