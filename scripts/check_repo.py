#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate():
    errors = []
    project = load_json("PROJECT.json")
    manifest = load_json("manuscript/manifest.json")
    audio = load_json("audio/manifest.json")

    if project.get("default_mode") != "rehearsal":
        errors.append("PROJECT.json default_mode must be rehearsal")
    if project.get("frontiers", {}).get("story") != "r079":
        errors.append("story frontier must be r079")

    records = manifest.get("records", [])
    if len(records) != 79:
        errors.append(f"expected 79 manuscript records, found {len(records)}")

    ids = [r.get("id") for r in records]
    if len(ids) != len(set(ids)):
        errors.append("record ids must be unique")

    slots = [r.get("slot") for r in records]
    if len(slots) != len(set(slots)):
        errors.append("record slots must be unique")

    for index, rec in enumerate(records, start=1):
        expected_id = f"r{index:03d}"
        expected_slot = f"{index:03d}"
        if rec.get("id") != expected_id:
            errors.append(f"record {index} id should be {expected_id}")
        if rec.get("slot") != expected_slot:
            errors.append(f"record {index} slot should be {expected_slot}")
        path = ROOT / rec.get("path", "")
        original = ROOT / "manuscript" / "records" / expected_slot / "versions" / "original-run.md"
        if not path.is_file():
            errors.append(f"missing current prose: {rec.get('path')}")
        if not original.is_file():
            errors.append(f"missing original-run version for {expected_id}")
        if path.is_file() and original.is_file() and path.read_bytes() != original.read_bytes():
            # Initial import must still be identical until that record is actually restored.
            if rec.get("prose_status") in {"reference", "needs_rehearsal"}:
                errors.append(f"{expected_id} current differs from original-run before restored status")
        if index <= 10:
            if rec.get("prose_status") != "reference":
                errors.append(f"{expected_id} must start as reference prose")
            if not rec.get("published"):
                errors.append(f"{expected_id} must start published")
        else:
            if rec.get("prose_status") not in {"needs_rehearsal", "restored"}:
                errors.append(f"{expected_id} has invalid rehearsal status")

    for rec_id, item in audio.get("records", {}).items():
        if rec_id not in set(ids):
            errors.append(f"audio references unknown record {rec_id}")
            continue
        if item.get("status") != "published":
            continue
        rec = next(r for r in records if r["id"] == rec_id)
        current = ROOT / rec["path"]
        expected_hash = item.get("source_sha256")
        if not expected_hash or (current.is_file() and sha256(current) != expected_hash):
            errors.append(f"published audio for {rec_id} is stale or missing source_sha256")
        src = item.get("src", "")
        if src and not (src.startswith("http://") or src.startswith("https://")):
            if not (ROOT / src).is_file():
                errors.append(f"published audio asset missing for {rec_id}: {src}")

    index_html = (ROOT / "index.html").read_text(encoding="utf-8")
    for required in ["PROJECT.json", "manuscript/manifest.json", "audio/manifest.json", "work=1"]:
        if required not in index_html:
            errors.append(f"reader missing runtime contract: {required}")
    if list((ROOT / "records").glob("*.html")) if (ROOT / "records").exists() else []:
        errors.append("generated record HTML pages are not allowed")

    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("3L repository validation failed:")
        for problem in problems:
            print(f"- {problem}")
        sys.exit(1)
    print("3L repository validation passed")
