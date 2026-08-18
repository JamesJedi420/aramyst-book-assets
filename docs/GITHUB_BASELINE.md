# Aramyst GitHub Baseline

Status: **CONTROLLED — current repository-control baseline**

Baseline established: 2026-08-14
Last refreshed: 2026-08-18
Repository: `JamesJedi420/aramyst-book-assets`
Default branch: `main`
Visibility: public
Canonical Drive root: `1IBbWIFfAuJpB7I9jc7yrjb461mPnuGnq`

## Purpose

This file is the single current-state entry point for GitHub repository control. It records the repository's present operating model, control architecture, branch state, CI responsibilities, and maintenance rules.

Dated audits and reconciliations remain historical evidence. They do not override this baseline merely because they contain later-looking prose. When a dated audit establishes a stable repository-wide control, that current-state fact should be folded into this file during the next baseline refresh while the dated audit remains as evidence of how the decision was reached.

Git history preserves earlier baseline snapshots. This file is intentionally current-state oriented rather than a chronological log of every prior repository condition.

## Documentation authority model

Current repository-control state is read in this order:

1. `docs/GITHUB_BASELINE.md` — current repository-control baseline.
2. Controlling domain policies — authoritative within their specific scope:
   - `docs/SOURCE_OF_TRUTH.md`;
   - `docs/NAMING_AND_VERSIONING.md`;
   - `docs/DEPENDENCY_GOVERNANCE_POLICY.md`;
   - `docs/APPROVED_ASSET_PROVENANCE.md`;
   - `docs/MAIN_PROTECTION_POLICY.md`;
   - `docs/VISUAL_STYLE_GUIDE.md` where visual-production rules are involved.
3. Machine-readable registries, schemas, validators, workflow configuration, and the PR template — authoritative for the exact state they encode and enforce.
4. Dated audits/reconciliations — evidence records, not parallel current-state baselines.

Asset-specific audits remain authoritative evidence for the classifications or reconciliations they establish where a controlling registry or policy explicitly cites them, but they do not become general repository-control documents.

## Source-of-truth boundary

`docs/SOURCE_OF_TRUTH.md` remains controlling for GitHub/Drive ownership.

GitHub owns stable asset identity, status, version, machine-readable records, naming/version rules, validation, repository paths, fixed-layout page order, dependency admission records, approved provenance sidecars, and promoted release-ready repository exports.

Google Drive owns manuscript prose, research/source notes, editable working documents, working briefs, review material, and working art before repository promotion unless a specific controlling record states otherwise.

GitHub maintenance must not independently create or revise story canon, geography authority, mechanics, manuscript prose, creative approval, or publication identity. GitHub records already-authorized project decisions and enforces repository consistency around them.

## Registry authority

Current asset state is owned by the registries, not by counts copied into this baseline:

- `manifest.json` — machine-readable asset/page authority;
- `ASSET_MANIFEST.csv` — synchronized operational mirror;
- `docs/ASSET_MANIFEST.md` — synchronized human-readable registry.

The baseline deliberately does not duplicate a current planned/in-progress/approved count because those values change with legitimate production work and are already machine-governed. Historical counts remain available in Git history and dated audit records.

A material asset change retains the Asset ID, follows the approved versioning rules, synchronizes all required registry representations, and passes CI. A new Asset ID is created only when production identity or approval history must remain independent.

## Current branch, PR, and issue state

Verified on 2026-08-18 before this refresh branch was created:

- `main` — authoritative protected production branch;
- `agent/map-hou-001-functional-adjacency` — intentional historical-provenance exception;
- `agent/q-023-cross-system-sync` — intentional historical-provenance exception;
- zero open pull requests;
- zero open issues.

`agent/continuity-gate-audit` was audited, confirmed to have no unique commits ahead of `main`, explicitly authorized for deletion, deleted through the GitHub UI, and verified absent afterward.

The two surviving non-`main` refs are the only persistent branch exceptions. They are non-authoritative historical records and must not be used as bases for new production work:

- `agent/map-hou-001-functional-adjacency` preserves unique superseded PR #4 schematic/QA history;
- `agent/q-023-cross-system-sync` preserves unique superseded PR #11 implementation/reconciliation history.

Routine `agent/<scope>` branches are ephemeral. After their work merges or is abandoned, they should be removed unless a specific preservation audit establishes a new historical-provenance exception.

Closed issues and superseded PR bodies are point-in-time historical records. Stale warning language inside them does not create a current blocker.

## Main protection

GitHub currently reports `main` as protected. `docs/MAIN_PROTECTION_POLICY.md` and `.github/rulesets/protect-main.json` record the controlled protection design; the last full ruleset verification was 2026-08-14.

