# Aramyst Asset Manifest

Canonical human-readable registry for Aramyst visual assets. `manifest.json` is the machine-readable source; this file and `ASSET_MANIFEST.csv` must remain synchronized.

## Rules

1. Asset IDs are permanent and never reused.
2. Versions use `v001` format and change only for material revisions.
3. Status changes must be synchronized across JSON, CSV, Markdown, and the Drive production record.
4. Drive owns briefs and working records; GitHub owns identity, status, version, validation, page order, and release-ready exports.
5. Exported or published assets require a registered GitHub export path.
6. Fixed-layout page order is governed by `manifest.json`.

## Status Values

| Status | Meaning |
|---|---|
| planned | Identified but not fully defined. |
| briefed | Requirements and purpose are defined. |
| in-progress | Active generation, illustration, composition, or revision is underway. |
| review | A specific version is ready for creative, canon, and production review. |
| approved | The version is accepted for its intended use. |
| exported | A delivery-ready output exists at its registered path. |
| published | The asset appears in a released product. |
| superseded | Replaced by another version or asset. |
| archived | Retained for history but excluded from active production. |

## Master Asset Index

| Asset ID | Title | Category | Context | Status | Version | Source | Export |
|---|---|---|---|---|---|---|---|
| AST-COVER-001 | Main Book Cover | cover | Whole book | planned | v001 | covers/ | pages/001_cover.png.b64 |
| AST-MAP-001 | Aramyst World Map | map | Whole book | planned | v001 | maps/ | — |
| AST-MAP-002 | Opening Region Map | map | Opening arc | planned | v001 | maps/ | — |
| AST-CHAR-001 | Primary Protagonist Portrait | character | Whole book | planned | v001 | characters/ | — |
| AST-CHAR-002 | Primary Antagonist Portrait | character | Whole book | planned | v001 | characters/ | — |
| AST-LOC-001 | Opening Location Key Art | location | Opening arc | planned | v001 | locations/ | — |
| AST-SYM-001 | Aramyst Seal / Emblem | symbol | Whole book | planned | v001 | symbols/ | — |
| AST-TYPE-001 | Main Title Treatment | typography | Whole book | planned | v001 | typography/ | — |
| AST-CHAR-003 | Tobin Marr Portrait | character | Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk | in-progress | v001 | Aramyst/05 — Assets/Characters/cart_driver_portrait | — |
| AST-CHAR-004 | Sister Aneth Portrait | character | Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk | in-progress | v001 | Aramyst/05 — Assets/Characters/sister_aneth_portrait | — |
| AST-CHAR-005 | Sergeant Bren Vask Portrait | character | Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk | in-progress | v001 | Aramyst/05 — Assets/Characters/gate_sergeant_portrait | — |
| AST-LOC-002 | Gate at Dusk Backdrop | location | Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk | in-progress | v001 | Aramyst/05 — Assets/Locations & Scene Art/gate_at_dusk_backdrop | — |
| AST-SYM-002 | Black Door Sign | symbol | Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk | in-progress | v001 | Aramyst/05 — Assets/Locations & Scene Art/black_door_sign | — |
| AST-SYM-003 | Triangle Token | symbol | Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk | in-progress | v001 | Aramyst/05 — Assets/Symbols & Tokens/triangle_token | — |

## Detailed Asset Records

### AST-COVER-001 — Main Book Cover

- **Category:** cover
- **Context:** Whole book
- **Purpose:** Primary cover for Aramyst: The Keep, the Road, and the Caves
- **Subjects:** Main title, core theme, optional lead subject, approved emblem
- **Required Dimensions:** 6x9 fixed-layout page; final bleed and platform specifications TBD
- **Status / Version:** planned / v001
- **Drive File ID:** —
- **Drive URL:** —
- **Drive Path:** —
- **GitHub Source Path:** covers/
- **GitHub Export Path:** pages/001_cover.png.b64
- **Prompt / Reference:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** AST-SYM-001; AST-TYPE-001; Final publishing specifications
- **Approval:** Not approved
- **Notes:** Anchor cover asset; preserve layered source; dark field with antique gold or silver hierarchy

### AST-MAP-001 — Aramyst World Map

