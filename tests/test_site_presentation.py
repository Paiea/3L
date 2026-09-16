import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SitePresentationTests(unittest.TestCase):
    def setUp(self):
        self.html = (ROOT / "index.html").read_text(encoding="utf-8")

    def test_hero_is_cinematic_editorial_not_split_card(self):
        self.assertIn(".story-hero-art{aspect-ratio:3/1", self.html)
        self.assertIn("grid-template-areas", self.html)
        self.assertNotIn("grid-template-columns:minmax(0,1.18fr)", self.html)

    def test_hero_and_social_preview_use_optimized_local_asset(self):
        self.assertIn("visual/3l1.webp", self.html)
        self.assertNotIn("dragon-bargain.png", self.html)
        self.assertTrue((ROOT / "visual" / "3l1.webp").exists())

    def test_nhal_is_an_inset_visual_with_only_the_approved_caption(self):
        self.assertIn(".nhal-card{max-width:34rem", self.html)
        self.assertIn("aspect-ratio:3/2", self.html)
        self.assertIn("object-fit:contain", self.html)
        self.assertIn("<figcaption>Nhal · The Bound One</figcaption>", self.html)
        self.assertNotIn("Deeper in the record", self.html)
        self.assertIn("visual/3l2.webp", self.html)
        self.assertTrue((ROOT / "visual" / "3l2.webp").exists())

    def test_hero_controls_are_restrained_not_pill_heavy(self):
        self.assertIn(".hero-actions a{", self.html)
        self.assertIn("border-radius:6px", self.html)
        self.assertNotIn(".hero-actions a{display:inline-flex;align-items:center;justify-content:center;min-height:2.85rem;padding:.62rem 1rem;border-radius:999px", self.html)


if __name__ == "__main__":
    unittest.main()