The protected workflow requires the normal publication path to use pull requests and the `validate` GitHub Actions job. The controlled design also requires review-thread resolution, up-to-date validation before merge, linear history, force-push prevention, deletion restriction, and no standing bypass actor.

Substantive repository maintenance therefore uses a scoped `agent/<scope>` branch and merges only after the protected validation gate succeeds.

## CI architecture

`.github/workflows/validate-assets.yml` is the controlling workflow. It runs on pull requests, pushes to `main`, and manual dispatch; uses Python 3.12; installs pinned validation dependencies; compiles all validators; runs the complete regression suite; validates the registries/filesystem/dependency state; and validates approved-asset provenance.

The current control surface is best understood as five coordinated layers.

### Layer 1 — manifest schema and registry semantics

Owned primarily by `schemas/asset-manifest.schema.json` and `scripts/validate_manifest.py`.

CI enforces schema validity, Asset-ID/category/version/status structure, required semantic fields, source-location rules, page rules, filename/path rules, JSON/CSV synchronization, and presence of registered Asset IDs in the human-readable manifest.

### Layer 2 — registry-to-filesystem integrity

Owned by `scripts/validate_manifest.py` plus `schemas/filesystem-integrity-allowlist.json`.

Materialized registered files must exist where required; materialized page/export paths must agree; unexplained files inside asset-owned directories fail validation; and explicit superseded/provenance exceptions are allowed only through the machine-readable allowlist. Active asset paths may not point at allowlisted superseded/provenance files.

### Layer 3 — dependency governance

Owned by `docs/DEPENDENCY_GOVERNANCE_POLICY.md`, `schemas/external-authority-registry.json`, `schemas/dependency-classification-registry.json`, their schemas, `scripts/validate_manifest.py`, and the dependency regression tests.

CI enforces:

- registered `AST-*` asset edges;
- exact external authority IDs;
- bounded external authority ranges;
- exact controlled records for title-bound, composite, and long-term prose dependencies;
- exact permitted Asset-ID use for prose dependencies;
- classification-registry/manifest occurrence synchronization;
- existence of cited evidence paths;
- schema validity for the classification and external-authority registries.

CI does not decide prose semantics, invent authority IDs, or determine scope equivalence. Those remain human authority judgments under the controlling policy.

### Layer 4 — objective asset-governance invariants

Owned by `scripts/check_asset_governance.py` and `tests/test_asset_governance.py`.

Regression-backed checks enforce that:

- a Drive-backed asset carries `drive_file_id`, `drive_url`, and `drive_path` together;
- Drive URLs use HTTPS on `docs.google.com` or `drive.google.com` and identify the recorded Drive file ID;
- an explicit `v###` token in a concrete GitHub source/export filename agrees with the manifest version;
- `approved`, `exported`, and `published` assets do not directly contradict their promoted status with approval text stating `not approved`.

Material-change significance, strict lifecycle-transition matrices, and substantive approval sufficiency remain human-governed because the repository has not adopted objective data capable of deciding them safely.

### Layer 5 — approved-asset provenance

Owned by `docs/APPROVED_ASSET_PROVENANCE.md`, `schemas/approved-asset-provenance.schema.json`, `scripts/validate_approved_provenance.py`, `tests/test_approved_provenance.py`, and `provenance/*.json`.

Every asset in `approved`, `exported`, or `published` state must have exactly one schema-valid provenance sidecar. CI cross-checks the sidecar against the manifest for Asset ID, version, status, Drive file ID, GitHub source path, and GitHub export path; validates approval-date/evidence bindings; and recomputes repository-verifiable hashes.

The provenance contract explicitly distinguishes `google_drive` masters from `github` masters. For Drive masters, GitHub records and validates the expected SHA-256 contract bound to the exact Drive identity but does not claim to re-download private Drive binaries during Actions. For GitHub masters and repository source/export bindings, supported hashes are recomputed in CI.

Promotion to `approved`, `exported`, or `published` must therefore add/update the provenance sidecar in the same controlled approval change set.

## Contributor and PR control

`.github/PULL_REQUEST_TEMPLATE.md` is the contributor-facing dependency-governance review surface.

The checklist distinguishes:

- human semantic review;
- CI-backed authority resolution and classification synchronization;
- evidence existence checked by CI versus evidence substance checked by humans;
- the required `Validate Aramyst Assets` gate.

A separate diff-aware dependency checker is intentionally not present. The 2026-08-18 checklist audit established that the objective repository-state invariants are already enforced by the end-state validator, while the remaining checklist questions require semantic judgment. A future diff-aware check should be added only for a concrete transition invariant that can pass the end-state validator yet is still objectively machine-detectable from the PR transition.