- **Category:** map
- **Context:** Whole book
- **Purpose:** Canonical world-geography reference and possible publication map
- **Subjects:** Continents, regions, seas, borders, major settlements, and major routes
- **Required Dimensions:** Scalable or high-resolution master; final placement TBD
- **Status / Version:** planned / v001
- **Drive File ID:** —
- **Drive URL:** —
- **Drive Path:** —
- **GitHub Source Path:** maps/
- **GitHub Export Path:** —
- **Prompt / Reference:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** Canon geography decisions
- **Approval:** Not approved
- **Notes:** Governs regional-map consistency

### AST-MAP-002 — Opening Region Map

- **Category:** map
- **Context:** Opening arc
- **Purpose:** Regional map for the opening story arc
- **Subjects:** Starting region, settlements, routes, boundaries, and landmarks
- **Required Dimensions:** TBD
- **Status / Version:** planned / v001
- **Drive File ID:** —
- **Drive URL:** —
- **Drive Path:** —
- **GitHub Source Path:** maps/
- **GitHub Export Path:** —
- **Prompt / Reference:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** AST-MAP-001
- **Approval:** Not approved
- **Notes:** Derive geography and naming from the approved world map

### AST-CHAR-001 — Primary Protagonist Portrait

- **Category:** character
- **Context:** Whole book
- **Purpose:** Definitive visual continuity reference for the primary protagonist
- **Subjects:** Primary protagonist
- **Required Dimensions:** High-resolution master suitable for crop variants
- **Status / Version:** planned / v001
- **Drive File ID:** —
- **Drive URL:** —
- **Drive Path:** —
- **GitHub Source Path:** characters/
- **GitHub Export Path:** —
- **Prompt / Reference:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** Approved character canon brief
- **Approval:** Not approved
- **Notes:** Continuity anchor for future protagonist art

### AST-CHAR-002 — Primary Antagonist Portrait

- **Category:** character
- **Context:** Whole book
- **Purpose:** Definitive visual continuity reference for the primary antagonist
- **Subjects:** Primary antagonist
- **Required Dimensions:** High-resolution master suitable for crop variants
- **Status / Version:** planned / v001
- **Drive File ID:** —
- **Drive URL:** —
- **Drive Path:** —
- **GitHub Source Path:** characters/
- **GitHub Export Path:** —
- **Prompt / Reference:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** Approved character canon brief
- **Approval:** Not approved
- **Notes:** Continuity anchor for future antagonist art

### AST-LOC-001 — Opening Location Key Art

- **Category:** location
- **Context:** Opening arc
- **Purpose:** Environment concept and mood anchor for the opening location
- **Subjects:** Opening location, architecture, terrain, weather, and relevant story details
- **Required Dimensions:** Landscape master unless final layout requires otherwise
- **Status / Version:** planned / v001
- **Drive File ID:** —
- **Drive URL:** —
- **Drive Path:** —
- **GitHub Source Path:** locations/
- **GitHub Export Path:** —
- **Prompt / Reference:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** Approved location canon brief
- **Approval:** Not approved
- **Notes:** Establish recurring environmental and architectural language

### AST-SYM-001 — Aramyst Seal / Emblem

- **Category:** symbol
- **Context:** Whole book
- **Purpose:** Recurring visual mark for title pages, cover design, chapter art, and project identity
- **Subjects:** Canonical seal, sigil, emblem, or magical/heraldic motif
- **Required Dimensions:** Vector master preferred; transparent PNG and one-color exports required
- **Status / Version:** planned / v001
- **Drive File ID:** —
- **Drive URL:** —
- **Drive Path:** —
- **GitHub Source Path:** symbols/
- **GitHub Export Path:** —
- **Prompt / Reference:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** Approved symbolic and thematic direction
- **Approval:** Not approved
- **Notes:** Keep text separable from the emblem

### AST-TYPE-001 — Main Title Treatment

- **Category:** typography
- **Context:** Whole book
- **Purpose:** Canonical Aramyst title lettering and display treatment
- **Subjects:** Aramyst title typography
- **Required Dimensions:** Vector or editable high-resolution master; horizontal and stacked variants recommended
- **Status / Version:** planned / v001
- **Drive File ID:** —
- **Drive URL:** —
- **Drive Path:** —
- **GitHub Source Path:** typography/
- **GitHub Export Path:** —
- **Prompt / Reference:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** AST-SYM-001; Approved cover direction
- **Approval:** Not approved
- **Notes:** Keep title lettering separate from background artwork

