# Aramyst GitHub Baseline

Baseline established: 2026-08-14 09:13 CDT

## Baseline identity

- Repository: `JamesJedi420/aramyst-book-assets`
- Default branch: `main`
- Visibility: public
- Baseline `main` commit: `73ec4650b8c8733f03348e88710d17b223348cd8`
- Repository role: controlled asset registry, machine-readable production metadata, validation, naming/versioning rules, publication paths, and promoted release-ready assets for the Aramyst book project.
- Canonical Drive root recorded by the repository: `1IBbWIFfAuJpB7I9jc7yrjb461mPnuGnq`

## Repository inventory audit

The authenticated account currently owns four repositories:

- `JamesJedi420/aramyst-book-assets`
- `JamesJedi420/containment-protocol`
- `JamesJedi420/dead-air-website`
- `JamesJedi420/tinyfolk-realm-of-giants`

Repository search found no additional installed repositories matching `Aramyst`, `Mystara`, or `Blackmoor`. For this project, `JamesJedi420/aramyst-book-assets` is therefore the current GitHub baseline repository.

## Source-of-truth boundaries

The existing `docs/SOURCE_OF_TRUTH.md` remains controlling.

GitHub owns:

- asset IDs;
- asset status and version;
- `manifest.json`;
- `ASSET_MANIFEST.csv`;
- `docs/ASSET_MANIFEST.md`;
- naming and version rules;
- visual-style rules;
- fixed-layout page order;
- repository paths and promoted release-ready exports.

Google Drive owns:

- manuscript prose;
- research and source notes;
- editable working documents;
- working briefs and generation prompts unless promoted;
- working art prior to repository promotion;
- review and QA records unless explicitly promoted to GitHub.

No GitHub maintenance action should silently create or revise story canon, geography authority, mechanics, manuscript prose, or approval state. GitHub records approved project decisions; it does not originate them.

## Registry snapshot

At the baseline commit, `manifest.json` contained:

- 16 registered assets;
- 7 `planned` assets;
- 6 `in-progress` assets;
- 3 `approved` assets;
- 1 planned fixed-layout page record (`pages/001_cover.png.b64`).

Approved registered assets at that baseline point:

- `AST-MAP-002` — MAP-REG-001 First-Playable Region GM Reference, `v002`;
- `AST-MAP-003` — MAP-ENV-001 Keep / Lower Road / Last-Bell Local GM Schematic, `v001`;
- `AST-MAP-004` — MAP-HOU-001 Last-Bell House Controlling Physical Floorplan, `v001`.

Manual audit confirmed that the same 16 asset IDs were represented in:

- `manifest.json`;
- `ASSET_MANIFEST.csv`;
- `docs/ASSET_MANIFEST.md`.

The registered GitHub source paths for `AST-MAP-002`, `AST-MAP-003`, and `AST-MAP-004` existed on `main`.

`maps/map-reg-001-gm-reference-v001.svg` remains present as superseded historical material, while `v002` is the registered active source.

This section records the original baseline snapshot; later approved asset-state changes are governed by the current registries rather than by these historical counts.

## Repository structure

Current top-level structure includes the controlled registries and category folders expected by the project:

- `.github/`
- `characters/`
- `covers/`
- `docs/`
- `exports/`
- `factions/`
- `locations/`
- `maps/`
- `prompts/`
- `references/`
- `schemas/`
- `scripts/`
- `symbols/`
- `tests/`
- `typography/`
- `ASSET_MANIFEST.csv`
- `README.md`
- `manifest.json`
- `requirements-validation.txt`

Several category folders remain placeholders, which is consistent with the current asset-development stage.

## Branch and pull-request state

At baseline:

- `main` is the default branch.
- One pre-existing non-main branch remained: `agent/map-hou-001-functional-adjacency`.
- PR #5, `Bind approved MAP-HOU-001 FP01-R1 floorplan`, was merged.
- There were no open GitHub issues in this repository.

Post-baseline reconciliation on 2026-08-14:

