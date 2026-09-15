import json
import unittest
from pathlib import Path

from scripts.check_repo import validate

ROOT = Path(__file__).resolve().parents[1]


class RepoContractTests(unittest.TestCase):
    def test_repository_validator_is_green(self):
        self.assertEqual(validate(), [])

    def test_project_exposes_distinct_story_and_rehearsal_frontiers(self):
        project = json.loads((ROOT / "PROJECT.json").read_text(encoding="utf-8"))
        self.assertEqual(project["frontiers"]["story"], "r079")
        self.assertEqual(project["frontiers"]["reference_quality_through"], "r010")
        self.assertEqual(project["frontiers"]["rehearsal_target"], "r011")
        self.assertEqual(project["frontiers"]["next_new"], "r080")
        self.assertEqual(project["default_mode"], "rehearsal")

    def test_manifest_owns_order_and_quality_state(self):
        manifest = json.loads((ROOT / "manuscript" / "manifest.json").read_text(encoding="utf-8"))
        records = manifest["records"]
        self.assertEqual(len(records), 79)
        self.assertEqual(records[0]["id"], "r001")
        self.assertEqual(records[-1]["id"], "r079")
        self.assertTrue(all(r["prose_status"] == "reference" for r in records[:10]))
        self.assertTrue(all(r["prose_status"] in {"needs_rehearsal", "restored"} for r in records[10:]))
        self.assertTrue(all(r["published"] for r in records[:12]))
        self.assertTrue(all(not r["published"] for r in records[12:]))

    def test_reader_is_single_runtime_surface_and_audio_aware(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("manuscript/manifest.json", html)
        self.assertIn("audio/manifest.json", html)
        self.assertIn("work=1", html)
        self.assertNotIn("records/001.html", html)
        self.assertFalse((ROOT / "records").exists())

    def test_reference_audio_is_public_and_library_first(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        audio = json.loads((ROOT / "audio" / "manifest.json").read_text(encoding="utf-8"))
        self.assertTrue(all(audio["records"][f"r{i:03d}"]["status"] == "published" for i in range(1, 13)))
        self.assertIn('id="audioLibrary"', html)
        self.assertIn("Audio Library", html)
        self.assertIn("duration_seconds", html)

    def test_autoplay_next_is_user_controlled_and_persistent(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="autoplayNext"', html)
        self.assertIn("3l.autoplayNext", html)
        self.assertIn("localStorage", html)
        self.assertIn("addEventListener('ended'", html)

    def test_audio_start_precedes_async_prose_fetch(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        play = html.index("if(startPlayback&&canUseAudio(current))")
        prose_fetch = html.index("const prose=await fetch(current.path")
        self.assertLess(play, prose_fetch)

    def test_agent_handshake_keeps_archive_cold(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8").lower()
        self.assertIn("project.json", agents)
        self.assertIn("current.md", agents)
        self.assertIn("development/archive", agents)
        project = json.loads((ROOT / "PROJECT.json").read_text(encoding="utf-8"))
        hot = project["modes"]["rehearsal"]["read_first"]
        self.assertFalse(any("archive" in path for path in hot))


if __name__ == "__main__":
    unittest.main()
