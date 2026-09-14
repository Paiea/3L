# 3L Audio

Audio is the flagship public rendering when a finished recording exists. It is derived from approved manuscript prose and never outranks the manuscript.

## Production contract

- Source: `manuscript/records/<slot>/current.md` after prose approval.
- Greg voice: narration and all remembered human dialogue.
- Ithar voice: only Ithar's actual spoken dialogue.
- Chunking, routing, takes, and assembly are production mechanics, not story authority.
- Rehearsal/listen-back audio is disposable and does not count as production audio.
- Do not generate production audio automatically when prose changes.

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
5. Assemble and verify the final record audio.
6. Add/update the manifest entry with source SHA-256 and final source URL/path.
7. Publish deliberately.

No worker claims, capture manifests, or automated audio build graph belongs in the default writing handshake. If scale later requires production workers, keep their state under `audio/production/` and make the final manifest the only public contract.