### AST-CHAR-003 — Tobin Marr Portrait

- **Category:** character
- **Context:** Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk
- **Purpose:** NPC portrait for the frightened cart-driver, witness, hook-carrier, and survivor who brings the missing escort mystery to the Keep
- **Subjects:** Tobin Marr, a weathered frontier cart-driver in his late thirties or forties, frightened and exhausted at torchlit dusk
- **Required Dimensions:** Portrait format or square; suitable for NPC card/avatar
- **Status / Version:** in-progress / v001
- **Drive File ID:** 1dPcCTGJmJIPx1mdaKh9X5EPN7tE0OyJ69kzfDhaBQj8
- **Drive URL:** https://docs.google.com/document/d/1dPcCTGJmJIPx1mdaKh9X5EPN7tE0OyJ69kzfDhaBQj8
- **Drive Path:** Aramyst/05 — Assets/Characters/cart_driver_portrait
- **GitHub Source Path:** —
- **GitHub Export Path:** —
- **Prompt / Reference:** Drive brief contains generation prompt and negative prompt
- **Owner:** TBD
- **Dependencies:** Scene 01 canon; Character continuity approval
- **Approval:** Production opened; visual output not approved
- **Notes:** Grounded dark fantasy; ordinary working man; no armor, weapon, heroic pose, or exaggerated horror expression

### AST-CHAR-004 — Sister Aneth Portrait

- **Category:** character
- **Context:** Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk
- **Purpose:** NPC portrait for the Chapel witness and moral counterweight who protects frightened people and inconvenient evidence
- **Subjects:** Sister Aneth in plain frontier clerical garb, composed and watchful with quiet fear beneath her calm
- **Required Dimensions:** Portrait format or square; suitable for NPC card/avatar
- **Status / Version:** in-progress / v001
- **Drive File ID:** 1EouMk8YQlgIpJKpexebnhjgaia-BGR8uMWVvskDDGkg
- **Drive URL:** https://docs.google.com/document/d/1EouMk8YQlgIpJKpexebnhjgaia-BGR8uMWVvskDDGkg
- **Drive Path:** Aramyst/05 — Assets/Characters/sister_aneth_portrait
- **GitHub Source Path:** —
- **GitHub Export Path:** —
- **Prompt / Reference:** Drive brief contains generation prompt and negative prompt
- **Owner:** TBD
- **Dependencies:** Scene 01 canon; Chapel continuity approval
- **Approval:** Production opened; visual output not approved
- **Notes:** Austere grounded cleric; no halo, ornate robes, battle-priest styling, or magical glow

### AST-CHAR-005 — Sergeant Bren Vask Portrait

- **Category:** character
- **Context:** Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk
- **Purpose:** NPC portrait for the veteran gate sergeant who embodies Keep law, controls entry, and pressures the heroes to define themselves
- **Subjects:** Sergeant Bren Vask, a middle-aged weather-beaten frontier veteran in practical worn mail and leather
- **Required Dimensions:** Portrait format or square; suitable for NPC card/avatar
- **Status / Version:** in-progress / v001
- **Drive File ID:** 1AQeaiqhWB0z-UTCYF_Dwp8n95vT6m38W15mDFJmjD5M
- **Drive URL:** https://docs.google.com/document/d/1AQeaiqhWB0z-UTCYF_Dwp8n95vT6m38W15mDFJmjD5M
- **Drive Path:** Aramyst/05 — Assets/Characters/gate_sergeant_portrait
- **GitHub Source Path:** —
- **GitHub Export Path:** —
- **Prompt / Reference:** Drive brief contains generation prompt and negative prompt
- **Owner:** TBD
- **Dependencies:** Scene 01 canon; Keep guard continuity approval
- **Approval:** Production opened; visual output not approved
- **Notes:** Suspicious, exhausted, controlled; no ornate plate, polished knightly splendor, or superhero armor

