# Manuscript Versioning

The version model is intentionally simple.

## Current authority

`manuscript/records/<slot>/current.md` is the current prose authority for that record. It wins over every draft, archived version, brain file, development note, audio file, image, or old-repository copy.

## Preserved versions

Meaningful superseded versions live under:

`manuscript/records/<slot>/versions/`

The initial migration preserves the old-repository prose as `versions/original-run.md` and also installs that same text as `current.md`.

Do not create a named version for every small edit. Git history already handles fine-grained recovery. Create explicit versions for meaningful rewrites, restoration passes, structural experiments, or user-requested alternatives worth comparing later.

## Drafts and rehearsal candidates

Exploratory prose belongs under:

`drafts/record-<slot>/`

The standard restoration candidate may simply be:

`drafts/record-<slot>/rehearsal.md`

Drafts may contradict each other and never publish automatically.

## Promotion

Before replacing an existing `current.md` with a meaningfully revised winner, preserve the superseded current text under `versions/` unless an identical named version already exists. Then replace `current.md`, update `manuscript/manifest.json`, and update derived brain files only when story facts or current working state actually changed.

Authority is determined by path, not timestamps: `current.md` always wins.
