# Third-Party License Boundaries

This file records initial license and import/copy boundaries for third-party submodules. Exact legal interpretation remains review-required; agents should behave conservatively.

| Path | License File | Boundary |
|---|---|---|
| `third_party/vibe-modeling` | `third_party/vibe-modeling/LICENSE` | Temporary reference. Do not copy implementation into FabLab core without explicit review. |
| `third_party/vibe-cutting` | `third_party/vibe-cutting/LICENSE` | Temporary reference. Migrate concepts and docs with provenance; do not make runtime depend on it. |
| `third_party/text-to-cad` | `third_party/text-to-cad/LICENSE` | Temporary reference. Assimilate patterns and route long-term dependencies through provider boundaries. |
| `third_party/boxes` | `third_party/boxes/LICENSE.txt` | Wrapped provider boundary. Invoke as helper; do not import code into FabLab core without review. |
| `third_party/lasergrbl` | `third_party/lasergrbl/LICENSE.md` | Manual operator reference. Do not link or import into FabLab runtime. |
| `third_party/cadquery` | `third_party/cadquery/LICENSE` | Provider dependency boundary. Treat as external dependency, not copied FabLab source. |
| `third_party/cq_gears` | `third_party/cq_gears/LICENSE` | Wrapped provider boundary. Helper output is source/provenance until validated. |
| `third_party/bosl2` | `third_party/bosl2/LICENSE` | OpenSCAD library/reference boundary. Generated/comparison output requires FabLab validation. |
| `third_party/freecad-gears` | `third_party/freecad-gears/LICENSE` | Inspection-only provider boundary. Do not treat outputs as authoritative fabrication claims. |
| `third_party/step.parts` | `third_party/step.parts/LICENSE` | Component source boundary. Component models require provenance and fit validation. |
| `third_party/cad-viewer` | not found in top-level checkout | Viewer reference boundary. Treat license as `review_required` until upstream license is recorded. |

## Default Rule

When license or provenance is unclear, classify the boundary as `review_required` and do not copy third-party implementation code into FabLab core.
