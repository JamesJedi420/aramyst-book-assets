# Governance Machine-Enforcement Audit — 2026-08-18

Status: **CONTROL AUDIT — COMPLETE**

## Scope

Audit remaining repository-governance rules that exist primarily in prose and determine whether any objective end-state invariant is not yet represented in CI. Primary review targets:

- `docs/SOURCE_OF_TRUTH.md`;
- `docs/NAMING_AND_VERSIONING.md`;
- `schemas/asset-manifest.schema.json`;
- `scripts/validate_manifest.py` and current regression tests.

This audit does not attempt to infer creative approval, canon correctness, or whether a change is materially significant.

## Existing controls already machine-enforced

Current CI already enforces, among other controls:

- valid Asset IDs, categories, statuses, and `v###` version syntax;
- JSON/CSV synchronization for status, version, source/export paths, approval text, and other operational fields;
- presence of at least one source locator;
- paired Drive file ID and URL;
- GitHub export paths for `exported` and `published` assets;
- materialized GitHub source/export file existence for review/approved/exported/published states;
- page/export agreement and materialized page existence;
- schema, dependency-governance, and filesystem-integrity controls.

## Newly identified objective gaps

Four end-state invariants were sufficiently explicit and objective to enforce without interpreting prose semantics.

### 1. Complete Drive locator bundle

When any Drive locator is present, the record must contain all three:

- `drive_file_id`;
- `drive_url`;
- `drive_path`.

Previously the validator paired only file ID and URL. A missing Drive path could therefore survive despite the source-of-truth policy treating Drive path as part of the synchronized source record.

### 2. Drive URL host and identity

A Drive-backed asset's URL must:

- use HTTPS;
- use `docs.google.com` or `drive.google.com`;
- identify the recorded `drive_file_id` in the URL path.

This prevents a syntactically populated but non-Drive or unrelated source URL from satisfying the source-authority record.

### 3. Explicit filename version agreement

If a concrete `github_source_path` or `github_export_path` filename contains an explicit `v###` token, that token must equal the asset's manifest `version`.

This is intentionally conditional. Files without an explicit version token are not rejected because the repository does not currently require every concrete source/export filename to carry one.

### 4. Direct promoted-status approval contradiction

An asset with status `approved`, `exported`, or `published` may not carry approval text containing the direct statement `not approved`.

CI does not decide whether arbitrary approval prose is substantively adequate. It rejects only this explicit machine-detectable contradiction.

## Implementation

These checks are implemented in `scripts/check_asset_governance.py` and covered by `tests/test_asset_governance.py`.

The normal workflow already runs every `tests/test_*.py` regression test, so the current repository must satisfy these invariants and deliberately invalid fixtures must be rejected before the required `validate` job passes.

The supplemental checker is deliberately narrow. It does not duplicate schema, dependency, filesystem, or registry-mirror logic already owned by `scripts/validate_manifest.py`.

## Controls deliberately not converted into CI rules

### Material change → version increment

`docs/SOURCE_OF_TRUTH.md` and `docs/NAMING_AND_VERSIONING.md` require a version increment for a material asset change and identify examples of material versus metadata-only changes.

This remains human-governed because determining whether a change affects composition, visual direction, canon interpretation, publication role, or approval-significant presentation is semantic. A generic diff cannot reliably distinguish a true material asset change from a metadata/provenance correction.

A machine rule here would either miss material changes or force unnecessary version bumps for allowed metadata-only changes.

### Strict status-transition state machine

The naming/version policy labels `planned → briefed → wip → review → approved → exported → published` as the **normal production flow**, not an exhaustive mandatory transition matrix.

Current authorized work also demonstrates that a direct promotion such as `in-progress → approved` can be legitimate when explicit approval has already occurred outside the repository and the PR is synchronizing that approved state.

CI therefore must not reject skipped intermediate statuses unless the project separately adopts a strict transition policy.

### Approval sufficiency

The source-of-truth policy states that approval ambiguity blocks promotion to `approved`, `exported`, or `published`. Whether evidence actually resolves that ambiguity requires human review of the controlling approval source. CI can reject a direct contradiction but cannot determine that arbitrary prose constitutes sufficient creative/canon approval.

### Source-sidecar semantic synchronization

Several approved assets have GitHub source/provenance records that state version, Drive identity, approval, dimensions, hashes, or visual authority ceilings. These sidecars do not yet share a formal machine-readable schema or one mandatory metadata format across asset categories.

CI should not parse free-form Markdown heuristically. If the project later standardizes promoted-source metadata as structured JSON/YAML or a fixed front matter contract, exact source-record synchronization becomes a strong future machine-enforcement candidate.

## Result

**PASS WITH FOUR NEW OBJECTIVE CI CONTROLS.**

The remaining unautomated governance rules require semantic judgment or a stricter policy/data model that the repository does not currently possess. They are intentionally not converted into guessed machine rules.

## Reopen conditions

Revisit transition/lifecycle automation when any of the following occurs:

1. the project approves an explicit allowed status-transition matrix rather than a normal-flow guideline;
2. material-version triggers are represented by objective structured fields or approved change classes;
3. approval evidence receives a structured machine-readable authority record with required fields;
4. promoted source/provenance records adopt a single structured metadata contract that can be compared exactly with the manifest.
