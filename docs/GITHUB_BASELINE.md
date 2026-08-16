# Aramyst GitHub Baseline

Baseline established: 2026-08-14 09:13 CDT
Repository-control audit refreshed: 2026-08-16

## Baseline identity

- Repository: `JamesJedi420/aramyst-book-assets`
- Default branch: `main`
- Visibility: public
- Baseline `main` commit: `73ec4650b8c8733f03348e88710d17b223348cd8`
- Repository role: controlled production-asset registry, machine-readable production metadata, validation, naming/versioning rules, publication paths, and promoted release-ready assets for the standalone TTRPG project currently using `Aramyst` as a temporary development alias.
- Canonical Drive root recorded by the repository: `1IBbWIFfAuJpB7I9jc7yrjb461mPnuGnq`

## Repository inventory audit

The authenticated account currently owns four repositories:

- `JamesJedi420/aramyst-book-assets`
- `JamesJedi420/containment-protocol`
- `JamesJedi420/dead-air-website`
- `JamesJedi420/tinyfolk-realm-of-giants`

Repository search found no additional repository matching the Aramyst/Mystara/Blackmoor project identity. For this project, `JamesJedi420/aramyst-book-assets` remains the GitHub baseline repository.

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

The `schemas/` control surface now includes four distinct machine-readable control roles:

- `asset-manifest.schema.json` — structural contract for `manifest.json`;
- `external-authority-registry.json` plus its schema — durable non-asset authority ID/range resolution;
- `dependency-classification-registry.json` plus its schema — mandatory classification records for title-bound, composite, and long-term prose dependencies;
- `filesystem-integrity-allowlist.json` — explicit superseded/provenance filesystem exceptions.

`schemas/dependency-classification-registry.json` is the required machine-readable record for every current and future dependency classified as `title_bound_authority`, `composite_gate`, or `long_term_prose_gate`. The manifest's prose dependency cannot be treated as admitted merely because it is human-readable; the matching controlled classification record must exist and name the exact Asset IDs authorized to use it.

`schemas/filesystem-integrity-allowlist.json` remains the required mechanism for retaining otherwise-unregistered superseded/provenance files inside asset-owned directories.

## Branch and pull-request state

At the original baseline:

- `main` was the default branch.
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

Repository-hygiene audit on 2026-08-15:

- no open or draft pull requests remained at the close of that audit;
- merged `agent/` branches had already been cleaned up;
- exactly two non-main `agent/` branches remained, both intentionally preserved for historical provenance rather than active development:
  - `agent/map-hou-001-functional-adjacency` — preserves the unique PR #4 functional-adjacency schematic and QA record that never entered `main`;
  - `agent/q-023-cross-system-sync` — preserves the superseded PR #11 implementation history that was reconciled and replaced by merged PRs #14 and #15, with later attribution cleanup in PR #17;
- both provenance branches are non-authoritative and must not be treated as current production sources merely because their refs remain present;
- do not delete either provenance branch during routine cleanup unless a later explicit archival/deletion decision replaces this preservation rule.

Normal post-audit `agent/` branches created for subsequent controlled work are expected to be removed automatically after their PRs merge; they do not alter the intentional provenance disposition above.

## Issue-tracker state

Audit refreshed on 2026-08-15:

- no open issues remain in `JamesJedi420/aramyst-book-assets`;
- issue #7, `Restore GitHub Actions account access`, is closed as completed after runner-backed validation resumed;
- issue #12, `Activate Protect main ruleset`, is closed as completed after the live ruleset and protected PR path were verified;
- the bodies of closed issues #7 and #12 remain point-in-time historical problem statements. Language inside those closed issue bodies describing a billing lock or missing ruleset is not a current repository warning and should not be rewritten as though the historical problem never existed.

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
- runs the full validator regression-test suite;
- runs the complete manifest/page-registry/filesystem/dependency-governance validator.

The validator enforces four coordinated layers of control.

Layer 1 — machine-readable JSON Schema contract:

- loads `schemas/asset-manifest.schema.json`;
- checks that the schema itself is valid Draft 2020-12 JSON Schema;
- validates `manifest.json` with `jsonschema`'s `Draft202012Validator`;
- reports schema violations with manifest paths;
- fails closed when the required `jsonschema` dependency is unavailable.

Layer 2 — Aramyst registry semantics and cross-file consistency:

- project constants;
- asset-ID/category/version/status formats and category-code agreement;
- required semantic fields;
- Drive/GitHub source-location requirements;
- dependency duplication;
- repository-relative path and filename rules;
- page-number/path/asset-reference rules;
- JSON/CSV registry synchronization;
- presence of every registered asset ID in `docs/ASSET_MANIFEST.md`.

Layer 3 — registry-to-filesystem integrity:

- concrete registered GitHub source/export files must exist for materialized `review`, `approved`, `exported`, and `published` assets when those paths are present;
- `planned`, `briefed`, and `in-progress` future paths may remain unmaterialized;
- materialized page files must exist and page paths must agree with the associated asset's registered `github_export_path` when one exists;
- asset-owned directories are scanned for unexplained files;
- `.gitkeep`, registered concrete files, and explicitly declared superseded/provenance exceptions are permitted;
- active materialized paths may not point at files classified as superseded/provenance.

