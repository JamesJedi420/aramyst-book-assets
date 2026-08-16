# Aramyst Dependency Vocabulary Audit — 2026-08-15

Audit target: `JamesJedi420/aramyst-book-assets` / `main`
Audited main SHA: `98bde283a5aa31bb5953a830a520390db096a847`
Scope: every `dependencies` entry in `manifest.json` / `ASSET_MANIFEST.csv`.

This audit does **not** mint authority IDs, change asset dependencies, alter approval state, or reinterpret canon. It classifies the vocabulary already present and identifies candidates for later machine resolution.

**Resolution update — 2026-08-16:** the original `MAP-ENV-001` ambiguity identified below is resolved by `docs/MAP_ENV_001_RECONCILIATION_2026-08-16.md`. `MAP-ENV-001` is the distinct durable map-product authority implemented by production asset `AST-MAP-003`; the existing `AST-MAP-004` dependency remains `MAP-ENV-001`. Machine resolution for the already-ID-shaped dependencies is now established through `schemas/external-authority-registry.json` and its schema/test contract.

## Result

The 16 registered assets currently contain **41 dependency entries** representing **33 distinct dependency strings**.

They fall into three materially different classes:

1. **Registered asset dependencies** — already machine-resolvable `AST-*` IDs.
2. **Durable external authority identifiers** — strings that already behave like stable project IDs or ID ranges.
3. **Descriptive external gates / authority phrases** — human-readable requirements that may intentionally remain descriptive until a controlling project record exists.

The dependency field is therefore carrying both graph edges and prose gates. The repository now has machine resolution for the current ID-shaped non-asset dependencies, but it must not begin inventing IDs for descriptive gates.

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

## Named authority document without durable ID

`MAP-REG-001 Geometry Specification v001 — CONTROLLING` is not casual prose: it names a specific controlling Drive authority used by `AST-MAP-002`. It remains a high-priority candidate to receive or be mapped to an existing durable authority ID.

This audit and the external authority registry do **not** mint that ID. The correct next action is to locate the controlling specification's existing project identifier, if one exists, before creating any new namespace entry.

## Class 3 — descriptive external gates and authority phrases

The following dependency strings are not presently safe to resolve mechanically because they describe approval conditions, broad canon bodies, or decisions rather than a uniquely identified repository object:

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

`Scene 01 canon` is particularly important because it is reused by six assets (`AST-CHAR-003`, `AST-CHAR-004`, `AST-CHAR-005`, `AST-LOC-002`, `AST-SYM-002`, and `AST-SYM-003`). Repetition makes it a strong candidate for replacement by a durable Scene 01 authority ID once the controlling scene/canon record is identified. The existing `SCN-NODE-001` dependency is not assumed to be equivalent.

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

The effective dependency model now distinguishes:

- `asset` — exact registered `AST-*` dependency;
- `authority` — exact external project authority ID resolved through `schemas/external-authority-registry.json`;
- `authority_range` — deterministic bounded range resolved through the same registry;
- `gate` — intentionally descriptive approval/canon condition that has no stable authority ID yet.

The asset manifest's flat string list remains authoritative; the external registry supplies resolution metadata without forcing an immediate manifest schema migration.

## Priority conversion queue

### Priority A — completed for current ID-shaped dependencies

A machine-readable external authority index now resolves the current durable IDs and ranges used by the registry. `MAP` and `GXR` are included alongside the requested stable `ATLAS`, `GEO`, `ROUTE`, `ENV`, `HOU`, `REL`, and `SCN` namespaces because current dependencies already use them and complete resolution would otherwise remain partial.

### Priority B — remaining named/repeated authorities

1. Find the existing durable project ID, if any, for `MAP-REG-001 Geometry Specification v001 — CONTROLLING`.
2. Identify the controlling durable record for `Scene 01 canon` before changing the six dependent assets.

### Priority C — map continuity phrases only when authority exists

Match each continuity phrase to an already-approved continuity record where possible. Do not create IDs solely to eliminate prose.

### Priority D — retain genuine gates descriptively

Keep publication/art-direction requirements descriptive until they become formal controlled records. A readable gate is preferable to a fabricated identifier.

## Control rules for future dependency edits

1. Never invent a durable authority ID solely during GitHub maintenance.
2. Use `AST-*` only for registered production assets.
3. Prefer an existing approved authority ID over a prose synonym when identity is certain.
4. Do not replace a prose dependency with an ID when equivalence is ambiguous.
5. Preserve bounded range semantics; do not silently expand or contract ranges.
6. Treat repeated descriptive gates as candidates for authority identification, not automatic ID creation.
7. Add new durable external IDs/ranges to `schemas/external-authority-registry.json` with a concrete controlling source before relying on them as machine-resolvable dependencies.
8. Any future dependency-schema migration must update `manifest.json`, `ASSET_MANIFEST.csv`, JSON Schema, validator tests, and human-readable registry documentation together.

## Audit conclusion

**PASS — vocabulary is heterogeneous but the current durable external IDs are now machine-resolvable.**

No current `AST-*` dependency is dangling, and the repository regression test now requires every current ID-shaped non-asset dependency to resolve through the external authority registry. Descriptive gates remain intentionally descriptive until the project possesses stable identity for them.
