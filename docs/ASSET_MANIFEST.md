# Aramyst Asset Manifest

Human-readable registry for planned, active, approved, exported, and published Aramyst assets.

The synchronized machine source is `manifest.json`. The compact operational mirror is `ASSET_MANIFEST.csv`. Source ownership and synchronization rules are defined in `docs/SOURCE_OF_TRUTH.md`.

## Rules

1. Assign one stable Asset ID to every meaningful asset.
2. Never reuse or renumber an Asset ID.
3. Increment the version when the visual, source, composition, dimensions, or publication role materially changes.
4. Do not delete historical records; use `superseded` or `archived`.
5. Every asset must have either a Drive source reference or a GitHub source path.
6. Assets marked `exported` or `published` must have a GitHub export path.
7. Update this file, `ASSET_MANIFEST.csv`, and `manifest.json` together.
8. Run `python scripts/validate_manifest.py` before merging or publishing.

## Asset ID Format

```text
AST-{CATEGORY}-{NUMBER}
```

| Code | Category |
|---|---|
| COVER | Cover art and layout |
| MAP | Maps and diagrams |
| CHAR | Character art and continuity |
| FACT | Faction art and heraldry |
| LOC | Location and environment art |
| SYM | Symbols, clues, seals, and tokens |
| TYPE | Typography and title treatments |
| PROMPT | Reusable prompts |
| REF | Reference material |
| MISC | Other registered assets |

## Status Values

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

## Canonical Fields

| Field | Requirement |
|---|---|
| Asset ID | Stable and unique |
| Title | Human-readable name |
| Category | Controlled category |
| Context | Book, campaign, chapter, or scene |
| Purpose | Production or story function |
| Subjects | What the asset depicts |
| Required Dimensions | Aspect ratio, resolution, or format |
| Status | Current production state |
| Version | `v001` format |
| Drive File ID / URL / Path | Required for Drive-backed sources |
| GitHub Source Path | Required when GitHub holds the source |
| GitHub Export Path | Required for exported or published assets |
| Prompt / Reference | Brief, prompt, or supporting material |
| Owner | Responsible person or process |
| Dependencies | Decisions or assets required first |
| Approval | Current approval state |
| Notes | Constraints and continuity information |

## Master Asset Index

| Asset ID | Title | Category | Context | Status | Version | Source | Export | Dependencies |
|---|---|---|---|---|---|---|---|---|
| AST-COVER-001 | Main Book Cover | cover | Whole book | planned | v001 | `covers/` | `pages/001_cover.png.b64` | AST-SYM-001; AST-TYPE-001; publishing specifications |
| AST-MAP-001 | Aramyst World Map | map | Whole book | planned | v001 | `maps/` | — | Canon geography decisions |
| AST-MAP-002 | Opening Region Map | map | Opening arc | planned | v001 | `maps/` | — | AST-MAP-001 |
| AST-CHAR-001 | Primary Protagonist Portrait | character | Whole book | planned | v001 | `characters/` | — | Character canon brief |
| AST-CHAR-002 | Primary Antagonist Portrait | character | Whole book | planned | v001 | `characters/` | — | Character canon brief |
| AST-LOC-001 | Opening Location Key Art | location | Opening arc | planned | v001 | `locations/` | — | Location canon brief |
| AST-SYM-001 | Aramyst Seal / Emblem | symbol | Whole book | planned | v001 | `symbols/` | — | Symbol and theme direction |
| AST-TYPE-001 | Main Title Treatment | typography | Whole book | planned | v001 | `typography/` | — | AST-SYM-001; cover direction |
| AST-CHAR-003 | Tobin Marr Portrait | character | Scene 01 — The Gate at Dusk | briefed | v001 | Google Drive | — | Scene 01 canon; character continuity |
| AST-CHAR-004 | Sister Aneth Portrait | character | Scene 01 — The Gate at Dusk | briefed | v001 | Google Drive | — | Scene 01 canon; Chapel continuity |
| AST-CHAR-005 | Sergeant Bren Vask Portrait | character | Scene 01 — The Gate at Dusk | briefed | v001 | Google Drive | — | Scene 01 canon; Keep guard continuity |
| AST-LOC-002 | Gate at Dusk Backdrop | location | Scene 01 — The Gate at Dusk | briefed | v001 | Google Drive | — | Scene 01 canon; Keep exterior continuity |
| AST-SYM-002 | Black Door Sign | symbol | Scene 01 — The Gate at Dusk | briefed | v001 | Google Drive | — | Door/time-gate motif continuity |
| AST-SYM-003 | Triangle Token | symbol | Scene 01 — The Gate at Dusk | briefed | v001 | Google Drive | — | Kael symbol continuity |

## Planned Foundation Assets

### AST-COVER-001 — Main Book Cover

