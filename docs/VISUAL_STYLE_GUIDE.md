# Aramyst Visual Style Guide

Canonical visual-direction document for the project currently using **Aramyst** as a development alias. The final publication/setting title remains unresolved. Under `SYS-001`, this is a standalone game/book project; this guide does not assert 5e compatibility.

This guide governs covers, page art, character and creature illustrations, locations, maps, symbols, typography, borders, and production-ready page assets. It should be read together with:

- `docs/ASSET_MANIFEST.md`
- `docs/NAMING_AND_VERSIONING.md`
- `ASSET_MANIFEST.csv`
- `manifest.json` when fixed-layout pages are assembled

## 1. Approved Direction

The approved direction is **restrained old-school grim-frontier fantasy** presented as a **manuscript or sacred frontier record**, not a modern poster collage.

Primary mood and layout references:

- *The Black Hours*
- Morgan MS 493

These references define hierarchy, atmosphere, ornament, and material character. They are not templates to copy literally.

### Core Qualities

Every major asset should reinforce at least three of these qualities:

- weathered
- solemn
- dangerous
- devotional
- remote
- tactile
- legible
- historically layered
- restrained rather than maximal

### Avoid

- crowded montage compositions
- glossy high-fantasy advertising language
- neon or highly saturated palettes
- clean modern UI styling inside book pages
- generic cinematic lens flares
- excessive magical particle effects
- decorative borders that overpower the content
- pseudo-medieval typography that harms readability
- unrelated visual motifs used only to fill space

## 2. Production Format

The canonical book format is fixed-layout **6 × 9 inches**, a 2:3 page ratio.

### Page Pipeline

- Numeric prefixes control page order.
- `manifest.json` is the ordering source of truth.
- Page images are stored as fixed-layout raster outputs.
- Base64-wrapped page assets use the original extension followed by `.b64`.
- The current cover target is `pages/001_cover.png.b64`.

### Resolution

- Work at print resolution whenever practical.
- A 6 × 9 inch page at 300 DPI is 1800 × 2700 pixels before bleed.
- Keep editable or layered masters whenever the source format supports them.
- Do not bake trim, bleed, or platform-specific spine measurements into canonical art until publishing specifications are confirmed.

### Safe Composition

- Keep critical faces, text, symbols, and landmarks away from trim edges.
- Leave generous internal margins appropriate to a manuscript page.
- Do not place critical information across a gutter unless the spread is intentionally designed for it.
- Background texture may reach the edge; essential content should not.

## 3. Visual Hierarchy

Pages and covers should read in this order:

1. primary title or subject
2. central image, seal, map, or focal ornament
3. section or chapter information
4. supporting labels and marginal details
5. texture and secondary decoration

Use a clear central hierarchy. Empty space is part of the design and should not automatically be filled.

## 4. Composition Language

### Preferred Structures

- centered title above a single dominant emblem or scene
- framed manuscript panel with controlled marginal decoration
- symmetrical or near-symmetrical cover architecture
- isolated figure or object against a dark field
- landscape illustration treated as a recorded place rather than a panoramic advertisement
- maps framed as working documents, chronicles, or sacred records

### Border System

Borders should feel drawn, engraved, stamped, illuminated, or assembled from repeated symbolic marks.

Use borders to:

- establish page hierarchy
- separate primary content from marginal notes
- reinforce factions, regions, or chapters
- create continuity across the book

Borders should normally use one primary line weight and one secondary detail weight. Avoid more than three competing ornament systems on one page.

## 5. Color System

The default palette is dark, mineral, parchment-based, and low saturation.

| Role | Suggested Color | Hex | Use |
|---|---|---:|---|
| Deep field | Charcoal-black | `#15140F` | Covers, title fields, deep shadows |
| Warm paper | Aged parchment | `#D2C29C` | Page grounds, labels, map fields |
| Light paper | Bone vellum | `#E5D9BC` | High-legibility text grounds |
| Primary metal | Antique gold | `#A78345` | Titles, seals, key borders, sacred emphasis |
| Secondary metal | Tarnished silver | `#969693` | Secondary lettering, cold factions, restrained highlights |
| Earth accent | Oxide red | `#71362E` | Warnings, bloodline or danger accents, limited emphasis |
| Forest accent | Pine charcoal | `#29332B` | Wilderness, frontier maps, muted natural variation |
| Ink | Brown-black | `#241F19` | Body text, line art, map labels |

### Palette Rules

- Metallic colors are accents, not large flat fills.
- Use one dominant accent family per asset.
- Reserve red for narrative or navigational significance.
- Keep most illustrations below full saturation.
- Black should retain visible material texture rather than becoming a featureless digital void.

## 6. Typography

Typography should evoke an old record while remaining practical for sustained reading.

### Roles

- **Primary display:** engraved, inscriptional, uncial-influenced, or formal old-style display face.
- **Secondary display:** restrained small caps or narrow serif for chapter and section headings.
- **Body text:** readable old-style serif with open counters and durable print performance.
- **Map and marginal labels:** compact serif, small caps, or hand-lettered style with controlled variation.
- **Numbers and rules data:** highly legible serif or humanist companion face; clarity outranks atmosphere.

