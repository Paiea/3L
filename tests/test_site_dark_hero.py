from pathlib import Path
import unittest


class DarkHeroPresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = Path("index.html").read_text(encoding="utf-8")

    def test_uses_new_ithar_hero_art(self):
        self.assertIn('src="visual/1212.png"', self.html)
        self.assertIn('content="https://paiea.github.io/3L/visual/1212.png"', self.html)

    def test_hero_is_single_full_bleed_scene_with_overlay(self):
        self.assertIn('.story-hero{position:relative;', self.html)
        self.assertIn('.story-hero-art{position:absolute;inset:0;', self.html)
        self.assertIn('.story-hero-overlay{position:relative;', self.html)

    def test_dark_site_palette_uses_cold_blue_sparingly(self):
        self.assertIn('color-scheme:dark', self.html)
        self.assertIn('--paper:#11100e', self.html)
        self.assertIn('--ink:#eee7db', self.html)
        self.assertIn('--accent:#5ba8d1', self.html)

    def test_overlay_copy_is_restrained(self):
        self.assertIn('3L · Record 001', self.html)
        self.assertIn('Six days up.', self.html)
        self.assertIn('The first thing Ithar calls him is food.', self.html)
        self.assertNotIn('This version is built to listen first', self.html)


if __name__ == "__main__":
    unittest.main()
