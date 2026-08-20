# Aramyst Naming and Versioning

Canonical naming, path, version, status, and fixed-layout page-order rules for the project currently using **Aramyst** as a development alias. The final publication/setting title is unresolved and must not be inferred from repository names, existing slugs, or examples.

This document applies to source art, prompts, references, maps, typography, exported images, fixed-layout pages, `.b64` wrappers, provenance-bound repository paths, and related production files.

## 1. Core Principles

1. **Asset IDs are permanent.** Filenames may change; Asset IDs do not.
2. **Names describe content and file role.** Do not rely on folder location alone.
3. **Versions represent meaningful iterations.** Do not increment for every autosave or lifecycle-state change.
4. **Registry status is authoritative metadata.** Canonical registered filenames do not encode lifecycle status.
5. **Status and version are separate.** A status change does not by itself require a version change, and a version token does not establish approval state.
6. **Page order is numeric.** Page filenames use zero-padded numeric prefixes.
7. **`manifest.json` is authoritative for fixed-layout order and machine-readable asset state.** Filenames support retrieval but do not replace the manifest.
8. **Repository paths are controlled identifiers once registered.** For promoted assets, provenance sidecars bind exact source/export paths.
9. **Source files are preserved.** Published outputs do not replace editable or authoritative masters.

## 2. Asset IDs

Use:

```text
AST-{CATEGORY}-{NUMBER}
```

Examples:

```text
AST-COVER-001
AST-MAP-001
AST-CHAR-001
AST-LOC-001
AST-SYM-001
AST-TYPE-001
```

### Category Codes

| Code | Category |
|---|---|
| COVER | Covers and cover-layout assets |
| MAP | Maps and diagrams |
| CHAR | Character assets |
| FACT | Faction assets |
| LOC | Location and environment assets |
| SYM | Symbols, seals, and icons |
| TYPE | Typography and title treatments |
| PROMPT | Prompt documents and reusable prompt templates |
| REF | Reference and research assets |
| MISC | Assets without another suitable category |

### Numbering Rules

- Use three digits beginning at `001`.
- Assign the next unused number within the category.
- Never renumber existing assets to close gaps.
- Never reuse a retired or deleted Asset ID.
- Variants normally share one Asset ID unless they have independent approval, ownership, or publication roles.

## 3. General Filename Pattern

Use lowercase kebab-case:

```text
{category}-{subject}-{purpose}-{variant}-v{NNN}.{ext}
```

`variant` is optional. Omit it when it adds no useful distinction.

Lifecycle status is intentionally absent from the canonical filename pattern. Status belongs in `manifest.json` and its synchronized registry mirrors.

Examples:

```text
cover-project-main-front-v001.psd
cover-project-main-front-v003.png
character-protagonist-portrait-front-v002.png
character-protagonist-costume-winter-v001.png
map-opening-region-player-v004.svg
map-opening-region-gm-v004.svg
symbol-project-seal-one-color-v002.svg
typography-title-stacked-v003.svg
prompt-character-portrait-base-v001.md
```

## 4. Filename Components

### Category

Use the lowercase category name:

```text
cover
map
character
faction
location
symbol
typography
prompt
reference
misc
```

### Subject

Use the canonical proper noun or stable role slug:

```text
project
protagonist
opening-region
keep
western-road
cave-mouth
moon-seal
```

Do not create multiple spellings for the same subject. When a proper noun becomes canonical, update future filenames and record the former name in manifest notes if needed.

Until successor naming is approved, do not mint new publication-facing filenames that treat `aramyst` or the retired long-form title as final identity. Use stable functional slugs, approved setting-local names, or existing technical IDs instead.

### Purpose

Describe what the file does or what delivery role it serves:

```text
portrait
turnaround
key-art
front-cover
chapter-opener
player-map
gm-map
source
master
preview
print
web
thumbnail
one-color
transparent
```

`source`, `master`, `preview`, `print`, and `web` are file-role or delivery-purpose terms. They are **not** lifecycle statuses.

### Variant

Use only when necessary:

```text
front
profile
winter
damaged
night
horizontal
stacked
with-labels
without-labels
```

### Version

Use a three-digit version:

```text
v001
v002
v003
```

If a concrete `github_source_path` or `github_export_path` contains an explicit `v###` token, that token must equal the asset's `manifest.json` version. This relationship is regression-enforced by `scripts/check_asset_governance.py`.

### Lifecycle Status

Lifecycle status is stored in the registry, not inferred from a filename. The exact manifest vocabulary is:

```text
planned
briefed
in-progress
review
approved
exported
published
superseded
archived
```

Do not substitute filename vocabulary for these states:

- `wip` is not a registry alias for `in-progress`.
- `draft` is not a registry status.
- `final` is not a registry status and must not be used as a synonym for `approved`, `exported`, or `published`.
- `print`, `web`, `source`, `master`, and `preview` describe file role or purpose, not approval state.

