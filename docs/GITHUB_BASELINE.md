# Aramyst GitHub Baseline

Status: **CONTROLLED — current repository-control baseline**

Baseline established: 2026-08-14  
Last refreshed: 2026-08-24  
Repository: `JamesJedi420/aramyst-book-assets`  
Default branch: `main`  
Visibility: public  
Canonical Drive root: `1IBbWIFfAuJpB7I9jc7yrjb461mPnuGnq`

## Purpose

This file is the single current-state entry point for GitHub repository control. Dated audits and reconciliations remain evidence records; they do not operate as parallel current-state baselines.

When a dated audit establishes a stable repository-wide control, fold that current fact into this file during the next baseline refresh. Preserve the dated audit as evidence of how the decision was reached. Git history preserves prior baseline snapshots.

Repository state that already has an exact machine-readable owner should not be copied here as a fixed member count or hand-maintained “current set.” This baseline should point to the controlling registry and summarize the architecture. Branch/PR/issue state is different: no machine-readable branch-exception registry currently exists, so those values may be recorded here only as an explicitly dated live-state snapshot and must be re-verified before action.

## Documentation authority

Read repository-control state in this order:

1. `docs/GITHUB_BASELINE.md` — current repository-control state.
2. Controlling domain policies within their scope:
   - `docs/SOURCE_OF_TRUTH.md`
   - `docs/NAMING_AND_VERSIONING.md`
   - `docs/DEPENDENCY_GOVERNANCE_POLICY.md`
   - `docs/APPROVED_ASSET_PROVENANCE.md`
   - `docs/MAIN_PROTECTION_POLICY.md`
   - `docs/VISUAL_STYLE_GUIDE.md` for visual-production rules.
3. Machine-readable registries, schemas, validators, workflow configuration, and the PR template for the exact state they encode.
4. Dated audits/reconciliations as evidence records.

Asset-specific reconciliation documents may remain controlling evidence where a registry or policy cites them, but they are not general repository-control baselines.

## Source-of-truth boundary

`docs/SOURCE_OF_TRUTH.md` remains controlling for GitHub/Drive ownership.

GitHub owns stable asset identity, status, version, machine-readable registries, naming/version rules, dependency admission records, approved provenance sidecars, validation, repository paths, fixed-layout page order, and promoted release-ready repository exports.

Google Drive owns manuscript prose, research/source notes, editable working documents, working briefs, review material, and working art before repository promotion unless a specific controlling record says otherwise.

GitHub maintenance must not independently create or revise story canon, geography authority, mechanics, manuscript prose, creative approval, or publication identity.

## Registry authority

Current asset state is owned by:

- `manifest.json` — machine-readable asset/page authority;
- `ASSET_MANIFEST.csv` — synchronized operational mirror;
- `docs/ASSET_MANIFEST.md` — synchronized human-readable registry.

Current dependency state is owned by the live dependency lists plus the machine-readable authority/classification registries:

- `manifest.json` / `ASSET_MANIFEST.csv` — dependency strings actually used by assets;
- `schemas/external-authority-registry.json` — admitted durable external authority IDs/ranges;
- `schemas/dependency-classification-registry.json` — title-bound, composite, and long-term prose dependency classifications and their exact affected Asset-ID sets.

Current provenance-controlled coverage is derived from `manifest.json` together with the validated `provenance/*.json` sidecar set under `docs/APPROVED_ASSET_PROVENANCE.md`.

This baseline does not duplicate volatile asset-status counts, dependency-class counts, provenance-sidecar counts, or other registry-owned membership totals. Read the corresponding live registry instead.

## Current branch, PR, and issue state

Live-state snapshot verified on 2026-08-24 before this refresh branch was created. This is a dated baseline observation, not a permanent numeric invariant; re-read GitHub before acting on branch, PR, or issue state.

At that verification point:

- `main` — authoritative protected production branch;
- `agent/map-hou-001-functional-adjacency` — intentional historical-provenance exception;
- `agent/q-023-cross-system-sync` — intentional historical-provenance exception;
- zero open pull requests;
- zero open issues.

