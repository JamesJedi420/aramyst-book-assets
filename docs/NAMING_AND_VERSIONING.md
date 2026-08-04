# Aramyst Naming and Versioning

Canonical naming, path, version, status, and fixed-layout page-order rules for **Aramyst: The Keep, the Road, and the Caves**.

This document applies to source art, prompts, references, maps, typography, exported images, fixed-layout pages, `.b64` wrappers, and related production files.

## 1. Core Principles

1. **Asset IDs are permanent.** Filenames may change; Asset IDs do not.
2. **Names describe content.** Do not rely on folder location alone.
3. **Versions represent meaningful iterations.** Do not increment for every autosave.
4. **Status and version are separate.** `v003-review` is a version plus a workflow state.
5. **Page order is numeric.** Page filenames use zero-padded numeric prefixes.
6. **`manifest.json` is authoritative for fixed-layout order.** Filenames support ordering but do not replace the manifest.
7. **Repository paths are canonical.** Manifest records use repository-relative paths.
8. **Source files are preserved.** Published outputs do not replace editable masters.

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
{category}-{subject}-{purpose}-{variant}-v{NNN}-{status}.{ext}
```

`variant` is optional. Omit it when it adds no useful distinction.

Examples:

```text
cover-aramyst-main-front-v001-wip.psd
cover-aramyst-main-front-v003-approved.png
character-protagonist-portrait-front-v002-review.png
character-protagonist-costume-winter-v001-wip.png
map-opening-region-player-v004-approved.svg
map-opening-region-gm-v004-approved.svg
symbol-aramyst-seal-one-color-v002-approved.svg
typography-aramyst-title-stacked-v003-approved.svg
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
aramyst
protagonist
opening-region
keep
western-road
cave-mouth
moon-seal
```

Do not create multiple spellings for the same subject. When a proper noun becomes canonical, update future filenames and record the former name in the manifest notes if needed.

### Purpose

Describe what the file does:

```text
portrait
turnaround
key-art
front-cover
chapter-opener
player-map
gm-map
print
web
thumbnail
one-color
transparent
```

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

### Status

Approved status suffixes:

```text
planned
briefed
wip
review
approved
exported
published
superseded
archived
```

The manifest uses `in-progress`; filenames use the shorter `wip` form.

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
- publication role
- content that changes canon or reader interpretation

Do not increment the canonical version for:

- autosaves
- hidden-layer experiments
- temporary exports
- metadata-only changes
- file moves with identical content
- spelling corrections in an internal note that do not affect the asset

### Working Copies

Tool-generated autosaves and experiments may add a local suffix after the version:

```text
character-protagonist-portrait-front-v003-wip-test-a.png
character-protagonist-portrait-front-v003-wip-test-b.png
```

These working suffixes do not become manifest versions unless promoted.

## 6. Status Flow

Normal production flow:

```text
planned → briefed → wip → review → approved → exported → published
```

Retirement flow:

```text
approved/exported/published → superseded → archived
```

Rules:

- `approved` means creative direction and canon are accepted.
- `exported` means a delivery-ready file exists.
- `published` means the asset appears in a released or distributed product.
- `superseded` identifies replaced work; it is not the same as a failed draft.
- `archived` means retained for history but excluded from active production.

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
```

Fixed-layout page outputs use:

```text
pages/
```

### Source and Export Separation

- Editable or highest-quality masters remain in the category folder.
- General delivery-ready outputs belong in `exports/`.
- Final fixed-layout page images and their `.b64` wrappers belong in `pages/`.
- Prompts and generation notes belong in `prompts/`.
- External references, mood boards, and citation records belong in `references/`.

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
- If a page moves, update both its filename and `manifest.json` in the same commit.
- Do not create suffixes such as `001a` or `001-final-final`.
- Inserted pages require an intentional renumbering pass and manifest update.

## 9. `manifest.json` Synchronization

Whenever a fixed-layout page is added, removed, renamed, or reordered:

1. update the page filename
2. update `manifest.json`
3. update any path recorded in `docs/ASSET_MANIFEST.md`
4. update `ASSET_MANIFEST.csv`
5. verify that referenced `.b64` files exist
6. verify that no duplicate page number exists

The file list, manifest order, and asset registry must agree before publication.

## 10. CSV and Markdown Registry Rules

`docs/ASSET_MANIFEST.md` is the detailed canonical record.

`ASSET_MANIFEST.csv` is the compact operational tracker.

When an asset changes:

- update both files in the same work session
- keep Asset ID, status, version, owner, dependencies, and paths synchronized
- use semicolons inside CSV cells for multi-value fields
- leave unavailable output paths blank until an export actually exists
- do not create a second CSV row for a routine version update; update the existing row

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

Do not use:

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

## 13. Renaming and Superseding

When renaming a file without changing its content:

- keep the same Asset ID and version
- update all manifest paths
- record the rename in the commit message

When replacing an asset with a materially different asset:

- either increment the version under the same Asset ID, or
- assign a new Asset ID if ownership, purpose, or approval history must remain independent

Mark the replaced record `superseded` and identify its replacement in the notes.

## 14. Commit Message Conventions

Recommended patterns:

```text
Add AST-CHAR-001 protagonist portrait brief
Revise AST-MAP-001 to v003
Approve AST-SYM-001 v002
Export AST-COVER-001 for page 001
Reorder fixed-layout pages 010–014
Archive superseded AST-TYPE-001 v001
```

Commit messages should identify the Asset ID when the change concerns a registered asset.

## 15. Pre-Commit Checklist

Before committing an asset change:

- Asset ID is valid and not reused.
- Filename uses lowercase kebab-case.
- Version and status are correct.
- Source and export files are in the correct directories.
- Markdown and CSV manifests agree.
- Fixed-layout filename and `manifest.json` agree when applicable.
- `.b64` wrappers retain the original extension.
- No `final-final`, duplicate page number, or ambiguous copy filename remains.

## Change Log

| Date | Change | Author |
|---|---|---|
| 2026-08-04 | Created canonical naming, versioning, and fixed-layout page-order rules. | JamesJedi420 / ChatGPT |
