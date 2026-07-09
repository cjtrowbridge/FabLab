# vibe-modeling Assimilation Report

## Source Overview

`third_party/vibe-modeling` is a temporary assimilation source for the additive/OpenSCAD half of FabLab. It provides a reusable agentic pipeline for OpenSCAD designs with JSON configs, numbered revisions, generated STL/PNG artifacts, immutable revision snapshots, build manifests, and structural-review language.

## Inventory

| Area | Source Paths | FabLab Disposition |
|---|---|---|
| OpenSCAD project layout | `designs/<design>/src/`, `designs/<design>/configs/` | `planned_fablab_native` |
| Build scripts | `scripts/scad_build.py`, `scripts/scad_build_all.py`, `scripts/scad_new_revision.py` | `planned_fablab_native` |
| Generated artifacts | `output/`, `revisions/` | `planned_fablab_native` |
| Agent workflows | `playbooks/` | `planned_fablab_native` |
| Structural rules | README design conventions and structural playbooks | `planned_fablab_native` |
| Example fixtures | `designs/example_box`, `designs/cyberdeck`, `designs/lovelace`, `designs/cottage_pi6_plus` | `migration_debt` |
| Servo/mechanism lessons | `designs/lovelace`, `designs/cyberdeck`, related configs/docs | `planned_fablab_native` |

## Capabilities To Preserve

- OpenSCAD design authoring with `main.scad` entrypoints.
- JSON-driven parameter revisions using `configs/rev_000N.json`.
- Numbered revision creation.
- STL generation.
- Multi-view PNG preview generation.
- Complete multi-part build/audit behavior through part manifests.
- Source/config provenance and build manifests.
- Immutable revision folders.
- Structural join review.
- Minimum wall thickness and minimum internal material width review.
- Sectional inspection workflow.
- Explicit language that render success does not imply structural safety or fabrication readiness.

## Candidate Parity Fixtures

- `designs/example_box`: smallest additive pipeline smoke fixture.
- `designs/cyberdeck`: multi-part, electronics-envelope, and UI-heavy fixture.
- `designs/lovelace`: mechanism/component design lessons.
- `designs/cottage_pi6_plus`: multi-part enclosure and airflow fixture.

## Migration Targets

- `providers/openscad/`
- `tool_adapters/openscad.json`
- `scripts/fablab.py build`
- `scripts/validate_project.py`
- `docs/tools/openscad.md`
- `docs/validation-contract.md`
- `playbooks/how_to_author_additive_parts.md`
- `playbooks/how_to_validate_structural_parts.md`
- `playbooks/how_to_migrate_legacy_vibe_modeling_projects.md`
- `schemas/project.schema.json`
- `schemas/artifact_manifest.schema.json`
- `schemas/build_manifest.schema.json`

## Risks

- OpenSCAD availability varies by host and must be checked rather than assumed.
- Structural review cannot be reduced to render success or manifold STL checks.
- Generated output directories must remain scratch or immutable according to their role.
- Servo geometry must not be guessed from memory.

## Retirement Evidence

`third_party/vibe-modeling` can be retired only after FabLab builds migrated additive fixtures, audits manifests, preserves revision behavior, records structural review output, and has user approval.
