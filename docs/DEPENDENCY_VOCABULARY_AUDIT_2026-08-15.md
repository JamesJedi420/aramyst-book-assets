# Aramyst Dependency Vocabulary Audit — 2026-08-15

Audit target: `JamesJedi420/aramyst-book-assets` / `main`
Audited main SHA: `98bde283a5aa31bb5953a830a520390db096a847`
Scope: every `dependencies` entry in `manifest.json` / `ASSET_MANIFEST.csv`.

This audit does **not** mint authority IDs, change asset dependencies, alter approval state, or reinterpret canon. It classifies the vocabulary already present and identifies candidates for later machine resolution.

**Resolution update — 2026-08-16:** the original `MAP-ENV-001` ambiguity is resolved by `docs/MAP_ENV_001_RECONCILIATION_2026-08-16.md`. `MAP-ENV-001` is the distinct durable map-product authority implemented by production asset `AST-MAP-003`; the existing `AST-MAP-004` dependency remains `MAP-ENV-001`. Machine resolution for the already-ID-shaped dependencies is established through `schemas/external-authority-registry.json` and its schema/test contract.

**Named-authority update — 2026-08-16:** `docs/MAP_REG_001_GEOMETRY_AUTHORITY_RECONCILIATION_2026-08-16.md` records the completed search for a durable ID for `MAP-REG-001 Geometry Specification v001 — CONTROLLING`. No existing project ID was found that is explicitly assigned to that specification. Its current prose dependency therefore remains authoritative and intentionally unnormalized; the exact Drive file ID is the equivalence anchor for any future normalization.

**Scene-01 update — 2026-08-16:** `docs/SCENE_01_CANON_DEPENDENCY_RECONCILIATION_2026-08-16.md` resolves the repeated `Scene 01 canon` dependency as an intentional composite gate. No existing single durable authority was found that is equivalent to Scene-01-only canon across the six affected character/location/symbol assets. `SCN-INV-001` is broader scenario-package identity; `SCN-NODE-001`, `SCN-TRUTH-001`, and other `SCN-*` records govern narrower facets. The dependency therefore remains unchanged and is no longer treated as an unresolved vocabulary defect.

## Result

The 16 registered assets currently contain **41 dependency entries** representing **33 distinct dependency strings**.

They fall into three materially different classes:

1. **Registered asset dependencies** — already machine-resolvable `AST-*` IDs.
2. **Durable external authority identifiers** — strings that already behave like stable project IDs or ID ranges.
3. **Descriptive external gates / authority phrases** — human-readable requirements that may intentionally remain descriptive when no single equivalent durable authority exists.

The dependency field is therefore carrying both graph edges and prose gates. The repository has machine resolution for the current ID-shaped non-asset dependencies, but it must not invent IDs or substitute broader/narrower authorities for descriptive or title-only gates.

## Class 1 — registered asset dependencies

Current exact Asset-ID edges:

- `AST-COVER-001` → `AST-SYM-001`
- `AST-COVER-001` → `AST-TYPE-001`
- `AST-TYPE-001` → `AST-SYM-001`

These are already in the preferred machine-resolvable form and require no vocabulary change.

## Class 2 — durable external authority identifiers

The following dependencies already have durable identifier-like form and resolve through the controlled external authority registry rather than being converted into `AST-*` IDs:

### Atlas / geography authorities

- `ATLAS-ARCH-001`
- `ATLAS-REG-DATA-001`
- `GEO-000002–GEO-000010`
- `ROUTE-000001–ROUTE-000007`
- `GXR-000001–GXR-000016`

### Local environment / scenario authorities

- `MAP-ENV-001`
- `MAP-ENV-001-FOUND-001`
- `ENV-SD-001–ENV-SD-007`
- `ENV-GD-001–ENV-GD-010`
- `MAP-ENV-001-QA-001`
- `SCN-NODE-001`

### House / geometry / relationship authorities

- `MAP-HOU-001-CTRL-001`
- `MAP-HOU-001-FP-GD-001`
- `HOU-FP-GD-001–HOU-FP-GD-022`
- `MAP-HOU-001-FP01-R1-QA-001`
- `REL-CHAP-HOUSE-001`
- `HOU-PD-012`

These strings communicate stable identity and should not be rewritten as loose prose. Their machine-resolution source is `schemas/external-authority-registry.json`; bounded ranges retain their exact prefix, width, and start/end semantics.

### Resolved identifier: `MAP-ENV-001`

`MAP-ENV-001` is **not** an alias for `AST-MAP-003`.

The controlling Drive foundation explicitly declares `MAP-ENV-001` as the Map Product ID and `MAP-ENV-001-FOUND-001` as its Foundation ID. The MAP-ENV QA record separately identifies the repository source asset. The Last-Bell House foundation names `MAP-ENV-001 approved package / AST-MAP-003` as related governing sources, and `SCN-NODE-001` lists both identifiers independently.

Therefore:

- use `MAP-ENV-001` for the durable approved map-product/local-geometry authority;
- use `AST-MAP-003` for the registered production asset;
- do not normalize one identifier into the other.

## Named authority document without durable ID — reconciled

`MAP-REG-001 Geometry Specification v001 — CONTROLLING` names a specific controlling Drive authority used by `AST-MAP-002`.

The reconciliation in `docs/MAP_REG_001_GEOMETRY_AUTHORITY_RECONCILIATION_2026-08-16.md` searched the controlling document and surrounding project records for an existing durable project ID. None was found that is explicitly defined as the identity of the geometry specification itself.

The exact controlling document is anchored by Drive file ID `1HKS3TPvCenAKeqC77glZtgT2xXwUwogkDv3AVL8OEdE`. Nearby identifiers such as `MAP-REG-001`, `ATLAS-REG-DATA-001`, QA/audit IDs, and the derived layout register identify related but different records and must not be substituted.

