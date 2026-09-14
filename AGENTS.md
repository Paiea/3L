# 3L Agent Handshake

Read `PROJECT.json` first. It tells you which mode is active and the smallest context set to load. Do not begin by searching the repository or loading every authority file.

## Authority

1. `manuscript/records/<slot>/current.md` is story authority for that record.
2. `manuscript/manifest.json` owns record order, publication state, and prose-status metadata.
3. `brain/` files are derived working context and must yield to current prose.
4. `drafts/` is exploratory and non-authoritative.
5. `versions/` is historical reference. `current.md` always wins.
6. `development/archive/` is cold storage, never default context.
7. Audio and images are derived presentation assets, never story authority.

## Default mode

The current default mode is rehearsal/restoration beginning at Record 011. Follow `PROJECT.json.modes.rehearsal.read_first` before loading deeper files.

Records 001–010 are the prose-quality reference. Records 011–079 are valid story material that may need restoration. Do not discard their events merely because their prose is thinner.

## Rehearsal behavior

Read `REHEARSAL.md`. Restore only what is missing. Do not mechanically rewrite strong material. Work one record at a time and seam-check in five-record batches.

Use one working candidate under `drafts/record-<slot>/` rather than creating permanent artifacts for every restoration lens.

When a revised record wins, preserve the superseded meaningful version, replace `current.md`, update the manifest, and update brain files only if the underlying story state changed.

## New writing

If explicitly asked to write beyond the existing frontier, use `PROJECT.json.modes.new_writing`. The next unwritten record is `r080`. Do not confuse the rehearsal frontier with the story frontier.

## Navigation and structure

Never assume previous/next record is numeric ±1. Use manifest order. This allows future splits such as `r041b` without renumbering the existing book.

## Audio

Audio is the flagship public experience when available. Production audio must be derived from the approved current prose and store the source prose SHA-256 in `audio/manifest.json`. If prose changes afterward, the old audio is stale until deliberately rebuilt.

Do not auto-generate audio on manuscript commits.

## Images

Images are sparse optional anchors. Do not create a per-record image quota or image pipeline unless the user explicitly changes that direction.
