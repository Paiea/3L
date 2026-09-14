# 3L · The Third Leg

This repository is the authoritative home for 3L.

## AI handshake

Read `PROJECT.json` first. It names the current frontier and the smallest context set required to resume work. Do not search the repository before following that router unless the requested task requires deeper context.

For normal story continuation, read only the files in `read_first`. Load `deep_context_if_needed` only when continuity, time, promises, or whole-book structure actually requires it.

## Authority

**Canonical prose wins.** For each record, `manuscript/records/NNN/canonical.md` is the story authority. If any brain, timeline, promise, draft, development note, or archived version conflicts with canonical prose, fix the supporting file rather than bending the prose to match it.

Current reference frontier: Records 001–010.

Records 011+ in the older `Paiea/peg-leg-greg-reader` repository are development/archive material until explicitly promoted here.

## Writing loop

1. Draft interactively with the user.
2. Save exploratory versions under `drafts/record-NNN/` when useful.
3. When the user approves a record, promote its exact text to `manuscript/records/NNN/canonical.md`.
4. If replacing existing canon, archive the superseded canonical text first under that record's `versions/` directory.
5. Update `brain/CURRENT.md` and `brain/TIMELINE.md` after canon changes. Update deeper files only when their information actually changes.
6. Advance `PROJECT.json` only when canon is approved.

## Reader

`index.html` is one runtime Markdown reader. It reads `PROJECT.json` and loads canonical Markdown directly. There are no generated per-record HTML pages and no manuscript-triggered build pipeline.

Audio is intentionally outside v1. The prose reader must remain useful even when no audio exists.
