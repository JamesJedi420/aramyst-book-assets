# Scene 01 In-Progress Provenance Readiness Audit — 2026-08-18

Status: **CONTROLLED readiness audit — no approval-state change**

Scope: `AST-CHAR-003`, `AST-CHAR-005`, and `AST-LOC-002`.

Purpose: prepare the remaining in-progress Scene 01 visual assets so any future approval PR is born compliant with `docs/APPROVED_ASSET_PROVENANCE.md` and `schemas/approved-asset-provenance.schema.json`, rather than requiring a post-hoc provenance reconciliation.

## Governing rule

Do **not** create `provenance/*.json` sidecars while these assets remain `in-progress`. The provenance validator requires the sidecar set to match assets in `approved`, `exported`, or `published` state exactly; a premature sidecar would correctly fail CI.

For each future approval PR, create the provenance sidecar in the **same PR** that promotes the asset to `approved` (or later controlled state), using the final approved master identity, approval date, repository evidence path, and hash bindings produced by that approval.

The current Drive production records remain briefs/work records, not approved visual masters.

---

## AST-CHAR-003 — Tovin Marr Portrait

Current repository state:

- Asset ID: `AST-CHAR-003`
- Version: `v001`
- Status: `in-progress`
- Current Drive production record: `1dPcCTGJmJIPx1mdaKh9X5EPN7tE0OyJ69kzfDhaBQj8`
- Current dependency gates: `Scene 01 canon`; `Character continuity approval`
- No approved master identity is currently registered.
- No concrete GitHub source/export binding is currently registered.

Drive readiness finding:

The current Drive record is explicitly an `in-progress` v001 NPC portrait brief for Tovin Marr. It establishes the production brief and visual ceiling but is not itself an approved generated master.

### Future approval PR package

When a candidate is explicitly approved, the same PR should contain:

1. a repository source/evidence record, recommended path:
   `characters/ast-char-003-tovin-marr-source-v001.md`;
2. a concrete GitHub export/provenance binding if the approved binary remains in Drive, recommended path:
   `exports/ast-char-003-tovin-marr-master-v001.md`;
3. synchronized promotion in `manifest.json`, `ASSET_MANIFEST.csv`, and `docs/ASSET_MANIFEST.md`;
4. `provenance/ast-char-003-v001.json` created in that same PR;
5. final authoritative Drive master file ID and Drive path/URL replacing the current brief locator as the manifest's master identity when the approved binary is stored in Drive;
6. the approved master SHA-256;
7. approval date and controlled approval-evidence path;
8. repository-verifiable `source_hash` and, when a concrete export binding exists, `export_hash`.

Expected provenance topology if the raster master remains in Drive:

- `master.system`: `google_drive`
- `master.drive_file_id`: exact approved PNG master ID
- `master.hash.algorithm`: `sha256`
- `master.hash.value`: approved master SHA-256

Approval must preserve the established grounded cart-driver brief and must not silently broaden character canon. The existing descriptive dependency gates remain valid upstream controls; their presence does not eliminate the need for explicit visual approval.

Readiness status: **READY FOR APPROVAL-PACKAGE CONSTRUCTION ONCE AN ACTUAL MASTER IS APPROVED.**

---

## AST-CHAR-005 — Sergeant Beran Vask Portrait

Current repository state:

- Asset ID: `AST-CHAR-005`
- Version: `v001`
- Status: `in-progress`
- Current Drive production record: `1AQeaiqhWB0z-UTCYF_Dwp8n95vT6m38W15mDFJmjD5M`
- Current dependency gates: `Scene 01 canon`; `Keep guard continuity approval`
- No approved master identity is currently registered.
- No concrete GitHub source/export binding is currently registered.

Drive readiness finding:

The current Drive record is explicitly an `in-progress` v001 NPC portrait brief for Sergeant Beran Vask. It establishes function and visual direction but is not an approved generated master.

The active continuity risk register notes that the AST-CHAR-003 and AST-CHAR-005 Drive briefs were corrected under the current project-identity control. Any future generated master must therefore be judged against the corrected brief, not an older compatibility-framed or superseded description.

### Future approval PR package

When a candidate is explicitly approved, the same PR should contain:

1. a repository source/evidence record, recommended path:
   `characters/ast-char-005-sergeant-beran-vask-source-v001.md`;
2. a concrete GitHub export/provenance binding if the approved binary remains in Drive, recommended path:
   `exports/ast-char-005-sergeant-beran-vask-master-v001.md`;
