# Aramyst Source of Truth

Status: **CONTROLLING cross-system ownership and synchronization policy**

This document defines which system owns each type of Aramyst project information and how Google Drive and GitHub remain synchronized. `docs/GITHUB_BASELINE.md` records the current repository-control state; this file remains controlling for the GitHub/Drive ownership boundary.

## Systems

### GitHub

GitHub owns stable production-asset identity, asset status and version, machine-readable repository control records, dependency admission records, approved-asset provenance sidecars, naming/version rules, validation, publication paths, fixed-layout page order, and promoted release-ready repository exports.

GitHub does **not** originate story canon, geography authority, mechanics, manuscript prose, creative approval, or publication identity merely because those decisions are referenced by repository records.

### Google Drive

Google Drive owns manuscript prose, research and source notes, editable working documents, working briefs, review material, and working art before repository promotion unless a specific controlling repository record says otherwise.

An approved binary/master may remain in Drive. The approved-provenance contract records whether the authoritative master is in `google_drive` or `github`; promotion does not require moving a Drive master into GitHub.

Canonical Drive root:

- Folder: `Aramyst`
- Folder ID: `1IBbWIFfAuJpB7I9jc7yrjb461mPnuGnq`

## Canonical GitHub Control Surface

Current repository-wide control state is summarized in:

- `docs/GITHUB_BASELINE.md` — current repository-control baseline.

Core policies:

- `docs/SOURCE_OF_TRUTH.md` — cross-system ownership and synchronization;
- `docs/NAMING_AND_VERSIONING.md` — naming, status, version, and page-order rules;
- `docs/DEPENDENCY_GOVERNANCE_POLICY.md` — dependency classification and admission;
- `docs/APPROVED_ASSET_PROVENANCE.md` — provenance requirements for `approved`, `exported`, and `published` assets;
- `docs/MAIN_PROTECTION_POLICY.md` — protected `main` workflow;
- `docs/VISUAL_STYLE_GUIDE.md` — visual-production direction.

Asset registries and machine-readable controls:

- `manifest.json` — machine-readable asset and page authority;
- `ASSET_MANIFEST.csv` — operational mirror;
- `docs/ASSET_MANIFEST.md` — human-readable asset registry;
- `schemas/asset-manifest.schema.json` — manifest structural contract;
- `schemas/external-authority-registry.json` and its schema — durable non-asset authority ID/range resolution;
- `schemas/dependency-classification-registry.json` and its schema — controlled records for title-bound, composite, and long-term prose dependencies;
- `schemas/filesystem-integrity-allowlist.json` — explicit superseded/provenance filesystem exceptions;
- `schemas/approved-asset-provenance.schema.json` and `provenance/*.json` — approved-asset provenance contract and per-asset sidecars.

Validation and contributor controls:

- `scripts/validate_manifest.py` — manifest, registry, filesystem, and dependency-governance validation;
- `scripts/check_asset_governance.py` — objective Drive/version/approval consistency checks exercised by regression tests;
- `scripts/validate_approved_provenance.py` — approved-provenance validation;
- `.github/workflows/validate-assets.yml` — protected full validation workflow;
- `.github/PULL_REQUEST_TEMPLATE.md` — contributor-facing dependency-governance and validation review surface.

Dated audits and reconciliations are evidence records. They may support a policy, registry entry, or asset decision, but they do not become parallel repository-wide current-state baselines unless a controlling policy explicitly incorporates their result.

## Ownership Matrix

