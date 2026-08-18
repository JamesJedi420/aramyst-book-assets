# Approved Asset Provenance Contract

Status: **CONTROLLING repository policy — CI enforced**

Every asset whose manifest status is `approved`, `exported`, or `published` must have exactly one machine-readable JSON sidecar in `provenance/` satisfying `schemas/approved-asset-provenance.schema.json`.

The sidecar supplements `manifest.json`; it does not replace the asset registry and does not move authoritative masters out of Google Drive.

## Required manifest bindings

CI requires each sidecar to agree exactly with the corresponding `manifest.json` record for:

- Asset ID;
- version;
- status;
- Drive file ID;
- GitHub source path;
- GitHub export path.

The sidecar also records an ISO approval date and a controlled repository evidence path. The approval date must be corroborated either by the manifest approval/notes text or by the named approval-evidence file.

## Master systems

`master.system` is explicit because approved assets currently use two valid storage topologies.

### `google_drive`

Use this when the authoritative binary/master remains in Google Drive. The sidecar binds the master to the exact manifest Drive file ID and records its expected SHA-256.

GitHub Actions cannot independently download private Drive binaries. Therefore CI verifies the identity binding and SHA-256 contract but does not claim to recompute the Drive master hash. Changing the Drive binary without updating/reapproving its recorded hash is a provenance violation detectable when the asset is next verified against Drive.

### `github`

Use this when the approved repository source itself is the controlling asset master, as with the current approved SVG map assets. The sidecar records the exact GitHub path and a repository-verifiable hash. CI recomputes that hash from the checked-out file.

## Repository hash bindings

The contract supports three hash modes:

- `git-blob-sha1` — recomputed using Git's canonical blob-object hash over repository file bytes;
- `sha256` — raw-file SHA-256;
- `sha256-base64-decoded` — SHA-256 of the decoded payload stored in a `.b64` wrapper.

A concrete `github_export_path` requires an `export_hash`, and CI recomputes it. `source_hash` may be supplied for a concrete GitHub provenance/source record and is likewise recomputed.

## Admission and promotion rule

Before an asset may enter `approved`, `exported`, or `published` status in GitHub:

1. establish the approval and authoritative master outside or inside GitHub as appropriate;
2. create/update its provenance JSON sidecar;
3. bind the sidecar to the exact manifest Asset ID, version, status, Drive identity, and repository paths;
4. record the approval date and controlled evidence path;
5. record the authoritative master hash and any repository source/export hashes;
6. update the normal manifest mirrors as required by existing policy;
7. pass `Validate Aramyst Assets`.

Removing or downgrading a controlled asset must also remove or deliberately migrate its sidecar so that the set of sidecars exactly matches assets currently in `approved`, `exported`, or `published` state.

## Current migration

The initial migration covers the five approved assets present on `main` when this control was introduced:

- `AST-MAP-002` — GitHub SVG master, Drive geometry authority;
- `AST-MAP-003` — GitHub SVG master, Drive local-geometry authority;
- `AST-MAP-004` — GitHub SVG master, Drive floorplan approval authority;
- `AST-SYM-002` — Drive PNG master, GitHub provenance record and base64 preview derivative;
- `AST-SYM-003` — Drive PNG master, GitHub provenance record and base64 preview derivative.

Future controlled assets must satisfy the same schema rather than inventing a new free-form provenance format.
