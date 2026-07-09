# vibe-cutting Assimilation Report

## Source Overview

`third_party/vibe-cutting` is a temporary assimilation source for FabLab's subtractive and laser workflow. It provides a configuration-driven pipeline for laser-cut and laser-engraved projects, portable bootstrap tooling, machine/material profiles, helper adapters, validation checks, operation-stage G-code, and readiness language.

## Inventory

| Area | Source Paths | FabLab Disposition |
|---|---|---|
| Laser build pipeline | `scripts/laser_build.py` | `planned_fablab_native` |
| Portable bootstrap | `setup/`, `docs/host-bootstrap.md` | `planned_fablab_native` |
| Helper adapters | `scripts/helper_tool.py`, `tool_adapters/` | `permanent_provider_boundary` |
| Machine profiles | `machines/` | `planned_fablab_native` |
| Material profiles | `materials/` | `planned_fablab_native` |
| Laser docs | `docs/`, `docs/tools/`, `docs/safety/` | `planned_fablab_native` |
| Mechanism model | `docs/mechanism-model.md`, tests/scripts | `planned_fablab_native` |
| Example fixtures | `designs/shot_coins`, `designs/hug_coins`, `designs/primitive_power_extender_laser_0_1` | `migration_debt` |
| Permanent helpers | `third_party/boxes`, `cadquery`, `cq_gears`, `bosl2`, `freecad-gears`, `lasergrbl` | `permanent_provider_boundary` |

## Capabilities To Preserve

- Laser design configs.
- SVG output.
- Preview PNG output.
- GRBL G-code output.
- Operation-stage G-code.
- Job plans and build manifests.
- Machine and material profiles.
- Material setup docs and safety notes.
- Engraving containment checks.
- Bounds validation.
- Duplicate-cut and overburn checks.
- Helper routing for Boxes.py, CQ_Gears, BOSL2, and FreeCAD Gears.
- Host-owned mechanism validation.
- Portable bootstrap behavior with explicit download approval.
- Readiness language that keeps generated G-code calibration-only until physical checks pass.

## Candidate Parity Fixtures

- `designs/shot_coins`: default laser artifact and operation-stage fixture.
- `designs/hug_coins`: repeated text substitution and layout fixture.
- `designs/primitive_power_extender_laser_0_1`: mechanism/gear validation fixture.
- `designs/bwb_merit_badges`: multi-item engraving/layout fixture.

## Migration Targets

- `providers/native_vector/`
- `providers/laser_grbl/`
- `scripts/fablab.py build`
- `scripts/provider_tool.py`
- `setup/bootstrap.sh`
- `docs/tools/lasergrbl.md`
- `docs/process-selection.md`
- `docs/material-selection.md`
- `docs/validation-contract.md`
- `playbooks/how_to_author_laser_cut_parts.md`
- `playbooks/how_to_validate_laser_jobs.md`
- `playbooks/how_to_migrate_legacy_vibe_cutting_projects.md`
- `schemas/machine_profile.schema.json`
- `schemas/material_profile.schema.json`
- `schemas/validation_report.schema.json`

## Risks

- G-code generation must not imply machine safety or readiness.
- Machine/material profiles may be provisional and require calibration.
- Helper-generated SVG/STEP/geometry is provenance, not final authority.
- Provider setup may require downloads and must remain explicit.

## Retirement Evidence

`third_party/vibe-cutting` can be retired only after FabLab builds migrated laser fixtures, emits operation-stage artifacts, validates bounds/mechanisms, preserves machine/material setup docs, documents provider boundaries, and has user approval.
