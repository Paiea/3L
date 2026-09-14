# 3L · The Third Leg

3L is an audio-first long-form fantasy record. This repository is its story authority, rehearsal workspace, reader, and production handoff.

## Start here

AI workers read `AGENTS.md`, then `PROJECT.json`. `PROJECT.json` names the working mode and the smallest files needed for the next job. Do not begin with repository-wide search.

## Authority

For any record, `manuscript/records/<slot>/current.md` wins every story conflict. Brain files, manifests, drafts, archived systems, audio, images, and old versions must yield to current prose.

All Records 001–079 are preserved story authority. Records 001–010 are the current prose-quality reference. Records 011–079 are valid story material marked `needs_rehearsal`, not discarded canon.

`manuscript/manifest.json` owns record order. Never infer previous/next from arithmetic. This lets a future rehearsal split a record without renumbering the whole book.

## Rehearsal

`REHEARSAL.md` defines the restoration pass. The default working target is Record 011. Rehearsal restores missing resolution in layers rather than rewriting everything indiscriminately.

The normal unit is one record. The seam-check unit is five records.

## Versions

`current.md` is always the winner. Meaningful superseded versions live under that record's `versions/` directory. Git history remains the fine-grained recovery layer.

Exploratory prose belongs under `drafts/` and cannot publish accidentally.

## Reader

`index.html` is the whole reader application. It loads Markdown at runtime from the manifest. There are no generated per-record HTML pages.

Public navigation shows only records marked published. `?record=011&work=1` may be used as an unlinked working preview for a preserved or rehearsed record.

## Audio

Audio is the flagship presentation layer when it exists. Production audio is derived from the approved `current.md`, never a competing story authority. `audio/manifest.json` records published audio and the source prose hash used to make it.

Audio is produced deliberately after prose approval. Saving manuscript prose does not automatically generate audio.

## Images

Images are sparse and optional. There is no chapter-art quota or image-production pipeline. Use art only when a cover, frontispiece, major location, or rare story anchor earns it.

## Old repository

`Paiea/peg-leg-greg-reader/3l` remains historical archaeology. Selected old authority files are copied under `development/archive/` for reference, but they are never default handshake material.
