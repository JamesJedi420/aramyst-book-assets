# Main Branch Protection Policy

Status: **verified active — current operational verification; exact target configuration controlled in repository**

Repository: `JamesJedi420/aramyst-book-assets`
Target branch: `main`
GitHub mechanism: repository branch ruleset
Ruleset name: `Protect main`
Ruleset ID: `20862839`
Enforcement target: active
Exact live-ruleset configuration last inspected: 2026-08-14
Operationally re-verified: 2026-08-24

## Purpose

Protect the authoritative `main` branch from accidental direct or destructive changes while preserving the project's pull-request workflow and making the existing `Validate Aramyst Assets` CI gate mandatory before merge.

## Required rules

1. **Require a pull request before merging.**
   - Direct updates to `main` are not the normal publication path.
   - Required approving reviews: `0` while the repository is maintained by a single owner.
   - Required review-thread resolution: enabled.
   - Allowed merge methods: squash and rebase.

2. **Require status checks to pass before merging.**
   - Required check context: `validate`.
   - Expected source: GitHub Actions (`github-actions`, app ID `15368`).
   - Require branches to be up to date before merging: enabled.
   - This binds merge eligibility to the `Validate Aramyst Assets` workflow's `validate` job.

3. **Block force pushes.**
   - Non-fast-forward updates to `main` are prohibited.

4. **Restrict deletions.**
   - `main` may not be deleted through normal repository operations.

5. **Require linear history.**
   - Merge commits are not permitted on `main`.
   - Squash or rebase merges remain available.

## Deliberately not enabled

- Required signed commits: not enabled because the repository currently contains unsigned commits and enabling this would disrupt normal maintenance without solving the current control objective.
- Required approving review count greater than zero: not enabled while the repository has a single maintainer; this can be raised when an independent reviewer exists.
- Restrict updates: not enabled because it would prevent normal PR merges unless a bypass actor were granted.
- Bypass actors: none by controlled target. Emergency changes should be made by temporarily editing or disabling the ruleset in repository administration, leaving the settings change visible in GitHub's rule history rather than maintaining a standing bypass.

## Machine-readable target

`.github/rulesets/protect-main.json` records the controlled API/import target corresponding to this policy. The file remains the auditable configuration source; GitHub's active repository ruleset is the enforcement mechanism.

The policy and machine-readable target were compared again on 2026-08-24 and agree on every encoded control:

- target `refs/heads/main`;
- active enforcement target;
- empty controlled bypass-actor set;
- deletion restriction;
- non-fast-forward restriction;
- required linear history;
- pull request requirement;
- squash/rebase merge methods;
- zero required approving reviews;
- required review-thread resolution;
- required `validate` status check from integration ID `15368`;
- strict/up-to-date required-status policy.

No ruleset-file reconciliation change was required.

## Verification model

Repository-ruleset state has two distinct verification levels and they must not be conflated.

### Exact configuration verification

An exact configuration verification means the live repository-ruleset object itself has been inspected and compared field-by-field with this policy and `.github/rulesets/protect-main.json`.

The last exact live-ruleset configuration inspection was **2026-08-14**. It confirmed the complete target, rule parameters, bypass state, enforcement state, and integration binding described below.

The currently connected GitHub interface does not expose the repository-ruleset read endpoint. Its public branch endpoint reports whether `main` is protected, but its legacy `protection` object does not enumerate repository-ruleset internals. Therefore the 2026-08-24 audit does **not** falsely replace the 2026-08-14 exact-configuration date.

### Operational re-verification

Operational re-verification checks current observable repository behavior and state without claiming access to hidden ruleset fields.

On **2026-08-24**:

- GitHub's live branch endpoint reported `main` as `protected: true`;
- the live `main` head was `12ed74d8a80a1111a03996710830277d96ef2316`, produced by merged PR #54;
- PR #54 targeted `main` and merged through the pull-request path;
- PR #54's head `666fac4068aad6f8ad1d5a9f218dee01034b3337` received successful `Validate Aramyst Assets` run #128, including the `validate` job;
- PR #54 had no unresolved review threads at merge;
- the resulting `main` commit has one parent, consistent with the controlled linear-history/squash workflow;
- recent `main` history continues to show PR/squash-style publication for the current maintenance sequence.

These observations support continued active enforcement and reveal no operational drift from the controlled target. They do not independently re-prove every non-observable field such as deletion restriction, non-fast-forward restriction, exact bypass actors, or strict-status parameters.

## Verification record — 2026-08-14 exact configuration

Protection was exactly verified on 2026-08-14 through both configuration inspection and an actual protected pull-request cycle.

Confirmed in GitHub repository settings/API:

- active ruleset `Protect main` targets `refs/heads/main`;
- pull requests are required;
- the `validate` status check is required from GitHub Actions;
- strict/up-to-date status checking is enabled;
- force pushes are blocked;
- deletion is restricted;
- linear history is required;
- no standing bypass actors exist and the authenticated maintainer cannot bypass the ruleset.

Operational verification at that time:

- PR #16, `Verify active main protection baseline`, passed the required `validate` check;
- PR #16 was merged through the protected `main` path;
- the resulting `main` push triggered a fresh `Validate Aramyst Assets` run, which also passed;
- issue #12, `Activate Protect main ruleset`, was closed as completed after verification.

## Controlling interpretation

This document records an active repository control, not a pending target. When exact live-ruleset inspection is available, compare the live object directly with `.github/rulesets/protect-main.json` and update the exact-configuration verification date only if that comparison is actually performed.

Until then, operational verification may refresh the active-control evidence date but must not silently certify unobserved rule fields.
