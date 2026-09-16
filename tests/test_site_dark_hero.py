from pathlib import Path
import unittest


class DarkHeroPresentationTests(unittest.TestCase):
    """Presentation contract for the dark 3L landing hero."""

    @classmethod
    def setUpClass(cls):
        cls.html = Path("index.html").read_text(encoding="utf-8")

    def test_uses_current_ithar_hero_art(self):
        self.assertIn('src="visual/3L%20site.png"', self.html)
        self.assertIn('content="https://paiea.github.io/3L/visual/3L%20site.png"', self.html)

    def test_art_is_preserved_as_a_clean_widescreen_plate(self):
        self.assertIn('.story-hero-art{position:relative;aspect-ratio:16/9;', self.html)
        self.assertIn('.story-hero-art img{width:100%;height:100%;object-fit:cover;', self.html)
        self.assertIn('filter:none', self.html)
        self.assertNotIn('.story-hero-art:after', self.html)

    def test_copy_lives_in_an_editorial_band_below_the_art(self):
        self.assertIn('.story-hero-copy{position:relative;z-index:2;', self.html)
        self.assertIn('margin:-2.25rem auto 0', self.html)
        self.assertIn('class="hero-title-block"', self.html)
        self.assertIn('class="hero-detail"', self.html)
        self.assertNotIn('story-hero-overlay', self.html)

    def test_dark_site_palette_uses_cold_blue_sparingly(self):
        self.assertIn('color-scheme:dark', self.html)
        self.assertIn('--paper:#11100e', self.html)
        self.assertIn('--ink:#eee7db', self.html)
        self.assertIn('--accent:#5ba8d1', self.html)

    def test_hero_copy_remains_restrained(self):
        self.assertIn('3L · Record 001', self.html)
        self.assertIn('Six days up.', self.html)
        self.assertIn('The first thing Ithar calls him is food.', self.html)
        self.assertNotIn('This version is built to listen first', self.html)

    def test_hero_identifies_greg_as_peg_leg_greg(self):
        self.assertIn('B-Class Named Ranker', self.html)
        self.assertIn('Designation: Peg-Leg Greg', self.html)
        self.assertIn('class="hero-identity"', self.html)

    def test_mobile_band_stacks_without_covering_the_art(self):
        self.assertIn('@media(max-width:760px)', self.html)
        self.assertIn('.story-hero-copy{grid-template-columns:1fr;', self.html)
        self.assertIn('margin:-1.15rem .7rem 0', self.html)


if __name__ == "__main__":
    unittest.main()
