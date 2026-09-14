# Manuscript Versioning

The version system is deliberately simple.

## Canon

`manuscript/records/NNN/canonical.md` is the only canonical prose for Record NNN. The newest approved `canonical.md` wins over every draft, superseded version, brain file, development note, or old-repository copy.

## Drafts

Exploratory prose belongs under:

`drafts/record-NNN/draft-NNN-label.md`

Drafts are non-canonical and may contradict each other freely.

## Replacing canon

Before replacing an existing canonical record, preserve its exact superseded text under:

`manuscript/records/NNN/versions/vNNN-label.md`

Then write the newly approved text to `canonical.md`.

The `versions/` directory is historical reference only. Never infer authority from timestamps or version numbers. `canonical.md` always wins.

Git history remains a second recovery layer beneath these explicit human-readable versions.
