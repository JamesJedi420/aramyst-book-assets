# Aramyst Asset Manifest

Canonical registry for all planned, in-progress, approved, exported, and published assets in the Aramyst book project.

This file is the source of truth for asset identity, ownership, location, version, production status, and publication readiness.

## Rules

1. Assign one stable Asset ID to every meaningful asset.
2. Never reuse an Asset ID, even after an asset is retired.
3. Increment the version whenever the visual, source, composition, dimensions, or publication role materially changes.
4. Do not delete historical records. Mark replaced work as `superseded` or `archived`.
5. Use repository-relative paths.
6. Use lowercase kebab-case filenames.
7. Keep editable work in its category folder and delivery-ready files in `exports/`.
8. Every approved asset must identify its source file, export file, and supporting prompt or reference material when applicable.

## Asset ID Format

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
| COVER | Cover art and cover-layout assets |
| MAP | World, regional, settlement, route, and diagram maps |
| CHAR | Character portraits, turnarounds, costume sheets, and expression sheets |
| FACT | Faction emblems, banners, heraldry, uniforms, and reference boards |
| LOC | Location art, architecture, environment concepts, and scene-setting images |
| SYM | Symbols, glyphs, seals, icons, magical marks, and recurring motifs |
| TYPE | Title treatments, lettering, chapter marks, and typography studies |
| PROMPT | Reusable generation prompts and prompt templates |
| REF | Research images, mood boards, visual references, and citation notes |
| MISC | Assets that do not fit another category |

## Status Values

| Status | Meaning |
|---|---|
| planned | Identified but not yet fully briefed |
| briefed | Requirements and purpose are defined |
| in-progress | Actively being created or revised |
| review | Ready for creative or production review |
| approved | Creative direction is approved |
| exported | Delivery-ready output exists |
| published | Used in a released or distributed product |
| superseded | Replaced by another version or asset |
| archived | Retained for historical reference only |

## Version Format

```text
v001
v002
v003
```

Version numbers identify meaningful iterations, not every autosave or minor edit.

## Filename Convention

```text
{category}-{subject}-{purpose}-{version}-{status}.{ext}
```

Examples:

```text
cover-aramyst-main-concept-v001-wip.png
character-protagonist-portrait-front-v003-approved.png
map-western-realm-print-v002-review.svg
symbol-moon-seal-transparent-v001-final.png
prompt-character-portrait-template-v001.md
```

## Canonical Fields

| Field | Required | Description |
|---|---:|---|
| Asset ID | Yes | Stable unique identifier |
| Title | Yes | Human-readable asset name |
| Category | Yes | Controlled category |
| Purpose | Yes | Production or story function |
| Book / Chapter / Scene | Yes | Narrative or publication context |
| Subjects | Yes | Characters, locations, objects, or concepts shown |
| Required Dimensions | Yes | Dimensions, aspect ratio, resolution, or format requirements |
| Status | Yes | Current production state |
| Current Version | Yes | Current meaningful version |
| Source File Path | Yes | Editable or highest-quality source path |
| Export Path | When exported | Publication-ready output path |
| Prompt / Reference Path | When applicable | Supporting prompt, brief, or references |
| Owner | Recommended | Person or process responsible for the asset |
| Dependencies | Recommended | Other assets or decisions required first |
| Approval | Recommended | Approval date, approver, or approval note |
| Notes | Optional | Constraints, replacements, rights, or special instructions |

## Entry Template

```md
### AST-XXXX-000 — Asset Title

- **Category:**
- **Purpose:**
- **Book / Chapter / Scene:**
- **Subjects:**
- **Required Dimensions:**
- **Status:** planned
- **Current Version:** v001
- **Source File Path:**
- **Export Path:**
- **Prompt / Reference Path:**
- **Owner:**
- **Dependencies:**
- **Approval:**
- **Notes:**
```

## Master Asset Index

| Asset ID | Title | Category | Context | Status | Version | Source Path | Export Path | Dependencies |
|---|---|---|---|---|---|---|---|---|
| AST-COVER-001 | Main Book Cover | cover | Whole book | planned | v001 | covers/ | exports/ | AST-SYM-001; AST-TYPE-001 |
| AST-MAP-001 | Aramyst World Map | map | Whole book | planned | v001 | maps/ | exports/ | Canon geography decisions |
| AST-MAP-002 | Opening Region Map | map | Opening arc | planned | v001 | maps/ | exports/ | AST-MAP-001 |
| AST-CHAR-001 | Primary Protagonist Portrait | character | Whole book | planned | v001 | characters/ | exports/ | Character canon brief |
| AST-CHAR-002 | Primary Antagonist Portrait | character | Whole book | planned | v001 | characters/ | exports/ | Character canon brief |
| AST-LOC-001 | Opening Location Key Art | location | Opening arc | planned | v001 | locations/ | exports/ | Location canon brief |
| AST-SYM-001 | Aramyst Seal / Emblem | symbol | Whole book | planned | v001 | symbols/ | exports/ | Symbol and theme direction |
| AST-TYPE-001 | Main Title Treatment | typography | Whole book | planned | v001 | typography/ | exports/ | AST-SYM-001; cover direction |