- **Purpose:** Primary front-cover asset.
- **Subjects:** Main title, core theme, optional lead subject, and approved emblem.
- **Required Dimensions:** 6 × 9 fixed-layout page; final bleed and platform specifications TBD.
- **Status / Version:** planned / v001
- **GitHub Source Path:** `covers/`
- **GitHub Export Path:** `pages/001_cover.png.b64`
- **Dependencies:** AST-SYM-001; AST-TYPE-001; final publishing specifications.
- **Approval:** Not approved.
- **Notes:** Preserve layered source; use the approved restrained grim-frontier direction.

### AST-MAP-001 — Aramyst World Map

- **Purpose:** Canonical world-geography reference and possible publication map.
- **Required Dimensions:** Scalable or high-resolution master.
- **Status / Version:** planned / v001
- **GitHub Source Path:** `maps/`
- **Dependencies:** Canon geography decisions.
- **Approval:** Not approved.

### AST-MAP-002 — Opening Region Map

- **Purpose:** Regional map for the opening story arc.
- **Status / Version:** planned / v001
- **GitHub Source Path:** `maps/`
- **Dependencies:** AST-MAP-001.
- **Approval:** Not approved.

### AST-CHAR-001 — Primary Protagonist Portrait

- **Purpose:** Definitive protagonist continuity reference.
- **Required Dimensions:** High-resolution master suitable for crop variants.
- **Status / Version:** planned / v001
- **GitHub Source Path:** `characters/`
- **Dependencies:** Approved character canon brief.
- **Approval:** Not approved.

### AST-CHAR-002 — Primary Antagonist Portrait

- **Purpose:** Definitive antagonist continuity reference.
- **Required Dimensions:** High-resolution master suitable for crop variants.
- **Status / Version:** planned / v001
- **GitHub Source Path:** `characters/`
- **Dependencies:** Approved character canon brief.
- **Approval:** Not approved.

### AST-LOC-001 — Opening Location Key Art

- **Purpose:** Environment concept and mood anchor for the opening location.
- **Required Dimensions:** Landscape master unless final layout requires otherwise.
- **Status / Version:** planned / v001
- **GitHub Source Path:** `locations/`
- **Dependencies:** Approved location canon brief.
- **Approval:** Not approved.

### AST-SYM-001 — Aramyst Seal / Emblem

- **Purpose:** Recurring project, title-page, cover, and chapter mark.
- **Required Dimensions:** Vector master preferred; transparent and one-color exports required.
- **Status / Version:** planned / v001
- **GitHub Source Path:** `symbols/`
- **Dependencies:** Approved symbolic and thematic direction.
- **Approval:** Not approved.

### AST-TYPE-001 — Main Title Treatment

- **Purpose:** Canonical Aramyst title lettering and display treatment.
- **Required Dimensions:** Editable vector or high-resolution master; horizontal and stacked variants recommended.
- **Status / Version:** planned / v001
- **GitHub Source Path:** `typography/`
- **Dependencies:** AST-SYM-001; approved cover direction.
- **Approval:** Not approved.

## Scene 01 — The Gate at Dusk

### AST-CHAR-003 — Tobin Marr Portrait

- **Category:** character
- **Purpose:** NPC portrait for the frightened cart-driver, witness, hook-carrier, and survivor who brings the missing escort mystery to the Keep.
- **Subjects:** Tobin Marr, a weathered frontier working man in his late thirties or forties, frightened and exhausted at torchlit dusk.
- **Required Dimensions:** Portrait format or square; suitable for an NPC card or avatar.
- **Status / Version:** briefed / v001
- **Drive File ID:** `1dPcCTGJmJIPx1mdaKh9X5EPN7tE0OyJ69kzfDhaBQj8`
- **Drive URL:** `https://docs.google.com/document/d/1dPcCTGJmJIPx1mdaKh9X5EPN7tE0OyJ69kzfDhaBQj8`
- **Drive Path:** `Aramyst/05 — Assets/Characters/cart_driver_portrait`
- **Dependencies:** Scene 01 canon; character continuity approval.
- **Approval:** Brief registered; visual output not approved.
- **Notes:** No armor, weapon, heroic pose, or exaggerated horror expression.

### AST-CHAR-004 — Sister Aneth Portrait

- **Category:** character
- **Purpose:** NPC portrait for the Chapel witness and moral counterweight who protects frightened people and inconvenient evidence.
- **Subjects:** Sister Aneth in plain frontier clerical garb, composed and watchful with quiet fear beneath her calm.
- **Required Dimensions:** Portrait format or square; suitable for an NPC card or avatar.
- **Status / Version:** briefed / v001
- **Drive File ID:** `1EouMk8YQlgIpJKpexebnhjgaia-BGR8uMWVvskDDGkg`
- **Drive URL:** `https://docs.google.com/document/d/1EouMk8YQlgIpJKpexebnhjgaia-BGR8uMWVvskDDGkg`
- **Drive Path:** `Aramyst/05 — Assets/Characters/sister_aneth_portrait`
- **Dependencies:** Scene 01 canon; Chapel continuity approval.
- **Approval:** Brief registered; visual output not approved.
- **Notes:** Austere and grounded; no halo, ornate robes, battle-priest styling, or magical glow.

