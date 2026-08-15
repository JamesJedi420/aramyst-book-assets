# Aramyst Registry-to-Filesystem Integrity Audit — 2026-08-15

Audit target: `JamesJedi420/aramyst-book-assets` / `main`
Audited main SHA: `f3aaf69d9806a2397601c6ad294d40db608bdffe`
Scope: registry mirrors, dependency references, registered GitHub source/export paths, page paths, and asset-relevant repository files.

No asset status, version, approval, canon, or source-authority decision is changed by this audit.

## Result

**PASS with one expected planned-path exception.**

- Registered assets: **16**
- Current status distribution: **7 planned / 4 in-progress / 5 approved**
- JSON/CSV asset membership mismatches: **0**
- JSON/CSV status/version/field mismatches: **0**
- JSON/CSV dependency mismatches: **0**
- Human-readable index asset-ID omissions: **0**
- Human-readable index status/version mismatches observed: **0**
- Missing concrete active GitHub source files: **0**
- Missing concrete active GitHub export files for currently approved assets: **0**
- Unexplained/orphaned asset files: **0**
- Active registry paths pointing to superseded files: **0**
- Planned registered page/export paths not yet materialized: **1** — `pages/001_cover.png.b64`

The unmaterialized cover path is not an integrity failure because both `AST-COVER-001` and the page-1 record are `planned / v001`. No `pages/` directory or cover export currently exists on `main`.

## Registry mirror verification

`manifest.json` and `ASSET_MANIFEST.csv` contain the same 16 Asset IDs. Their mirrored fields, including `status`, `version`, GitHub source/export paths, Drive source metadata, approval text, and dependency lists, are aligned under the current validator contract.

`docs/ASSET_MANIFEST.md` contains all 16 registered Asset IDs. Its Master Asset Index matches the current status/version values:

- planned / v001: `AST-COVER-001`, `AST-MAP-001`, `AST-CHAR-001`, `AST-CHAR-002`, `AST-LOC-001`, `AST-SYM-001`, `AST-TYPE-001`;
- in-progress / v001: `AST-CHAR-003`, `AST-CHAR-004`, `AST-CHAR-005`, `AST-LOC-002`;
- approved: `AST-MAP-002` / v002, `AST-MAP-003` / v001, `AST-MAP-004` / v001, `AST-SYM-002` / v001, `AST-SYM-003` / v001.

## Per-asset filesystem verification

| Asset | Status / Version | Registered GitHub path state | Filesystem result | Dependency result |
|---|---|---|---|---|
| `AST-COVER-001` | planned / v001 | source directory `covers/`; future export `pages/001_cover.png.b64` | `covers/` exists; export/page file not yet materialized | `AST-SYM-001` and `AST-TYPE-001` both resolve in registry; external publishing-spec dependency remains external |
| `AST-MAP-001` | planned / v001 | source directory `maps/` | directory exists | external canon-geography dependency; no unresolved Asset ID |
| `AST-MAP-002` | approved / v002 | `maps/map-reg-001-gm-reference-v002.svg` | file exists and source title identifies v002 | external atlas/GEO/ROUTE/GXR authorities; no unresolved Asset ID |
| `AST-MAP-003` | approved / v001 | `maps/map-env-001-gm-schematic-v001.svg` | file exists and source title identifies approved v001 | external atlas/ENV/QA/scenario authorities; no unresolved Asset ID |
| `AST-MAP-004` | approved / v001 | `maps/map-hou-001-fp01-r1-neutral-v001.svg` | file exists and identifies approved/controlling geometry | external MAP/HOU/REL authorities; no unresolved Asset ID |
| `AST-CHAR-001` | planned / v001 | source directory `characters/` | directory exists | external approved-character-brief dependency |
| `AST-CHAR-002` | planned / v001 | source directory `characters/` | directory exists | external approved-character-brief dependency |
| `AST-LOC-001` | planned / v001 | source directory `locations/` | directory exists | external approved-location-brief dependency |
| `AST-SYM-001` | planned / v001 | source directory `symbols/` | directory exists | external symbolic/thematic-direction dependency |
| `AST-TYPE-001` | planned / v001 | source directory `typography/` | directory exists | `AST-SYM-001` resolves in registry; cover-direction dependency remains external |
| `AST-CHAR-003` | in-progress / v001 | Drive-only source; no GitHub source/export path | no GitHub file expected at current state | external Scene 01 / continuity dependencies |
| `AST-CHAR-004` | in-progress / v001 | Drive-only source; no GitHub source/export path | no GitHub file expected at current state | external Scene 01 / Chapel-continuity dependencies |
| `AST-CHAR-005` | in-progress / v001 | Drive-only source; no GitHub source/export path | no GitHub file expected at current state | external Scene 01 / guard-continuity dependencies |
| `AST-LOC-002` | in-progress / v001 | Drive-only source; no GitHub source/export path | no GitHub file expected at current state | external Scene 01 / Keep-exterior dependencies |
| `AST-SYM-002` | approved / v001 | `symbols/symbol-black-door-sign-source-v001.md`; `exports/symbol-black-door-sign-preview-v001.webp.b64` | both files exist and are non-empty; source sidecar records approved v001 and same Drive master ID | external Scene 01 / motif-continuity dependencies |
| `AST-SYM-003` | approved / v001 | `symbols/symbol-triangle-token-source-v001.md`; `exports/symbol-triangle-token-preview-v001.webp.b64` | both files exist and are non-empty; source sidecar records approved v001 and same Drive master ID | external Scene 01 / Kael-symbol dependencies |

