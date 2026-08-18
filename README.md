# Aramyst Book Assets

Production-asset repository for the standalone Aramyst TTRPG project. “Aramyst” is a temporary development alias; the final publication/setting title remains unresolved.

This repository stores source assets, working references, prompts, and export-ready files used during development and production.

For the current repository-control state, branch exceptions, CI architecture, and maintenance rules, read [`docs/GITHUB_BASELINE.md`](docs/GITHUB_BASELINE.md). Dated audits and reconciliations are evidence records rather than parallel current-state baselines unless a controlling policy explicitly incorporates their result.

Before adding or editing an asset dependency, read [`docs/DEPENDENCY_GOVERNANCE_POLICY.md`](docs/DEPENDENCY_GOVERNANCE_POLICY.md). Dependency strings are CI-governed: durable IDs/ranges must resolve through the external-authority registry, and title-bound, composite, or long-term prose dependencies require a controlled record in `schemas/dependency-classification-registry.json`.

## Folder Structure

```text
covers/       Cover concepts, cover exports, mockups, and source files.
maps/         World maps, regional maps, settlement maps, route diagrams, and map source files.
characters/  Character portraits, outfit references, silhouettes, expression sheets, and model notes.
factions/    Faction marks, banners, heraldry, sigils, uniforms, and faction reference boards.
locations/   Location art, architectural references, environment concepts, and scene-setting images.
symbols/     Icons, glyphs, magical marks, seals, emblems, and recurring visual motifs.
typography/  Font notes, title treatments, lettering experiments, and typography references.
prompts/     AI image, video, and audio prompts; prompt templates; negative prompts; and generation notes.
references/  External reference boards, research images, citation notes, and visual inspiration.
exports/     Final or near-final assets prepared for layout, sharing, upload, or publication.
docs/        Asset rules, naming conventions, production notes, briefs, and decision records.
```

## Suggested Naming Convention

Use lowercase kebab-case with a clear category, subject, purpose, and version.

```text
category-subject-purpose-v001.ext
```

Examples:

```text
cover-aramyst-main-concept-v001.png
character-lyra-portrait-front-v003.png
map-western-realm-print-v002.svg
symbol-moon-seal-transparent-v001.png
prompt-character-portrait-template-v001.md
```

The `aramyst` slug in existing development examples is a temporary project alias, not an approved publication-final title slug. Do not invent or propagate a successor title slug before that naming decision is approved.

## Asset Status Tags

Recommended status suffixes:

```text
-draft
-wip
-review
-final
-print
-web
-source
```

## Notes

- Keep source files when possible.
- Put final export-ready files in `exports/`.
- Store reusable prompt templates in `prompts/`.
- Use `docs/` for conventions, production notes, and asset decisions.