3. synchronized promotion in `manifest.json`, `ASSET_MANIFEST.csv`, and `docs/ASSET_MANIFEST.md`;
4. `provenance/ast-char-005-v001.json` in the same PR;
5. final approved Drive master file ID/path/URL if Drive remains authoritative;
6. approved master SHA-256;
7. approval date and controlled approval-evidence path;
8. repository-verifiable source/export hashes.

Expected provenance topology if the raster master remains in Drive:

- `master.system`: `google_drive`
- exact approved master Drive file ID
- expected raw master SHA-256

Approval must preserve the corrected practical frontier-veteran/Keep-law visual ceiling and must not add unsupported rank, heraldry, polished knightly styling, or other canon claims beyond the approved brief.

Readiness status: **READY FOR APPROVAL-PACKAGE CONSTRUCTION ONCE AN ACTUAL MASTER IS APPROVED.**

---

## AST-LOC-002 — Gate at Dusk Backdrop

Current repository state:

- Asset ID: `AST-LOC-002`
- Version: `v001`
- Status: `in-progress`
- Current Drive production record: `1hquQaX1nqk83qKZGbWK5IyTF2rgUgU-8LPGXvXmrsGg`
- Current dependency gates: `Scene 01 canon`; `Keep exterior continuity`
- No approved master identity is currently registered.
- No concrete GitHub source/export binding is currently registered.

Drive readiness finding:

The current Drive record is explicitly an `in-progress` v001 story-scene backdrop brief for Scene 01. It is a production specification, not an approved backdrop master.

The current continuity controls treat `Keep exterior continuity` as a descriptive gate rather than an alias for `MAP-ENV-001`; therefore a future backdrop approval must be reviewed against the actual approved Scene 01/Keep exterior evidence and may not treat the local schematic as permission to invent a complete Keep exterior.

### Future approval PR package

When a candidate is explicitly approved, the same PR should contain:

1. a repository source/evidence record, recommended path:
   `locations/ast-loc-002-gate-at-dusk-source-v001.md`;
2. a concrete export/provenance binding if the approved raster remains in Drive, recommended path:
   `exports/ast-loc-002-gate-at-dusk-master-v001.md`;
3. synchronized promotion in `manifest.json`, `ASSET_MANIFEST.csv`, and `docs/ASSET_MANIFEST.md`;
4. `provenance/ast-loc-002-v001.json` in the same PR;
5. final approved Drive master file ID/path/URL if Drive remains authoritative;
6. approved master SHA-256;
7. approval date and controlled approval-evidence path;
8. repository-verifiable source/export hashes.

Expected provenance topology if the raster master remains in Drive:

- `master.system`: `google_drive`
- exact approved backdrop master Drive file ID
- expected raw master SHA-256

Approval must preserve the Scene 01 opening-state function while respecting the existing Keep-exterior uncertainty ceiling. The image may depict only exterior facts actually authorized by the controlling Scene 01/location records; it must not promote inferred architecture or local-map abstractions into canon merely because they are visually convenient.

Readiness status: **READY FOR APPROVAL-PACKAGE CONSTRUCTION ONCE AN ACTUAL MASTER IS APPROVED.**

---

## Common approval-PR admission checklist

For all three assets, a future approval PR should be rejected before CI if any of the following is missing:

- explicit visual approval of one identified candidate;
- final approved master location and immutable file identity;
- master dimensions/format recorded in the evidence record;
- master SHA-256;
- synchronized manifest/CSV/Markdown status, version, Drive identity, source/export paths, approval text, and notes;
- concrete repository source/evidence record;
- concrete repository export/provenance binding when applicable;
- provenance JSON created in the same PR as promotion;
- sidecar `asset_id`, `version`, `status`, `drive_file_id`, `github_source_path`, and `github_export_path` exactly matching `manifest.json`;
- ISO approval date corroborated by manifest text or controlled evidence;
- `source_hash`/`export_hash` values computed from the exact repository files referenced;
- all existing dependency-governance and filesystem-integrity checks passing;
- `Validate approved asset provenance` passing before merge.

## What is intentionally not pre-created

No placeholder provenance JSON files are added by this audit. Placeholder values such as future Drive IDs, hashes, or approval dates would create false provenance and would fail the current exact-sidecar-set rule.

No asset status, version, dependency, approval, Drive locator, canon, or master identity is changed by this audit.

## Audit result

All three remaining Scene 01 in-progress visual assets are **provenance-process ready but not approval ready**. Their current blockers are substantive rather than repository-structural: an actual visual master must be selected and explicitly approved, and the final master identity/hash must then be recorded. Once that occurs, each approval PR has a defined same-PR provenance package and should not require the type of post-hoc reconciliation that was necessary for PR #34.