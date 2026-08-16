# Aramyst Dependency Vocabulary Audit — 2026-08-15

Audit target: `JamesJedi420/aramyst-book-assets` / `main`
Audited main SHA: `98bde283a5aa31bb5953a830a520390db096a847`
Scope: every `dependencies` entry in `manifest.json` / `ASSET_MANIFEST.csv`.

This audit does **not** mint authority IDs, change asset dependencies, alter approval state, or reinterpret canon. It classifies the vocabulary already present and identifies candidates for later machine resolution.

## Result

The 16 registered assets currently contain **41 dependency entries** representing **33 distinct dependency strings**.

They fall into three materially different classes:

1. **Registered asset dependencies** — already machine-resolvable `AST-*` IDs.
2. **Durable external authority identifiers** — strings that already behave like stable project IDs or ID ranges, but are not yet resolved by the repository validator.
3. **Descriptive external gates / authority phrases** — human-readable requirements that may intentionally remain descriptive until a controlling project record exists.

The dependency field is therefore carrying both graph edges and prose gates. The current validator correctly resolves exact `AST-*` dependencies, but it should not begin inventing IDs for the other classes.

## Class 1 — registered asset dependencies

Current exact Asset-ID edges:

- `AST-COVER-001` → `AST-SYM-001`
- `AST-COVER-001` → `AST-TYPE-001`
- `AST-TYPE-001` → `AST-SYM-001`

These are already in the preferred machine-resolvable form and require no vocabulary change.

## Class 2 — durable external authority identifiers

The following dependencies already have durable identifier-like form and are strong candidates for resolution through a future **external authority registry**, rather than being converted into `AST-*` IDs:

### Atlas / geography authorities

- `ATLAS-ARCH-001`
- `ATLAS-REG-DATA-001`
- `GEO-000002–GEO-000010`
- `ROUTE-000001–ROUTE-000007`
- `GXR-000001–GXR-000016`

### Local environment / scenario authorities

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

These strings already communicate stable identity and should not be rewritten as loose prose. Their long-term machine-resolution problem is infrastructural: GitHub needs a controlled authority index capable of resolving external project IDs and, separately, deterministic ID-range syntax.

### Ambiguous identifier requiring reconciliation before automation

`MAP-ENV-001` appears as a dependency of `AST-MAP-004` while `AST-MAP-003` is the registered asset whose title begins `MAP-ENV-001`.

This dependency must **not** be automatically normalized. A later reconciliation must determine whether it means:

- the registered visual asset `AST-MAP-003`, in which case the dependency should eventually become `AST-MAP-003`; or
- a separate non-asset MAP-ENV-001 authority/specification, in which case it should resolve through the external authority registry.

Until that semantic distinction is explicitly approved, `MAP-ENV-001` should remain unchanged.

## Named authority document without durable ID

`MAP-REG-001 Geometry Specification v001 — CONTROLLING` is not casual prose: it names a specific controlling Drive authority used by `AST-MAP-002`. It is therefore a high-priority candidate to receive or be mapped to an existing durable authority ID.

The audit does **not** mint that ID. The correct next action is to locate the controlling specification's existing project identifier, if one exists, before creating any new namespace entry.

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

`Scene 01 canon` is particularly important because it is reused by six assets (`AST-CHAR-003`, `AST-CHAR-004`, `AST-CHAR-005`, `AST-LOC-002`, `AST-SYM-002`, and `AST-SYM-003`). Repetition makes it a strong candidate for replacement by a durable Scene 01 authority ID once the controlling scene/canon record is identified. The existing `SCN-NODE-001` dependency on `AST-MAP-003` is not assumed to be equivalent.

### Continuity / approval gates

- `Character continuity approval`
- `Chapel continuity approval`
- `Keep guard continuity approval`
- `Keep exterior continuity`
- `Door/time-gate motif continuity`
- `Kael symbol continuity`

These phrases express real gates, but the registry alone does not establish which concrete continuity record controls each phrase. They should remain descriptive until matched to already-approved continuity IDs or until a separate authority decision creates those IDs.

## Recommended dependency architecture

Do **not** overload `AST-*` as a universal authority namespace. Asset IDs should continue to mean production assets.

A future machine-resolvable dependency model should support at least:

- `asset` — exact registered `AST-*` dependency;
- `authority` — exact external project authority ID such as `ATLAS-REG-DATA-001` or `REL-CHAP-HOUSE-001`;
- `authority_range` — deterministic bounded ranges such as `GEO-000002–GEO-000010`;
- `gate` — intentionally descriptive approval/canon condition that has no stable authority ID yet.

The current flat string list can remain authoritative until such a schema change is separately approved. This audit recommends classification before migration, not immediate structural conversion.

## Priority conversion queue

### Priority A — resolve existing durable IDs

Create or connect a machine-readable external authority index for the already-ID-shaped dependencies listed in Class 2. No new semantic identifiers are needed for these entries; only resolution infrastructure is missing.

### Priority B — reconcile ambiguous/named authorities

1. Determine whether `MAP-ENV-001` means `AST-MAP-003` or a distinct authority.
2. Find the existing durable project ID, if any, for `MAP-REG-001 Geometry Specification v001 — CONTROLLING`.
3. Identify the controlling durable record for `Scene 01 canon` before changing the six dependent assets.

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
7. Any future dependency-schema migration must update `manifest.json`, `ASSET_MANIFEST.csv`, JSON Schema, validator tests, and human-readable registry documentation together.

## Audit conclusion

**PASS — vocabulary is usable but heterogeneous.**

No current dependency is dangling under the repository's existing `AST-*` resolution rule. The main improvement opportunity is not to rewrite all free text, but to distinguish external durable authorities from intentional descriptive gates and then add machine resolution only where the project already possesses stable identity.