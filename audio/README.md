# 3L Audio

Audio is the flagship public rendering when a finished recording exists. It is derived from approved manuscript prose and never outranks the manuscript.

## Production contract

- Source: `manuscript/records/<slot>/current.md` after prose approval.
- Current production mapping: Greg = `deep`; Ithar = `normal`.
- Greg voice owns narration and all remembered human dialogue.
- Ithar voice owns only Ithar's actual spoken dialogue.
- Chunking, routing, takes, and assembly are production mechanics, not story authority.
- Rehearsal/listen-back audio is disposable and does not count as production audio.
- Do not generate production audio automatically when prose changes.

## Speaker-routing contract

**Exact manuscript wording owns the speaker. Time never owns the speaker.**

Before generation, route the canonical prose into explicit speaker segments. For Ithar, the routing authority stores the complete exact quoted speech from the manuscript, not a timestamp window and not merely a guessed duration. Everything outside those locked Ithar quotes belongs to Greg unless a future manuscript explicitly introduces another production voice.

Rules:

- Never infer speaker ownership from start/end times in an older recording.
- Never let a chunk cross a Greg/Ithar ownership boundary.
- A long speech may be split into multiple capture-safe chunks, but every resulting chunk keeps the same locked speaker.
- If a locked quote is unique, exact text is sufficient.
- If identical quoted text occurs more than once, lock the exact text plus its 1-based occurrence in the manuscript. Never use audio timing to disambiguate duplicates.
- If a lock cannot resolve exactly against current prose, routing fails instead of guessing.
- Timestamps may be used after routing for editing, navigation, or QC. They may never decide who speaks.

This exists specifically to prevent a timing drift from causing Ithar to read Greg's next line or Greg to read Ithar's line.

## Seam and pause contract

**Assembly owns silence.** Do not rely on whatever leading or trailing silence happens to exist in generated takes, and do not hard-splice separate performances just because the waveform joins cleanly.

Every join should be classified by what the listener experiences:

- **continuation**: same speaker, same thought, no dramatic beat. Usually very small or no inserted pause when a capture split occurs mid-sentence.
- **paragraph / thought turn**: same voice, new sentence group or meaningful shift. Start around 350–500 ms.
- **action beat**: dialogue or narration gives way to a physical action, observation, or reaction that should register before speech resumes. Start around 500–800 ms.
- **Greg ↔ Ithar handoff**: different embodied speaker. Default production baseline is about 1100 ms, usually within 900–1200 ms. Never hard-splice this transition.
- **major beat / scene turn**: the listener should feel the record breathe. Start around 1200–1600 ms.

These are starting ranges, not immutable timing law. The ear wins. If a seam sounds crowded, widen it. If it sounds theatrically slow, tighten it.

A capture-safe split inside one sentence is different from a dramatic seam. Keep that join extremely small so production chunking does not become audible performance punctuation.

Prefer trimming take tails to a consistent small base and inserting pause at assembly time. That makes pacing deterministic and prevents different TTS generations from carrying accidental silence into the final record.

Speaker transitions and action seams are priority QC points. A technically correct splice is not approved if the speaker change, reaction, or action lands too quickly to register.

## Listen-back standard

A finished record is not release-ready merely because all transcript text is present and every take verifies.

Before publication, listen specifically for:

- Greg-to-Ithar and Ithar-to-Greg handoffs,
- dialogue-to-action and action-to-dialogue joins,
- places where a reaction needs a beat before the next line,
- clipped breaths or accidental double-pauses,
- seams where two individually good takes sound like separate recordings when joined,
- any wrong-speaker line, which is an automatic rejection.

A seam mistake is considered a release defect because it breaks immersion even when the voice performance itself is strong.

## Staleness

Every published audio entry in `audio/manifest.json` stores the SHA-256 of the exact `current.md` used to make it.

If current prose changes, that audio is stale until deliberately rebuilt and the manifest is updated. Validation should fail a `published` audio entry whose source hash does not match current prose.

## Public assets

Finished record audio may live at:

`audio/assets/<record-id>.mp3`

The manifest may also point at a stable external URL if storage later moves away from the repository. The reader only needs one final playable source per published record.

## Production loop

1. Restore/approve prose.
2. Listen-rehearse prose cheaply if useful.
3. Lock the source text for production.
4. Build exact quote-locked speaker routing from current prose.
5. Generate Greg/Ithar takes only from those owned segments.
6. Assemble with deliberate seam classification and pause insertion.
7. Listen through the final record, with extra attention to voice handoffs and action beats.
8. Add/update the manifest entry with source SHA-256 and final source URL/path.
9. Publish deliberately.

No worker claims or automated audio build graph belongs in the default writing handshake. If scale later requires production workers, keep their state under `audio/production/` and make the final manifest the only public contract.
