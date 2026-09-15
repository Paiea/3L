import json
import unittest
from pathlib import Path
from collections import defaultdict

from scripts.audio_route import manuscript_body, quoted_spans

ROOT = Path(__file__).resolve().parents[1]


def quote_probe(slot, start_marker, end_marker):
    source = (ROOT / f"manuscript/records/{slot}/current.md").read_text(encoding="utf-8")
    body = manuscript_body(source)
    found = list(quoted_spans(body))
    counts = defaultdict(int)
    out = []
    for index, (start, end, quote) in enumerate(found, start=1):
        counts[quote] += 1
        if body.find(start_marker) <= start < body.find(end_marker):
            out.append({
                "quote_index": index,
                "occurrence": counts[quote],
                "text": quote,
            })
    return out


class QuoteLockProbe(unittest.TestCase):
    def test_probe_mixed_voice_quotes(self):
        result = {
            "017": quote_probe("017", "The cave returned around me", "The memory took me back to the table."),
            "020": quote_probe("020", "Nothing happened that year.", "I closed my eyes."),
        }
        self.fail(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    unittest.main()
