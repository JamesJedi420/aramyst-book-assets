## Scope

Describe the repository change and its controlling source/authorization.

## Dependency governance

Complete this section **only if the PR adds, removes, or changes an asset dependency**. See `docs/DEPENDENCY_GOVERNANCE_POLICY.md`.

- [ ] Dependency class is identified: `asset_edge`, `external_authority`, `title_bound_authority`, `composite_gate`, or `long_term_prose_gate`.
- [ ] Authority resolution is correct: `AST-*` targets exist, external IDs/ranges resolve through `schemas/external-authority-registry.json`, or prose remains prose because no scope-equivalent durable authority exists.
- [ ] For `title_bound_authority`, `composite_gate`, or `long_term_prose_gate`, `schemas/dependency-classification-registry.json` is synchronized with the exact dependency string and affected Asset ID(s).
- [ ] The PR or a controlled repository record cites the evidence/reconciliation establishing the classification and any required source anchor, constituent-authority rationale, or reopen/satisfaction condition.

If this PR does **not** change dependencies, write `Dependency changes: none` in the PR description rather than checking these boxes.

## Validation

- [ ] `Validate Aramyst Assets` passes before merge.