## Detailed Starter Records

### AST-COVER-001 — Main Book Cover

- **Category:** cover
- **Purpose:** Primary front-cover concept and final cover asset.
- **Book / Chapter / Scene:** Whole book
- **Subjects:** Main title, core theme, optional lead subject, approved emblem
- **Required Dimensions:** TBD after trim size, page count, paper type, and publishing platform are confirmed
- **Status:** planned
- **Current Version:** v001
- **Source File Path:** covers/
- **Export Path:** exports/
- **Prompt / Reference Path:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** AST-SYM-001; AST-TYPE-001; final publishing specifications
- **Approval:** Not approved
- **Notes:** Treat this as the anchor cover asset. Preserve editable layered source files.

### AST-MAP-001 — Aramyst World Map

- **Category:** map
- **Purpose:** Canonical world-geography reference and possible publication map.
- **Book / Chapter / Scene:** Whole book
- **Subjects:** Continents, regions, seas, borders, major settlements, and major routes
- **Required Dimensions:** TBD; preserve a scalable or high-resolution master
- **Status:** planned
- **Current Version:** v001
- **Source File Path:** maps/
- **Export Path:** exports/
- **Prompt / Reference Path:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** Canon geography decisions
- **Approval:** Not approved
- **Notes:** This asset governs regional-map consistency.

### AST-MAP-002 — Opening Region Map

- **Category:** map
- **Purpose:** Regional map for the opening story arc.
- **Book / Chapter / Scene:** Opening arc
- **Subjects:** Starting region, settlements, routes, boundaries, and landmarks
- **Required Dimensions:** TBD
- **Status:** planned
- **Current Version:** v001
- **Source File Path:** maps/
- **Export Path:** exports/
- **Prompt / Reference Path:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** AST-MAP-001
- **Approval:** Not approved
- **Notes:** Derive geography and naming from the approved world map.

### AST-CHAR-001 — Primary Protagonist Portrait

- **Category:** character
- **Purpose:** Definitive visual reference for the primary protagonist.
- **Book / Chapter / Scene:** Whole book
- **Subjects:** Primary protagonist
- **Required Dimensions:** TBD; create a high-resolution master suitable for crop variants
- **Status:** planned
- **Current Version:** v001
- **Source File Path:** characters/
- **Export Path:** exports/
- **Prompt / Reference Path:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** Approved character canon brief
- **Approval:** Not approved
- **Notes:** Use this record as the continuity anchor for future protagonist art.

### AST-CHAR-002 — Primary Antagonist Portrait

- **Category:** character
- **Purpose:** Definitive visual reference for the primary antagonist.
- **Book / Chapter / Scene:** Whole book
- **Subjects:** Primary antagonist
- **Required Dimensions:** TBD; create a high-resolution master suitable for crop variants
- **Status:** planned
- **Current Version:** v001
- **Source File Path:** characters/
- **Export Path:** exports/
- **Prompt / Reference Path:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** Approved character canon brief
- **Approval:** Not approved
- **Notes:** Use this record as the continuity anchor for future antagonist art.

### AST-LOC-001 — Opening Location Key Art

- **Category:** location
- **Purpose:** Environment concept and mood anchor for the opening location.
- **Book / Chapter / Scene:** Opening arc
- **Subjects:** Opening location, architecture, terrain, weather, and relevant story details
- **Required Dimensions:** TBD; favor a landscape master unless layout requires otherwise
- **Status:** planned
- **Current Version:** v001
- **Source File Path:** locations/
- **Export Path:** exports/
- **Prompt / Reference Path:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** Approved location canon brief
- **Approval:** Not approved
- **Notes:** Establish recurring environmental and architectural language.

### AST-SYM-001 — Aramyst Seal / Emblem

- **Category:** symbol
- **Purpose:** Recurring visual mark for title pages, cover design, chapter art, and project identity.
- **Book / Chapter / Scene:** Whole book
- **Subjects:** Canonical seal, sigil, emblem, or magical/heraldic motif
- **Required Dimensions:** Vector master preferred; transparent PNG exports required
- **Status:** planned
- **Current Version:** v001
- **Source File Path:** symbols/
- **Export Path:** exports/
- **Prompt / Reference Path:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** Approved symbolic and thematic direction
- **Approval:** Not approved
- **Notes:** Avoid embedding small text in the emblem unless separately controlled.

### AST-TYPE-001 — Main Title Treatment

- **Category:** typography
- **Purpose:** Canonical title lettering and display treatment.
- **Book / Chapter / Scene:** Whole book
- **Subjects:** Aramyst title typography
- **Required Dimensions:** Vector or editable high-resolution master; horizontal and stacked variants recommended
- **Status:** planned
- **Current Version:** v001
- **Source File Path:** typography/
- **Export Path:** exports/
- **Prompt / Reference Path:** prompts/; references/
- **Owner:** TBD
- **Dependencies:** AST-SYM-001; approved cover direction
- **Approval:** Not approved
- **Notes:** Keep title lettering separate from background artwork for reuse.

## Change Log

| Date | Change | Author |
|---|---|---|
| 2026-08-04 | Created canonical asset manifest and starter asset records. | JamesJedi420 / ChatGPT |
