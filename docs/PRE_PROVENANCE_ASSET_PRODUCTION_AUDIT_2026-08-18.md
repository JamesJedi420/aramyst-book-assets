# Pre-Provenance Asset-Production Audit — 2026-08-18

Status: **CONTROLLED repository audit**

Purpose: identify any still-open pull request or surviving branch that began an `in-progress` → `approved` asset promotion before the approved-asset provenance contract was introduced, so the work can be reconciled before merge rather than failing late in CI.

## Current open PR state

At audit time, the repository has **zero open pull requests**.

Therefore there is no currently open asset-production PR awaiting provenance reconciliation.

PR #34 — the only identified pre-contract approval promotion requiring reconciliation — has already been reconciled against current `main`, supplied with `provenance/ast-char-004-v001.json`, passed `Validate approved asset provenance`, and merged.

## Surviving non-main branches

Three non-`main` branches remain at audit time:

### `agent/map-hou-001-functional-adjacency`

Disposition: **PRESERVED HISTORICAL PROVENANCE — NOT ACTIVE ASSET PRODUCTION.**

This is the previously audited superseded MAP-HOU functional-adjacency branch retained because it carries unique historical schematic/QA material. It is not an active approval branch and must not be revived as an asset-production base.

### `agent/q-023-cross-system-sync`

Disposition: **PRESERVED HISTORICAL PROVENANCE — NOT ACTIVE ASSET PRODUCTION.**

This is the previously audited superseded Q-023 implementation branch retained to preserve reconciliation history. It is not an active approval branch and must not be revived as an asset-production base.

### `agent/continuity-gate-audit`

Disposition: **STALE MERGED AUDIT REF — NO UNMERGED ASSET PROMOTION.**

GitHub reports no commits between current `main` and this branch when a PR is attempted, so it carries no unique unmerged work relative to `main`.

Its historical manifest snapshot also leaves the relevant Scene 01 visual records (`AST-CHAR-003`, `AST-CHAR-004`, `AST-CHAR-005`, and `AST-LOC-002`) in `in-progress` state. It therefore does not contain a hidden pre-contract `in-progress` → `approved` promotion.

This branch must not be used as the base for new production because its working tree predates later provenance controls and newer approved asset state. New work starts from current `main`.

## Finding

**PASS — no unreconciled pre-provenance asset-approval work is currently open.**

There is no surviving branch or open PR that both:

1. contains an unmerged asset promotion to `approved`, `exported`, or `published`; and
2. predates the approved-asset provenance contract without the required `provenance/*.json` sidecar.

The currently surviving unique branches are historical provenance branches, not production branches. The additional continuity-audit ref has no commits ahead of `main` and carries no hidden approval promotion.

## Required rule for future approval work

Any future asset approval branch MUST:

1. branch from current protected `main` after the provenance contract;
2. promote the asset and add/update its machine-readable provenance sidecar in the same PR;
3. bind the final Asset ID, version, status, Drive master identity, source/export paths, approval date, evidence record, and hashes;
4. pass `Validate Aramyst Assets`, including `Validate approved asset provenance`, before merge.

Do not revive historical or stale branches for new asset production. If historical work must be reused, create a new branch from current `main` and deliberately port only the still-authorized content.

## Audit hygiene note

During this audit two temporary no-op PRs (#40 and #41) were inadvertently opened solely while probing whether the preserved historical branches carried unique commits. Both were immediately closed without merge or branch modification. They have no authority and do not change the preservation disposition of either branch.

## Conclusion

The repository has no active pre-provenance approval promotion requiring reconciliation. The late-CI failure mode that affected PR #34 is therefore cleared from the current open-work surface. Future approval work is controlled by the same-PR provenance rule and must start from current `main`.