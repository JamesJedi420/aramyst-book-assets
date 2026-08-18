# Pre-Provenance Asset-Production Audit — 2026-08-18

Status: **CONTROLLED repository audit**

Purpose: identify any still-open pull request or surviving branch that began an `in-progress` → `approved` asset promotion before the approved-asset provenance contract was introduced, so the work can be reconciled before merge rather than failing late in CI.

## Current open PR state

At audit time, the repository has **zero open pull requests**.

Therefore there is no currently open asset-production PR awaiting provenance reconciliation.

PR #34 — the only identified pre-contract approval promotion requiring reconciliation — has already been reconciled against current `main`, supplied with `provenance/ast-char-004-v001.json`, passed `Validate approved asset provenance`, and merged.

## Surviving non-main branches

Three non-`main` branches remained at the original audit point:

### `agent/map-hou-001-functional-adjacency`

Disposition: **PRESERVED HISTORICAL PROVENANCE — NOT ACTIVE ASSET PRODUCTION.**

This is the previously audited superseded MAP-HOU functional-adjacency branch retained because it carries unique historical schematic/QA material. It is not an active approval branch and must not be revived as an asset-production base.

### `agent/q-023-cross-system-sync`

Disposition: **PRESERVED HISTORICAL PROVENANCE — NOT ACTIVE ASSET PRODUCTION.**

This is the previously audited superseded Q-023 implementation branch retained to preserve reconciliation history. It is not an active approval branch and must not be revived as an asset-production base.

### `agent/continuity-gate-audit`

Original disposition: **STALE MERGED AUDIT REF — NO UNMERGED ASSET PROMOTION.**

GitHub reported no commits between then-current `main` and this branch when a PR was attempted, so it carried no unique unmerged work relative to `main`.

Its historical manifest snapshot also left the relevant Scene 01 visual records (`AST-CHAR-003`, `AST-CHAR-004`, `AST-CHAR-005`, and `AST-LOC-002`) in `in-progress` state. It therefore did not contain a hidden pre-contract `in-progress` → `approved` promotion.

The branch was not a valid base for new production because its working tree predated later provenance controls and newer approved asset state.

## Post-audit branch cleanup — 2026-08-18

The stale `agent/continuity-gate-audit` ref was separately audited against current `main` and confirmed to have no unique commits ahead of `main`. Explicit deletion authority was then granted, the branch was deleted through the GitHub UI, and a follow-up connector inventory verified that the ref no longer exists.

Steady-state branch inventory after that cleanup is therefore:

- `main` — authoritative production branch;
- `agent/map-hou-001-functional-adjacency` — **intentional historical-provenance exception** preserving unique superseded PR #4 schematic/QA history;
- `agent/q-023-cross-system-sync` — **intentional historical-provenance exception** preserving unique superseded PR #11/reconciliation history.

The two remaining non-`main` branches are not unexplained stale work and are not candidates for routine branch cleanup. They are explicitly preserved, non-authoritative historical-provenance exceptions. They must not be used as bases for new production work, and they must not be deleted unless a later explicit archival/deletion decision supersedes this preservation rule.

## Finding

**PASS — no unreconciled pre-provenance asset-approval work is currently open.**

There is no surviving branch or open PR that both:

1. contains an unmerged asset promotion to `approved`, `exported`, or `published`; and
2. predates the approved-asset provenance contract without the required `provenance/*.json` sidecar.

The two surviving non-`main` branches are intentional historical-provenance exceptions, not production branches. The stale continuity-audit ref has been deleted after a zero-unique-commit verification.

## Required rule for future approval work

Any future asset approval branch MUST:

1. branch from current protected `main` after the provenance contract;
2. promote the asset and add/update its machine-readable provenance sidecar in the same PR;
3. bind the final Asset ID, version, status, Drive master identity, source/export paths, approval date, evidence record, and hashes;
4. pass `Validate Aramyst Assets`, including `Validate approved asset provenance`, before merge.

Do not revive historical branches for new asset production. If historical work must be reused, create a new branch from current `main` and deliberately port only the still-authorized content.

## Audit hygiene note

During the original audit two temporary no-op PRs (#40 and #41) were inadvertently opened solely while probing whether the preserved historical branches carried unique commits. Both were immediately closed without merge or branch modification. They have no authority and do not change the preservation disposition of either branch.

## Conclusion

The repository has no active pre-provenance approval promotion requiring reconciliation. The late-CI failure mode that affected PR #34 is cleared from the current open-work surface. The stale `agent/continuity-gate-audit` ref has been removed, and the two remaining non-`main` branches are explicitly controlled historical-provenance exceptions. Future approval work is controlled by the same-PR provenance rule and must start from current `main`.