Layer 4 — dependency governance:

- every `AST-*` dependency must resolve to an existing registered production asset; malformed or dangling asset edges fail validation;
- every exact ID-shaped external dependency must resolve through `schemas/external-authority-registry.json`;
- every bounded external authority range must resolve inside a registered range with matching prefix and identifier width;
- exact registered authority IDs are resolved before range parsing, preventing multi-segment exact IDs from being mistaken for ranges;
- every remaining prose dependency must have an exact controlled record in `schemas/dependency-classification-registry.json`;
- classification is limited to the policy's prose classes: `title_bound_authority`, `composite_gate`, and `long_term_prose_gate`;
- every prose dependency occurrence must be explicitly authorized for the Asset ID using it;
- each classification record's declared Asset-ID set must exactly match actual manifest use, preventing stale classifications and unauthorized reuse;
- classification records must cite an existing repository evidence document and reference only existing Asset IDs;
- the classification registry itself is validated against `schemas/dependency-classification-registry.schema.json`;
- CI does not infer prose semantics, choose a class, decide equivalence, or invent authority IDs. It enforces the previously approved classification record.

The controlling semantic policy is `docs/DEPENDENCY_GOVERNANCE_POLICY.md`. `schemas/dependency-classification-registry.json` is the mandatory machine-readable admission record for title-bound, composite, and long-term prose dependencies. A future dependency edit in one of those classes must update that registry in the same controlled change set before the manifest can pass CI.

Schema enforcement is regression-tested against the current manifest and against an intentionally invalid copy containing an undeclared top-level property. The latter must be rejected by the schema's `additionalProperties: false` contract.

Filesystem-integrity enforcement is regression-tested against the current repository plus deliberately invalid cases covering missing approved sources, unexplained asset-directory files, planned/unmaterialized future paths, and documented provenance exceptions.

Dependency-governance enforcement is regression-tested against deliberately invalid cases covering dangling `AST-*` asset edges, unknown external authority IDs, out-of-range external authority ranges, unclassified prose dependencies, and use of a classified prose dependency by an Asset ID not authorized by its classification record.

### Dependency classification control

`schemas/dependency-classification-registry.json` is the sole routine machine-readable control for prose dependency classifications admitted under the dependency-governance policy.

Each prose record must be governed by `schemas/dependency-classification-registry.schema.json` and must identify at minimum the exact dependency phrase, approved classification, exact affected Asset IDs, controlled evidence path, rationale, and reopen/satisfaction condition. Class-specific data such as a source anchor for title-bound authorities or constituent authorities for composite gates is recorded where required by the schema.

The registry is deliberately separate from `manifest.json`: the manifest continues to carry the dependency string used by the asset, while the classification registry records why that otherwise non-machine-resolvable string is admitted and exactly where it may be used.

Future dependency edits must follow this order:

1. establish the semantic classification under `docs/DEPENDENCY_GOVERNANCE_POLICY.md`;
2. create or update the controlled evidence record when needed;
3. update `schemas/dependency-classification-registry.json` for title-bound, composite, or long-term prose dependencies;
4. update `manifest.json` and `ASSET_MANIFEST.csv` together;
5. pass CI.

Do not add an unclassified prose dependency and rely on a later audit to legitimize it. CI now rejects that state.

### Filesystem provenance exception control

`schemas/filesystem-integrity-allowlist.json` is the sole routine mechanism for allowing an otherwise-unregistered file to remain inside an asset-owned directory because it is intentionally retained as superseded or provenance material.

Each allowlist entry must provide:

- a safe repository-relative `path` inside an asset-owned directory;
- `classification` of `superseded` or `provenance`;
- a non-empty `reason` establishing why the file is retained.

The validator also requires allowlisted files to physically exist, rejects duplicate allowlist paths and unsupported classifications, and prevents active materialized registry paths from pointing at allowlisted files. The allowlist is therefore an explicit provenance control, not a general CI bypass. Do not add unexplained files merely to silence orphan detection; establish the supersession/provenance basis first.

The initial controlled exception is `maps/map-reg-001-gm-reference-v001.svg`, classified `superseded` because AST-MAP-002 v002 is the active registered source while v001 is retained for development history.

The manual registry-to-filesystem audit recorded in `docs/REGISTRY_FILESYSTEM_AUDIT_2026-08-15.md` passed before automation. PR #20, `Automate registry filesystem integrity`, subsequently merged as `e28f38dde6c967927b947adb0e37bfdceb26ee37`, and the resulting `main` validation passed. The former manual filesystem-control gap is therefore resolved.

Post-baseline CI restoration on 2026-08-14:

- PR #8, `Restore reliable GitHub Actions validation`, was merged.
- The prior account-level billing lock stopped blocking runners.
- PR-branch validation completed successfully.
- A fresh `main` push validation after the merge also completed successfully.
- Issue #7, `Restore GitHub Actions account access`, was closed after runner-backed validation was observed.