Therefore the dependency remains `MAP-REG-001 Geometry Specification v001 — CONTROLLING` as intentional title-based authority. It must remain outside `schemas/external-authority-registry.json` unless a durable project ID is later assigned or discovered and proven equivalent to that exact Drive file.

## Class 3 — descriptive external gates and authority phrases

The following dependency strings are not safe to resolve mechanically because they describe approval conditions, broad canon bodies, decisions, composite authority gates, or title-only authorities rather than one uniquely equivalent durable project ID.

### Publication / art-direction gates

- `Final publishing specifications`
- `Approved symbolic and thematic direction`
- `Approved cover direction`

These may remain descriptive until the project establishes a controlling publication/art-direction record with a durable ID.

### Broad canon / brief gates

- `Canon geography decisions`
- `Approved character canon brief`
- `Approved location canon brief`
- `Scene 01 canon`

### Resolved composite gate: `Scene 01 canon`

`Scene 01 canon` is reused by six assets: `AST-CHAR-003`, `AST-CHAR-004`, `AST-CHAR-005`, `AST-LOC-002`, `AST-SYM-002`, and `AST-SYM-003`.

The reconciliation in `docs/SCENE_01_CANON_DEPENDENCY_RECONCILIATION_2026-08-16.md` found no existing single durable authority that is equivalent to the complete Scene-01-specific canon needed by all six assets.

- `SCN-INV-001` is the broader investigation/scenario package identity, not a Scene-01-only canon record.
- `SCN-NODE-001` governs investigation-node structure, not all Scene 01 character/location/symbol continuity.
- `SCN-TRUTH-001` governs hidden-event reconstruction, not all Scene 01 presentation canon.
- each affected asset also carries a subject-specific continuity gate, confirming that the shared Scene 01 requirement is distributed rather than owned by one already-defined authority.

Therefore `Scene 01 canon` remains an intentional composite descriptive gate. Its repetition is no longer a conversion candidate unless the project later creates or identifies a Scene-01-only canon authority proven equivalent for all six assets.

### Continuity / approval gates

- `Character continuity approval`
- `Chapel continuity approval`
- `Keep guard continuity approval`
- `Keep exterior continuity`
- `Door/time-gate motif continuity`
- `Kael symbol continuity`

These phrases express real gates, but the registry alone does not establish which concrete continuity record controls each phrase. They should remain descriptive until matched to already-approved continuity IDs or until a separate authority decision creates those IDs.

## Machine-resolvable dependency architecture

Do **not** overload `AST-*` as a universal authority namespace. Asset IDs continue to mean production assets.

The effective dependency model distinguishes:

- `asset` — exact registered `AST-*` dependency;
- `authority` — exact external project authority ID resolved through `schemas/external-authority-registry.json`;
- `authority_range` — deterministic bounded range resolved through the same registry;
- `gate` — intentionally descriptive, composite, or title-based approval/canon condition that has no single stable equivalent authority ID.

The asset manifest's flat string list remains authoritative; the external registry supplies resolution metadata without forcing an immediate manifest schema migration.

## Priority conversion queue

### Priority A — completed for current ID-shaped dependencies

A machine-readable external authority index resolves the current durable IDs and ranges used by the registry. `MAP` and `GXR` are included alongside the requested stable `ATLAS`, `GEO`, `ROUTE`, `ENV`, `HOU`, `REL`, and `SCN` namespaces because current dependencies already use them and complete resolution would otherwise remain partial.

### Priority B — reconciled title/composite gates

- `MAP-REG-001 Geometry Specification v001 — CONTROLLING`: reviewed; no durable ID exists for the exact specification, so title-based dependency retained.
- `Scene 01 canon`: reviewed; no single equivalent Scene-01-only authority exists, so composite gate retained.

Reopen either item only when new source evidence establishes a directly equivalent durable authority.

### Priority C — map continuity phrases only when authority exists

Match each continuity phrase to an already-approved continuity record where possible. Do not create IDs solely to eliminate prose.

### Priority D — retain genuine gates descriptively

Keep publication/art-direction requirements descriptive until they become formal controlled records. A readable gate is preferable to a fabricated identifier.

## Control rules for future dependency edits

1. Never invent a durable authority ID solely during GitHub maintenance.
2. Use `AST-*` only for registered production assets.
3. Prefer an existing approved authority ID over a prose synonym when identity is certain.
4. Do not replace a prose dependency with an ID when equivalence is ambiguous, broader, narrower, or otherwise unproven.
5. Preserve bounded range semantics; do not silently expand or contract ranges.
6. Treat repeated descriptive gates as candidates for authority identification, not automatic ID creation.
7. Add new durable external IDs/ranges to `schemas/external-authority-registry.json` with a concrete controlling source before relying on them as machine-resolvable dependencies.
8. For a title-only controlling authority, retain the title until a durable ID exists; use the exact source locator as the future equivalence anchor.
9. For a composite gate, retain the prose when multiple narrower authorities jointly govern the requirement and no single equivalent authority exists.
10. Any future dependency-schema migration must update `manifest.json`, `ASSET_MANIFEST.csv`, JSON Schema, validator tests, and human-readable registry documentation together.

## Audit conclusion

**PASS — vocabulary is heterogeneous but controlled.**

Current durable external IDs are machine-resolvable. The MAP-REG title-only authority and repeated `Scene 01 canon` gate have both been explicitly reconciled rather than force-normalized. No current `AST-*` dependency is dangling, and descriptive gates remain descriptive where replacing them with an existing ID would distort scope or authority.
