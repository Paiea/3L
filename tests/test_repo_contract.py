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
        self.assertEqual(project["frontiers"]["restored_through"], "r010")
        self.assertEqual(project["frontiers"]["rehearsal_target"], "r011")
        self.assertEqual(project["frontiers"]["next_new"], "r080")
        self.assertEqual(project["default_mode"], "rehearsal")

    def test_manifest_owns_order_and_current_quality_state(self):
        manifest = json.loads((ROOT / "manuscript" / "manifest.json").read_text(encoding="utf-8"))
        records = manifest["records"]
        self.assertEqual(len(records), 79)
        self.assertEqual(records[0]["id"], "r001")
        self.assertEqual(records[-1]["id"], "r079")
        self.assertTrue(all(r["prose_status"] == "reference" for r in records[:10]))
        self.assertTrue(all(r["prose_status"] == "restored" for r in records[10:13]))
        self.assertTrue(all(r["prose_status"] == "needs_rehearsal" for r in records[13:]))
        self.assertTrue(all(r["published"] for r in records[:10]))
        self.assertTrue(all(not r["published"] for r in records[10:]))

    def test_reader_is_single_runtime_surface_and_audio_aware(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("manuscript/manifest.json", html)
        self.assertIn("audio/manifest.json", html)
        self.assertIn("work=1", html)
        self.assertNotIn("records/001.html", html)
        self.assertFalse((ROOT / "records").exists())

    def test_work_reader_can_preview_candidate_audio_without_publication(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("status==='candidate'", html)
        self.assertIn("working", html)
        audio = json.loads((ROOT / "audio" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(audio["records"]["r002"]["status"], "candidate")
        self.assertEqual(audio["records"]["r002"]["src"], "audio/assets/record-002-quote-locked-v2.mp3")

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
