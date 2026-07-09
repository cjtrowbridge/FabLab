# Migration Parity Matrix

This matrix maps README-required capabilities to their current disposition and retirement evidence.

| Capability | Source | FabLab Target | Disposition | Evidence Required |
|---|---|---|---|---|
| OpenSCAD design authoring | `vibe-modeling` | `providers/openscad/`, additive playbooks | `planned_fablab_native` | Migrated additive fixture builds from FabLab command. |
| Parameterized JSON configs | `vibe-modeling` | `schemas/project.schema.json`, project configs | `planned_fablab_native` | Config fixtures validate and build. |
| Numbered revisions | `vibe-modeling` | project revision workflow | `planned_fablab_native` | New revision command creates immutable revision. |
| STL/3MF/preview generation | `vibe-modeling` | additive provider output bundle | `planned_fablab_native` | Output bundle contains expected artifacts and previews. |
| Build manifests | both legacy repos | `build_manifest.json`, `artifact_manifest.json` | `planned_fablab_native` | Bundle audit validates manifests. |
| Structural review | `vibe-modeling` | `docs/validation-contract.md`, validators | `planned_fablab_native` | Structural report records passed/failed/unverified states. |
| Laser SVG/preview/G-code | `vibe-cutting` | native vector/laser provider | `planned_fablab_native` | Migrated laser fixture emits SVG, PNG, G-code. |
| Operation-stage G-code | `vibe-cutting` | laser output bundle | `planned_fablab_native` | Operation artifacts are present and manifest-listed. |
| Machine/material profiles | `vibe-cutting` | catalogs and schemas | `planned_fablab_native` | Profile fixtures validate and appear in setup docs. |
| Helper adapters | `vibe-cutting` | `tool_adapters/*.json`, `scripts/provider_tool.py` | `permanent_provider_boundary` | Provider manifest validation passes. |
| Mechanism validation | `vibe-cutting` | validation layer | `planned_fablab_native` | Gear/mechanism fixture produces validation report. |
| Portable bootstrap | `vibe-cutting` | `setup/bootstrap.sh`, `setup/bootstrap.ps1` | `planned_fablab_native` | `doctor` passes on supported host. |
| STEP-first CAD | `text-to-cad` | build123d/STEP provider boundary | `planned_fablab_native` | STEP fixture validates and enters output bundle. |
| CAD viewer patterns | `text-to-cad` | `tool_adapters/cad_viewer.json`, docs | `permanent_provider_boundary` | Viewer reference docs and manifest exist. |
| Off-the-shelf STEP sourcing | `text-to-cad`, `step.parts` | component source provider | `permanent_provider_boundary` | Component provenance fixture validates. |
| Purchased-part truth layer | README new scope | schemas, catalogs, docs | `planned_fablab_native` | Component manifest blocks unverified high-risk readiness. |
| Servo safeguards | `vibe-modeling`, README new scope | servo schema/profile/docs | `planned_fablab_native` | Servo fixture checks shaft/horn/screw/wire/service constraints. |
| Output README generation | all scopes | output bundle layer | `planned_fablab_native` | Generated output README explains artifacts and validation states. |

## Initial Fixture Candidates

- Additive smoke: `third_party/vibe-modeling/designs/example_box`
- Additive multi-part: `third_party/vibe-modeling/designs/cyberdeck`
- Laser smoke: `third_party/vibe-cutting/designs/shot_coins`
- Laser mechanism: `third_party/vibe-cutting/designs/primitive_power_extender_laser_0_1`
- STEP/component: text-to-cad benchmark-style calibration part plus `step.parts` lookup pattern

## Retirement Evidence Summary

- `vibe-modeling`: additive fixtures build and audit under FabLab without runtime dependency.
- `vibe-cutting`: laser fixtures build and audit under FabLab without runtime dependency.
- `text-to-cad`: useful STEP/viewer/component patterns are FabLab-native or permanent-provider-routed.
