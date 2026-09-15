#!/usr/bin/env python3
"""Build deterministic, quote-locked audio routing plans from canonical prose.

Speaker ownership comes only from exact quoted manuscript text. When identical
quotes repeat, a lock may name the exact 1-based occurrence of that quote.
Timestamps are not accepted as routing input. Canonical prose is never modified.
"""

import hashlib
import json
import re
import sys
from pathlib import Path


def manuscript_body(source: str) -> str:
    """Return prose after the first two markdown H2 headings."""
    matches = list(re.finditer(r"^##\s+.+?$", source, flags=re.MULTILINE))
    if len(matches) < 2:
        raise ValueError("manuscript must contain record and title headings")
    body = source[matches[1].end():]
    return body.lstrip("\r\n")


def quoted_spans(text: str):
    """Yield (start, end, exact_quote) for curly-quoted spans.

    Paragraphs inside one speech may repeat the opening curly quote without a
    closing quote. The next closing curly quote ends the full spoken span.
    """
    pos = 0
    while True:
        start = text.find("“", pos)
        if start < 0:
            return
        end = text.find("”", start + 1)
        if end < 0:
            raise ValueError(f"unclosed curly quote beginning at offset {start}")
        end += 1
        yield start, end, text[start:end]
        pos = end


def split_exact(text: str, limit: int):
    """Split without changing a byte of text, preferring paragraph boundaries."""
    if limit < 80:
        raise ValueError("max_chars is unrealistically small")
    out = []
    remaining = text
    while len(remaining) > limit:
        window = remaining[:limit]
        cut = window.rfind("\n\n")
        if cut >= max(40, limit // 3):
            cut += 2
        else:
            cut = window.rfind(" ")
            if cut < max(40, limit // 3):
                cut = limit
            else:
                cut += 1
        out.append(remaining[:cut])
        remaining = remaining[cut:]
    if remaining:
        out.append(remaining)
    return out


def _resolve_dragon_indices(found_quotes, locks):
    """Return indices of quoted spans explicitly owned by Ithar.

    A lock may be either:
      - an exact quote string, which must be unique in the manuscript, or
      - {"text": exact_quote, "occurrence": N}, where N is the 1-based
        occurrence among identical exact quotes.

    An empty lock list means the record contains no Ithar dialogue and every
    quoted span remains Greg-owned remembered dialogue.
    """
    if not locks:
        return set()

    selected = set()
    lock_keys = set()
    for lock in locks:
        if isinstance(lock, str):
            text = lock
            matches = [i for i, quote in enumerate(found_quotes) if quote == text]
            if len(matches) != 1:
                raise ValueError(
                    f"plain dragon quote must appear exactly once; found {len(matches)}: {text[:80]!r}"
                )
            key = (text, 1)
            index = matches[0]
        elif isinstance(lock, dict):
            text = lock.get("text")
            occurrence = lock.get("occurrence")
            if not isinstance(text, str) or not text:
                raise ValueError("occurrence lock requires non-empty text")
            if not isinstance(occurrence, int) or occurrence < 1:
                raise ValueError("occurrence lock requires occurrence >= 1")
            matches = [i for i, quote in enumerate(found_quotes) if quote == text]
            if occurrence > len(matches):
                raise ValueError(
                    f"dragon quote occurrence {occurrence} not found; only {len(matches)} matches: {text[:80]!r}"
                )
            key = (text, occurrence)
            index = matches[occurrence - 1]
        else:
            raise ValueError("dragon quote locks must be strings or {text, occurrence} objects")

        if key in lock_keys:
            raise ValueError(f"duplicate dragon quote lock: {key!r}")
        if index in selected:
            raise ValueError(f"multiple dragon locks resolve to quoted span {index + 1}")
        lock_keys.add(key)
        selected.add(index)

    return selected


def build_plan(source: str, config: dict) -> dict:
    if config.get("routing_mode") != "exact_quote_locked":
        raise ValueError("routing_mode must be exact_quote_locked")

    body = manuscript_body(source)
    found = list(quoted_spans(body))
    found_quotes = [q for _, _, q in found]
    dragon_indices = _resolve_dragon_indices(found_quotes, config.get("dragon_quotes", []))

    raw = []
    cursor = 0
    for quote_index, (start, end, quote) in enumerate(found):
        if start > cursor:
            raw.append(("greg", body[cursor:start]))
        speaker = "ithar" if quote_index in dragon_indices else "greg"
        raw.append((speaker, quote))
        cursor = end
    if cursor < len(body):
        raw.append(("greg", body[cursor:]))

    # Merge adjacent material owned by the same speaker before preview-safe splitting.
    merged = []
    for speaker, text in raw:
        if not text:
            continue
        if merged and merged[-1][0] == speaker:
            merged[-1] = (speaker, merged[-1][1] + text)
        else:
            merged.append((speaker, text))

    voices = config.get("voices", {})
    max_chars = int(config.get("max_chars", 480))
    pauses = config.get("pause_ms", {})
    paragraph_pause = int(pauses.get("paragraph", 450))
    continuation_pause = int(pauses.get("continuation", 220))
    handoff_pause = int(pauses.get("speaker_handoff", 1100))

    segments = []
    for speaker, text in merged:
        voice = voices.get(speaker)
        if not voice:
            raise ValueError(f"missing voice mapping for {speaker}")
        for piece in split_exact(text, max_chars):
            segments.append({
                "index": len(segments) + 1,
                "speaker": speaker,
                "voice_id": voice,
                "transcript": piece,
                "pause_after_ms": paragraph_pause if piece.endswith("\n\n") else continuation_pause,
            })

    for i in range(len(segments) - 1):
        if segments[i]["speaker"] != segments[i + 1]["speaker"]:
            segments[i]["pause_after_ms"] = max(segments[i]["pause_after_ms"], handoff_pause)

    return {
        "record": config.get("record"),
        "routing_mode": "exact_quote_locked",
        "uses_timestamps_for_speaker_assignment": False,
        "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "audio_body": body,
        "segments": segments,
    }


def main(argv):
    if len(argv) != 4:
        raise SystemExit("usage: audio_route.py SOURCE.md CONFIG.json OUTPUT.json")
    source_path = Path(argv[1])
    config_path = Path(argv[2])
    output_path = Path(argv[3])
    source = source_path.read_text(encoding="utf-8")
    config = json.loads(config_path.read_text(encoding="utf-8"))
    plan = build_plan(source, config)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(plan['segments'])} exact-routed segments to {output_path}")


if __name__ == "__main__":
    main(sys.argv)
