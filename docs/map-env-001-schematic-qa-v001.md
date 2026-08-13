# MAP-ENV-001 — Controlled Local Schematic QA v001

Status: **APPROVED — controlling local geometry**

Source asset: `maps/map-env-001-gm-schematic-v001.svg`

Review register: `MAP-ENV-001-QA-001`

Controlling approval record: Google Drive document `1MDOXkIeBrNNkeafJUpqfpyp41PiiIaTkc5Ci7TR7oeI`.

Authority: approved `ENV-SD-001` through `ENV-SD-007`; `ATLAS-REG-DATA-001`; `MAP-REG-001 Geometry Specification v001 — CONTROLLING`; `SCN-NODE-001`.

## Approved geometry decisions

- `ENV-GD-001` — North-up, non-metric local design window independent of regional coordinates.
- `ENV-GD-002` — `GEO-000003` is represented at its principal-gate interface; this is not a Keep centroid, wall face, or footprint.
- `ENV-GD-003` — `GEO-000004` is represented at its threshold/lamp exterior interface; this is not a House centroid, frontage, property line, or footprint.
- `ENV-GD-004` — `ROUTE-000001` uses the approved distinct curved approach geometry within the `GEO-000009` problem area to the `GEO-000003` principal-gate interface.
- `ENV-GD-005` — `ROUTE-000002` uses the approved separate curved access geometry within the `GEO-000009` problem area to the `GEO-000004` threshold/lamp interface.
- `ENV-GD-006` — `ROUTE-000001` and `ROUTE-000002` share no physical segment or junction in v001. This is the approved v001 layout, not a general rule for future versions.
- `ENV-GD-007` — `O-G` is an approved positive observation position from which the principal-gate interface is plausibly visible.
- `ENV-GD-008` — `O-L` is a separate approved positive observation position from which the Last-Bell threshold/lamp interface is plausibly visible.
- `ENV-GD-009` — No position is required to see both interfaces; v001 asserts no negative visibility from other positions.
- `ENV-GD-010` — Zero local choke points are established in v001.

## Acceptance tests

1. Geographic scope resolves only to `GEO-000003`, `GEO-000004`, `GEO-000007`, and `GEO-000009`: **PASS**.
2. Principal gate remains an endpoint role of `GEO-000003`; no new GEO record is created: **PASS**.
3. No Keep wall footprint, tower, extra gate, internal ward, or street plan appears: **PASS**.
4. No Last-Bell property boundary, frontage, full building footprint, or internal plan appears: **PASS**.
5. `GEO-000007` remains contextual; no Tarl boundary, jurisdiction polygon, wall-side claim, or works-road line appears: **PASS**.
6. `ROUTE-000003` has no physical line: **PASS**.
7. `ROUTE-000004` has no physical line: **PASS**.
8. The reviewed `ROUTE-000001` and `ROUTE-000002` geometry passed the proposal gate and is accepted as v001 local approximate geometry: **PASS**.
9. Positive sight-line annotations have a geometric basis and do not imply universal visibility: **PASS**.
10. No choke point is invented; zero is the approved v001 result: **PASS**.
11. No geographic distance, travel time, route width, scale bar, grid, hex, or movement rate appears: **PASS**.
12. No terrain, vegetation, ditch, ravine, stream, bridge, ford, extra structure, or decorative settlement appears: **PASS**.
13. Unknown local space remains blank: **PASS**.
14. No B2, Mystara, or other external-source geometry supplied the layout: **PASS BY CONSTRUCTION**.
15. The scenario evidence ceiling remains intact; geometry constrains plausibility only: **PASS**.

## Geometry-state effect

`ROUTE-000001`, `ROUTE-000002`, `GXR-000010`, and `GXR-000011` are `APPROXIMATE` at MAP-ENV-001 local-schematic scale through the approved v002 atlas deltas. No other GEO, ROUTE, or GXR geometry state advances.

## Held geometry

- `ROUTE-000003` physical custody/administrative path: **NOT ESTABLISHED**.
- `ROUTE-000004` physical works/service path: **RELATIONAL ONLY**.
- Keep wall footprint and gate-facing wall segment: **NOT ESTABLISHED**.
- Last-Bell frontage, property boundary, full footprint, and Service Yard placement: **NOT ESTABLISHED**.
- Tarl Yard exact wall side, boundary, and works-road alignment: **NOT ESTABLISHED**.
- Occlusion model and negative sight lines: **NOT ESTABLISHED**.
- Terrain profile, contours, measured slope, road surface, road width, distance, travel time, and movement calibration: **NOT ESTABLISHED**.

## Sequencing note — 2026-08-13

`AST-MAP-002` registry reconciliation was completed before this MAP-ENV-001 package was formally accepted into the current production sequence. This synchronization changes repository status wording only; it does not alter approved local geometry.

## QA result

**PASS / APPROVED.** `AST-MAP-003` remains approved local approximate geometry and is not publication-final cartography. No player-facing derivative is authorized by this QA record.
