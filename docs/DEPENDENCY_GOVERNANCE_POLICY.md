# Aramyst Dependency Governance Policy

Status: **CONTROLLING repository policy**
Scope: dependency entries proposed for `manifest.json` and `ASSET_MANIFEST.csv`

This policy consolidates the dependency-vocabulary audit and subsequent reconciliation work into one admission rule for the asset registry. It governs dependency representation; it does not create canon, mint authority IDs, approve assets, or replace the controlling source behind a dependency.

## 1. Governing principle

Every dependency entered into the asset registry MUST be classified before entry as exactly one of five semantic classes:

1. `asset_edge` — registered `AST-*` production-asset dependency;
2. `external_authority` — durable external authority ID or bounded authority range;
3. `title_bound_authority` — one specific controlling authority document with no proven durable project ID;
4. `composite_gate` — a requirement jointly governed by multiple narrower authorities with no single equivalent authority;
5. `long_term_prose_gate` — a real prerequisite whose controlling authority is not yet created, approved, complete, or scope-equivalent.

The manifest may continue to store dependencies as flat strings. Classification is a governance decision applied before a string is admitted; representation must preserve the semantics of its class.

A dependency MUST NOT be rewritten merely to make it look machine-resolvable. Exact authority and scope take precedence over identifier uniformity.

## 2. Admission sequence

For every proposed dependency, evaluate the following questions in order.

### Step A — Is the dependency another registered production asset?

If the prerequisite is the existence, state, or output of a specific asset already registered under an `AST-*` ID, classify it as `asset_edge` and use the exact Asset ID.

Do not use `AST-*` for canon records, map-product authorities, scenario authorities, approvals, specifications, or other non-asset records.

### Step B — Does one durable external authority exactly own the prerequisite?

If one approved project authority has a stable ID and its scope and completion state are directly equivalent to the dependency, classify it as `external_authority` and use the exact durable ID.

If the prerequisite is a deterministic bounded set of same-family authorities, a bounded range may be used only when the range preserves exact prefix, identifier width, start, end, and intended membership.

The ID or range MUST resolve through `schemas/external-authority-registry.json` before it enters the asset registry.

### Step C — Is there one exact controlling document but no durable ID for that document?

If one specific controlling document exactly owns the prerequisite but no existing durable project ID is explicitly assigned to that document, classify it as `title_bound_authority`.

Use a stable, unambiguous controlling title in the dependency string. Record an exact source locator in the reconciliation/audit documentation so future normalization can prove equivalence. Do not substitute a nearby project ID whose scope is broader, narrower, derived, or merely related.

A title-bound authority remains outside `schemas/external-authority-registry.json` until a durable ID is assigned or discovered and proven equivalent to that exact authority.

### Step D — Is the prerequisite distributed across multiple authorities?

If multiple narrower approved authorities jointly govern the prerequisite and no one authority is scope-equivalent to the whole requirement, classify it as `composite_gate`.

Retain concise prose that describes the combined gate. Do not replace it with one member authority, a broader package identity, or a fabricated umbrella ID merely to eliminate prose.

A composite gate may be normalized later only when a single approved authority explicitly assumes the complete scope represented by the gate.

### Step E — Is the prerequisite real but not yet fully controlled?

If the prerequisite depends on future canon, approval, art direction, geography, publication requirements, or another decision whose controlling authority is missing, provisional, partial, incomplete, or not scope-equivalent, classify it as `long_term_prose_gate`.

Retain readable prose. Nearby authorities may be documented as supporting or likely future owners, but they do not satisfy the gate until their approved scope and completion state become equivalent.

If none of these five classes can be established, the dependency MUST NOT enter the registry. Resolve the ambiguity first.

## 3. Class requirements

### 3.1 `asset_edge`

Required conditions:

- target is a registered production asset;
- exact `AST-*` identity exists in the asset registry;
- dependency semantics are genuinely asset-to-asset rather than authority-to-asset.

Required representation: exact `AST-*` ID.

Validation expectation: target Asset ID exists; no dangling edge.

Current examples include `AST-COVER-001` depending on `AST-SYM-001` and `AST-TYPE-001`.

### 3.2 `external_authority`

Required conditions:

- authority is external to the production-asset namespace;
- durable project ID exists;
- controlling source is known;
- dependency scope is directly equivalent to that authority;
- authority is registered in `schemas/external-authority-registry.json` before use.

Required representation: exact authority ID, or exact bounded range when the dependency truly requires that bounded set.

Range rules:

- do not silently expand or contract a range;
- do not change prefix or numeric width;
- do not convert a range into a vague family dependency;
- do not infer missing members beyond the stated bounds.

Examples include `ATLAS-ARCH-001`, `MAP-ENV-001`, `SCN-NODE-001`, and controlled bounded `GEO-*`, `ROUTE-*`, `GXR-*`, `ENV-*`, and `HOU-*` ranges.

### 3.3 `title_bound_authority`

Required conditions:

- exactly one controlling authority document exists;
- no durable project ID has been proven to identify that exact document;
- title is sufficiently specific to distinguish the controlling source;
- an exact source locator/equivalence anchor is recorded in repository audit or reconciliation documentation.

Required representation: exact controlling title or established title-bound dependency phrase.

Prohibited actions:

- inventing an ID during repository maintenance;
- substituting a related ID;
- adding the title itself to the external-authority registry as though it were an ID.

Current precedent: `MAP-REG-001 Geometry Specification v001 — CONTROLLING`.

### 3.4 `composite_gate`

Required conditions:

- prerequisite is real and presently controlled in parts;
- two or more narrower authorities jointly govern it;
- no single existing authority is equivalent to the full gate;
- selecting only one constituent authority would distort or omit required scope.

