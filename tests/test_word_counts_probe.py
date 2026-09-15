import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class WordCountProbe(unittest.TestCase):
    def test_probe_promoted_word_counts(self):
        counts = {}
        for slot in ["010", "014", "015", "016", "017", "018", "019", "020"]:
            text = (ROOT / f"manuscript/records/{slot}/current.md").read_text(encoding="utf-8")
            lines = text.splitlines()
            body = "\n".join(lines[4:]) if len(lines) >= 4 else text
            counts[slot] = {
                "split_all": len(text.split()),
                "split_body": len(body.split()),
            }
        self.fail(json.dumps(counts, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
