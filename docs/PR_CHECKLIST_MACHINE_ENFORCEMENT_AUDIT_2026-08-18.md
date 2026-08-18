# PR Checklist Machine-Enforcement Audit — 2026-08-18

Status: **CONTROL AUDIT — COMPLETE**

## Question

Should the dependency-governance checklist in `.github/PULL_REQUEST_TEMPLATE.md` gain additional CI logic that inspects pull-request diffs and requires matching classification/evidence changes?

## Finding

**Do not add a separate diff-aware dependency-checker at this time.** The objective parts of the checklist are already enforced by the repository's end-state validator, while the remaining parts require semantic authority judgment that CI is intentionally not allowed to infer.

The current protected `Validate Aramyst Assets` gate already fails when:

- an `AST-*` dependency does not resolve to a registered Asset ID;
- an exact external authority ID does not resolve through `schemas/external-authority-registry.json`;
- a bounded external authority range is not contained in a registered range;
- a prose dependency lacks a record in `schemas/dependency-classification-registry.json`;
- a prose dependency is used by an Asset ID not authorized by its classification record;
- the classification registry's declared Asset-ID set does not exactly match actual prose-dependency use;
- a classification record cites a missing evidence document;
- JSON/CSV dependency mirrors diverge;
- the classification registry or its schema is invalid.

These controls enforce the repository state that a diff-aware checker would attempt to reconstruct. Requiring both would duplicate logic and create a second implementation that could disagree with the authoritative validator.

## Checklist boundary

### Already machine-enforced

The following checklist claims have objective CI enforcement:

- `AST-*` target existence;
- external authority ID/range resolution;
- required prose-classification record;
- exact affected Asset-ID synchronization for prose dependencies;
- existence of the cited controlled evidence file;
- manifest/CSV synchronization;
- successful repository validation before merge.

### Human semantic review remains mandatory

CI must **not** decide:

- whether the selected dependency class is semantically correct;
- whether an existing durable authority is truly scope-equivalent rather than merely related;
- whether a prose dependency should remain title-bound/composite/long-term rather than normalize;
- whether the cited evidence actually proves the asserted authority relationship;
- whether a source anchor, constituent-authority rationale, or reopen condition is substantively sufficient.

Those decisions require source/authority interpretation and remain governed by `docs/DEPENDENCY_GOVERNANCE_POLICY.md`.

## Why no PR-diff coupling rule

A rule such as "dependency changed, therefore the classification registry or evidence file must also change in the same PR" would be incorrect in legitimate cases. An asset may add an already-registered external authority, reuse an already-controlled prose gate for an Asset ID already authorized by the classification record, or rely on a valid pre-existing evidence record. The authoritative requirement is that the resulting repository state is valid, not that particular files must always appear together in a diff.

Likewise, requiring CI to parse PR-body checkboxes would verify form completion rather than repository correctness and could be bypassed or become inconsistent with machine-readable state.

## Control decision

1. Keep `scripts/validate_manifest.py` and its regression suite as the machine authority for dependency-governance invariants.
2. Keep the PR checklist as the contributor-facing review surface.
3. Mark checklist items that are objectively CI-backed versus items requiring human semantic confirmation.
4. Do not add a second diff-aware dependency validator unless a future invariant genuinely depends on the transition between base and head rather than the validity of the resulting repository state.

## Reopen condition

Revisit this decision only if a concrete dependency-control defect can pass the end-state validator while still being objectively detectable from the PR transition without interpreting prose semantics.