## Current machine-readable control inventory

The principal schema/registry controls are:

- `schemas/asset-manifest.schema.json`;
- `schemas/approved-asset-provenance.schema.json`;
- `schemas/external-authority-registry.json` and its schema;
- `schemas/dependency-classification-registry.json` and its schema;
- `schemas/filesystem-integrity-allowlist.json`.

The current validator scripts are:

- `scripts/validate_manifest.py`;
- `scripts/check_asset_governance.py`;
- `scripts/validate_approved_provenance.py`.

The regression suite currently includes dedicated tests for manifest validation, external-authority resolution, dependency governance, asset-governance invariants, and approved provenance.

## Dated-document consolidation audit — 2026-08-18

The documentation audit classified the current dated records as follows.

### Current-state facts folded into this baseline

- `docs/GITHUB_BASELINE_BRANCH_STATE_2026-08-18.md` — branch cleanup and the two historical-provenance exceptions. This temporary supplement is redundant after this refresh and should be removed in the same PR.
- `docs/GOVERNANCE_MACHINE_ENFORCEMENT_AUDIT_2026-08-18.md` — the four objective asset-governance controls and the explicit semantic boundary.
- `docs/PR_CHECKLIST_MACHINE_ENFORCEMENT_AUDIT_2026-08-18.md` — the contributor-checklist/CI boundary and the decision not to add redundant diff-aware validation.
- `docs/PRE_PROVENANCE_ASSET_PRODUCTION_AUDIT_2026-08-18.md` — completed deletion of the stale continuity-audit ref and the resulting steady-state branch exception set.
- `docs/REGISTRY_FILESYSTEM_AUDIT_2026-08-15.md` and `docs/DEPENDENCY_VOCABULARY_AUDIT_2026-08-15.md` — their stable repository-wide outcomes were already represented by filesystem and dependency CI and are reaffirmed here.

These dated records remain historical evidence except for the branch-state supplement, whose purpose is exhausted by this refresh.

### Evidence that should remain outside the baseline

The following are intentionally not folded into general repository-control state because they are asset-, authority-, or gate-specific evidence:

- `docs/MAP_ENV_001_RECONCILIATION_2026-08-16.md`;
- `docs/MAP_REG_001_GEOMETRY_AUTHORITY_RECONCILIATION_2026-08-16.md`;
- `docs/SCENE_01_CANON_DEPENDENCY_RECONCILIATION_2026-08-16.md`;
- `docs/SUBJECT_CONTINUITY_GATE_AUDIT_2026-08-16.md`;
- `docs/BROAD_DESCRIPTIVE_GATE_AUDIT_2026-08-16.md`;
- `docs/SCENE_01_IN_PROGRESS_PROVENANCE_READINESS_AUDIT_2026-08-18.md`.

Their continuing value is evidentiary and asset-specific. Current asset status remains in the registries; current dependency admission remains in the classification registry; current provenance requirements remain in the controlling provenance policy.

## Baseline health

Status: **controlled**.

Current strengths include:

- explicit GitHub/Drive ownership boundaries;
- protected authoritative `main`;
- synchronized registry mirrors;
- schema-enforced manifest structure;
- automated filesystem integrity;
- CI-enforced dependency governance;
- objective Drive/version/approval consistency checks;
- schema-governed approved-asset provenance and repository hash verification;
- contributor-facing dependency review boundaries;
- only two intentional persistent non-`main` provenance refs;
- no current open repository-control issue or PR blocker at the start of this refresh.

No unresolved repository-control warning is identified by this consolidation audit.

## Change-control rules

Until explicitly superseded:

1. Treat `main` as the authoritative repository branch.
2. Use scoped `agent/<scope>` branches for substantive changes.
3. Merge only through the protected PR path after `validate` succeeds.
4. Do not modify canon, approval state, geography authority, mechanics, or manuscript prose without prior project authorization.
5. Keep registry mirrors synchronized for every relevant asset change.
6. Apply dependency classification before registry entry; never mint an authority ID merely for neatness or CI convenience.
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
4. leave the dated audit as evidence rather than a competing current-state source;
5. remove temporary `GITHUB_BASELINE_*` supplements once their facts are folded;
6. do not duplicate volatile asset counts or per-asset state already owned by registries;
7. create a new baseline supplement only when the baseline itself cannot be updated in the same controlled change, and give that supplement an explicit fold-back target.

This process makes `docs/GITHUB_BASELINE.md` the durable current-state control surface while retaining dated audits for traceability.