| Information | Canonical system |
|---|---|
| Asset IDs | GitHub |
| Asset status and version | GitHub |
| Machine-readable asset/page records | GitHub `manifest.json` |
| Human-readable asset records | GitHub `docs/ASSET_MANIFEST.md` |
| Operational tracking table | GitHub `ASSET_MANIFEST.csv` |
| Naming and version rules | GitHub |
| Dependency representation/admission records | GitHub |
| Durable external-authority resolution records | GitHub |
| Approved-asset provenance sidecars | GitHub |
| Fixed-layout page order | GitHub `manifest.json` |
| Visual style rules | GitHub |
| Manuscript prose | Google Drive |
| Research and source notes | Google Drive |
| Asset briefs and generation prompts | Google Drive unless explicitly promoted to GitHub |
| Editable working art | Google Drive until repository promotion unless the approved master is repository-native |
| Review and QA records | Google Drive by default; GitHub when explicitly promoted as controlled evidence |
| Approved binary/master | Drive or GitHub as declared by the approved-provenance sidecar |
| Approved release-ready repository exports | GitHub |
| Superseded working material | Google Drive archive by default; GitHub only when deliberately retained as controlled provenance/superseded history |

## Registry and Cross-System Fields

`schemas/asset-manifest.schema.json` defines the exact structural contract and nullability for registered asset fields. Cross-system synchronization uses, among other fields:

```text
asset_id
title
category
context
status
version
drive_file_id
drive_url
drive_path
github_source_path
github_export_path
owner
dependencies
approval
```

An asset must have at least one valid source locator as allowed by the manifest contract.

If any Drive locator is present, the controlled Drive locator bundle is:

- `drive_file_id`;
- `drive_url`;
- `drive_path`.

The Drive URL must identify the recorded Drive file ID and use the supported Google Drive/Docs HTTPS host. These objective relationships are regression-enforced by the repository governance checks.

Assets with status `exported` or `published` must have the repository export path required by the manifest rules. Every asset in `approved`, `exported`, or `published` state must also have exactly one valid `provenance/*.json` sidecar under `docs/APPROVED_ASSET_PROVENANCE.md`.

## Dependency Authority and Synchronization

Every dependency must be classified before registry entry under `docs/DEPENDENCY_GOVERNANCE_POLICY.md` as one of:

- `asset_edge`;
- `external_authority`;
- `title_bound_authority`;
- `composite_gate`;
- `long_term_prose_gate`.

Repository maintenance must not invent authority IDs merely to make a dependency machine-resolvable.

Durable external IDs/ranges must resolve through `schemas/external-authority-registry.json`. Title-bound, composite, and long-term prose dependencies require exact controlled records in `schemas/dependency-classification-registry.json`, including their authorized Asset-ID use and evidence linkage.

Dependency changes must keep the manifest and CSV representations synchronized and must update the relevant control registry in the same change set when required by the dependency class.

## Synchronization Rules

When a registered asset changes materially:

1. Keep its existing Asset ID unless its production identity/approval history must remain independent.
2. Increment its version when the change is materially version-significant under `docs/NAMING_AND_VERSIONING.md`.
3. Update `manifest.json`.
4. Update the matching row in `ASSET_MANIFEST.csv`.
5. Update the matching record in `docs/ASSET_MANIFEST.md` when the human-readable registry is affected.
6. Update Drive and GitHub locators if controlled files moved.
7. Reconcile dependencies under `docs/DEPENDENCY_GOVERNANCE_POLICY.md` when dependency meaning or representation changes.
8. Record approval state accurately.
9. For `approved`, `exported`, or `published` assets, add or update the machine-readable provenance sidecar in the same controlled change set, including required identity, approval evidence/date, master, path, and hash bindings.
10. Pass the complete `Validate Aramyst Assets` workflow before merge.

Materiality and substantive approval sufficiency remain human judgments. CI enforces the objective structured representation after those decisions are made; it does not decide canon or creative approval.

## Status Authority

The status stored in GitHub is authoritative.

- `planned` — identified, requirements incomplete
- `briefed` — purpose and requirements defined
- `in-progress` — active production
- `review` — submitted for review
- `approved` — creative and canon approval complete
- `exported` — release-ready output exists
- `published` — included in a released product
- `superseded` — replaced by another version or asset
- `archived` — retained only for history

The documented lifecycle is not, by itself, a strict machine transition matrix. An authorized synchronization may legitimately skip intermediate statuses when the controlling approval/state already exists outside GitHub. Approval ambiguity still blocks promotion.