- PR #4 was reconciled against the approved `MAP-HOU-001 / AST-MAP-004` state.
- Disposition: **SUPERSEDED — closed without merge or rebase**.
- The functional-adjacency schematic was valid as an intermediate requirements visualization while physical geometry was intentionally unresolved.
- `AST-MAP-004` now resolves and controls the physical/topological relationships that PR #4 deliberately left unknown, including room/yard placement, controlled openings, Bell Stair attachment/access, Record Room → Back Archive Loft vertical relation, Burial Court placement/branches, Guest Hall ↔ Kitchen/Winter Store, and Kitchen/Winter Store ↔ Service Yard.
- Merging PR #4 unchanged would create stale authority language beside the approved floorplan; rebasing it into a current diagram would duplicate `AST-MAP-004` rather than preserve an independent production purpose.
- The PR and branch history retain the intermediate artifact for development provenance. No Asset ID is minted for it, and neither proposed file becomes an active source on `main`.
- The historical branch may remain until normal branch cleanup; its presence does not confer active authority.

## Validation and CI state

The repository contains `.github/workflows/validate-assets.yml`.

Current workflow behavior:

- runs on every pull request;
- runs on every push to `main`;
- supports explicit `workflow_dispatch`;
- cancels superseded in-progress validation runs for the same ref;
- uses a five-minute job timeout;
- installs the pinned validation dependency from `requirements-validation.txt`;
- compiles `scripts/validate_manifest.py`;
- runs the JSON Schema enforcement regression tests;
- runs the complete manifest/page-registry validator.

The validator enforces two layers of control.

Layer 1 — machine-readable JSON Schema contract:

- loads `schemas/asset-manifest.schema.json`;
- checks that the schema itself is valid Draft 2020-12 JSON Schema;
- validates `manifest.json` with `jsonschema`'s `Draft202012Validator`;
- reports schema violations with manifest paths;
- fails closed when the required `jsonschema` dependency is unavailable.

Layer 2 — Aramyst repository semantics and cross-file consistency:

- project constants;
- asset-ID/category/version/status formats and category-code agreement;
- required semantic fields;
- Drive/GitHub source-location requirements;
- dependency duplication;
- repository-relative path and filename rules;
- page-number/path/asset-reference rules;
- exported/published page-file presence;
- JSON/CSV registry synchronization;
- presence of every registered asset ID in `docs/ASSET_MANIFEST.md`.

Schema enforcement is regression-tested against the current manifest and against an intentionally invalid copy containing an undeclared top-level property. The latter must be rejected by the schema's `additionalProperties: false` contract.

Post-baseline CI restoration on 2026-08-14:

- PR #8, `Restore reliable GitHub Actions validation`, was merged.
- The prior account-level billing lock stopped blocking runners.
- PR-branch validation completed successfully.
- A fresh `main` push validation after the merge also completed successfully.
- Issue #7, `Restore GitHub Actions account access`, was closed after runner-backed validation was observed.

Branch-protection settings could not be verified through the connected GitHub integration and remain unconfirmed.

## Baseline health

Status: **controlled with one remaining repository-control warning**.

Strengths:

- explicit GitHub/Drive source-of-truth division;
- permanent asset IDs and controlled versions;
- synchronized machine-readable, CSV, and human-readable registries;
- approved map assets retain explicit authority, dependencies, holds, and supersession history;
- repository changes are handled through scoped `agent/` branches and pull requests;
- stale pre-approval PR #4 has been explicitly reconciled and closed as superseded;
- GitHub Actions executes successfully as a real validation gate;
- the JSON Schema is now an enforced machine-readable contract rather than passive documentation;
- schema enforcement has a regression test that proves invalid structure is rejected.

Warning:

1. Branch-protection status is unverified.

## Change-control baseline for this thread

Until superseded by an explicit project decision, GitHub maintenance in this thread should follow these rules:

1. Treat `main` as the authoritative repository branch.
2. Make substantive changes on `agent/<scope>` branches.
3. Default to draft pull requests rather than direct writes to `main`.
4. Do not modify canon or approval state without an already-authorized project decision.
5. When a registered asset changes materially, synchronize `manifest.json`, `ASSET_MANIFEST.csv`, and `docs/ASSET_MANIFEST.md` in the same change set.
6. Preserve superseded assets when they carry approval, QA, or provenance history unless explicit archival/deletion authority is given.
7. Require the GitHub Actions validation gate to pass before merge; reproduce the validator manually only as a diagnostic supplement, not as a replacement for a failed or unavailable gate.
8. Record any unresolved synchronization conflict as a blocker rather than guessing which source is correct.
9. Re-audit this baseline whenever repository ownership, source-of-truth rules, validation architecture, or release structure changes materially.

## Immediate follow-up queue

1. Verify and, if appropriate, establish branch-protection requirements for `main`.
