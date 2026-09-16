# Open-Circuit Authority and Record 045 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reconcile 3L authority with the approved First-Life open-circuit support progression, then replace the stale Life-Two Record 045 with the next First-Life chapter without writing ahead.

**Architecture:** Canonical prose through Record 044 remains supreme. The approved open-circuit design becomes durable pressure in the brain authority files, while Record 045 begins the progression indirectly through normal support doctrine, mobility, feedback, and deeper Barrier specialization rather than prematurely introducing Draw. Existing later raw prose remains salvage material, not fixed choreography.

**Tech Stack:** Markdown manuscript and authority files, JSON manifest, pytest repository contract, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-15-first-life-open-circuit-support-design.md`

## Global Constraints

- Canonical prose wins every conflict.
- Future routing is authoritative pressure, not fixed chapter choreography.
- Barrier remains the root discipline; Draw is learned later by studying what defeats barriers.
- Draw is primarily anti-ward / drain technique, not normal support doctrine.
- Continuous personal aura materially interferes with tactical Draw-routing; Greg later chooses open-circuit operation as a real durability sacrifice.
- Mana cycling redistributes existing capacity and regeneration opportunity; it never creates free mana.
- Mobility/stamina remains necessary because proximity improves sensing, transfer, reacquisition, and control.
- Conventional support doctrine is rational. Critics must sometimes be correct about Greg's unsafe or inefficient implementations.
- Greg's advantage is iterative feedback and architecture, not universal genius or secret warrior power.
- First-Life peak is relational/open-circuit; Life-Two revenge architecture becomes increasingly closed/self-contained.
- Record 045 only. Do not write Record 046.
- Record 045 must not introduce mature Draw/cycling before prose earns the bridge.

---

### Task 1: Reconcile hot authority

**Files:**
- Modify: `brain/CURRENT.md`
- Modify: `brain/STORY.md`
- Modify: `brain/TIMELINE.md`
- Modify if needed for durable promise wording: `brain/PROMISES.md`

**Interfaces:**
- Consumes: canonical Records 001-044 and the approved open-circuit design spec.
- Produces: durable routing pressure for future prose workers and an accurate Record 045 frontier.

- [ ] **Step 1: Update CURRENT.md**

Set restored/public prose frontier to Record 044 and current rehearsal target to Record 045. Preserve the separate raw story frontier through 079. Summarize the immediate 044 state: three-month north-road contract, Calder/Orla/Senn/Taris, Greg learning that five-second brilliance can overspend the six-hour road, and temporary belonging. State that 045 begins the long First-Life support climb and should establish normal doctrine/friction before Draw.

- [ ] **Step 2: Extend STORY.md support authority**

Under Barrier/support authority, add the approved chain: Barrier specialization -> study counters -> Draw as ward-drain -> controlled allied relief -> redistribution/cycling -> linking/network architecture. Add aura conflict, open-circuit cost, mobility requirement, regeneration/capacity allocation, party-size/control bottleneck, rational pushback, and Life-Two closed-circuit inversion. Preserve existing S-class/Nhal facts.

- [ ] **Step 3: Reconcile TIMELINE.md**

Replace the compressed "over decades" support climb with a broad multi-stage First-Life development runway after Record 044. Keep exact record numbers flexible. Explicitly move the full First-Life climb/Nhal before the Life-Two catastrophe because canonical prose has already opened that rewind. Fix any stale Life-Two child language to canonical twins Mira and Tomas where encountered.

- [ ] **Step 4: Check PROMISES.md for contradictions**

If PROMISES contains stale progression or family facts, minimally reconcile them. Do not duplicate the entire design spec into PROMISES.

- [ ] **Step 5: Commit authority reconciliation**

Commit message: `story: lock Greg open-circuit support progression`

---

### Task 2: Write Record 045 only

**Files:**
- Modify: `manuscript/records/045/current.md`
- Read for continuity: `manuscript/records/043/current.md`, `manuscript/records/044/current.md`, `REHEARSAL.md`, Records 001-010 as voice baseline.

**Interfaces:**
- Consumes: reconciled authority and Record 044 ending state.
- Produces: one complete reader-facing Record 045. No 046 prose.

- [ ] **Step 1: Preserve the old 045 concept as salvage, not canon pressure**

Treat `THE RIVAL` / Juna Marr as later Life-Two material available for reuse. Do not force it into the current First-Life chronology.

- [ ] **Step 2: Draft the new 045 around doctrine friction**

Continue the three-month north-road contract. Give Greg repeated exposure to what competent conventional support actually does: self-aura, stable positioning, planned target priority, reserve discipline, and reliability. Let Greg be told directly that some of his movement/intervention habits are wasteful or unsafe. Make at least one critic demonstrably correct in-scene.

- [ ] **Step 3: Give Greg an embodied mobility problem**

Create an event where Greg sees a useful intervention but cannot reach/retarget/maintain it cleanly while preserving his own support state. His warrior background helps but is insufficient. The lesson should arise through lungs, legs, casting precision, distance, timing, and recovery rather than an abstract lecture.

- [ ] **Step 4: Push Greg toward deeper Barrier specialization without Draw yet**

End with Greg asking a more specialist question about Barrier failure/counters, or seeking someone who knows how maintained wards are actually defeated. This is the causal door toward Draw, not the Draw breakthrough itself.

- [ ] **Step 5: Prose audit**

Check that Young Greg owns perception, Old Greg owns selection, action is legible in audio, mundane texture remains present, Greg is funny without becoming quippy, and the ending does not resolve into another explicit theorem like 041-044. Avoid deterministic foreshadowing.

- [ ] **Step 6: Commit prose**

Commit message: `story: rehearse record 045`

---

### Task 3: Advance publication contract for 045

**Files:**
- Modify: `manuscript/manifest.json`
- Modify: `tests/test_repo_contract.py` only if the repository's explicit frontier assertion requires it.

**Interfaces:**
- Consumes: completed Record 045.
- Produces: manifest/public reader frontier through 045 while audio remains unchanged.

- [ ] **Step 1: Inspect current manifest entry and frontier test**

Confirm the exact quality/publication fields used by Record 044 and mirror the established pattern for 045. Do not touch audio fields beyond preserving their current state.

- [ ] **Step 2: Write/adjust the frontier expectation first if required**

If `test_manifest_owns_order_and_quality_state` explicitly asserts 044, change the expected prose/public frontier to 045 before changing the manifest.

- [ ] **Step 3: Run the focused contract test and confirm it fails for the old manifest state**

Run: `pytest tests/test_repo_contract.py::test_manifest_owns_order_and_quality_state -v`

Expected: failure showing 045 is not yet the expected public/quality frontier, if the test architecture exposes this transition.

- [ ] **Step 4: Update manifest**

Promote Record 045 using the exact same prose/publication state pattern as Record 044. Keep audio frontier at its existing value.

- [ ] **Step 5: Run focused test**

Run: `pytest tests/test_repo_contract.py::test_manifest_owns_order_and_quality_state -v`

Expected: PASS.

- [ ] **Step 6: Run full repository contract tests**

Run: `pytest tests/test_repo_contract.py -v`

Expected: all tests PASS.

- [ ] **Step 7: Commit publication contract**

Commit message: `story: publish record 045`

---

### Task 4: Verify main and stop

**Files:** none unless verification exposes a real defect.

**Interfaces:**
- Consumes: authority, prose, and publication commits.
- Produces: fresh evidence that Record 045 is the prose frontier and no 046 work was performed.

- [ ] **Step 1: Inspect git diff/commits**

Verify only intended authority/spec/plan/045/manifest/test files changed and Record 046 is untouched.

- [ ] **Step 2: Verify CI status for the final commit**

Check the repository's validation workflow for the final publication commit. Do not claim success until the run reports success.

- [ ] **Step 3: Verify Pages if publication triggers deployment**

Check the Pages workflow associated with the final commit and confirm success before claiming the public site is updated.

- [ ] **Step 4: Stop at 045**

Report Record 045 title, what changed in Greg's progression, authority files updated, test result, CI/Pages result, and explicitly state that Record 046 was not written.
