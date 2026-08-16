# MAP-ENV-001 Dependency Reconciliation — 2026-08-16

## Decision

`MAP-ENV-001` is a **distinct durable map-product authority**, not an alias for production asset `AST-MAP-003`.

The existing `AST-MAP-004` dependency on `MAP-ENV-001` is therefore semantically correct and is retained unchanged.

`AST-MAP-003` remains the separate production-asset identifier for the approved GitHub local schematic implementing the MAP-ENV-001 product.

## Source basis

The controlling Drive foundation explicitly declares:

- Map Product ID: `MAP-ENV-001`;
- Foundation ID: `MAP-ENV-001-FOUND-001`;
- approved `ENV-SD-001` through `ENV-SD-007`;
- approved `ENV-GD-001` through `ENV-GD-010`.

The controlled QA record separately identifies:

- Map Product ID: `MAP-ENV-001`;
- Review Register ID: `MAP-ENV-001-QA-001`;
- repository source asset: `maps/map-env-001-gm-schematic-v001.svg`.

The Last-Bell House foundation names its governing source as `MAP-ENV-001 approved package / AST-MAP-003`, demonstrating that the project already treats the map-product authority and the production asset as related but distinct identities.

`SCN-NODE-001` likewise lists both `MAP-ENV-001` and `AST-MAP-003` as separate dependencies.

## Identity rule

Use:

- `MAP-ENV-001` when depending on the approved map product / local-geometry authority and its threshold/lamp interface;
- `AST-MAP-003` when depending on the registered production asset itself.

Do not normalize one identifier to the other.

## Registry consequence

`MAP-ENV-001` is entered in `schemas/external-authority-registry.json` with:

- `kind: map_product`;
- `implemented_by_asset_id: AST-MAP-003`;
- `identity_rule: distinct_from_asset`.

This resolves the ambiguity identified in `docs/DEPENDENCY_VOCABULARY_AUDIT_2026-08-15.md` without changing any current dependency string, approval state, geometry, or asset identity.