### AST-LOC-002 — Gate at Dusk Backdrop

- **Category:** location
- **Context:** Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk
- **Purpose:** Primary opening Story Scene backdrop establishing the Keep as a hard frontier sanctuary and tense military checkpoint
- **Subjects:** Fortified frontier Keep gate, muddy road, torch smoke, stopped supply cart, frightened horse, guards, travelers, and Chapel bell tower at dusk
- **Required Dimensions:** 16:9; preferably 1920x1080 or larger
- **Status / Version:** in-progress / v001
- **Drive File ID:** 1hquQaX1nqk83qKZGbWK5IyTF2rgUgU-8LPGXvXmrsGg
- **Drive URL:** https://docs.google.com/document/d/1hquQaX1nqk83qKZGbWK5IyTF2rgUgU-8LPGXvXmrsGg
- **Drive Path:** Aramyst/05 — Assets/Locations & Scene Art/gate_at_dusk_backdrop
- **GitHub Source Path:** —
- **GitHub Export Path:** —
- **Prompt / Reference:** Drive brief contains composition, lighting, generation prompt, and negative prompt
- **Owner:** TBD
- **Dependencies:** Scene 01 canon; Keep exterior continuity
- **Approval:** Production opened; visual output not approved
- **Notes:** Story Scene backdrop, not a battlemap; no combat or visible monsters

### AST-SYM-002 — Black Door Sign

- **Category:** symbol
- **Context:** Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk
- **Purpose:** Prop and supernatural clue showing the crude black door-shaped mark on Tobin Marr's supply cart
- **Subjects:** Crooked black doorway or gate mark smeared in mud, ash, or tar on rough wooden planking
- **Required Dimensions:** Square or 4:3; usable as a handout or prop reference
- **Status / Version:** in-progress / v001
- **Drive File ID:** 1AATmXz1vGcjmx-7ohSyezNFXN_EUyj2QPORh_ORwNM4
- **Drive URL:** https://docs.google.com/document/d/1AATmXz1vGcjmx-7ohSyezNFXN_EUyj2QPORh_ORwNM4
- **Drive Path:** Aramyst/05 — Assets/Locations & Scene Art/black_door_sign
- **GitHub Source Path:** —
- **GitHub Export Path:** —
- **Prompt / Reference:** Drive brief contains composition, generation prompt, negative prompt, and GM interpretation notes
- **Owner:** TBD
- **Dependencies:** Scene 01 canon; Door/time-gate motif continuity
- **Approval:** Production opened; visual output not approved
- **Notes:** No readable letters, clean logo treatment, skull, pentagram, or obvious demonic face

### AST-SYM-003 — Triangle Token

- **Category:** symbol
- **Context:** Campaign One: The Last Quiet Spring / Scene 01 — The Gate at Dusk
- **Purpose:** Player clue handout linking the strange crate to the deeper Kael and Keep symbol language of home, breath, and marked safety
- **Subjects:** Thumb-sized handmade wooden token with a simple triangle mark, worn edges, and wet black soil
- **Required Dimensions:** Square, high detail, suitable as a player handout
- **Status / Version:** in-progress / v001
- **Drive File ID:** 12SODmxlLg1Mko_zaQ-B4jfuLhBRhojJZnBe3sEucOx0
- **Drive URL:** https://docs.google.com/document/d/12SODmxlLg1Mko_zaQ-B4jfuLhBRhojJZnBe3sEucOx0
- **Drive Path:** Aramyst/05 — Assets/Symbols & Tokens/triangle_token
- **GitHub Source Path:** —
- **GitHub Export Path:** —
- **Prompt / Reference:** Drive brief contains composition, generation prompt, negative prompt, and GM interpretation notes
- **Owner:** TBD
- **Dependencies:** Scene 01 canon; Kael symbol continuity
- **Approval:** Production opened; visual output not approved
- **Notes:** The triangle is not evil; no text, metal, ornate jewelry, or magical glow

## Change Log

| Change | Result |
|---|---|
| Canon and specification foundation created | Five canonical Drive documents added under `04 — Canon & Specifications`. |
| Scene 01 production opened | AST-CHAR-003 through AST-SYM-003 advanced from `briefed` to `in-progress` at v001. |