Required representation: concise stable prose naming the combined requirement.

The gate's audit/reconciliation record SHOULD identify the important constituent authorities and explain why none is singly equivalent.

Current precedent: `Scene 01 canon`.

### 3.5 `long_term_prose_gate`

Required conditions:

- prerequisite is intentionally unresolved or incomplete;
- no current authority has both equivalent scope and required completion/approval state;
- retaining the gate prevents premature production based on partial, provisional, or adjacent authority.

Required representation: concise prerequisite prose describing what must become approved/final before the dependent asset may proceed.

Current precedents:

- `Approved character canon brief`;
- `Approved location canon brief`;
- `Canon geography decisions`;
- `Final publishing specifications`;
- `Approved symbolic and thematic direction`;
- `Approved cover direction`.

## 4. Equivalence test

An existing authority may replace prose only when all of the following are true:

1. **Identity:** the proposed authority is the actual controlling record, not a related record.
2. **Scope:** it covers the whole dependency, not a subset or neighboring concern.
3. **Completion state:** it is approved/final to the degree demanded by the dependency.
4. **Direction:** the dependency actually points to that authority rather than to an asset produced under it.
5. **Durability:** its identifier is stable enough for registry resolution.
6. **Evidence:** repository or controlling-source evidence supports the mapping directly.

Failure of any item blocks normalization.

Examples of prohibited false equivalence include:

- `MAP-ENV-001` → `AST-MAP-003`;
- `Canon geography decisions` → `ATLAS-ARCH-001`;
- `Canon geography decisions` → `ATLAS-REG-DATA-001`;
- `Approved cover direction` → Book Production Specification;
- `Final publishing specifications` → the current Book Production Specification while final platform/bleed requirements remain unresolved;
- `Scene 01 canon` → `SCN-NODE-001` or `SCN-INV-001` when those authorities do not own all Scene-01 canon required by the affected assets.

## 5. Mandatory pre-entry record

Every future dependency addition or semantic replacement MUST include enough review evidence to answer:

- proposed dependency string;
- affected Asset ID(s);
- assigned class from this policy;
- controlling source or, for an unresolved gate, the missing approval/decision;
- equivalence rationale;
- machine-resolution status when class is `asset_edge` or `external_authority`;
- source locator/equivalence anchor when class is `title_bound_authority`;
- constituent-authority rationale when class is `composite_gate`;
- reopen/satisfaction condition when class is `long_term_prose_gate`.

This evidence may live in the PR body, a dedicated reconciliation/audit document, or another controlled repository record. It MUST exist before the dependency edit is merged.

## 6. Registry-entry gate

A dependency edit MUST NOT merge into `manifest.json` or `ASSET_MANIFEST.csv` unless:

1. the dependency has been assigned exactly one of the five classes;
2. its representation conforms to that class;
3. any `AST-*` target exists;
4. any durable external ID/range resolves through `schemas/external-authority-registry.json`;
5. any title-bound authority has a documented exact source anchor;
6. any composite gate has documented no-single-authority reasoning;
7. any long-term prose gate states a real unresolved prerequisite rather than vague placeholder language;
8. equivalence has not been inferred from mere topical similarity;
9. manifest and CSV dependency representations remain synchronized;
10. repository validation passes.

Reviewers MUST reject dependency edits that omit classification evidence or force a dependency into the wrong class for cosmetic consistency.

## 7. Changes between classes

Classification may change only when project authority changes or new evidence proves a different classification.

Permitted migrations include:

- `long_term_prose_gate` → `external_authority` when the missing final authority is approved, durable, and scope-equivalent;
- `composite_gate` → `external_authority` when one approved authority formally assumes the complete composite scope;
- `title_bound_authority` → `external_authority` when a durable ID is assigned/discovered and proven equivalent to the exact controlling document;
- prose gate → `asset_edge` only when the prerequisite itself genuinely becomes a registered production asset and dependency semantics are asset-to-asset.

Every migration MUST preserve meaning. A migration that broadens, narrows, weakens, or prematurely satisfies the prerequisite is prohibited.

## 8. Authority-ID discipline

Repository maintenance MUST NOT mint project authority IDs merely to eliminate prose dependencies.

New authority IDs belong to the workflow that owns the underlying canon, map, scenario, continuity, publication, or other authority. Once approved there, the asset repository may register and reference them.

`AST-*` remains exclusively the production-asset namespace.

## 9. Synchronization rule

The flat dependency list remains authoritative in both `manifest.json` and `ASSET_MANIFEST.csv` until a separately approved schema migration changes that architecture.

Any future structural migration of dependency classification into machine-readable manifest fields MUST update together:

- `manifest.json`;
- `ASSET_MANIFEST.csv`;
- `schemas/asset-manifest.schema.json`;
- `schemas/external-authority-registry.json` and its schema when applicable;
- validator implementation;
- validator regression tests;
- human-readable registry/documentation.

No partial schema migration is permitted.

## 10. Existing dependency disposition

This policy ratifies rather than reinterprets the completed audits:

- current `AST-*` edges remain `asset_edge`;
- current durable external IDs/ranges remain `external_authority`;
- `MAP-REG-001 Geometry Specification v001 — CONTROLLING` remains `title_bound_authority`;
- `Scene 01 canon` remains `composite_gate`;
- the six broad descriptive gates audited on 2026-08-16 remain `long_term_prose_gate`;
- other continuity/approval prose dependencies remain subject to this policy and must be reconciled before any future normalization.

## 11. Controlling rule

When identifier neatness conflicts with authority accuracy, **authority accuracy wins**.

A readable, correctly scoped prose dependency is valid. A machine-resolvable identifier that changes the dependency's meaning is not.
