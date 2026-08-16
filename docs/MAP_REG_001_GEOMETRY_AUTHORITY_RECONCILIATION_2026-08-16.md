# MAP-REG-001 Geometry Specification Authority Reconciliation — 2026-08-16

Status: COMPLETE — no existing durable project ID located; prose dependency preserved.

## Target

Named dependency currently used by `AST-MAP-002`:

`MAP-REG-001 Geometry Specification v001 — CONTROLLING`

Controlling Drive document:

- Title: `Aramyst — MAP-REG-001 Geometry Specification v001 — CONTROLLING`
- Drive file ID: `1HKS3TPvCenAKeqC77glZtgT2xXwUwogkDv3AVL8OEdE`
- Classification: controlling authority / canon specification.

## Search result

The project records consistently identify this authority by its exact title plus the Drive file ID above. No existing durable project authority ID was found that is explicitly defined as the identity of this geometry specification itself.

Nearby identifiers are not equivalent and must not be reused:

- `MAP-REG-001` — map product identity, not the geometry-spec document ID.
- `ATLAS-REG-DATA-001` — regional geographic truth-layer register.
- `QA-MAP-REG-001-v0.1` — vector-draft QA report.
- `ATLAS-XSC-AUDIT-001` — three-map cross-scale consistency audit.
- the derived MAP-REG layout register and later acceptance audits are separate records.

The controlling specification is repeatedly cited as `MAP-REG-001 Geometry Specification v001 — CONTROLLING` with Drive ID `1HKS3TPvCenAKeqC77glZtgT2xXwUwogkDv3AVL8OEdE`; those citations do not assign it a separate durable project ID.

## Decision

The equivalence condition required for dependency normalization is **not met**.

Therefore:

1. `AST-MAP-002` retains the existing prose dependency `MAP-REG-001 Geometry Specification v001 — CONTROLLING`.
2. No entry is added to `schemas/external-authority-registry.json` for this document because that registry resolves durable project IDs/ranges, not title-only authorities.
3. No new ID is minted during GitHub maintenance.
4. The Drive file ID remains the authoritative locator for the named controlling document until the project separately assigns or discovers a durable authority ID.
5. If a durable ID is later established, equivalence must be demonstrated against this exact Drive file ID before replacing the prose dependency.

## Guardrail

Do not substitute `MAP-REG-001`, `ATLAS-REG-DATA-001`, a QA/audit ID, or a derived-layout ID for the geometry specification merely because those records participate in the same map-production chain.

## Outcome

**PASS — named authority resolved as intentionally unnormalized.**

The repository now has a documented negative reconciliation: the authority is real and controlling, but it does not currently possess a proven durable project ID suitable for machine-resolution through the external-authority registry.