### Typography Rules

- Do not use ornate display lettering for paragraphs.
- Maintain clear contrast between title, heading, body, caption, and marginal note.
- Keep the main title treatment separate from background art.
- Preserve editable title text and vector masters when possible.
- Avoid more than two display families and one body family in a single production system.
- Confirm commercial-use licensing before a font becomes canonical.

## 7. Illustration Direction

### Rendering

Preferred rendering should feel:

- painterly, engraved, inked, or manuscript-adjacent
- materially textured
- grounded in practical clothing, tools, architecture, and terrain
- dramatic through value and composition rather than effects overload

Photorealism is not required. Consistency and world specificity matter more than surface realism.

### Lighting

- Favor firelight, overcast daylight, moonlight, candlelight, storm light, and deep interior shadow.
- Use light as a story condition rather than a glamour effect.
- Maintain readable silhouettes.
- Magical illumination should have a defined source, color logic, and narrative purpose.

### Characters

- Prioritize recognizable silhouette, equipment, posture, age, and lived-in clothing.
- Costumes should show repair, use, climate, and social role.
- Avoid generic pristine armor unless canon requires it.
- Character continuity assets should document front view, profile, key equipment, palette, and distinguishing marks.
- Heroic framing should remain severe and grounded rather than triumphant by default.

### Creatures

- Build creatures from ecological, folkloric, or magical logic.
- Define scale with environment or human comparison when useful.
- Avoid arbitrary spikes, glowing seams, or anatomy added only to signal danger.
- Distinguish ordinary fauna, corrupted creatures, spirits, and legendary entities through consistent visual rules.

### Locations

- Architecture should reflect available materials, climate, defense needs, trade, and history.
- Repeated construction details should establish regional identity.
- Show evidence of occupation: repairs, soot, tracks, refuse, offerings, weathering, or abandoned tools.
- Landscapes should communicate navigational and encounter-relevant information where possible.

## 8. Maps and Diagrams

Maps must remain usable at 6 × 9 inches.

### Map Rules

- Establish a clear scale and orientation when relevant.
- Use a limited symbol vocabulary.
- Maintain strong distinction among roads, rivers, borders, elevation, settlements, ruins, and encounter sites.
- Keep labels horizontal where possible and avoid collisions.
- Use decorative monsters, compass roses, or marginal art sparingly.
- Ensure important locations remain identifiable in grayscale.
- Preserve a scalable master or the highest-resolution editable source.

### Map Styling

Maps should resemble functional frontier records: surveyed, copied, amended, inherited, or sanctified. Imperfection may be visible, but geography must remain internally consistent.

## 9. Symbols, Seals, and Faction Marks

Symbols should be simple enough to recognize at small sizes and specific enough to belong to this setting/project.

Every canonical symbol should have:

- a full-detail master
- a simplified small-size version
- a one-color version
- a transparent-background export
- documented meaning and ownership

Avoid embedding small text inside emblems. Text and symbol should remain separable whenever possible.

## 10. Texture and Material Treatment

Approved texture families include:

- vellum and aged paper
- ink bloom and dry-brush edges
- engraved or stamped metal
- soot, ash, mud, and weathering
- faded mineral pigment
- restrained gold or silver leaf effects

Texture must support hierarchy. Do not use uniform noise over every element.

## 11. Asset-Specific Requirements

### Cover

- Dark field.
- Antique gold or silver title hierarchy.
- Decorated border with a clear central axis.
- One primary image, seal, or scene.
- No poster-collage assembly.
- Title, emblem, and background remain separately editable.

### Interior Full-Page Art

- Compose for 2:3 portrait output unless a spread is approved.
- Keep essential narrative details inside the safe composition area.
- Leave intentional space for captions or page furniture when required.

### Spot Art

- Use strong silhouette and limited local complexity.
- Prepare transparent-background versions when appropriate.
- Confirm that fine detail survives at intended print size.

### Chapter Openers

- Use repeatable hierarchy: chapter mark, title, short descriptor, controlled ornament, and one focal illustration or symbol.
- Preserve continuity while allowing chapter-specific motif changes.

## 12. Approval Checklist

An asset is ready for `review` only when:

- its Asset ID exists in `docs/ASSET_MANIFEST.md` and `ASSET_MANIFEST.csv`
- its filename follows `docs/NAMING_AND_VERSIONING.md`
- the current version is recorded
- source and output paths are known
- the composition fits the intended 6 × 9 use
- typography is legible at final size
- palette and ornament follow this guide
- required continuity references were used
- no unlicensed font, stock, or third-party material is embedded without documentation

An asset is ready for `approved` only after creative direction, canon consistency, and production suitability are all accepted.

## 13. Change Control

Changes to the approved direction should be recorded in this file and dated. A single experimental asset does not redefine the canonical style.

## Change Log

| Date | Change | Author |
|---|---|---|
| 2026-08-14 | Q-023 continuity synchronization: made publication identity explicitly unresolved and removed the obsolete 5e-compatibility claim under standalone `SYS-001`. | JamesJedi420 / ChatGPT |
| 2026-08-04 | Created canonical visual style guide from the approved grim-frontier manuscript direction. | JamesJedi420 / ChatGPT |