A filename containing words such as `approved`, `exported`, `published`, `final`, `wip`, or `review` does not grant or override repository status. New canonical registered paths should remain status-neutral.

## 5. Version Rules

Increment the version when any of the following materially changes:

- composition
- visual direction
- character design or equipment
- map geography or labels
- page dimensions or crop
- title or typography treatment
- source resolution
- color treatment that affects approval
- publication role when it changes the asset itself rather than merely its registry state
- content that changes canon or reader interpretation

Do not increment the canonical version for:

- autosaves
- hidden-layer experiments
- temporary exports
- metadata-only changes
- file moves or renames with identical content
- lifecycle status advancement with no material asset change
- spelling corrections in an internal note that do not affect the asset

Materiality remains a human governance judgment. CI verifies objective version/path consistency after the version decision is made; it does not decide whether a creative change is material.

### Promoted Asset Version and Provenance Rules

For assets in `approved`, `exported`, or `published` state:

- exactly one provenance sidecar is required under `docs/APPROVED_ASSET_PROVENANCE.md`;
- the sidecar must match the manifest Asset ID, version, status, Drive identity, GitHub source path, and GitHub export path;
- a material change that requires a new version must update the manifest mirrors and provenance sidecar in the same controlled change set and must preserve/re-establish approval evidence as required;
- a status-only advance such as `approved` → `exported` does not require a new version when the underlying asset is unchanged, but the manifest and provenance sidecar must be synchronized to the new status and any new export binding;
- a path-only rename with identical bytes does not require a new version, but every affected manifest and provenance path binding must be updated in the same change set.

### Working Copies

Tool-generated autosaves and experiments outside canonical registered repository paths may add a local/working suffix after the version:

```text
character-protagonist-portrait-front-v003-test-a.png
character-protagonist-portrait-front-v003-test-b.png
```

These working suffixes do not become manifest versions unless promoted. Local or Drive-side temporary labels such as `working` or `wip` may be used for human convenience, but they carry no GitHub lifecycle authority and should be removed when the file becomes a canonical registered source/export path.

Do not place unexplained working-copy files in asset-owned repository directories; repository filesystem-integrity rules still apply.

## 6. Status Flow

Normal descriptive production flow:

```text
planned → briefed → in-progress → review → approved → exported → published
```

Retirement flow:

```text
approved/exported/published → superseded → archived
```

Rules:

- `approved` means creative and canon approval is established.
- `exported` means a release/delivery-ready repository output exists as required by the registry.
- `published` means the asset appears in a released or distributed product.
- `superseded` identifies an asset record replaced by another asset identity or explicitly retired state; it is not the same as a failed draft.
- `archived` means retained for history but excluded from active production.

This is the normal lifecycle model, not a strict machine-enforced transition graph. An authorized synchronization may legitimately skip intermediate states when the controlling project state already exists outside GitHub. Approval ambiguity still blocks promotion.

## 7. Directory Rules

Use the established category directories:

```text
covers/
maps/
characters/
factions/
locations/
symbols/
typography/
prompts/
references/
exports/
docs/
provenance/
```

Fixed-layout page outputs use:

```text
pages/
```

### Source and Export Separation

- Editable or repository-native authoritative masters remain in the appropriate category folder when GitHub is the master system.
- Drive may remain the authoritative master system for approved binary assets under the provenance contract.
- General delivery-ready repository outputs belong in `exports/`.
- Fixed-layout page images and their `.b64` wrappers belong in `pages/`.
- Prompts and generation notes belong in `prompts/` when intentionally promoted to GitHub.
- External references, mood boards, and citation records belong in `references/` when intentionally promoted to GitHub.
- Approved-asset machine-readable sidecars belong in `provenance/`.

## 8. Fixed-Layout Page Naming

Use a three-digit page-order prefix followed by a concise underscore-separated slug:

```text
pages/{NNN}_{page-slug}.{ext}
```

Examples:

```text
pages/001_cover.png
pages/002_title-page.png
pages/003_credits.png
pages/010_chapter-one-opener.png
pages/011_the-keep-overview.png
```

Base64-wrapped page assets append `.b64` to the full original filename:

```text
pages/001_cover.png.b64
pages/010_chapter-one-opener.png.b64
```

The current canonical cover target is:

```text
pages/001_cover.png.b64
```

### Page-Order Rules

- Always use three digits, including leading zeros.
- Numeric prefixes support file browsing and review.
- `manifest.json` remains the source of truth for actual assembly order.
- If a page moves, update both its filename and `manifest.json` in the same controlled change.
- Do not create suffixes such as `001a` or `001-final-final`.
- Inserted pages require an intentional renumbering pass and manifest update.

## 9. `manifest.json` Synchronization

Whenever a fixed-layout page is added, removed, renamed, or reordered:

1. update the page filename;
2. update `manifest.json`;
3. update any corresponding asset path recorded in the synchronized registries;
4. verify that required materialized `.b64` files exist;
5. verify that no duplicate page number exists;
6. update any promoted-asset provenance binding if a bound source/export path changed;
7. pass `Validate Aramyst Assets`.

The file list, manifest order, and asset registry must agree before publication.

## 10. Registry Rules

`manifest.json` is the machine-readable authority for current asset/page state.

`ASSET_MANIFEST.csv` is the compact operational mirror.

`docs/ASSET_MANIFEST.md` is the synchronized human-readable registry.

When an asset changes:

- update all affected registry representations in the same controlled change;
- keep Asset ID, status, version, owner, dependencies, and paths synchronized;
- use semicolons inside CSV cells for multi-value fields;
- leave unavailable output paths blank until the relevant output actually exists;
- do not create a second CSV row for a routine version update; update the existing row;
- update the provenance sidecar in the same change when a promoted asset's bound status, version, identity, source path, export path, approval evidence, or required hash changes.

Create a new row only when a genuinely new Asset ID is assigned.

## 11. Extension Rules

Preferred source formats:

```text
.psd
.afdesign
.ai
.svg
.blend
.kra
.clip
```

Preferred delivery formats:

```text
.png
.jpg
.webp
.svg
.pdf
```

Documentation and tracking:

```text
.md
.csv
.json
```

Base64 wrappers:

```text
{original-filename}.{original-extension}.b64
```

Never remove the original extension before `.b64`.

## 12. Prohibited Naming Patterns

Do not use ambiguous canonical names such as:

```text
final.png
final-final.png
new-cover.png
copy-of-map.png
IMG_4837.png
untitled-2.psd
john-version.png
cover 3 FINAL revised.png
```

Do not use:

- spaces
- ambiguous dates as the only version system
- uppercase extensions
- punctuation other than hyphens, underscores in fixed-layout page names, and the period before extensions
- personal initials as a substitute for an Asset ID or owner field
- `final` as an approval/publication marker
- `wip` or `draft` as a substitute for manifest `in-progress`
- lifecycle-status suffixes on new canonical registered asset paths

## 13. Renaming, Version Replacement, and Superseding

When renaming a file without changing its content:

- keep the same Asset ID and version;
- update all manifest/registry paths;
- update any affected provenance path binding for promoted assets;
- record the rename in the commit message.

When materially revising the same production asset:

- keep the same Asset ID when purpose, ownership, and approval history remain one continuous asset identity;
- increment the version as required;
- update the current registry record to the new version and correct current status;
- retain or archive the prior file only under the repository's filesystem/provenance rules.

Do **not** mark the current Asset ID `superseded` merely because it advances from `v001` to `v002`. `superseded` is a current asset-record status, not a label for every historical version file.

When replacing an asset with a genuinely independent asset identity:

- assign a new Asset ID when ownership, purpose, or approval history must remain independent;
- mark the replaced Asset ID `superseded` when that is the correct current disposition;
- identify its replacement in notes/evidence as appropriate.

## 14. Commit Message Conventions

Recommended patterns:

```text
Add AST-CHAR-001 protagonist portrait brief
Revise AST-MAP-001 to v003
Approve AST-SYM-001 v002
Export AST-COVER-001 for page 001
Reorder fixed-layout pages 010–014
Archive superseded AST-TYPE-001
```

Commit messages should identify the Asset ID when the change concerns a registered asset. Workflow verbs in commit messages may describe the change; they do not alter registry status by themselves.

## 15. Pre-Commit Checklist

Before committing an asset change:

- Asset ID is valid and not reused.
- Canonical filename uses lowercase kebab-case and is status-neutral.
- Manifest status uses the exact controlled vocabulary.
- Version is correct for the material change.
- Any explicit `v###` in a registered source/export filename matches the manifest version.
- Source and export files are in the correct directories.
- `manifest.json`, CSV, and human-readable registry agree where affected.
- Fixed-layout filename and `manifest.json` agree when applicable.
- `.b64` wrappers retain the original extension.
- Promoted assets have a synchronized schema-valid provenance sidecar.
- Bound path changes for promoted assets are reflected in provenance.
- No `final-final`, lifecycle-status suffix, duplicate page number, or ambiguous copy filename remains.
- `Validate Aramyst Assets` passes before merge.

## Change Log

| Date | Change | Author |
|---|---|---|
| 2026-08-19 | Separated authoritative lifecycle status from canonical filename vocabulary; removed `wip`/status suffixes from the canonical pattern; aligned version, rename, supersession, and promoted-asset path rules with the approved-provenance contract and objective version checks. | JamesJedi420 / ChatGPT |
| 2026-08-14 | Q-023 continuity synchronization: made publication naming explicitly unresolved and replaced publication-final identity examples with neutral functional slugs. | JamesJedi420 / ChatGPT |
| 2026-08-04 | Created canonical naming, versioning, and fixed-layout page-order rules. | JamesJedi420 / ChatGPT |
