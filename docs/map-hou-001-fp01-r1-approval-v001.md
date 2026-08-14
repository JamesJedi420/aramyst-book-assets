# MAP-HOU-001 — FP01-R1 Approval Binding v001

Status: APPROVED / CONTROLLING PHYSICAL FLOORPLAN REFERENCE

Approval date: 2026-08-14

## Authority

- MAP-HOU-001-CTRL-001 — Controlling Topology & Floorplan Authorization
- MAP-HOU-001-FP-GD-001 — FP01 Candidate Geometry Approval Register
- HOU-FP-GD-001 through HOU-FP-GD-022 — APPROVED / CONTROLLING
- MAP-HOU-001-FP01-R1-QA-001 — FP-01 through FP-14 PASS
- Candidate A — Compact Procedural Hub — controlling topology
- HOU-PD-011 — APPROVED / GOVERNING
- HOU-PD-012 — DEFERRED / GOVERNING

## Controlling source

Repository path: `maps/map-hou-001-fp01-r1-neutral-v001.svg`

Active source SHA-256: `30d3b68113b62987380c945a919c9091a1e56b8ebec7db3fcdc9cdde311058d9`

Pre-approval QA-artifact SHA-256: `a6276209d66453bc13cf3d714c3999978f751a4feff8318b47a15951930e0413`

After geometry approval, the source SVG received a status-label-only synchronization so the visible artifact no longer declared its approved geometry to be candidate/not established. The only changes were human-readable approval/provenance text: the subtitle/status line, one R1 control-note line, and the controlled-opening legend/approval-state text. A structural comparison with all `<text>` elements removed returned exact equality between the QA-reviewed pre-approval SVG and the active approved SVG. No room/yard boundary, coordinate, opening, branch, GD tag, shape, line, or other geometry changed.

The pre-approval checksum is retained above so the artifact lineage remains auditable. Current authority is established by this binding, the Drive control record, the approved geometry register, the R1 QA record, and the asset registry.

## Geometry promoted

Only HOU-FP-GD-001 through HOU-FP-GD-022 are promoted. This includes the approved plan-relative principal mass, established room/yard shapes and placements, controlled openings and access relations, the direct Street Court → Threshold Porch → Petition Hall sequence, Petition Hall distribution geometry, the Guest Hall ↔ Kitchen/Winter Store direct controlled opening, Kitchen/Winter Store ↔ Service Yard opening, Bell Stair attachment/access relation, Record Room → Back Archive Loft exclusive vertical relation, Burial Court placement and two controlled branches, Service Yard interface, and the approved non-metric relative alignment/proportion package.

## Explicit exclusions / continuing holds

HOU-FP-X-001 through HOU-FP-X-008 remain excluded and non-canonical.

HOU-PD-012 remains deferred. The approved floorplan does **not** establish numeric dimensions, map scale, wall thickness, construction materials, decorative architecture, exact compass orientation, window placement, structural system, detailed architectural stair form, or publication styling.

No B2, Mystara, historical church/monastery plan, generic fantasy religious plan, Candidate B geometry, or Candidate C geometry supplies this floorplan.

## Superseded history

The original FP01 candidate failed QA and remains preserved as development history. `MAP-HOU-001-FP01-QA-001` is superseded for active control by the R1 QA and approved geometry package; its failure findings are not deleted or rewritten into a pass.

## Production rule

This asset visualizes approved canon geometry but does not independently expand canon. Any later revision that changes HOU-FP-GD-001–022 requires a new geometry decision/QA cycle. Pure status/provenance-label corrections may be made only when a structural geometry-equivalence check confirms that no geometry changed and both before/after checksums are recorded.

## Geometry freeze — 2026-08-14

Freeze state: **ACTIVE** for `AST-MAP-004` v001.

`HOU-FP-GD-001` through `HOU-FP-GD-022` are frozen as the controlling physical geometry package for `MAP-HOU-001-FP01-R1`. Downstream scenario documents, GM references, workbook material, atlas records, player derivatives, and publication preparation may reference or reproduce this geometry but may not alter it silently.

Any geometry-modifying change to room or yard shape/placement, approved controlled openings, access relationships, the principal-mass envelope, Bell Stair attachment/access relation, Record Room → Back Archive Loft vertical relation, Burial Court branches, Service Yard interface, or the approved relative alignment/proportion package requires all of the following before becoming controlling:

1. a new explicit geometry decision;
2. a new geometry QA cycle; and
3. an appropriate asset-version change.

Non-geometric metadata, provenance, approval-label, or reference corrections may be made without reopening the geometry only when the structural geometry remains unchanged and the audit trail is preserved.

The freeze does **not** reopen `HOU-PD-012`. Numeric dimensions, map scale, wall thickness, construction materials, decorative architecture, exact compass orientation, window placement beyond already approved access openings, structural system, detailed architectural stair form, and publication styling remain **DEFERRED / GOVERNING**. If a later product or procedure genuinely requires one of these categories, it must be returned as a separate `HOU-PD-012` approval gate rather than being inferred from this asset.
