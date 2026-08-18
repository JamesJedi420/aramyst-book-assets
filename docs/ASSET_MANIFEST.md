# Aramyst Asset Manifest

Canonical human-readable registry for the project currently using **Aramyst** as a development alias. The final publication/setting identity remains unresolved. `manifest.json` is the machine-readable source; `ASSET_MANIFEST.csv` is the operational mirror. GitHub owns asset identity, status, version, validation, and repository paths.

## Registry Rules

1. Asset IDs are permanent and never reused.
2. Material revisions retain the asset ID and increment the `v###` version.
3. `manifest.json`, `ASSET_MANIFEST.csv`, and this file must identify the same registered assets.
4. Google Drive remains the authority for working briefs, editable documents, and QA records unless promoted to GitHub.
5. `approved` means accepted for the stated use; it does not imply publication-final cartography or publication-final naming.
6. Before adding, removing, or changing any dependency, follow [`DEPENDENCY_GOVERNANCE_POLICY.md`](DEPENDENCY_GOVERNANCE_POLICY.md). Dependency classification is CI-enforced; prose dependencies require an authorized record in `../schemas/dependency-classification-registry.json` before registry entry.

## Master Asset Index

| Asset ID | Title | Category | Status | Version | Active source |
|---|---|---|---|---|---|
| AST-COVER-001 | Main Book Cover | cover | planned | v001 | `covers/` |
| AST-MAP-001 | World Map (Publication Identity Pending) | map | planned | v001 | `maps/` |
| AST-MAP-002 | MAP-REG-001 — First-Playable Region GM Reference | map | approved | v002 | `maps/map-reg-001-gm-reference-v002.svg` |
| AST-MAP-003 | MAP-ENV-001 — Keep / Lower Road / Last-Bell Local GM Schematic | map | approved | v001 | `maps/map-env-001-gm-schematic-v001.svg` |
| AST-MAP-004 | MAP-HOU-001 — Last-Bell House Controlling Physical Floorplan | map | approved | v001 | `maps/map-hou-001-fp01-r1-neutral-v001.svg` |
| AST-CHAR-001 | Primary Protagonist Portrait | character | planned | v001 | `characters/` |
| AST-CHAR-002 | Primary Antagonist Portrait | character | planned | v001 | `characters/` |
| AST-LOC-001 | Opening Location Key Art | location | planned | v001 | `locations/` |
| AST-SYM-001 | Project Seal / Emblem (Publication Identity Pending) | symbol | planned | v001 | `symbols/` |
| AST-TYPE-001 | Main Title Treatment (Publication Name Pending) | typography | planned | v001 | `typography/` |
| AST-CHAR-003 | Tovin Marr Portrait | character | in-progress | v001 | Drive brief |
| AST-CHAR-004 | Sister Aneth Portrait | character | approved | v001 | `characters/ast-char-004-sister-aneth-source-v001.md` |
| AST-CHAR-005 | Sergeant Beran Vask Portrait | character | in-progress | v001 | Drive brief |
| AST-LOC-002 | Gate at Dusk Backdrop | location | in-progress | v001 | Drive brief |
| AST-SYM-002 | Black Door Sign | symbol | approved | v001 | `symbols/symbol-black-door-sign-source-v001.md` |
| AST-SYM-003 | Triangle Token | symbol | approved | v001 | `symbols/symbol-triangle-token-source-v001.md` |

## Map Asset Records

### AST-MAP-001 — World Map (Publication Identity Pending)

- **Category:** map
- **Context:** Whole book
- **Purpose:** Canonical world-geography reference and possible publication map; final publication identity pending approved successor naming.
- **Status / Version:** planned / v001
- **GitHub Source Path:** `maps/`
- **Dependencies:** Canon geography decisions.
- **Approval:** Not approved.
- **Notes:** World geography remains independently deferred. AST-MAP-002 does not depend on completion of this asset. The asset title does not establish a successor publication or setting name.

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

### AST-CHAR-004 — Sister Aneth Portrait

- **Category:** character
- **Context:** Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk
- **Purpose:** NPC portrait for the Chapel witness and moral counterweight who protects frightened people and inconvenient evidence.
- **Subjects:** Sister Aneth of the Last Bell in plain frontier Chapel garb / dark traveling habit, composed and watchful with quiet fear beneath her calm.
- **Required Dimensions:** Portrait format or square; suitable for NPC card/avatar.
- **Status / Version:** approved / v001
- **Drive File ID:** `1yJErhP5P6eNAEIUBfjfTOsUERi6CbT0W`
- **Drive Path:** `Aramyst/05 — Assets/Characters/AST-CHAR-004 — Sister Aneth Portrait — Master v001.png`
- **GitHub Source Path:** `characters/ast-char-004-sister-aneth-source-v001.md`
- **GitHub Export Binding:** `exports/ast-char-004-sister-aneth-master-v001.md`
- **Prompt / Brief Authority:** Drive `1EouMk8YQlgIpJKpexebnhjgaia-BGR8uMWVvskDDGkg`
- **Dependencies:** Scene 01 canon; Chapel continuity approval.
- **Approval:** Approved visual master 2026-08-18; Drive PNG authoritative; GitHub source/export binding records.
- **Master SHA-256:** `1315736c793e2f3ff0bf05405a83e55664f250252298339f963f9c670a254236`.
- **Authority ceiling:** simple Chapel cord only if visible; no cross, medallion, halo, invented office/rank, priesthood cue, magical effect, weapon, ornate vestments, or unsupported lore.

The following registered non-map assets remain governed by the complete operational fields in `manifest.json` and `ASSET_MANIFEST.csv`:

AST-COVER-001, AST-CHAR-001, AST-CHAR-002, AST-LOC-001, AST-SYM-001, AST-TYPE-001, AST-CHAR-003, AST-CHAR-005, AST-LOC-002, AST-SYM-002, AST-SYM-003.

## Change Log

| Date | Change | Result |
|---|---|---|
| 2026-08-18 | TIN-274 / AST-CHAR-004 visual approval and integration | Approved Sister Aneth v001 under corrected locked brief; Drive PNG is authoritative; GitHub source/export binding records registered; no unsupported priesthood, rank, magical, weapon, or religious-symbol content authorized. |
| 2026-08-14 | Q-023 authorized continuity synchronization | Corrected current Approved Working Scene 01 identities to Tovin Marr and Sergeant Beran Vask; marked publication-identity-dependent planned assets as naming-pending; did not invent a successor title or change asset versions/approval state. |
| 2026-08-14 | AST-SYM-002 / AST-SYM-003 status-mirror reconciliation | Separately recorded the already-approved v001 status in the human-readable mirror and corresponding Drive production records; no approval, status authority, Asset ID, or version change was introduced. |
| 2026-08-14 | AST-MAP-004 MAP-HOU-001 floorplan binding | Registered FP01-R1 as the approved controlling non-metric Last-Bell House floorplan; promoted only HOU-FP-GD-001–022; retained HOU-PD-012 holds and original FP01 failure history; synchronized approval labels without changing geometry. |
| 2026-08-13 | AST-MAP-002 manifest reconciliation | Bound `maps/map-reg-001-gm-reference-v002.svg` as approved v002; recorded regional-data-first authority and PASS acceptance gate; v001 retained only as superseded history. |
| 2026-08-13 | AST-MAP-003 mirror synchronization | Existing approved MAP-ENV-001 local schematic is represented in the human-readable registry alongside JSON/CSV. |
| 2026-08-13 | Player-facing control | No MAP-REG-001 player derivative started; it remains explicitly blocked. |
