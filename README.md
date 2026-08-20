# Aramyst Book Assets

Production-asset repository for the standalone Aramyst TTRPG project. “Aramyst” is a temporary development alias; the final publication/setting title remains unresolved.

This repository stores source assets, working references, prompts, controlled production records, and promoted delivery/release-ready files used during development and publication.

For the current repository-control state, branch exceptions, CI architecture, and maintenance rules, read [`docs/GITHUB_BASELINE.md`](docs/GITHUB_BASELINE.md). Dated audits and reconciliations are evidence records rather than parallel current-state baselines unless a controlling policy explicitly incorporates their result.

For cross-system ownership and promotion rules, read [`docs/SOURCE_OF_TRUTH.md`](docs/SOURCE_OF_TRUTH.md). For canonical filename/version rules, read [`docs/NAMING_AND_VERSIONING.md`](docs/NAMING_AND_VERSIONING.md). For promoted-asset provenance, read [`docs/APPROVED_ASSET_PROVENANCE.md`](docs/APPROVED_ASSET_PROVENANCE.md).

Before adding or editing an asset dependency, read [`docs/DEPENDENCY_GOVERNANCE_POLICY.md`](docs/DEPENDENCY_GOVERNANCE_POLICY.md). Dependency strings are CI-governed: durable IDs/ranges must resolve through the external-authority registry, and title-bound, composite, or long-term prose dependencies require a controlled record in `schemas/dependency-classification-registry.json`.

## Folder Structure

```text
covers/       Cover concepts, cover exports, mockups, and repository-native source files.
maps/         World maps, regional maps, settlement maps, route diagrams, and map source files.
characters/   Character portraits, outfit references, silhouettes, expression sheets, and model notes.
factions/     Faction marks, banners, heraldry, sigils, uniforms, and faction reference boards.
locations/    Location art, architectural references, environment concepts, and scene-setting images.
symbols/      Icons, glyphs, magical marks, seals, emblems, and recurring visual motifs.
typography/   Font notes, title treatments, lettering experiments, and typography references.
prompts/      Promoted AI image, video, and audio prompts; prompt templates; negative prompts; generation notes.
references/   Promoted external reference boards, research images, citation notes, and visual inspiration.
exports/      Delivery/release-ready repository outputs and controlled export-binding records.
provenance/   Machine-readable provenance sidecars for approved/exported/published assets.
docs/         Asset rules, naming conventions, production notes, briefs, audits, and decision records.
pages/        Fixed-layout page outputs and approved wrappers used by the page registry.
```

Working/editable material may remain in Google Drive under the source-of-truth policy; repository folders do not imply that every working master must be copied into GitHub.

## Canonical Naming Convention

Use lowercase kebab-case with a clear category, subject, purpose, optional variant, and three-digit version:

```text
category-subject-purpose-variant-v001.ext
```

Examples:

```text
cover-project-main-front-v001.png
character-protagonist-portrait-front-v003.png
map-opening-region-print-v002.svg
symbol-project-seal-transparent-v001.png
prompt-character-portrait-base-v001.md
```

The `aramyst` slug is a temporary project alias, not an approved publication-final title slug. Do not invent or propagate a successor title slug before that naming decision is approved.

Canonical registered filenames are **status-neutral**. Lifecycle state is stored in the asset registry rather than inferred from filename suffixes.

## Registry Status vs. Filename Vocabulary

The exact authoritative asset-status vocabulary is:

```text
planned
briefed
in-progress
review
approved
exported
published
superseded
archived
```

These values come from `manifest.json` / `schemas/asset-manifest.schema.json` and their synchronized registry mirrors.

Do not use filename labels as substitutes for registry status:

- `wip` and `draft` do not mean `in-progress`.
- `final` is not a registry status and does not mean `approved`, `exported`, or `published`.
- `approved`, `exported`, `published`, and `review` should not be added as lifecycle suffixes to new canonical registered paths.
- `source`, `master`, `preview`, `print`, and `web` may describe a file's purpose or delivery role when accurate; they are not lifecycle states.

A filename never grants approval. GitHub registry status is authoritative, and every asset in `approved`, `exported`, or `published` state must satisfy the approved-provenance contract.

## Version and Provenance Rules

- Use `v001`, `v002`, `v003`, and so on for meaningful asset iterations.
- Do not increment version merely because lifecycle status changes when the underlying asset is unchanged.
- Any explicit `v###` in a concrete registered GitHub source/export filename must match the manifest version.
- Material changes require the version treatment defined in `docs/NAMING_AND_VERSIONING.md`.
- For `approved`, `exported`, and `published` assets, exact source/export paths and version/status values are bound by `provenance/*.json`; path changes must update those bindings in the same controlled change.

## Notes

- Preserve source/master files in their controlling system.
- Put promoted delivery-ready repository outputs in `exports/` when that is the registered export destination.
- Store reusable prompt templates in `prompts/` only when intentionally promoted to GitHub.
- Use `docs/` for controlled conventions, production notes, audits, and asset decisions.
- Do not create `final-final`, `wip`, or similar pseudo-status naming conventions for canonical registered assets.
- Run the protected `Validate Aramyst Assets` workflow before substantive changes merge to `main`.