A Drive filename containing words such as `FINAL`, `ACTIVE`, or `WORKING` does not override GitHub status.

## Page Assembly Authority

`manifest.json` is the source of truth for fixed-layout page order.

- Page numbers are unique integers.
- Page filenames use three-digit prefixes.
- A page move requires updating both the filename and `manifest.json`.
- Materialized exported or published pages must exist at their recorded repository path.
- `.b64` wrappers retain the original extension before `.b64`.

## Promotion and Approved-Provenance Gate

A working asset may remain Drive-only while it is `briefed`, `in-progress`, or `review` when the manifest and filesystem rules permit that state.

Before an asset enters `approved`, `exported`, or `published` status in GitHub:

1. Establish explicit approval and identify the authoritative master.
2. Preserve the editable/master file in its controlling system; do not move a Drive master merely to satisfy repository promotion.
3. Create or update required GitHub source/evidence/export files using canonical paths and filenames.
4. Update all affected manifest representations.
5. Create or update exactly one schema-valid `provenance/*.json` sidecar.
6. Bind the sidecar to the exact Asset ID, version, status, Drive identity, GitHub source/export paths, approval date/evidence, master identity, and required hashes.
7. Reconcile dependencies/classification records if the promotion changes any dependency state.
8. Pass `Validate Aramyst Assets` before merge.

A downgrade or removal from the controlled promoted states must remove or deliberately migrate the provenance sidecar so the sidecar set remains synchronized with current manifest status.

For `google_drive` masters, GitHub CI verifies the Drive identity and recorded expected SHA-256 contract but does not claim to download the private Drive binary during Actions. Repository-side source/export hashes are recomputed where the provenance contract requires them.

## Supersession and Historical Provenance

Google Drive remains the default archive for superseded working material. GitHub may retain superseded or provenance material when it is necessary for approval, QA, implementation, or development history.

Within asset-owned repository directories, otherwise-unregistered superseded/provenance files require an explicit entry in `schemas/filesystem-integrity-allowlist.json`. Active materialized registry paths may not point at files classified as historical exceptions.

Historical branches may also be deliberately preserved after audit. Their continued existence does not make them authoritative production sources.

## Validation Authority

The protected validation path is `.github/workflows/validate-assets.yml`, not a single local script invocation.

The workflow currently:

1. checks out the repository;
2. installs pinned validation dependencies;
3. compiles the validator scripts;
4. runs the complete regression suite;
5. runs `scripts/validate_manifest.py` for manifest/registry/filesystem/dependency controls;
6. runs `scripts/validate_approved_provenance.py` for promoted-asset provenance.

`scripts/check_asset_governance.py` is exercised through the regression suite and enforces the approved objective governance invariants there.

Local validators are useful diagnostics, but a substantive merge must pass the protected GitHub Actions `validate` job.

## Conflict Resolution

When records disagree:

1. Asset identity, status, version, and page order follow the GitHub registries.
2. Dependency representation and classification follow the controlling dependency policy and machine-readable authority/classification registries.
3. For `approved`, `exported`, or `published` assets, provenance-sidecar bindings must agree with the manifest and controlled evidence; a mismatch blocks merge/promotion.
4. Manuscript wording, research/source-note content, and unpromoted working-document content follow Drive.
5. Approval ambiguity blocks promotion to `approved`, `exported`, or `published`.
6. A Drive binary/master mismatch against its recorded provenance hash must be resolved and, when materially changed, reapproved/versioned as required before the asset is treated as synchronized.
7. Conflicts must be corrected in all affected mirrors/control records before production continues. Do not guess or silently normalize authority.

## Change Log

| Date | Change | Author |
|---|---|---|
| 2026-08-04 | Established GitHub and Google Drive source-of-truth boundaries. | JamesJedi420 / ChatGPT |
| 2026-08-18 | Refreshed canonical GitHub control inventory, dependency-governance synchronization, objective governance checks, approved-provenance promotion rules, historical-provenance exceptions, and full CI authority while preserving the existing GitHub/Drive ownership model. | JamesJedi420 / ChatGPT |
