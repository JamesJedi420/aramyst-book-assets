# Aramyst Broad Descriptive Dependency Gate Audit — 2026-08-16

Scope: six broad descriptive dependencies used by planned production assets:

- `Approved character canon brief`
- `Approved location canon brief`
- `Canon geography decisions`
- `Final publishing specifications`
- `Approved symbolic and thematic direction`
- `Approved cover direction`

Objective: distinguish genuine long-term prose gates from informal wording that already maps one-to-one to an existing controlled project authority. No authority ID is minted by this audit, and no dependency is normalized unless equivalence is direct.

## Result

**PASS — all six remain legitimate descriptive gates.**

No existing durable project authority was found whose scope is one-to-one equivalent to any of the six phrases. Several nearby controlled authorities exist, but each is narrower, broader, partial, provisional, or otherwise insufficient to replace the current gate without changing its meaning.

One phrase, `Final publishing specifications`, has a particularly close existing authority: `Aramyst — Book Production Specification` (Drive file `1Zz1dtGLdGUoEuQ61Muu-zPc20ViG0OgRrWuzZS4rv1M`). That document explicitly governs fixed-layout page production, visual asset preparation, export, review, and publication. However, the current asset registry still marks final bleed/platform specifications as TBD. The existing production specification therefore controls current production practice but does not prove completion of the future *final publishing specifications* gate. It is a supporting controlled authority, not a safe replacement.

## Gate-by-gate findings

### 1. `Approved character canon brief` — retain descriptive

Affected planned assets: `AST-CHAR-001` and `AST-CHAR-002`.

The repository describes these only as the future primary protagonist and primary antagonist portraits. Existing character-continuity infrastructure includes the generic Character Continuity Template, the Canon Fact & Document Registry, the Continuity Guide, and character-specific records for already-developed Scene 01 figures. None is an approved canon brief for the still-generic primary protagonist or antagonist represented by these two planned assets.

Disposition: retain `Approved character canon brief` as a future prerequisite. Normalize only after the actual protagonist/antagonist canon brief is approved and given a durable identity.

### 2. `Approved location canon brief` — retain descriptive

Affected planned asset: `AST-LOC-001` — Opening Location Key Art.

Existing records govern specific developed places and scenario locations, including regional atlas authorities, MAP-ENV local geometry, Last-Bell House records, and Scene 01 location material. `AST-LOC-001`, however, remains a generic whole-opening-arc location asset rather than a specific approved place identity. No existing location authority was found whose scope exactly equals the future approved location canon brief required by this asset.

Disposition: retain `Approved location canon brief` until the asset's exact location identity and controlling canon record are approved.

### 3. `Canon geography decisions` — retain descriptive

Affected planned asset: `AST-MAP-001` — World Map (Publication Identity Pending).

Existing durable geography authorities include:

- `ATLAS-ARCH-001` — World Atlas Architecture;
- `ATLAS-REG-DATA-001` — the current first-playable regional geographic truth layer;
- bounded `GEO-*`, `ROUTE-*`, and `GXR-*` records used by current regional/local work.

These authorities are real and machine-resolvable, but they do not equal completed canonical world geography. `ATLAS-ARCH-001` establishes architecture and uncertainty rules rather than finished geography; `ATLAS-REG-DATA-001` controls only the current regional truth layer. Replacing `Canon geography decisions` with either would incorrectly imply that the world map may be completed from partial geography.

Disposition: retain the prose gate until enough world-scale geography has been explicitly approved to support `AST-MAP-001`, or until a durable world-geography authority is created that expressly owns that complete scope.

### 4. `Final publishing specifications` — retain descriptive, but bind conceptually to current production authority

Affected planned asset: `AST-COVER-001` — Main Book Cover.

`Aramyst — Book Production Specification` is a controlled production authority and is the closest existing record. It governs fixed-layout production, visual asset preparation, export, review, and publication. Its Drive file ID is `1Zz1dtGLdGUoEuQ61Muu-zPc20ViG0OgRrWuzZS4rv1M`.

This is not enough to replace the dependency. `AST-COVER-001` itself states that final bleed and platform specifications are TBD. The phrase `Final publishing specifications` therefore represents the unresolved completion state of the production specification, including final platform-dependent requirements, rather than an informal alias for the current document.

Disposition: retain `Final publishing specifications` as a long-term completion gate. Treat the Book Production Specification as the current controlling production source that will likely absorb or supersede the gate once its final platform/bleed requirements are approved. Do not add it to the external-authority registry under a fabricated ID.

### 5. `Approved symbolic and thematic direction` — retain descriptive

Affected planned asset: `AST-SYM-001` — Project Seal / Emblem (Publication Identity Pending).

Searches found general continuity, canon, development-chronicle, production, and source-material records, but no approved project-wide symbolic/thematic direction authority with durable identity. Existing symbol-specific records such as the Black Door Sign and Triangle Token govern particular Scene 01 evidence props and cannot define the publication-wide seal/emblem direction.

Disposition: retain the gate until a project-wide symbolic/art-direction record is approved.

### 6. `Approved cover direction` — retain descriptive

Affected planned asset: `AST-TYPE-001` — Main Title Treatment (Publication Name Pending).

The Book Production Specification controls production mechanics but does not establish the final cover concept, visual hierarchy, final publication identity, emblem usage, or title-treatment direction. The project still records the publication name as pending, and the cover asset itself remains planned.

Disposition: retain `Approved cover direction` until a controlled cover/art-direction decision exists. Do not substitute the Book Production Specification, development chronicle, or provisional publication architecture.

## Classification

### Genuine long-term prose gates

All six currently belong in this class:

- `Approved character canon brief`
- `Approved location canon brief`
- `Canon geography decisions`
- `Final publishing specifications`
- `Approved symbolic and thematic direction`
- `Approved cover direction`

They are not vocabulary defects. Each expresses a prerequisite whose controlling record is either not yet created, not yet approved, incomplete in scope, or still awaiting final decisions.

### Controlled authorities nearby, but not equivalent

The audit specifically rejects these tempting substitutions:

- `Canon geography decisions` → `ATLAS-ARCH-001`;
- `Canon geography decisions` → `ATLAS-REG-DATA-001`;
- `Final publishing specifications` → the current Book Production Specification as though all final platform requirements were already settled;
- `Approved symbolic and thematic direction` → Scene-01-specific symbol assets or source texts;
- `Approved cover direction` → the Book Production Specification;
- character/location gates → generic templates, broad continuity registers, or unrelated already-developed character/location records.

## Reopen conditions

A gate may be normalized only when an existing or newly approved project authority explicitly covers the same scope and completion state. Supporting, partial, provisional, or neighboring authorities are insufficient.

For `Final publishing specifications`, reopen when the Book Production Specification (or an approved successor) explicitly incorporates the final bleed/platform requirements currently marked TBD and has a durable project identity suitable for dependency resolution.

For `Canon geography decisions`, reopen when a world-scale geography authority exists that expressly controls sufficient world geography for the planned world map rather than only atlas architecture or the first-playable region.

## Conclusion

The remaining broad descriptive dependencies are intentionally descriptive under the current project state. Their prose form correctly prevents incomplete or adjacent authorities from being treated as permission to produce assets whose underlying canon, art direction, or publication constraints are not yet final.