`agent/continuity-gate-audit` was previously audited, confirmed to have no unique commits ahead of `main`, explicitly authorized for deletion, deleted, and verified absent.

The persistent non-`main` historical-provenance exceptions verified at this refresh are the branches enumerated above:

- `agent/map-hou-001-functional-adjacency` preserves unique superseded PR #4 schematic/QA history;
- `agent/q-023-cross-system-sync` preserves unique superseded PR #11 implementation/reconciliation history.

Do not infer a permanent exception count from this prose. If a later preservation or deletion decision changes the set, re-verify live branches and refresh this section. A separate branch-exception registry should not be invented merely to remove prose unless the project explicitly adopts that architecture.

These preserved refs are non-authoritative and must not be used as bases for new production work. Routine `agent/<scope>` branches are ephemeral and should be removed after merge or abandonment unless a specific preservation audit establishes a new historical-provenance exception.

Closed issues and superseded PR bodies are point-in-time historical records. Stale warning language inside them does not create a current blocker.

## Main protection

GitHub's live branch endpoint reported `main` as protected on 2026-08-24. `docs/MAIN_PROTECTION_POLICY.md` and `.github/rulesets/protect-main.json` remain synchronized and record the exact controlled target: PR requirement, review-thread resolution, required `validate` check from GitHub Actions, strict/up-to-date status checking, linear history, non-fast-forward protection, deletion restriction, squash/rebase merge methods, zero required approving reviews, and no controlled standing bypass actor.

Protection verification is tracked at two levels:

- **Exact live-ruleset configuration inspection:** last completed 2026-08-14, when the live ruleset object was read field-by-field and matched to the controlled target.
- **Operational re-verification:** completed 2026-08-24. GitHub reported `main` as protected; current head PR #54 merged through the PR path after successful `Validate Aramyst Assets` run #128; its resulting `main` commit is single-parent and consistent with the linear squash workflow; no operational drift was observed.

The connected GitHub interface used for the 2026-08-24 audit does not expose the repository-ruleset read endpoint. Its branch endpoint exposes `protected: true` but not the ruleset's internal parameters. Therefore this baseline does not falsely re-date the last exact configuration inspection. Non-observable fields remain controlled by `.github/rulesets/protect-main.json` and the policy until a later exact live-ruleset read confirms them again.

The normal publication path remains: scoped branch → pull request → successful `validate` gate → resolved review threads → protected merge to `main`.

## CI architecture

`.github/workflows/validate-assets.yml` is the controlling workflow. It runs on pull requests, pushes to `main`, and manual dispatch; uses Python 3.12; installs pinned validation dependencies; compiles all validators; runs the regression suite; validates manifest/filesystem/dependency state; and validates approved-asset provenance.

The current control surface is organized into the coordinated layers below. The heading count is not an independent control inventory; the workflow, schemas, validator scripts, and tests are authoritative for what actually runs.

### 1. Manifest schema and registry semantics

Owned primarily by `schemas/asset-manifest.schema.json` and `scripts/validate_manifest.py`.

CI enforces schema validity, Asset-ID/category/version/status structure, required semantic fields, source-location rules, page rules, path/filename rules, JSON/CSV synchronization, and presence of registered Asset IDs in the human-readable registry.

### 2. Registry-to-filesystem integrity

Owned by `scripts/validate_manifest.py` and `schemas/filesystem-integrity-allowlist.json`.

Materialized registered files must exist where required; materialized page/export paths must agree; unexplained files inside asset-owned directories fail validation; explicit superseded/provenance exceptions require the allowlist; and active materialized paths may not point at allowlisted historical files.

### 3. Dependency governance

Owned by `docs/DEPENDENCY_GOVERNANCE_POLICY.md`, the external-authority registry, the dependency-classification registry, their schemas, `scripts/validate_manifest.py`, and regression tests.

