# Aramyst GitHub Baseline — Branch-State Supplement — 2026-08-18

Status: **CONTROLLED baseline supplement**

Purpose: synchronize the branch/provenance portion of `docs/GITHUB_BASELINE.md` after the approved deletion of the stale `agent/continuity-gate-audit` ref.

This supplement does not replace the historical baseline snapshots recorded in `docs/GITHUB_BASELINE.md`. It updates the current branch-state interpretation only. Where an older branch-count observation conflicts with the steady-state inventory below, this supplement governs current repository maintenance.

## Verified steady-state branch inventory

After the deletion of `agent/continuity-gate-audit` and subsequent connector verification, the repository contains exactly three branches in steady state:

- `main` — authoritative protected production branch;
- `agent/map-hou-001-functional-adjacency` — intentional historical-provenance exception;
- `agent/q-023-cross-system-sync` — intentional historical-provenance exception.

No other non-`main` branch is part of the controlled steady-state inventory.

Routine short-lived `agent/<scope>` branches created for new work are expected to disappear after their pull requests merge. Their temporary presence does not change the historical-provenance exception set above.

## Completed stale-branch deletion

`agent/continuity-gate-audit` was audited before deletion and confirmed to contain no unique commits ahead of current `main`. It was therefore classified as a stale merged audit ref rather than historical provenance requiring preservation.

Explicit deletion authority was granted. The branch was deleted through the GitHub UI because the connected GitHub toolset did not expose branch-ref deletion. A follow-up GitHub connector inventory verified that the branch no longer exists.

This deletion is complete and is not an outstanding maintenance item.

## Historical-provenance exceptions

### `agent/map-hou-001-functional-adjacency`

Disposition: **PRESERVE — HISTORICAL PROVENANCE EXCEPTION.**

Reason: preserves unique superseded PR #4 functional-adjacency schematic and QA material that never entered `main`. The branch is non-authoritative and must not be used as a current production source or as the base for new asset work.

### `agent/q-023-cross-system-sync`

Disposition: **PRESERVE — HISTORICAL PROVENANCE EXCEPTION.**

Reason: preserves unique superseded PR #11 implementation/reconciliation history later reconciled through the accepted GitHub synchronization work. The branch is non-authoritative and must not be used as a current production source or as the base for new asset work.

## Maintenance rule

The two provenance branches above are the only intentional non-`main` steady-state exceptions. Routine branch hygiene must therefore use this distinction:

1. merged or abandoned routine working branches with no required unique history should be removed;
2. `agent/map-hou-001-functional-adjacency` and `agent/q-023-cross-system-sync` must be retained unless an explicit later archival/deletion decision supersedes their preservation status;
3. new production work must branch from current protected `main`, never from either historical-provenance branch;
4. the mere age of a preserved provenance branch is not a deletion trigger;
5. any newly proposed long-term branch-retention exception must be audited and documented rather than silently added to the steady-state set.

## Pull-request state at synchronization

Immediately before this documentation-sync branch was created, GitHub search returned zero open pull requests. The documentation-sync PR itself is routine ephemeral maintenance and is not part of the steady-state branch exception set.

## Relationship to existing audits

This supplement synchronizes the current branch state with:

- `docs/GITHUB_BASELINE.md` — original repository baseline and branch-preservation policy;
- `docs/PRE_PROVENANCE_ASSET_PRODUCTION_AUDIT_2026-08-18.md` — audit of surviving pre-provenance asset-production work, now updated with the completed stale-branch deletion.

No asset status, version, dependency, approval, source authority, provenance sidecar, canon state, or validation architecture is changed by this branch-state synchronization.

## Current branch-control conclusion

Status: **CONTROLLED.**

The stale continuity-audit ref is gone. `main` remains the authoritative branch. The only two persistent non-`main` refs are intentional, documented, non-authoritative historical-provenance exceptions. No additional branch-cleanup task is implied by their continued existence.