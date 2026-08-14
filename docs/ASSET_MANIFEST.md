# Aramyst Asset Manifest

Canonical human-readable registry for Aramyst visual assets. `manifest.json` is the machine-readable source; `ASSET_MANIFEST.csv` is the operational mirror. GitHub owns asset identity, status, version, validation, and repository paths.

Project identity boundary: “Aramyst” is a temporary development alias; the final publication/setting title remains unresolved. The approved project model is a standalone TTRPG under SYS-001. This registry must not reintroduce compatibility-based framing or treat the development alias as a publication-final title.

## Registry Rules

1. Asset IDs are permanent and never reused.
2. Material revisions retain the asset ID and increment the `v###` version.
3. `manifest.json`, `ASSET_MANIFEST.csv`, and this file must identify the same registered assets.
4. Google Drive remains the authority for working briefs, editable documents, and QA records unless promoted to GitHub.
5. `approved` means accepted for the stated use; it does not imply publication-final cartography.

## Master Asset Index

| Asset ID | Title | Category | Status | Version | Active source |
|---|---|---|---|---|---|
| AST-COVER-001 | Main Book Cover | cover | planned | v001 | `covers/` |
| AST-MAP-001 | Aramyst World Map | map | planned | v001 | `maps/` |
| AST-MAP-002 | MAP-REG-001 — First-Playable Region GM Reference | map | approved | v002 | `maps/map-reg-001-gm-reference-v002.svg` |
| AST-MAP-003 | MAP-ENV-001 — Keep / Lower Road / Last-Bell Local GM Schematic | map | approved | v001 | `maps/map-env-001-gm-schematic-v001.svg` |
| AST-MAP-004 | MAP-HOU-001 — Last-Bell House Controlling Physical Floorplan | map | approved | v001 | `maps/map-hou-001-fp01-r1-neutral-v001.svg` |
| AST-CHAR-001 | Primary Protagonist Portrait | character | planned | v001 | `characters/` |
| AST-CHAR-002 | Primary Antagonist Portrait | character | planned | v001 | `characters/` |
| AST-LOC-001 | Opening Location Key Art | location | planned | v001 | `locations/` |
| AST-SYM-001 | Aramyst Seal / Emblem | symbol | planned | v001 | `symbols/` |
| AST-TYPE-001 | Main Title Treatment | typography | planned | v001 | `typography/` |
| AST-CHAR-003 | Tovin Marr Portrait | character | in-progress | v001 | Drive brief |
| AST-CHAR-004 | Sister Aneth Portrait | character | in-progress | v001 | Drive brief |
| AST-CHAR-005 | Sergeant Beran Vask Portrait | character | in-progress | v001 | Drive brief |
| AST-LOC-002 | Gate at Dusk Backdrop | location | in-progress | v001 | Drive brief |
| AST-SYM-002 | Black Door Sign | symbol | in-progress | v001 | Drive brief |
| AST-SYM-003 | Triangle Token | symbol | in-progress | v001 | Drive brief |

## Map Asset Records

### AST-MAP-001 — Aramyst World Map

- **Category:** map
- **Context:** Whole book
- **Purpose:** Canonical world-geography reference and possible publication map.
- **Status / Version:** planned / v001
- **GitHub Source Path:** `maps/`
- **Dependencies:** Canon geography decisions.
- **Approval:** Not approved.
- **Notes:** World geography remains independently deferred. AST-MAP-002 does not depend on completion of this asset.

### AST-MAP-002 — MAP-REG-001 — First-Playable Region GM Reference

