# 3L AI-First Repository Design

## Goal

Make Paiea/3L the authoritative 3L repository with a fast AI handshake, explicit manuscript authority, preserved rewrite history, and a single-file-style Markdown reader that does not require prose build automation.

## Authority

1. `manuscript/records/NNN/canonical.md` is story authority for that record.
2. `brain/CURRENT.md` is the hot handoff state and must yield to canonical prose on conflict.
3. `brain/TIMELINE.md`, `brain/STORY.md`, and `brain/PROMISES.md` are deeper working context and must yield to canonical prose.
4. `drafts/` is non-canonical.
5. `manuscript/records/NNN/versions/` preserves superseded approved/canonical versions for easy human and AI comparison. New canonical prose always trumps archived versions.
6. `development/` is research and optional deep context, never default handshake material.

## AI handshake

`PROJECT.json` is the first file an AI reads. It declares the canon frontier, active record, published frontier, required hot files, and optional deep-context files. Normal continuation should require `PROJECT.json`, `brain/CURRENT.md`, and the last one or two canonical records. Deep files are loaded only when relevant.

## Manuscript and revision flow

Draft prose lives under `drafts/record-NNN/`. A draft does not publish and does not advance canon. When the user approves a draft, its exact text becomes `manuscript/records/NNN/canonical.md`. If an existing canonical record is replaced, copy the superseded text into `manuscript/records/NNN/versions/vNNN-<label>.md` before replacing `canonical.md`.

Records 001-010 are migrated from the current 3L manuscript in `Paiea/peg-leg-greg-reader` and form the initial 3L Reference v1 frontier. Records 011+ remain in the old repository as development/archive material until explicitly promoted.

## Reader

The public reader is intentionally small. `index.html` is the reader application and loads canonical Markdown directly at runtime based on `?record=N`. It reads `PROJECT.json` to enforce the published frontier and navigation. No per-record HTML generation and no manuscript-triggered build workflow are required.

A minimal client-side Markdown renderer supports the syntax used by 3L canonical records. The reader shows prose only. Audio is absent in v1 and may later appear as optional metadata in `PROJECT.json` without changing manuscript authority.

## Site behavior

- Default visit opens Record 001 or a small landing/record selector within the same `index.html`.
- `?record=7` loads `manuscript/records/007/canonical.md`.
- Previous/next links stay within `published_through`.
- Missing or malformed records produce a readable error state rather than exposing internal project machinery.
- The page is mobile-first, light, text-focused, and fast.

## Repository structure

```text
PROJECT.json
README.md
index.html
assets/reader.css
brain/CURRENT.md
brain/TIMELINE.md
brain/STORY.md
brain/PROMISES.md
manuscript/records/001/canonical.md
...
manuscript/records/010/canonical.md
drafts/
development/
tests/
```

## Non-goals for v1

- No audio production pipeline.
- No parallel story-writing workers.
- No generated record pages.
- No automatic canon advancement.
- No migration of Records 011+.
- No migration of the old temporal/audio machinery into the hot path.
- No Google Drive synchronization.

## Success criteria

A fresh AI can determine the correct 3L authority and resume point from `PROJECT.json` plus the named hot files without repository-wide search. A user can open the GitHub Pages reader, navigate Records 001-010, and always see current canonical Markdown. Rewriting a record preserves the superseded version while making the new `canonical.md` unambiguously authoritative.