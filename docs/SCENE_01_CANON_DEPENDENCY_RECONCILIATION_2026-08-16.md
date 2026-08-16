# Scene 01 canon dependency reconciliation — 2026-08-16

## Scope

Resolve the repeated dependency string `Scene 01 canon`, currently used by six Scene-01 production assets, without inventing a new project identity or substituting a broader/narrower authority.

## Affected assets

The repeated dependency applies to:

- `AST-CHAR-003` — Tovin Marr Portrait
- `AST-CHAR-004` — Sister Aneth Portrait
- `AST-CHAR-005` — Sergeant Beran Vask Portrait
- `AST-LOC-002` — Gate at Dusk Backdrop
- `AST-SYM-002` — Black Door Sign
- `AST-SYM-003` — Triangle Token

Each asset also carries a more specific continuity dependency appropriate to its subject.

## Authority search

Project records establish several durable `SCN-*` authorities associated with the same campaign/scenario family:

- `SCN-INV-001` — durable investigation/scenario package identity used across the investigation node map, pressure/escalation material, GM tests, handout work, and simulations;
- `SCN-NODE-001` — Investigation Node Map authority inside `SCN-INV-001`;
- `SCN-TRUTH-001` — Hidden Event Reconstruction authority;
- `SCN-PRESS-001` — Scenario Pressure & Escalation Structure authority;
- additional `SCN-*` records governing NPC state, run procedure, tests, and other scenario facets.

The source search did **not** identify a durable authority ID explicitly defined as the complete canon authority for only `Scene 01 — The Gate at Dusk` across character appearance, location presentation, symbols, dialogue/behavior, and continuity.

## Reconciliation

**`Scene 01 canon` is a composite descriptive gate, not an alias for an existing single durable authority.**

In particular:

- it is **not equivalent to `SCN-NODE-001`**; the node map governs investigation structure rather than all scene-specific canon;
- it is **not equivalent to `SCN-TRUTH-001`**; the hidden-event reconstruction governs underlying scenario truth rather than all Scene 01 visual/person continuity;
- it is **not equivalent to `SCN-INV-001`**; `SCN-INV-001` is the broader investigation/scenario package identity and would broaden the current Scene-01-specific dependency;
- the differing companion continuity gates on the six assets confirm that Scene 01 production depends on multiple subject-specific authorities rather than one already-defined scene-canon record.

## Repository disposition

1. Preserve `Scene 01 canon` unchanged in the six asset dependencies.
2. Do not add `Scene 01 canon` to `schemas/external-authority-registry.json`.
3. Do not replace it with `SCN-INV-001`, `SCN-NODE-001`, or `SCN-TRUTH-001`.
4. Do not mint a new Scene 01 authority ID during GitHub maintenance.
5. If the project later creates or identifies a controlled Scene-01-only canon authority, replacement is permitted only after direct equivalence is established for all six dependent assets.

## Result

**RESOLVED — intentional composite gate retained.**

The repeated prose is no longer considered an unresolved vocabulary defect. Its repetition reflects a real shared gate whose controlling content is presently distributed across the broader scenario package and subject-specific continuity authorities. A fabricated or overly broad identifier would reduce precision rather than improve it.

No asset dependency, approval state, canon, production asset, or external-authority registry entry is changed by this reconciliation.