- **Category:** map
- **Context:** Campaign One: The Last Quiet Spring / First-Playable March
- **Purpose:** GM-facing regional reference showing only approved approximate geographic anchors and explicitly held unknown geography.
- **Subjects:** GEO-000003, GEO-000004, GEO-000006, GEO-000007, GEO-000008, GEO-000009; held GEO-000002, GEO-000005, GEO-000010; ROUTE/GXR topology annotations only.
- **Required Dimensions:** Scalable SVG master; current approved GM review-stage draft uses a 1600x1000 viewBox; publication dimensions TBD.
- **Status / Version:** approved / v002
- **Drive File ID:** `1HKS3TPvCenAKeqC77glZtgT2xXwUwogkDv3AVL8OEdE`
- **Drive Path:** MAP-REG-001 Geometry Specification v001 — CONTROLLING
- **GitHub Source Path:** `maps/map-reg-001-gm-reference-v002.svg`
- **Dependencies:** ATLAS-ARCH-001; ATLAS-REG-DATA-001; MAP-REG-001 Geometry Specification v001 — CONTROLLING; GEO-000002–GEO-000010; ROUTE-000001–ROUTE-000007; GXR-000001–GXR-000016.
- **Approval:** Approved GM review-stage asset; independence/no-invention acceptance gate PASS 2026-08-13; player-facing derivative blocked.
- **QA Record:** Drive `1CwRkw-MXqJzwtHPYwkT3-2z_I_Hn-pUNgLSqYxRyBjk`.
- **Supersession:** `maps/map-reg-001-gm-reference-v001.svg` is superseded and retained only for history.
- **Dependency rule:** Bottom-up/regional-data-first. This asset does **not** depend on a completed AST-MAP-001 world map.
- **Prohibited additions:** no roads, river courses, terrain, March boundary, distances, travel scale, added settlements, route junctions, or external-source geometry.

### AST-MAP-003 — MAP-ENV-001 — Keep / Lower Road / Last-Bell Local GM Schematic

- **Category:** map
- **Context:** Campaign One: The Last Quiet Spring / Keep–Last-Bell local cluster
- **Purpose:** GM-facing local evidence/navigation schematic for approved movement and positive sight-line geometry around the Keep, Lower Road Approach, Last-Bell House, and Tarl Yard context.
- **Subjects:** GEO-000003 principal-gate interface; GEO-000004 threshold/lamp interface; GEO-000007 context; GEO-000009; ROUTE-000001/000002 approved approximate geometry; O-G/O-L positive visibility; held ROUTE-000003/000004.
- **Required Dimensions:** Scalable SVG master; 1500x1000 viewBox; non-metric; publication dimensions TBD.
- **Status / Version:** approved / v001
- **Drive File ID:** `1w4UnjQpzTHQIE4UXpMrejuaKBLy6Y0XMSh6EiGx3nfg`
- **Drive Path:** MAP-ENV-001 Local Geometry Foundation & Spatial Approval Gate v0.1
- **GitHub Source Path:** `maps/map-env-001-gm-schematic-v001.svg`
- **Dependencies:** ATLAS-REG-DATA-001; MAP-ENV-001-FOUND-001; ENV-SD-001–ENV-SD-007; ENV-GD-001–ENV-GD-010; MAP-ENV-001-QA-001; SCN-NODE-001.
- **Approval:** Approved local approximate geometry; not final publication cartography.
- **Held geometry:** This asset itself does not depict or establish Keep/House footprints or frontages, Tarl boundary, terrain, measurement system, negative sight lines, occlusion model, or external-source geometry. Later MAP-HOU-001 / AST-MAP-004 independently establishes approved Last-Bell House physical geometry without retroactively changing MAP-ENV-001.

### AST-MAP-004 — MAP-HOU-001 — Last-Bell House Controlling Physical Floorplan

