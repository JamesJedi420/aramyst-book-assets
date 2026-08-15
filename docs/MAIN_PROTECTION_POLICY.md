# Main Branch Protection Policy

Status: **verified active**

Repository: `JamesJedi420/aramyst-book-assets`
Target branch: `main`
GitHub mechanism: repository branch ruleset
Ruleset name: `Protect main`
Ruleset ID: `20862839`
Enforcement: active
Verified: 2026-08-14

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
- Bypass actors: none by default. Emergency changes should be made by temporarily editing or disabling the ruleset in repository administration, leaving the settings change visible in GitHub's rule history rather than maintaining a standing bypass.

## Machine-readable target

`.github/rulesets/protect-main.json` records the controlled API/import target corresponding to this policy. The file remains the auditable configuration source; GitHub's active repository ruleset is the enforcement mechanism.

## Verification record

Protection was verified on 2026-08-14 through both configuration inspection and an actual protected pull-request cycle.

Confirmed in GitHub repository settings/API:

- active ruleset `Protect main` targets `refs/heads/main`;
- pull requests are required;
- the `validate` status check is required from GitHub Actions;
- strict/up-to-date status checking is enabled;
- force pushes are blocked;
- deletion is restricted;
- linear history is required;
- no standing bypass actors exist and the authenticated maintainer cannot bypass the ruleset.

Operational verification:

- PR #16, `Verify active main protection baseline`, passed the required `validate` check;
- PR #16 was merged through the protected `main` path;
- the resulting `main` push triggered a fresh `Validate Aramyst Assets` run, which also passed;
- issue #12, `Activate Protect main ruleset`, was closed as completed after verification.

This document therefore records an active repository control, not a pending target.
