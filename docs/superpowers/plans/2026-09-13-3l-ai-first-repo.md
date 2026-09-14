# 3L AI-First Repository Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish Paiea/3L as a fast AI-first story authority with explicit canonical/version semantics and a one-page Markdown reader for Records 001-010.

**Architecture:** `PROJECT.json` is the AI router. Canonical prose lives only at `manuscript/records/NNN/canonical.md`; drafts and superseded versions live outside the canonical path. `index.html` loads `PROJECT.json` and canonical Markdown directly, so prose publication needs no generated chapter HTML or manuscript-triggered workflow.

**Tech Stack:** Static HTML/CSS/vanilla JavaScript, Markdown source files, Python unittest for repository invariants.

**Spec:** `docs/superpowers/specs/2026-09-13-3l-ai-first-repo-design.md`

## Global Constraints

- Canonical manuscript prose outranks every brain/development file.
- Records 001-010 are the initial canonical and published frontier.
- Records 011+ are not migrated in v1.
- No audio pipeline or generated record pages in v1.
- Normal AI handshake begins with `PROJECT.json` and only its declared hot files.

---

### Task 1: Repository contract and failing tests

**Files:**
- Create: `tests/test_repo_contract.py`

**Interfaces:**
- Consumes: repository paths from the design spec.
- Produces: executable invariants for handshake, canonical frontier, version layout, and reader architecture.

- [ ] Write tests asserting `PROJECT.json` declares canon/published frontier 10, only canonical Records 001-010 exist, hot/deep files resolve, and `index.html` loads canonical Markdown rather than generated record HTML.
- [ ] Run `python -m unittest tests.test_repo_contract -v` and verify failures are caused by missing implementation files.
- [ ] Commit the failing contract test.

### Task 2: AI handshake and brain files

**Files:**
- Create: `PROJECT.json`
- Create: `README.md`
- Create: `brain/CURRENT.md`
- Create: `brain/TIMELINE.md`
- Create: `brain/STORY.md`
- Create: `brain/PROMISES.md`

**Interfaces:**
- Consumes: canonical baseline through Record 010 and established 3L authority.
- Produces: one-hop AI routing and compact hot/deep story context.

- [ ] Add `PROJECT.json` with `canon_frontier: 10`, `active_record: 11`, `published_through: 10`, hot file list, deep file list, and canonical path template.
- [ ] Add concise brain files that summarize only durable state through Record 010 and clearly state that canonical prose wins conflicts.
- [ ] Re-run contract tests and confirm only manuscript/reader assertions remain red.
- [ ] Commit handshake files.

### Task 3: Migrate canonical Records 001-010

**Files:**
- Create: `manuscript/records/001/canonical.md` through `manuscript/records/010/canonical.md`

**Interfaces:**
- Consumes: exact manuscript files from `Paiea/peg-leg-greg-reader/3l/manuscript/record-001.md` through `record-010.md`.
- Produces: 3L Reference v1 canonical prose.

- [ ] Copy each source record byte-for-byte into its new canonical path.
- [ ] Verify tests detect exactly ten canonical records and no 011+ canonical file.
- [ ] Spot-check source/new SHA-equivalent content using direct text comparison.
- [ ] Commit manuscript migration.

### Task 4: Single-page Markdown reader

**Files:**
- Create: `index.html`
- Create: `assets/reader.css`

**Interfaces:**
- Consumes: `PROJECT.json` and `manuscript/records/NNN/canonical.md`.
- Produces: `/?record=N` reading surface with prev/next navigation and no generated chapter pages.

- [ ] Implement the smallest client-side renderer needed by the migrated 3L Markdown syntax.
- [ ] Load the requested canonical record only when `1 <= record <= published_through`; default to Record 001.
- [ ] Render title/prose, previous/next navigation, record picker, and readable failure state.
- [ ] Ensure no audio UI appears in v1.
- [ ] Run contract tests and make them green.
- [ ] Commit reader.

### Task 5: Verification and publish readiness

**Files:**
- Verify all files above.

**Interfaces:**
- Consumes: completed v1 repository.
- Produces: evidence that the repo can be used as the new 3L authority and GitHub Pages source.

- [ ] Run `python -m unittest tests.test_repo_contract -v` with all tests passing.
- [ ] Verify `PROJECT.json` paths exist and Records 001-010 match old-repo source text.
- [ ] Inspect `index.html` for runtime fetches only to `PROJECT.json` and canonical Markdown paths.
- [ ] Open a PR, inspect the diff, and merge only after verification remains green.
