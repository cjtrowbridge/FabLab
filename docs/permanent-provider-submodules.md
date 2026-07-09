# Permanent Provider And Reference Submodules

Permanent provider/reference submodules are long-term third-party capabilities used through FabLab-owned boundaries.

| Provider | Path | Classification | Adapter | Boundary |
|---|---|---|---|---|
| Boxes.py | `third_party/boxes` | `permanent_provider` | `tool_adapters/boxes.json` | Wrapped helper; source geometry only until validated. |
| LaserGRBL | `third_party/lasergrbl` | `manual_operator_reference` | `tool_adapters/lasergrbl.json` | Manual operator reference; not imported or linked into FabLab runtime. |
| CadQuery | `third_party/cadquery` | `permanent_provider_dependency` | `tool_adapters/cadquery.json` | Python CAD dependency/provider boundary; not a readiness authority. |
| CQ_Gears | `third_party/cq_gears` | `permanent_provider` | `tool_adapters/cq_gears.json` | Wrapped gear source geometry; mechanism validation remains host-owned. |
| BOSL2 | `third_party/bosl2` | `permanent_reference` | `tool_adapters/bosl2.json` | OpenSCAD reference/library; comparison geometry only until validated. |
| FreeCAD Gears | `third_party/freecad-gears` | `inspection_only_provider` | `tool_adapters/freecad_gears.json` | Inspection/provenance provider; non-authoritative checks. |
| step.parts | `third_party/step.parts` | `component_source` | `tool_adapters/step_parts.json` | Component STEP source; purchased-part provenance only until verified. |
| CAD Viewer | `third_party/cad-viewer` | `viewer_reference` | `tool_adapters/cad_viewer.json` | Viewer/reference patterns for inspection UI and artifact review. |

## Provider Boundary Requirements

Each permanent provider/reference must define:

- what it is for
- what it is not for
- invocation mode
- license boundary
- output authority
- validation required before output can be used
- expected outputs
- untrusted provenance outputs
- setup/check command status
- readiness states it can and cannot support
