# MAP-ENV-001 — Controlled Local Schematic QA v001

Status: REVIEW — candidate geometry only

Source asset: `maps/map-env-001-gm-schematic-v001.svg`

Authority: approved `ENV-SD-001` through `ENV-SD-007`; `ATLAS-REG-DATA-001`; `MAP-REG-001 Geometry Specification v001 — CONTROLLING`; `SCN-NODE-001`.

## Candidate geometry decisions returned for review

- `ENV-GD-001` — Use a north-up, non-metric local design window independent of regional coordinates.
- `ENV-GD-002` — Represent `GEO-000003` at its principal-gate interface for this local view; this is not a Keep centroid, wall face, or footprint.
- `ENV-GD-003` — Represent `GEO-000004` at its threshold/lamp exterior interface for this local view; this is not a House centroid, frontage, property line, or footprint.
- `ENV-GD-004` — Candidate `ROUTE-000001` is a distinct curved approach path within the `GEO-000009` problem area to the `GEO-000003` principal-gate interface.
- `ENV-GD-005` — Candidate `ROUTE-000002` is a separate curved access path within the `GEO-000009` problem area to the `GEO-000004` threshold interface.
- `ENV-GD-006` — Candidate `ROUTE-000001` and `ROUTE-000002` do not share a physical segment or junction in v001. This is a candidate layout decision, not a general route rule.
- `ENV-GD-007` — `O-G` is a positive candidate observation position from which the principal-gate interface is plausibly visible.
- `ENV-GD-008` — `O-L` is a separate positive candidate observation position from which the Last-Bell threshold/lamp interface is plausibly visible.
- `ENV-GD-009` — No position is required to see both interfaces; v001 does not assert negative visibility from other positions.
- `ENV-GD-010` — Zero choke points are established in v001.

## Acceptance tests

1. Geographic scope resolves only to `GEO-000003`, `GEO-000004`, `GEO-000007`, and `GEO-000009`: PASS.
2. Principal gate remains an endpoint role of `GEO-000003`; no new GEO record is created: PASS.
3. No Keep wall footprint, tower, extra gate, internal ward, or street plan appears: PASS.
4. No Last-Bell property boundary, frontage, full building footprint, or internal plan appears: PASS.
5. `GEO-000007` is contextual only; no Tarl boundary, jurisdiction polygon, wall-side claim, or works-road line appears: PASS.
6. `ROUTE-000003` has no physical line: PASS.
7. `ROUTE-000004` has no physical line: PASS.
8. Candidate `ROUTE-000001` and `ROUTE-000002` lines are explicitly labeled PROPOSED: PASS.
9. Positive sight-line annotations identify their candidate geometric basis and do not imply universal visibility: PASS.
10. No choke point is invented; zero remains a valid candidate result: PASS.
11. No geographic distance, travel time, route width, scale bar, grid, hex, or movement rate appears: PASS. SVG pixel/viewBox values are production drawing coordinates only and are explicitly non-metric.
12. No terrain, vegetation, ditch, ravine, stream, bridge, ford, extra structure, or decorative settlement appears: PASS.
13. Unknown local space remains blank: PASS.
14. No external-source geometry was consulted or imported in producing the candidate: PASS BY CONSTRUCTION.
15. Scenario evidence ceiling remains intact; geometry constrains plausibility only and does not identify a culprit or resolve an unknowable chronology: PASS.

## Held geometry

- `ROUTE-000003` physical custody/administrative path: NOT ESTABLISHED.
- `ROUTE-000004` physical works/service path: RELATIONAL ONLY.
- Keep wall footprint and gate-facing wall segment: NOT ESTABLISHED.
- Last-Bell frontage, property boundary, full footprint, and service-yard placement: NOT ESTABLISHED.
- Tarl Yard exact wall side, boundary, and works-road alignment: NOT ESTABLISHED.
- Occlusion model and negative sight lines: NOT ESTABLISHED.
- Terrain profile, contours, measured slope, road surface, road width, distance, travel time, and movement calibration: NOT ESTABLISHED.

## QA result

The v001 schematic passes the approved no-invention and scenario-evidence gates as a **candidate review artifact**. It is not approved geographic geometry yet. No GEO, ROUTE, or GXR geometry state should advance until `ENV-GD-001` through `ENV-GD-010` are approved, rejected, or modified.
