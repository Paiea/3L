# 3L AI-First Repository Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans. The working branch is `setup/ai-first-reader`.

**Goal:** Establish `Paiea/3L` as a fast AI-first, audio-first story repository preserving Records 001–079 while beginning layered rehearsal at Record 011.

**Architecture:** `AGENTS.md` and `PROJECT.json` provide the shallow handshake. `manuscript/manifest.json` owns story order. Every record has `current.md` plus meaningful historical versions. A single `index.html` reads Markdown at runtime. Audio is pull-based and source-hash-bound. Images are sparse optional assets.

**Tech Stack:** Static HTML/CSS/vanilla JavaScript, Markdown, JSON manifests, Python standard-library validation, GitHub Actions for validation and Pages only.

**Spec:** `docs/superpowers/specs/2026-09-13-3l-ai-first-repo-design.md`

## Global Constraints

- Current manuscript prose wins story conflicts.
- Preserve the existing 001–079 story frontier exactly before restoration.
- Records 001–010 are the prose-quality reference.
- Records 011–079 start as `needs_rehearsal`, not noncanon.
- Manifest order controls navigation; never assume numeric ±1.
- Audio is flagship presentation but derived from prose.
- No automatic audio generation on manuscript commits.
- Images remain sparse and optional.
- No generated per-record HTML.

---

### Task 1: Fast AI handshake

- [x] Add `AGENTS.md`.
- [x] Route work through `PROJECT.json` modes and distinct frontiers.
- [x] Keep deep archives out of default context.

### Task 2: Layered rehearsal and version semantics

- [x] Make `current.md` the record authority.
- [x] Define meaningful versions under `versions/`.
- [x] Add `REHEARSAL.md` with shape, performance, life, listen, and five-record seam passes.

### Task 3: Audio-first and sparse visual contracts

- [x] Add pull-based `audio/manifest.json`.
- [x] Add source-hash staleness rules.
- [x] Preserve Greg/Ithar voice routing.
- [x] Document sparse optional images with no chapter quota.

### Task 4: One-file reader

- [x] Add self-contained `index.html`.
- [x] Read manifest order and current Markdown at runtime.
- [x] Put published audio above prose when available.
- [x] Support unlinked `work=1` preview for unreleased records.

### Task 5: Exact 001–079 migration

- [ ] Copy old `record-NNN.md` byte-for-byte into each `current.md`.
- [ ] Preserve identical `versions/original-run.md` copies.
- [ ] Generate the 79-record manuscript manifest with titles, word counts, quality state, and publication state.
- [ ] Verify all copies with `cmp`.
- [ ] Copy selected old authority files into cold archive.

### Task 6: Boring automation

- [x] Add PR/main validation workflow.
- [x] Add main-only static Pages deployment.
- [ ] Delete the one-shot bootstrap workflow after successful migration.

### Task 7: Verification and integration

- [ ] Run `python scripts/check_repo.py` successfully on migrated branch.
- [ ] Run `python -m unittest tests.test_repo_contract -v` successfully.
- [ ] Open PR and verify CI.
- [ ] Merge to `main` only after green checks.
- [ ] Verify Pages deployment or report the exact account-setting blocker if Pages has not yet been enabled for Actions.