### AST-CHAR-005 — Sergeant Bren Vask Portrait

- **Category:** character
- **Purpose:** NPC portrait for the veteran gate sergeant who embodies Keep law and controls entry.
- **Subjects:** A middle-aged, weather-beaten frontier veteran in practical worn mail and leather.
- **Required Dimensions:** Portrait format or square; suitable for an NPC card or avatar.
- **Status / Version:** briefed / v001
- **Drive File ID:** `1AQeaiqhWB0z-UTCYF_Dwp8n95vT6m38W15mDFJmjD5M`
- **Drive URL:** `https://docs.google.com/document/d/1AQeaiqhWB0z-UTCYF_Dwp8n95vT6m38W15mDFJmjD5M`
- **Drive Path:** `Aramyst/05 — Assets/Characters/gate_sergeant_portrait`
- **Dependencies:** Scene 01 canon; Keep guard continuity approval.
- **Approval:** Brief registered; visual output not approved.
- **Notes:** Suspicious, exhausted, and controlled; no ornate plate or polished knightly splendor.

### AST-LOC-002 — Gate at Dusk Backdrop

- **Category:** location
- **Purpose:** Primary opening Story Scene backdrop establishing the Keep as a hard frontier sanctuary and tense military checkpoint.
- **Subjects:** Keep gate, muddy road, torch smoke, stopped cart, frightened horse, guards, travelers, and Chapel bell tower at dusk.
- **Required Dimensions:** 16:9; preferably 1920 × 1080 or larger.
- **Status / Version:** briefed / v001
- **Drive File ID:** `1hquQaX1nqk83qKZGbWK5IyTF2rgUgU-8LPGXvXmrsGg`
- **Drive URL:** `https://docs.google.com/document/d/1hquQaX1nqk83qKZGbWK5IyTF2rgUgU-8LPGXvXmrsGg`
- **Drive Path:** `Aramyst/05 — Assets/Locations & Scene Art/gate_at_dusk_backdrop`
- **Dependencies:** Scene 01 canon; Keep exterior continuity.
- **Approval:** Brief registered; visual output not approved.
- **Notes:** Story Scene backdrop, not a battlemap; no combat or visible monsters.

### AST-SYM-002 — Black Door Sign

- **Category:** symbol
- **Purpose:** Prop and supernatural clue showing the crude black door-shaped mark on Tobin Marr's cart.
- **Subjects:** Crooked doorway or gate mark smeared in mud, ash, or tar on rough wooden planking.
- **Required Dimensions:** Square or 4:3; usable as a handout or prop reference.
- **Status / Version:** briefed / v001
- **Drive File ID:** `1AATmXz1vGcjmx-7ohSyezNFXN_EUyj2QPORh_ORwNM4`
- **Drive URL:** `https://docs.google.com/document/d/1AATmXz1vGcjmx-7ohSyezNFXN_EUyj2QPORh_ORwNM4`
- **Drive Path:** `Aramyst/05 — Assets/Locations & Scene Art/black_door_sign`
- **Dependencies:** Scene 01 canon; door/time-gate motif continuity.
- **Approval:** Brief registered; visual output not approved.
- **Notes:** No readable letters, clean logo treatment, skull, pentagram, or obvious demonic face.

### AST-SYM-003 — Triangle Token

- **Category:** symbol
- **Purpose:** Player clue handout linking the strange crate to the Kael and Keep symbol language of home, breath, and marked safety.
- **Subjects:** Thumb-sized handmade wooden token with a simple triangle mark, worn edges, and wet black soil.
- **Required Dimensions:** Square, high detail, suitable as a player handout.
- **Status / Version:** briefed / v001
- **Drive File ID:** `12SODmxlLg1Mko_zaQ-B4jfuLhBRhojJZnBe3sEucOx0`
- **Drive URL:** `https://docs.google.com/document/d/12SODmxlLg1Mko_zaQ-B4jfuLhBRhojJZnBe3sEucOx0`
- **Drive Path:** `Aramyst/05 — Assets/Symbols & Tokens/triangle_token`
- **Dependencies:** Scene 01 canon; Kael symbol continuity.
- **Approval:** Brief registered; visual output not approved.
- **Notes:** The triangle is not evil; no text, metal, ornate jewelry, or magical glow.

## Change Log

| Date | Change | Author |
|---|---|---|
| 2026-08-04 | Created canonical asset manifest and starter records. | JamesJedi420 / ChatGPT |
| 2026-08-04 | Added cross-system fields and registered six Scene 01 briefs. | JamesJedi420 / ChatGPT |
