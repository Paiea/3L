import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepoContractTests(unittest.TestCase):
    def test_project_router_declares_reference_frontier_and_resolvable_context(self):
        project = json.loads((ROOT / "PROJECT.json").read_text(encoding="utf-8"))
        self.assertEqual(project["project"], "3L")
        self.assertEqual(project["canon_frontier"], 10)
        self.assertEqual(project["active_record"], 11)
        self.assertEqual(project["published_through"], 10)
        self.assertEqual(project["canonical_record_template"], "manuscript/records/{record:03d}/canonical.md")
        for relative in project["read_first"] + project["deep_context_if_needed"]:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_initial_canonical_frontier_is_exactly_records_001_through_010(self):
        records = ROOT / "manuscript" / "records"
        canonical = sorted(records.glob("[0-9][0-9][0-9]/canonical.md"))
        self.assertEqual([p.parent.name for p in canonical], [f"{n:03d}" for n in range(1, 11)])
        self.assertFalse((records / "011" / "canonical.md").exists())

    def test_authority_and_revision_rules_are_explicit(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        versioning = (ROOT / "manuscript" / "VERSIONING.md").read_text(encoding="utf-8")
        self.assertIn("canonical.md", readme)
        self.assertIn("canonical prose wins", readme.lower())
        self.assertIn("versions/", versioning)
        self.assertIn("drafts/", versioning)
        self.assertIn("superseded", versioning.lower())

    def test_reader_is_one_runtime_markdown_surface_without_generated_record_pages_or_audio(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("PROJECT.json", html)
        self.assertIn("canonical.md", html)
        self.assertIn("URLSearchParams", html)
        self.assertNotIn("<audio", html.lower())
        self.assertNotRegex(html, re.compile(r"records/\d{3}\.html"))
        generated = list(ROOT.glob("records/[0-9][0-9][0-9].html"))
        self.assertEqual(generated, [])

    def test_reader_css_exists_as_the_only_required_static_asset(self):
        self.assertTrue((ROOT / "assets" / "reader.css").is_file())


if __name__ == "__main__":
    unittest.main()
