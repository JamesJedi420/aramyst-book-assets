# MAP-HOU-001 Functional Adjacency Schematic QA v001

Status: **PASS — candidate functional-adjacency schematic; no physical floorplan geometry approved.**

Authority: approved `HOU-SD-001–HOU-SD-012`; `REL-CHAP-HOUSE-001`; approved `MAP-ENV-001` threshold/lamp interface; `SCN-NODE-001`; `ATLAS-REG-DATA-001`.

Candidate source: `maps/map-hou-001-functional-adjacency-v001.svg`

## Result

The candidate contains exactly the twelve established Last-Bell House functions/features and represents only approved access, reachability, interface, and support relationships. SVG drawing positions are presentation-only and carry no spatial authority.

The candidate is not a floorplan. It establishes no footprint, room shape, floor assignment, wall, doorway, corridor, stair geometry, compass-facing wall, dimensions, scale, architectural style, property boundary, or neighboring geography.

## Acceptance tests

- PASS — all twelve established functions/features occur exactly once as functional nodes.
- PASS — no new room, religious architectural feature, service building, or property feature is introduced.
- PASS — relationship lines are labeled as public access, controlled/conditional access, functional connection, or interface annotation rather than measured corridors.
- PASS — public access does not automatically cross Witness Room, Record Room, Back Archive Loft, Guest Hall, Burial Court, Kitchen/Winter Store, or Service Yard.
- PASS — the Petition Hall branch structure supports multiple investigation paths instead of a fixed node order.
- PASS — Threshold Porch/Lamp Niche preserve the approved MAP-ENV-001 exterior interface and O-L positive visibility relationship without inventing frontage.
- PASS — Burial Court remains controlled-reachability only; origin/path/adjacency remain unresolved.
- PASS — Bell Stair remains operationally reachable; attachment/path remain unresolved and do not create archive/witness access.
- PASS — service/public access modes remain distinct without asserting a shared entrance, lane, yard, doorway, or intersection.
- PASS — no Keep geometry, road geometry, neighboring settlement geography, terrain, or external-source plan is imported.
- PASS BY CONSTRUCTION — no B2, Mystara, historical church plan, monastery plan, or generic fantasy religious layout supplied missing geometry.
- PASS — no floor count, compass orientation, door count, wall geometry, dimensions, scale, travel time, or architectural style is implied.
- PASS — unknown adjacency remains explicitly `NOT ESTABLISHED`.

## Geometry-state effect

No internal function receives a `GEO` ID or independent geometry state. `GEO-000004` remains the sole geographic identity for the site at this layer. The graph is an approved-requirements visualization only; it must not be traced as proportional floorplan input.

## Physical-layout hold

The still-needed physical decisions are intentionally kept outside this QA record in `MAP-HOU-001-PHYS-001`. No floorplan is authorized until those decisions are separately resolved or explicitly held for a topology-only intermediate pass.
