#!/usr/bin/env python3
import json
from pathlib import Path

for i in range(11, 21):
    slot = f"{i:03d}"
    route_path = Path(f"audio/production/record-{slot}/route-plan.json")
    if not route_path.exists():
        continue
    route = json.loads(route_path.read_text(encoding="utf-8"))
    out_dir = route_path.parent / "work-orders"
    out_dir.mkdir(parents=True, exist_ok=True)
    segments = route["segments"]
    for start in range(0, len(segments), 10):
        batch = segments[start:start+10]
        out = {
            "record": route["record"],
            "source_sha256": route["source_sha256"],
            "routing_mode": route["routing_mode"],
            "segments": batch,
        }
        first = batch[0]["index"]
        last = batch[-1]["index"]
        (out_dir / f"segments-{first:03d}-{last:03d}.json").write_text(
            json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