CI enforces registered `AST-*` asset edges, exact external authority IDs, bounded external authority ranges, controlled records for title-bound/composite/long-term prose dependencies, exact permitted Asset-ID use, registry/manifest occurrence synchronization, cited evidence-path existence, and registry-schema validity.

CI does not infer prose semantics, choose dependency classes, decide scope equivalence, or invent authority IDs. Those remain human authority judgments.

### 4. Objective asset-governance invariants

Owned by `scripts/check_asset_governance.py` and `tests/test_asset_governance.py`.

Regression-backed checks enforce that:

- a Drive-backed asset carries `drive_file_id`, `drive_url`, and `drive_path` together;
- Drive URLs use HTTPS on `docs.google.com` or `drive.google.com` and identify the recorded Drive file ID;
- an explicit `v###` token in a concrete GitHub source/export filename agrees with the manifest version;
- `approved`, `exported`, and `published` assets do not directly contradict their promoted status with approval text stating `not approved`.

Material-change significance, strict lifecycle-transition matrices, and substantive approval sufficiency remain human-governed because the repository has not adopted objective structured data that can decide them safely.

### 5. Approved-asset provenance

Owned by `docs/APPROVED_ASSET_PROVENANCE.md`, `schemas/approved-asset-provenance.schema.json`, `scripts/validate_approved_provenance.py`, `tests/test_approved_provenance.py`, and `provenance/*.json`.

Every `approved`, `exported`, or `published` asset must have exactly one schema-valid provenance sidecar. CI cross-checks Asset ID, version, status, Drive file ID, GitHub source/export paths, approval-date/evidence bindings, and repository-verifiable hashes.

The contract distinguishes `google_drive` masters from `github` masters. GitHub can recompute repository-side hashes; for private Drive masters it validates the expected SHA-256 contract bound to the exact Drive identity without claiming to re-download the binary during Actions.

Promotion to `approved`, `exported`, or `published` must add or update the provenance sidecar in the same controlled change set.

## Contributor and PR control

`.github/PULL_REQUEST_TEMPLATE.md` is the contributor-facing dependency-governance review surface. It distinguishes human semantic review, CI-backed authority/classification checks, evidence existence versus evidence substance, and the required validation gate.

A separate diff-aware dependency checker is intentionally absent. The 2026-08-18 checklist audit established that objective repository-state invariants are already enforced by the end-state validator; remaining checklist questions require semantic judgment. Add diff-aware validation only if a future transition-specific invariant can pass end-state validation yet remains objectively machine-detectable from the PR transition.

## Current machine-readable control inventory

Principal controls:

- `schemas/asset-manifest.schema.json`
- `schemas/approved-asset-provenance.schema.json`
- `schemas/external-authority-registry.json` and its schema
- `schemas/dependency-classification-registry.json` and its schema
- `schemas/filesystem-integrity-allowlist.json`

Validator scripts:

- `scripts/validate_manifest.py`
- `scripts/check_asset_governance.py`
- `scripts/validate_approved_provenance.py`

The regression suite includes dedicated tests for manifest validation, external-authority resolution, dependency governance, asset-governance invariants, and approved provenance.

## Dated-document consolidation audit — 2026-08-18

Stable repository-wide facts from these records are represented in this baseline:

- `docs/GITHUB_BASELINE_BRANCH_STATE_2026-08-18.md` — branch cleanup and the then-verified provenance exceptions; this temporary supplement was removed after fold-back.
- `docs/GOVERNANCE_MACHINE_ENFORCEMENT_AUDIT_2026-08-18.md` — objective asset-governance controls and semantic boundaries.
- `docs/PR_CHECKLIST_MACHINE_ENFORCEMENT_AUDIT_2026-08-18.md` — contributor-checklist/CI boundary and no redundant diff-aware checker.
- `docs/PRE_PROVENANCE_ASSET_PRODUCTION_AUDIT_2026-08-18.md` — completed stale-branch deletion and resulting steady-state exception set at that audit point.
- `docs/REGISTRY_FILESYSTEM_AUDIT_2026-08-15.md` and `docs/DEPENDENCY_VOCABULARY_AUDIT_2026-08-15.md` — repository-wide outcomes now represented by active CI controls.

