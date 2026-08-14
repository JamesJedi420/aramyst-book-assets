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

At the baseline commit, `manifest.json` contains:

- 16 registered assets;
- 7 `planned` assets;
- 6 `in-progress` assets;
- 3 `approved` assets;
- 1 planned fixed-layout page record (`pages/001_cover.png.b64`).

Approved registered assets:

- `AST-MAP-002` — MAP-REG-001 First-Playable Region GM Reference, `v002`;
- `AST-MAP-003` — MAP-ENV-001 Keep / Lower Road / Last-Bell Local GM Schematic, `v001`;
- `AST-MAP-004` — MAP-HOU-001 Last-Bell House Controlling Physical Floorplan, `v001`.

Manual audit confirms that the same 16 asset IDs are represented in:

- `manifest.json`;
- `ASSET_MANIFEST.csv`;
- `docs/ASSET_MANIFEST.md`.

The registered GitHub source paths for `AST-MAP-002`, `AST-MAP-003`, and `AST-MAP-004` all exist on `main`.

`maps/map-reg-001-gm-reference-v001.svg` remains present as superseded historical material, while `v002` is the registered active source.

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
- `typography/`
- `ASSET_MANIFEST.csv`
- `README.md`
- `manifest.json`

Several category folders remain placeholders, which is consistent with the current asset-development stage.

## Branch and pull-request state

At baseline:

- `main` is the default branch.
- One pre-existing non-main branch remains: `agent/map-hou-001-functional-adjacency`.
- Draft PR #4, `Review MAP-HOU-001 functional adjacency schematic v001`, remains open.
- PR #4 is 2 commits ahead of and 24 commits behind current `main`.
- PR #5, `Bind approved MAP-HOU-001 FP01-R1 floorplan`, is merged.
- There are no open GitHub issues in this repository.

PR #4 predates the approved controlling physical floorplan registered by PR #5. It must not be merged without an explicit reconciliation decision determining whether its functional-adjacency artifact is still independently useful, should be rebased and retained as historical/supporting material, or should be closed as superseded.

## Validation and CI state

The repository contains `.github/workflows/validate-assets.yml`, which runs `python scripts/validate_manifest.py` for manifest/page-control changes.

The validator currently checks:

- project constants;
- asset-ID/category/version/status formats;
- required fields;
- Drive/GitHub source-location requirements;
- dependency duplication;
- page-number/path rules;
- JSON/CSV registry synchronization;
- presence of every registered asset ID in `docs/ASSET_MANIFEST.md`.

Operational warning: PR #5 records that GitHub Actions could not start because the GitHub account was locked due to a billing issue. No workflow run is attached to the baseline `main` commit. CI therefore cannot currently be treated as an independently verified gate.

Validation coverage warning: `scripts/validate_manifest.py` loads `schemas/asset-manifest.schema.json` only to confirm that it is valid JSON; it does not execute JSON Schema validation against `manifest.json`. The script duplicates many schema checks manually, but the schema is not presently an enforced contract.

Branch-protection settings could not be verified through the connected GitHub integration and remain unconfirmed.

## Baseline health

Status: **controlled with operational warnings**.

Strengths:

- explicit GitHub/Drive source-of-truth division;
- permanent asset IDs and controlled versions;
- synchronized machine-readable, CSV, and human-readable registries;
- approved map assets retain explicit authority, dependencies, holds, and supersession history;
- repository changes are already being handled through scoped `agent/` branches and pull requests;
- validation code and a CI workflow exist.

Warnings:

1. GitHub Actions is not currently functioning as a reliable merge gate because of the reported billing lock.
2. Draft PR #4 is materially behind `main` and predates the controlling MAP-HOU-001 floorplan approval.
3. JSON Schema is documented but not actually enforced by the validator.
4. Branch-protection status is unverified.

## Change-control baseline for this thread

Until superseded by an explicit project decision, GitHub maintenance in this thread should follow these rules:

1. Treat `main` as the authoritative repository branch.
2. Make substantive changes on `agent/<scope>` branches.
3. Default to draft pull requests rather than direct writes to `main`.
4. Do not modify canon or approval state without an already-authorized project decision.
5. When a registered asset changes materially, synchronize `manifest.json`, `ASSET_MANIFEST.csv`, and `docs/ASSET_MANIFEST.md` in the same change set.
6. Preserve superseded assets when they carry approval, QA, or provenance history unless explicit archival/deletion authority is given.
7. Run or manually reproduce the repository validator before merge whenever CI is unavailable.
8. Record any unresolved synchronization conflict as a blocker rather than guessing which source is correct.
9. Re-audit this baseline whenever repository ownership, source-of-truth rules, validation architecture, or release structure changes materially.

## Immediate follow-up queue

1. Reconcile draft PR #4 against the approved MAP-HOU-001 / AST-MAP-004 state before any merge.
2. Restore GitHub Actions execution so `validate-assets.yml` can function as a real gate.
3. Strengthen `scripts/validate_manifest.py` so the JSON Schema is actually enforced or explicitly retire the schema as non-enforcing documentation.
4. Verify and, if appropriate, establish branch-protection requirements for `main`.
