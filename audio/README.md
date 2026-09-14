# 3L Audio

Audio is the flagship public rendering when a finished recording exists. It is derived from approved manuscript prose and never outranks the manuscript.

## Production contract

- Source: `manuscript/records/<slot>/current.md` after prose approval.
- Greg voice: narration and all remembered human dialogue.
- Ithar voice: only Ithar's actual spoken dialogue.
- Chunking, routing, takes, and assembly are production mechanics, not story authority.
- Rehearsal/listen-back audio is disposable and does not count as production audio.
- Do not generate production audio automatically when prose changes.

## Seam and pause contract

**Assembly owns silence.** Do not rely on whatever leading or trailing silence happens to exist in generated takes, and do not hard-splice separate performances just because the waveform joins cleanly.

Every join should be classified by what the listener experiences:

- **continuation**: same speaker, same thought, no dramatic beat. Start around 100–180 ms.
- **paragraph / thought turn**: same voice, new sentence group or meaningful shift. Start around 220–350 ms.
- **action beat**: dialogue or narration gives way to a physical action, observation, or reaction that should register before speech resumes. Start around 350–550 ms.
- **Greg ↔ Ithar handoff**: different embodied speaker. Start around 500–700 ms. Never hard-splice this transition.
- **major beat / scene turn**: the listener should feel the record breathe. Start around 800–1200 ms.

These are starting ranges, not immutable timing law. The ear wins. If a seam sounds crowded, widen it. If it sounds theatrically slow, tighten it.

Prefer trimming take tails to a consistent small base and inserting pause at assembly time. That makes pacing deterministic and prevents different TTS generations from carrying accidental silence into the final record.

Speaker transitions and action seams are priority QC points. A technically correct splice is not approved if the speaker change, reaction, or action lands too quickly to register.

## Listen-back standard

A finished record is not release-ready merely because all transcript text is present and every take verifies.

Before publication, listen specifically for:

- Greg-to-Ithar and Ithar-to-Greg handoffs,
- dialogue-to-action and action-to-dialogue joins,
- places where a reaction needs a beat before the next line,
- clipped breaths or accidental double-pauses,
- seams where two individually good takes sound like separate recordings when joined.

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
4. Generate Greg/Ithar takes from exact routed transcript.
5. Assemble with deliberate seam classification and pause insertion.
6. Listen through the final record, with extra attention to voice handoffs and action beats.
7. Add/update the manifest entry with source SHA-256 and final source URL/path.
8. Publish deliberately.

No worker claims, capture manifests, or automated audio build graph belongs in the default writing handshake. If scale later requires production workers, keep their state under `audio/production/` and make the final manifest the only public contract.
