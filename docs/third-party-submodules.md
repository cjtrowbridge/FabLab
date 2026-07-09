# Third-Party Submodules

This index classifies every top-level submodule under `third_party/`. The classification is explicit and does not depend on folder name alone.

| Path | Upstream | Pin | Classification | Status | Role |
|---|---|---:|---|---|---|
| `third_party/vibe-modeling` | https://github.com/cjtrowbridge/vibe-modeling | `7f7c8b9171b1ff2941f5435e3dbe4aeb2ef684bc` | `temporary_assimilation_source` | temporary | Source of additive/OpenSCAD workflow, revisions, structural review, and legacy examples. |
| `third_party/vibe-cutting` | https://github.com/cjtrowbridge/vibe-cutting | `d5c0280250269165956c38ca0319ee7403a6810e` | `temporary_assimilation_source` | temporary | Source of laser/subtractive workflow, helper boundaries, profiles, validation, and legacy examples. |
| `third_party/text-to-cad` | https://github.com/earthtojake/text-to-cad | `622c258fbdea64614056bfe33f3d3f183021a374` | `temporary_assimilation_source` | temporary | Source of STEP-first, CAD viewer, DXF, component lookup, and assembly-agent patterns. |
| `third_party/boxes` | https://github.com/florianfesti/boxes.git | `836f5f72bedb33ac4262ed925545eacb31e926a8` | `permanent_provider` | permanent | Laser-cut boxes, trays, shelves, panels, finger joints, and living hinges. |
| `third_party/lasergrbl` | https://github.com/arkypita/LaserGRBL.git | `1f9337b3af27133f8b1696e41cc110f2af74d04f` | `manual_operator_reference` | permanent | GRBL laser preview/streaming and operator workflow reference. |
| `third_party/cadquery` | https://github.com/CadQuery/cadquery.git | `f69500e54640a3da8fcee9d063a5a1f996d63263` | `permanent_provider_dependency` | permanent | Python parametric CAD and STEP/BREP-capable modeling foundation. |
| `third_party/cq_gears` | https://github.com/meadiode/cq_gears.git | `e73874cf17a25447a99b1e7c22a4d5af38560e9c` | `permanent_provider` | permanent | CadQuery-based gear source geometry for gears, racks, and mesh candidates. |
| `third_party/bosl2` | https://github.com/BelfrySCAD/BOSL2.git | `fbcdfdd511b6abfde93c43c8f85c2bd24ee7a02d` | `permanent_reference` | permanent | OpenSCAD library/reference and comparison geometry source. |
| `third_party/freecad-gears` | https://github.com/looooo/freecad.gears.git | `d55e8e3d21208e052379a8451507fb4a727ae292` | `inspection_only_provider` | permanent | FreeCAD gear inspection, STEP provenance, and non-authoritative geometry checks. |
| `third_party/step.parts` | https://github.com/earthtojake/step.parts | `c6113328a5695b976a010a203a90fe86191769bf` | `component_source` | permanent | Off-the-shelf STEP parts such as screws, bearings, motors, and connectors. |
| `third_party/cad-viewer` | https://github.com/earthtojake/cad-viewer | `50a09799a227e21203d882ba8d50014a3480aee8` | `viewer_reference` | permanent | Browser-based inspection patterns for CAD, G-code, robot, and viewer artifacts. |

## Rules

- Temporary assimilation sources are read-only references unless a task explicitly authorizes changes.
- Permanent providers and references remain long-term only through FabLab-owned documentation, adapters, setup/check paths, and validation gates.
- Helper output is provenance until FabLab validation promotes it.
- No third-party submodule owns FabLab readiness claims.
