# 3L AI-First Repository Design

## Goal

Make `Paiea/3L` the authoritative standalone home for the full 3L story through Record 079, optimized for fast AI handshakes, layered prose rehearsal, audio-first presentation, explicit version history, and a one-file runtime reader.

## Core rule

Complexity may exist behind the handshake. It may not sit inside the handshake.

A fresh AI starts with `AGENTS.md` and `PROJECT.json`, then loads only the files named for the requested mode.

## Authority

1. `manuscript/records/<slot>/current.md` is story authority for that record.
2. `manuscript/manifest.json` owns record order, publication state, title, and prose-status metadata.
3. `brain/` is derived context and yields to current prose.
4. `drafts/` is exploratory and cannot publish by accident.
5. `versions/` preserves meaningful superseded prose. `current.md` always wins.
6. `development/archive/` is cold historical research.
7. Audio and images are presentation assets, never story authority.

All Records 001–079 are preserved as valid story material. Records 001–010 are the current prose-quality reference. Records 011–079 begin as `needs_rehearsal` rather than being demoted to noncanon.

## Frontiers

`PROJECT.json` separates:

- story frontier: `r079`
- reference-quality frontier: `r010`
- restored frontier: `r010`
- rehearsal target: `r011`
- next unwritten record: `r080`

The default mode is rehearsal. Explicit new-writing work may continue beyond 079 without pretending the restoration frontier is the story frontier.

## Manuscript order

The manifest array owns navigation. Numeric arithmetic does not. This preserves stable existing record identities while allowing future structural discoveries such as `r041b` without renumbering later records or breaking audio links.

## Version model

Each migrated record contains:

- `current.md`: current authority
- `versions/original-run.md`: exact old-repository source preserved for comparison

Git history handles fine edits. Explicit versions are created only for meaningful rewrites, restoration passes, structural alternatives, or user-requested comparisons.

## Layered rehearsal

`REHEARSAL.md` is the primary revision method for 011–079.

The four restoration lenses are:

1. shape restoration
2. performance rehearsal
3. life restoration
4. listen rehearsal

They operate on one working candidate rather than spawning permanent artifacts for every pass. One record is the writing unit; five records are the seam-check unit. Passes restore missing information and leave strong existing material alone.

## Reader

`index.html` is the entire public reader application, with CSS and JavaScript inline. It fetches `PROJECT.json`, `manuscript/manifest.json`, current Markdown, and `audio/manifest.json` at runtime.

There are no generated per-record HTML files.

Public navigation exposes records marked `published`. An unlinked `work=1` query enables working preview of preserved/rehearsed records without changing publication state.

The manifest owns previous/next order.

## Audio

Audio is the flagship presentation layer when available. Prose remains the story authority.

Production audio is deliberately pull-based:

- source is approved `current.md`
- Greg voice owns narration and remembered human dialogue
- Ithar voice owns only Ithar's actual spoken dialogue
- production records exact source SHA-256
- a prose change makes previously published audio stale until rebuilt
- manuscript commits never automatically generate audio

Rehearsal voice playback is disposable and separate from production audio.

The public reader places playable audio above prose when a published audio manifest entry exists.

## Images

Images are sparse optional anchors, not a parallel chapter-production track. There is no per-record image quota and no automatic image pipeline. The reader must remain complete with zero images.

## Automation

Permanent automation is intentionally boring:

- `validate.yml`: repository contract and tests on PRs and main
- `pages.yml`: static GitHub Pages deployment from main

No manuscript-save workflow generates HTML or audio.

A temporary one-shot bootstrap workflow is allowed only to migrate the exact old manuscript, verify byte equality, and then be deleted before merge.

## Migration

Records 001–079 are copied byte-for-byte from `Paiea/peg-leg-greg-reader/3l/manuscript/record-NNN.md` into both `current.md` and `versions/original-run.md`. The bootstrap verifies both copies with `cmp` before commit.

Selected old authority documents are copied to `development/archive/legacy-authority/` only as cold historical reference.

## Success criteria

- a fresh AI can choose rehearsal or new-writing context without repo-wide search
- all 79 existing records are preserved exactly
- 001–010 are clearly the quality reference while 011–079 remain valid story authority
- meaningful rewrites remain easy to compare with older versions
- the website reads Markdown directly and uses manifest order
- audio can be the primary experience without becoming story authority
- a prose edit cannot silently leave published production audio claiming to be current
- image production remains optional and sparse
- normal writing does not wake a build/audio factory
