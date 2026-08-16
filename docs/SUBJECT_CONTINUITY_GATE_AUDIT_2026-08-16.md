# Aramyst Subject-Specific Continuity Gate Audit — 2026-08-16

Scope: six remaining descriptive continuity dependencies used by Scene 01 production assets:

- `Character continuity approval`
- `Chapel continuity approval`
- `Keep guard continuity approval`
- `Keep exterior continuity`
- `Door/time-gate motif continuity`
- `Kael symbol continuity`

Objective: normalize only where an already-existing durable project authority is proven to be one-to-one equivalent. No new authority IDs are minted by this audit.

## Result

**PASS — zero forced normalizations.**

All six phrases remain descriptive gates. Each was traced to relevant Drive records, but no existing durable authority ID was found whose scope exactly equals the dependency phrase. Available records are either broader continuity-control documents, narrower source/asset briefs, templates, source texts without durable authority identity, or authorities whose scope would distort the existing dependency if substituted.

## Gate-by-gate findings

### 1. `Character continuity approval` — retain descriptive

Affected asset: `AST-CHAR-003` — Tovin Marr Portrait.

Relevant records include the generic `Aramyst — Character Continuity Template`, the cross-project Continuity Guide (`CONT-GUIDE-001`), the Canon Fact & Document Registry, and the Tovin Marr production brief itself.

The Character Continuity Template is a reusable schema, not a completed Tovin-specific authority. `CONT-GUIDE-001` is a broad cross-project control layer and is not equivalent to Tovin-specific visual/character approval. The production brief is the asset source being gated, not an independent continuity authority.

Disposition: keep `Character continuity approval` descriptive until a Tovin-specific approved continuity record with durable ID exists.

### 2. `Chapel continuity approval` — retain descriptive

Affected asset: `AST-CHAR-004` — Sister Aneth Portrait.

Searches found the Sister Aneth production brief, Scene 01 working material, the broad Continuity Guide, and general canon/control registers. No durable Chapel-specific continuity authority was found that is explicitly one-to-one equivalent to Sister Aneth's chapel-role/appearance continuity gate.

Disposition: keep `Chapel continuity approval` descriptive. Do not substitute `CONT-GUIDE-001`, the Sister Aneth production brief, or general Scene 01 records.

### 3. `Keep guard continuity approval` — retain descriptive

Affected asset: `AST-CHAR-005` — Sergeant Beran Vask Portrait.

Relevant records include the Beran production brief, the Continuity Guide (`CONT-GUIDE-001`), continuity queue/register material, and Keep/garrison source-extraction records. Existing Keep/garrison authorities are broader or concern different named staff/roles; no durable Beran/Keep-guard continuity record was found whose scope exactly matches this gate.

Disposition: keep `Keep guard continuity approval` descriptive. Do not normalize to a broader Keep staffing, scenario, or continuity-control ID.

### 4. `Keep exterior continuity` — retain descriptive

Affected asset: `AST-LOC-002` — Gate at Dusk Backdrop.

Potential nearby authorities were rejected as non-equivalent. `MAP-ENV-001` governs approved local approximate geometry, but the asset registry explicitly states that it does not establish Keep/House footprints or frontages. Player-safe extraction and broad Keep records likewise do not constitute a single controlling Keep-exterior visual authority.

Disposition: keep `Keep exterior continuity` descriptive until a dedicated approved exterior/location continuity record exists.

### 5. `Door/time-gate motif continuity` — retain descriptive

Affected asset: `AST-SYM-002` — Black Door Sign.

Relevant records include the Black Door Sign production brief, Opening Draft 01, the Handout Registry & Production Standard, campaign/source material, and broader motif-bearing source texts. None provides a durable project authority ID that is explicitly defined as the controlling door/time-gate motif authority for this production asset.

Disposition: keep `Door/time-gate motif continuity` descriptive. Do not substitute a source-text file, handout standard, scenario package ID, or the asset's own brief.

### 6. `Kael symbol continuity` — retain descriptive

Affected asset: `AST-SYM-003` — Triangle Token.

Relevant records include the approved Triangle Token brief/master record, the Handout Registry & Production Standard, and `Prelude (Kael & Maela)`. The Prelude is source material for Kael symbolism, but no durable project authority ID was found that is explicitly assigned as the controlling Kael-symbol continuity record. The asset brief itself is not an independent upstream continuity authority.

Disposition: keep `Kael symbol continuity` descriptive until an approved Kael-symbol continuity record with durable identity exists.

## Normalization decision

No manifest dependency is changed by this audit.

The following substitutions are explicitly **not authorized**:

- any of the six gates → `CONT-GUIDE-001`;
- `Keep exterior continuity` → `MAP-ENV-001`;
- `Door/time-gate motif continuity` → `SCN-INV-001`, `SCN-NODE-001`, or a source-text file;
- `Kael symbol continuity` → the Triangle Token asset itself or `Prelude (Kael & Maela)` without a durable authority identity;
- character/chapel/guard gates → their own production briefs.

## Reopen conditions

A gate may be normalized later only if a durable project ID is discovered or created through the project's normal authority process and the controlling record explicitly covers the same scope as the current dependency. The equivalence must be direct; broad, narrower, adjacent, or merely supporting records are insufficient.

## Conclusion

The six subject-specific continuity phrases are not unresolved defects. They are intentional descriptive gates under the current authority model. Their persistence is preferable to replacing them with misleading machine-resolvable IDs.