Dependency-governance enforcement was added through PR #29, `Enforce dependency governance in CI`, merged as `05a73fc2bdbd300bdb32962f17d2b2d3c3936bc6`. Its successful protected PR run and post-merge `main` run established dependency classification and external-authority resolution as active CI controls rather than documentation-only policy.

The billing-lock language above is retained as historical restoration context; GitHub Actions is currently functioning as a real repository gate.

## Main branch protection

Protection verified on 2026-08-14.

Repository ruleset `Protect main` (ruleset ID `20862839`) is active and targets `refs/heads/main` only. GitHub's effective-rules evaluation for `main` confirms that the ruleset is currently applying the following controls:

- require changes to reach `main` through a pull request;
- require resolution of review threads;
- allow squash and rebase merge methods;
- require the `validate` status check from GitHub Actions (integration ID `15368`);
- require the branch to be up to date before merge;
- require linear history;
- block non-fast-forward / force-push updates;
- restrict deletion of `main`;
- no standing bypass actors; the authenticated maintainer cannot bypass the ruleset.

The controlled configuration is recorded in `docs/MAIN_PROTECTION_POLICY.md` and `.github/rulesets/protect-main.json`.

PR #16, `Verify active main protection baseline`, passed the required `validate` check and merged through the protected path. The resulting `main` push validation also passed. Issue #12 was then closed as completed.

## Baseline health

Status: **controlled**.

Strengths:

- explicit GitHub/Drive source-of-truth division;
- permanent asset IDs and controlled versions;
- synchronized machine-readable, CSV, and human-readable registries;
- approved map assets retain explicit authority, dependencies, holds, and supersession history;
- repository changes are handled through scoped `agent/` branches and pull requests;
- stale pre-approval PR #4 has been explicitly reconciled and closed as superseded;
- GitHub Actions executes successfully as a real validation gate;
- the JSON Schema is an enforced machine-readable contract rather than passive documentation;
- schema enforcement has a regression test that proves invalid structure is rejected;
- registry-to-filesystem integrity is enforced automatically, including materialized-path existence, page/export agreement, and asset-directory orphan detection;
- superseded/provenance filesystem exceptions are explicit and machine-readable through `schemas/filesystem-integrity-allowlist.json` rather than informal exclusions;
- dependency governance is CI-enforced: `AST-*` asset edges resolve, external IDs/ranges resolve through the external-authority registry, and every remaining prose dependency must have a controlled classification record;
- `schemas/dependency-classification-registry.json` is the mandatory machine-readable control for title-bound, composite, and long-term prose dependencies, including exact permitted Asset-ID use and evidence linkage;
- dependency semantics remain human-approved rather than machine-guessed, while CI enforces the approved representation and classification state;
- `main` is protected by an active repository ruleset requiring pull requests and the `validate` GitHub Actions check, with force-push and deletion protections and no standing bypass;
- issue tracker contains no unresolved repository-control blocker;
- surviving non-main provenance branches are deliberately classified historical records rather than unexplained stale work.

No unresolved repository-control warning remains from the baseline audit.

## Change-control baseline for this thread

Until superseded by an explicit project decision, GitHub maintenance in this thread should follow these rules:

1. Treat `main` as the authoritative repository branch.
2. Make substantive changes on `agent/<scope>` branches.
3. Default to draft pull requests rather than direct writes to `main`.
4. Do not modify canon or approval state without an already-authorized project decision.
5. When a registered asset changes materially, synchronize `manifest.json`, `ASSET_MANIFEST.csv`, and `docs/ASSET_MANIFEST.md` in the same change set.
6. Preserve superseded assets and branches when they carry approval, QA, implementation, or provenance history unless explicit archival/deletion authority is given.
7. Require the GitHub Actions validation gate to pass before merge; reproduce the validator manually only as a diagnostic supplement, not as a replacement for a failed or unavailable gate.
8. Record any unresolved synchronization conflict as a blocker rather than guessing which source is correct.
9. Treat closed issues and superseded PR bodies as historical records: do not infer a live blocker solely from stale wording inside a closed historical record.
10. For an otherwise-unregistered file retained inside an asset-owned directory solely as superseded/provenance history, add a justified entry to `schemas/filesystem-integrity-allowlist.json`; do not use the allowlist to hide unexplained or active production files.
11. Classify every proposed dependency under `docs/DEPENDENCY_GOVERNANCE_POLICY.md` before registry entry. For `title_bound_authority`, `composite_gate`, or `long_term_prose_gate`, add or update the exact controlled record in `schemas/dependency-classification-registry.json` in the same change set; for durable external IDs/ranges, ensure resolution through `schemas/external-authority-registry.json`; never invent an authority ID merely to satisfy CI.
12. Re-audit this baseline whenever repository ownership, source-of-truth rules, validation architecture, dependency-governance architecture, branch-protection architecture, issue-control state, or release structure changes materially.

## Immediate follow-up queue

No unresolved baseline-control task remains. Continue normal repository maintenance against approved project work under the CI-enforced dependency-governance policy.
