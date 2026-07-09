# text-to-cad Assimilation Report

## Source Overview

`third_party/text-to-cad` is a temporary assimilation source for STEP-first CAD, CAD viewer, DXF, robot-description, and off-the-shelf component sourcing patterns. It contributes agent skill organization and useful CAD/inspection workflows but should not become a long-term FabLab runtime dependency.

## Inventory

| Area | Source Paths | FabLab Disposition |
|---|---|---|
| CAD skill | `skills/cad/SKILL.md`, `packages/` | `planned_fablab_native` |
| CAD viewer skill | `skills/cad-viewer/SKILL.md`, `viewer/` | `permanent_provider_boundary` |
| step.parts skill | `skills/step-parts/SKILL.md` | `permanent_provider_boundary` |
| DXF workflow | `skills/dxf/SKILL.md` | `planned_fablab_native` |
| G-code/robot skills | `skills/gcode`, `skills/urdf`, `skills/sdf`, `skills/srdf` | `reference_only` |
| Benchmarks | `benchmarks/` | `migration_debt` |
| Plugin/skill packaging | `.codex-plugin`, `.claude-plugin`, `plugins/` | `reference_only` |

## Capabilities To Preserve

- STEP-first CAD generation/editing workflow.
- Optional STL, 3MF, and GLB exports.
- CAD viewer inspection patterns for CAD/G-code/robot files.
- DXF-oriented projection/cut-layout ideas.
- build123d-style assembly modeling conventions.
- Off-the-shelf STEP part discovery patterns.
- Datum, topology, measurement, and inspection conventions.

## Candidate Parity Fixtures

- Benchmark-style calibration block or flange for STEP-first schema/command fixtures.
- `skills/step-parts` patterns for purchased-part provenance fixtures.
- CAD viewer skill workflow for future artifact inspection.
- DXF skill workflow for future CAD projection and laser profile generation.

## Migration Targets

- `providers/build123d_step/`
- `providers/cad_projection/`
- `providers/step_parts/`
- `providers/cad_viewer/`
- `tool_adapters/step_parts.json`
- `tool_adapters/cad_viewer.json`
- `docs/tools/step-parts.md`
- `docs/tools/cad-viewer.md`
- `playbooks/how_to_author_step_assemblies.md`
- `playbooks/how_to_author_hybrid_assemblies.md`
- `schemas/component.schema.json`
- `schemas/component_instance.schema.json`

## Risks

- Some workflows assume external skills/plugin installers and should not be copied directly into FabLab.
- Viewer correctness is inspection support, not fabrication validation.
- STEP component models still require provenance, measurement confidence, and fit checks.

## Retirement Evidence

`third_party/text-to-cad` can be retired when useful CAD, viewer, DXF, and component-source patterns are represented in FabLab-native docs/providers or permanent submodules, and no runtime commands depend on the temporary repo.