## Page registry

`manifest.json` contains one page record:

- page 1 / `cover`;
- `AST-COVER-001`;
- `planned / v001`;
- path `pages/001_cover.png.b64`.

The path is syntactically valid and agrees with the cover asset's `github_export_path`, but the file and `pages/` directory do not yet exist. This is classified as **planned/unmaterialized**, not missing production output. It becomes a filesystem defect only if the page or asset advances to a state requiring the export while the file remains absent.

## Dependency integrity

The only dependencies using registered `AST-*` identifiers are:

- `AST-COVER-001` → `AST-SYM-001`;
- `AST-COVER-001` → `AST-TYPE-001`;
- `AST-TYPE-001` → `AST-SYM-001`.

All resolve to existing registered assets. No dangling Asset-ID dependency and no duplicate dependency entry was found.

Other dependency strings identify external project authorities, canon gates, geometry/QA records, or production decisions rather than repository file paths. This audit does not incorrectly classify those external authorities as missing GitHub files.

## Asset-relevant filesystem classification

### Active registered files

- `maps/map-reg-001-gm-reference-v002.svg` — `AST-MAP-002` active approved source.
- `maps/map-env-001-gm-schematic-v001.svg` — `AST-MAP-003` active approved source.
- `maps/map-hou-001-fp01-r1-neutral-v001.svg` — `AST-MAP-004` active approved source.
- `symbols/symbol-black-door-sign-source-v001.md` — `AST-SYM-002` GitHub source/authority sidecar.
- `symbols/symbol-triangle-token-source-v001.md` — `AST-SYM-003` GitHub source/authority sidecar.
- `exports/symbol-black-door-sign-preview-v001.webp.b64` — `AST-SYM-002` registered preview derivative.
- `exports/symbol-triangle-token-preview-v001.webp.b64` — `AST-SYM-003` registered preview derivative.

### Intentional historical/support files — not orphans

- `maps/map-reg-001-gm-reference-v001.svg` — explicitly superseded by `AST-MAP-002` v002 and retained only for history.
- `docs/map-env-001-schematic-qa-v001.md` — supporting QA record for the approved MAP-ENV-001 development/acceptance history.
- `docs/map-hou-001-fp01-r1-approval-v001.md` — explicit binding/approval sidecar for `AST-MAP-004`.
- category `.gitkeep` files — intentional directory placeholders.

Repository-control files (`README.md`, registry files, schemas, validation scripts/tests, workflow, ruleset, and control documentation) are infrastructure and are outside the asset-orphan category.

## Source-authority note

For `AST-SYM-002` and `AST-SYM-003`, the GitHub `github_source_path` points to a metadata/source sidecar while the authoritative lossless visual master is the Drive PNG identified by `drive_file_id` and `drive_path`. This is internally documented in each sidecar and in the registry approval field. The human-readable Master Asset Index's `Active source` column therefore names the GitHub-side source record, not the authoritative image bytes. This is not a filesystem mismatch, but future documentation should preserve that distinction.

## Audit boundary

This is a GitHub registry-to-filesystem audit. It verifies repository paths/files and registry metadata consistency. It does **not** re-open approval decisions or independently revalidate the contents/existence of Google Drive files, canon authorities, or external dependency records.

## Control gap resolved

At the time of the manual audit, filesystem existence and orphan detection were not generally enforced by `scripts/validate_manifest.py`. That gap was resolved on 2026-08-15 by PR #20, `Automate registry filesystem integrity`, merged to `main` as `e28f38dde6c967927b947adb0e37bfdceb26ee37`.

The validator now automatically:

- requires concrete registered GitHub source/export files for materialized `review`, `approved`, `exported`, and `published` assets when those paths are present;
- allows `planned`, `briefed`, and `in-progress` future paths to remain unmaterialized;
- requires materialized page files and checks page paths against an asset's registered `github_export_path` when one is present;
- resolves exact registered `AST-*` dependencies and rejects malformed or dangling Asset-ID dependencies;
- scans asset-owned directories for unexplained files;
- allows `.gitkeep`, registered concrete files, and explicitly controlled superseded/provenance exceptions;
- rejects active materialized paths that point at files classified as superseded/provenance.

### Required exception mechanism

Future unregistered files retained inside asset-owned directories solely for superseded or provenance purposes must be declared in `schemas/filesystem-integrity-allowlist.json`. Each entry must provide:

- a safe repository-relative `path` inside an asset-owned directory;
- `classification` of `superseded` or `provenance`;
- a non-empty `reason` explaining why the unregistered file must remain.

The allowlist is not a general bypass mechanism. Allowlisted files must physically exist, duplicate paths are rejected, unsupported classifications are rejected, and a materialized active asset may not point at an allowlisted file. Unexplained files must not be added to the allowlist merely to make CI pass; their provenance/supersession purpose must be established first.

The initial controlled exception is `maps/map-reg-001-gm-reference-v001.svg`, classified `superseded` because AST-MAP-002 v002 is the active registered source while v001 is retained for development history.

The post-merge `main` validation run for PR #20 passed, so this former manual control is now part of the protected CI gate.
