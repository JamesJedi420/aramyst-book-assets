# Aramyst Source of Truth

This document defines which system owns each type of Aramyst project information and how Google Drive and GitHub remain synchronized.

## Systems

### GitHub

GitHub owns stable identifiers, machine-readable records, naming rules, validation, publication paths, and release-ready repository exports.

Canonical GitHub files:

- `docs/ASSET_MANIFEST.md` — human-readable asset registry
- `ASSET_MANIFEST.csv` — compact operational mirror
- `manifest.json` — machine-readable asset and page manifest
- `schemas/asset-manifest.schema.json` — manifest contract
- `docs/VISUAL_STYLE_GUIDE.md` — visual direction
- `docs/NAMING_AND_VERSIONING.md` — naming, status, version, and page-order rules
- `scripts/validate_manifest.py` — consistency validator

### Google Drive

Google Drive owns manuscript prose, research, editable working documents, briefs, review records, and working art that has not yet been promoted into the repository.

Canonical Drive root:

- Folder: `Aramyst`
- Folder ID: `1IBbWIFfAuJpB7I9jc7yrjb461mPnuGnq`

## Ownership Matrix

| Information | Canonical system |
|---|---|
| Asset IDs | GitHub |
| Asset status and version | GitHub |
| Machine-readable asset records | GitHub `manifest.json` |
| Human-readable asset records | GitHub `docs/ASSET_MANIFEST.md` |
| Operational tracking table | GitHub `ASSET_MANIFEST.csv` |
| Naming and version rules | GitHub |
| Visual style rules | GitHub |
| Fixed-layout page order | GitHub `manifest.json` |
| Manuscript prose | Google Drive |
| Research and source notes | Google Drive |
| Asset briefs and generation prompts | Google Drive unless promoted to `prompts/` |
| Editable art working files | Google Drive until repository promotion |
| Review and QA records | Google Drive |
| Approved release-ready exports | GitHub |
| Superseded working material | Google Drive archive |

## Required Cross-System Fields

Every registered asset uses these fields:

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

An asset must have at least one valid source locator:

- a Drive file ID and Drive URL, or
- a GitHub source path.

Assets with status `exported` or `published` must have a GitHub export path.

## Synchronization Rules

When an asset changes materially:

1. Keep its existing Asset ID.
2. Increment its version.
3. Update `manifest.json`.
4. Update the matching row in `ASSET_MANIFEST.csv`.
5. Update the matching record in `docs/ASSET_MANIFEST.md`.
6. Update Drive and GitHub paths if the file moved.
7. Record approval state accurately.
8. Run `python scripts/validate_manifest.py` before merging or publishing.

Create a new Asset ID only when the production purpose, approval history, or identity must remain independent.

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

A Drive filename containing words such as `FINAL`, `ACTIVE`, or `WORKING` does not override the GitHub status.

## Page Assembly Authority

`manifest.json` is the source of truth for fixed-layout page order.

- Page numbers are unique integers.
- Page filenames use three-digit prefixes.
- A page move requires updating both the filename and `manifest.json`.
- Exported or published pages must exist at their recorded repository path.
- `.b64` wrappers retain the original extension before `.b64`.

## Promotion from Drive to GitHub

A working asset may remain Drive-only while it is `briefed`, `in-progress`, or `review`.

Before an asset becomes `exported`:

1. Preserve the editable master in Drive or the correct repository category folder.
2. Create the approved export using the canonical filename.
3. Add the export to GitHub.
4. Record its GitHub export path.
5. Update all three manifest representations.
6. Run validation.

## Conflict Resolution

When records disagree:

1. Asset identity, status, version, and page order follow GitHub.
2. Manuscript wording and working-document content follow Drive.
3. Approval ambiguity blocks promotion to `approved`, `exported`, or `published`.
4. The conflict must be corrected in all mirrors before production continues.

## Change Log

| Date | Change | Author |
|---|---|---|
| 2026-08-04 | Established GitHub and Google Drive source-of-truth boundaries. | JamesJedi420 / ChatGPT |
