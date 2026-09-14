# 3L Layered Rehearsal

Rehearsal is the main prose-restoration method for Records 011–079.

The model is image restoration: the story image already exists. Recover missing resolution in layers without repainting strong material merely because a pass is active.

## Quality reference

Records 001–010 define the current prose baseline: embodied Greg perception, lived time, material detail, dialogue, physical action, independent supporting-character behavior, ordinary-life texture, and scene completeness.

Word count is evidence, not a target.

## Unit of work

- Write/revise one record at a time.
- Read at least the immediate previous and next current records first.
- Seam-check five restored records together before advancing the restored frontier.
- Keep one active candidate, normally `drafts/record-<slot>/rehearsal.md`.
- Do not create four permanent files just because there are four lenses.

## Layer 1 · Shape restoration

Determine what the record actually contains before polishing sentences.

Check:
- what physically happens
- what changes by the end
- how much calendar time passes
- whether events are dramatized or merely summarized
- whether the record contains one scene, several compressed scenes, or a structural split hiding inside it
- whether neighboring records already own the same beat

Preserve valid discovered story. If a structural split or merge is genuinely needed, treat it as an explicit manifest-order decision rather than silently renumbering later records.

## Layer 2 · Performance rehearsal

Enact the record.

Restore blocking, tasks, interruption, dialogue, reaction, bodily behavior, spatial relationships, and supporting-character agency. Ask what Greg was doing while the information happened and what another person actually chose rather than what narration says they felt.

Performance exists to produce better prose. It is not a separate canon layer and does not require screenplay/performance artifacts unless a specific difficult scene benefits from them.

## Layer 3 · Life restoration

Restore the lived world where it has been compressed away.

Look for work, tools, food, rooms, weather, maintenance, money, travel, waiting, institutions, property, family, bodies, ordinary competence, inconvenience, and other people's schedules and needs.

Add only details that change how the scene feels or functions. Do not decorate for length.

## Layer 4 · Listen rehearsal

Read or listen to the candidate as a performance before promotion.

Catch:
- repetitive cadence
- unclear dialogue attribution
- exposition that sounds like notes
- paragraphs that drag in audio
- referents that are visually clear but aurally muddy
- places where Greg stops sounding like Greg
- transitions that skip lived action

A cheap rehearsal voice may be used here. Rehearsal audio is disposable and does not enter the production audio manifest.

## Batch seam pass

After five records are individually restored, read/listen to the five as one unit. Check repeated beats, elapsed time, relationship movement, body continuity, money/work continuity, promises, and whether one record stole another record's job.

Then update `PROJECT.json.frontiers.restored_through` and the next `rehearsal_target`.

## Promotion

When the user approves the candidate:

1. Preserve the superseded meaningful `current.md` under `versions/` if needed.
2. Replace `current.md` with the approved candidate.
3. Update the record entry in `manuscript/manifest.json`.
4. Mark `prose_status` as `restored` unless the user explicitly leaves further work open.
5. Update brain files only if story facts, promises, timeline, or the active handoff actually changed.
6. Production audio becomes stale if its stored source hash no longer matches the new current prose.

## Stop conditions

Do not force a pass to change prose that is already doing its job. Do not add words simply to match early-record length. Do not let a development map overrule the lived scene. Current manuscript prose remains the highest story authority.