- **Category:** map
- **Context:** Campaign One: The Last Quiet Spring / Last-Bell House
- **Purpose:** GM-facing non-metric physical floorplan reference implementing the approved Candidate A topology and HOU-FP-GD-001–022 geometry package.
- **Subjects:** GEO-000004 Last-Bell House; Street Court; Threshold Porch; Petition Hall; Witness Room; Record Room; Guest Hall; Kitchen and Winter Store; Bell Stair; Lamp Niche; Burial Court; Back Archive Loft; Service Yard; HOU-FP-GD-001–022.
- **Required Dimensions:** Scalable SVG master; 1500x1000 viewBox; non-metric; publication dimensions TBD.
- **Status / Version:** approved / v001
- **Drive File ID:** `1w7fd-wkY8ui2_mV6GO4N78lQWpTxDi55jTG0aeITmV4`
- **Drive Path:** `Aramyst/04 — Canon & Specifications/MAP-HOU-001 FP01 Candidate Geometry Approval Register v0.1`
- **GitHub Source Path:** `maps/map-hou-001-fp01-r1-neutral-v001.svg`
- **Dependencies:** MAP-HOU-001-CTRL-001; MAP-HOU-001-FP-GD-001; HOU-FP-GD-001–HOU-FP-GD-022; MAP-HOU-001-FP01-R1-QA-001; REL-CHAP-HOUSE-001; MAP-ENV-001; HOU-PD-012.
- **Approval:** Approved controlling non-metric physical geometry 2026-08-14; FP-01–FP-14 QA PASS; HOU-PD-012 remains deferred.
- **QA Record:** Drive `13vGwovr1KA8SlX5MYEbUdiYMqz3QEogu2ziaxAScEB8` — MAP-HOU-001-FP01-R1-QA-001.
- **Geometry Authority:** Drive `1w7fd-wkY8ui2_mV6GO4N78lQWpTxDi55jTG0aeITmV4` — MAP-HOU-001-FP-GD-001.
- **Active Source SHA-256:** `30d3b68113b62987380c945a919c9091a1e56b8ebec7db3fcdc9cdde311058d9`.
- **Pre-Approval QA-Artifact SHA-256:** `a6276209d66453bc13cf3d714c3999978f751a4feff8318b47a15951930e0413`.
- **Binding sidecar:** `docs/map-hou-001-fp01-r1-approval-v001.md`.
- **Status-label synchronization:** after approval, only visible approval/provenance text was updated. A structural comparison with all text elements removed confirmed that the active source has identical geometry to the QA-reviewed R1 artifact.
- **Explicit exclusions:** HOU-FP-X-001–008 are not part of the approved geometry. Numeric dimensions, scale, wall thickness, construction material, decorative architecture, exact compass orientation, windows, structural system, detailed architectural stair form, and publication styling remain unestablished under HOU-PD-012.
- **Superseded history:** Original FP01 failed QA; Drive `1jTI2CRKZYdhGkAGjWb__v1Uq-Oupgd0Qntf4EwV3qSk` is retained as superseded QA history and has no controlling geometry authority.

## Non-Map Assets

The following registered assets remain outside the detailed map records. Their complete operational fields are preserved in `manifest.json` and `ASSET_MANIFEST.csv`:

AST-COVER-001, AST-CHAR-001, AST-CHAR-002, AST-LOC-001, AST-SYM-001, AST-TYPE-001, AST-CHAR-003, AST-CHAR-004, AST-CHAR-005, AST-LOC-002, AST-SYM-002, AST-SYM-003.

## Change Log

| Date | Change | Result |
|---|---|---|
| 2026-08-14 | Q-023 cross-system identity synchronization | Updated Approved Working Scene 01 names to Tovin Marr and Sergeant Beran Vask in this registry and recorded the temporary development-alias / standalone-system boundary without changing Asset IDs or versions. |
| 2026-08-14 | AST-MAP-004 MAP-HOU-001 floorplan binding | Registered FP01-R1 as the approved controlling non-metric Last-Bell House floorplan; promoted only HOU-FP-GD-001–022; retained HOU-PD-012 holds and original FP01 failure history; synchronized approval labels without changing geometry. |
| 2026-08-13 | AST-MAP-002 manifest reconciliation | Bound `maps/map-reg-001-gm-reference-v002.svg` as approved v002; recorded regional-data-first authority and PASS acceptance gate; v001 retained only as superseded history. |
| 2026-08-13 | AST-MAP-003 mirror synchronization | Existing approved MAP-ENV-001 local schematic is represented in the human-readable registry alongside JSON/CSV. |
| 2026-08-13 | Player-facing control | No MAP-REG-001 player derivative started; it remains explicitly blocked. |