These remain historical evidence; any fixed counts or inventories they contain are point-in-time observations unless a current policy or registry explicitly incorporates them.

The following stay outside the general baseline because they are asset-, authority-, or gate-specific evidence:

- `docs/MAP_ENV_001_RECONCILIATION_2026-08-16.md`
- `docs/MAP_REG_001_GEOMETRY_AUTHORITY_RECONCILIATION_2026-08-16.md`
- `docs/SCENE_01_CANON_DEPENDENCY_RECONCILIATION_2026-08-16.md`
- `docs/SUBJECT_CONTINUITY_GATE_AUDIT_2026-08-16.md`
- `docs/BROAD_DESCRIPTIVE_GATE_AUDIT_2026-08-16.md`
- `docs/SCENE_01_IN_PROGRESS_PROVENANCE_READINESS_AUDIT_2026-08-18.md`

Current asset status remains in the registries; current dependency membership/classification remains in the manifest and dependency registries; current provenance coverage remains in the manifest plus validated provenance sidecars; current provenance requirements remain in the controlling provenance policy.

## Baseline health

Status: **controlled**.

At the 2026-08-24 refresh snapshot, strengths include explicit GitHub/Drive ownership, live `main` protection reporting, synchronized protection target files, current operational PR/CI verification, synchronized registries, schema-enforced manifest structure, automated filesystem integrity, CI-enforced dependency governance, objective Drive/version/approval consistency checks, schema-governed approved provenance, contributor-facing dependency review boundaries, explicitly enumerated persistent non-`main` provenance refs, and no open repository-control issue or PR blocker before this refresh branch was created.

No operational branch-protection drift or other unresolved repository-control warning was identified by this refresh. Exact live-ruleset field inspection remains dated 2026-08-14 until the ruleset-read endpoint is available again; this is a verification-scope limitation, not evidence of a configuration defect.

## Change-control rules

Until explicitly superseded:

1. Treat `main` as the authoritative repository branch.
2. Use scoped `agent/<scope>` branches for substantive changes.
3. Merge only through the protected PR path after `validate` succeeds.
4. Do not modify canon, approval state, geography authority, mechanics, or manuscript prose without prior project authorization.
5. Keep registry mirrors synchronized for every relevant asset change.
6. Classify dependencies before registry entry; never mint an authority ID merely for neatness or CI convenience.
7. Add/update approved provenance in the same PR that promotes or materially changes a controlled approved/exported/published asset.
8. Preserve explicitly classified historical-provenance branches/files unless later deletion/archive authority supersedes that disposition.
9. Treat closed issues, superseded PRs, and dated audits as historical records unless a current controlling policy or registry explicitly incorporates their result.
10. Record unresolved cross-system conflicts as blockers rather than guessing which source is correct.

## Periodic baseline refresh rule

Refresh this file whenever repository ownership, source-of-truth boundaries, branch-protection architecture, CI/validator architecture, dependency-governance architecture, approved-provenance architecture, persistent branch exceptions, issue-control state, or release structure changes materially.

During each refresh:

1. verify live branch/PR/issue state;
2. review new dated audits for stable repository-wide current facts;
3. fold those stable facts into this baseline;
4. leave dated audits as evidence rather than competing current-state sources;
5. remove temporary `GITHUB_BASELINE_*` supplements after fold-back;
6. avoid duplicating volatile asset, dependency, provenance, or other machine-registry membership counts;
7. record branch/PR/issue values only as dated live-state snapshots and re-verify them before action;
8. distinguish exact branch-protection configuration inspection from operational protection verification, and do not re-date unobserved rule fields;
9. create a new baseline supplement only when the baseline itself cannot be updated in the same controlled change, and give that supplement an explicit fold-back target.

This process makes `docs/GITHUB_BASELINE.md` the durable current-state control surface while retaining dated audits for traceability.
