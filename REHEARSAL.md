# 3L Layered Rehearsal

Rehearsal is the prose-restoration method for records whose `manuscript/manifest.json` entry is marked `needs_rehearsal`. Do not infer rehearsal status from a broad numeric range; the manifest owns per-record prose state.

The model is image restoration: the story image already exists. Recover missing resolution in layers without repainting strong material merely because a pass is active.

## Quality reference

Records 001–010 define the current prose baseline: embodied Greg perception, lived time, material detail, dialogue, physical action, independent supporting-character behavior, ordinary-life texture, and scene completeness.

Word count is evidence, not a target.

## Unit of work

- Write/revise one record at a time.
- Read at least the immediate previous and next current records first.
- Seam-check five restored records together before advancing the contiguous restored frontier.
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

## Timeline reorientation

3L may move associatively between the present Ithar cave, First Life, and Second Life. The transition does not need to be chronological. An object, phrase, person, or idea may carry Greg into another period when the connection is emotionally or causally useful.

Greg owns the association. Ithar owns the coordinates.

When a jump materially changes more than one timeline variable, re-anchor the reader quickly. Useful coordinates include:
- which life
- Greg's approximate age or career era
- before or after a major marker such as Vey, S-class recognition, marriage, the twins, or the family catastrophe
- whether Nessa or another central person is alive/present in that period
- the physical present cave when the narration returns to Ithar

The anchor may be one line. Do not turn every transition into a label card. If the context is already unmistakable, let it breathe. If several variables changed at once, prefer explicit orientation even when a careful reader could infer it.

Ithar should reorient because he is genuinely reconstructing Greg's causal history, not because he becomes an exposition device. He may interrupt with questions such as which life, how old Greg was, whether an event happened before or after Vey, or whether Nessa and the children existed yet. His questions should sometimes reveal what he thinks matters.

On a return to the present, restore the room as well as the date. A small physical cue from Ithar, Greg, the stone, the light, or Greg's current body is usually enough to make the cave real again.

Associative links are encouraged. Onions may lead to household load, household load to fatherhood, fatherhood to Arcrutus, Arcrutus to Vey, Vey to Pava, and Pava to the empty S-class seat. The narrative may wander by meaning because Ithar periodically restores the coordinates.

Do not withhold basic chronology merely to create mystery. Confusion is not depth. Deliberate uncertainty about causality, memory, or divergence is different and may remain unresolved when the story requires it.

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

Then update `PROJECT.json.frontiers.restored_through` only if the batch closes the next contiguous gap from the existing frontier. A later record may be marked `restored` in the manifest without advancing `restored_through` when an earlier unresolved record remains. Set `rehearsal_target` to the first unresolved record in manifest order.

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
