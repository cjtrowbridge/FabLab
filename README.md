# FabLab: Initial Project Spec

FabLab is a new agentic fabrication repository that unifies additive manufacturing, subtractive manufacturing, assembly-aware CAD, material/tool recommendation, fabrication planning, artifact generation, validation, and human-readable build documentation.

FabLab will begin by including the user’s agent framework and adding two distinct classes of external repositories:

1. **Temporary assimilation submodules**, used only while FabLab is being constructed:

   * `cjtrowbridge/vibe-modeling`
   * `cjtrowbridge/vibe-cutting`
   * `earthtojake/text-to-cad`
  
   [https://github.com/cjtrowbridge/agents](https://github.com/cjtrowbridge/agents) at ./agents  
   [https://github.com/cjtrowbridge/vibe-modeling](https://github.com/cjtrowbridge/vibe-modeling) at ./third_party/vibe-modelling  
   [https://github.com/cjtrowbridge/vibe-cutting](https://github.com/cjtrowbridge/vibe-cutting) at ./third_party/vibe-cutting  
   [https://github.com/earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) at ./third_party/text-to-cad  
    
   And then also all the submodules in third_party under both the vibe-modelling and vibe-cutting projects need to be added under ./third_party

2. **Permanent provider/reference submodules**, used as long-term third-party capabilities that FabLab agents can invoke through documented provider boundaries:

   * Boxes.py
   * LaserGRBL
   * CadQuery
   * CQ_Gears
   * BOSL2
   * FreeCAD Gears
   * `step.parts`
   * CAD viewer tooling
   * other future fabrication, CAD, CAM, robotics, and inspection helpers

Only the three temporary assimilation submodules are expected to be removed after FabLab reaches parity and replaces the prior separate user repositories. The permanent provider/reference submodules are part of FabLab’s intended long-term architecture.

Much of FabLab’s work is not to eliminate third-party tools. It is to make them usable by agents through stable documentation, schemas, provider manifests, setup scripts, validation gates, artifact manifests, license boundaries, and output explanations.

FabLab should eventually replace the previously separate additive and subtractive repositories with a single holistic fabrication system that can have a high-level conversation with an agent, decompose a project into parts, recommend materials and tools for each part, generate the appropriate artifacts for each manufacturing process, validate those artifacts, and produce a self-documenting output bundle with fabrication and assembly instructions.

## Source Context

The existing additive repo, `vibe-modeling`, already provides a reusable OpenSCAD project layout, JSON-driven parameter revisions, build helpers, revision snapshots, generated artifacts, agent playbooks, and structural verification expectations for printable CAD work.

The existing subtractive repo, `vibe-cutting`, already provides a laser fabrication pipeline with machine and material profiles, managed bootstrap tooling, helper adapters, SVG/PNG/G-code/manifests, operation-stage G-code, mechanism validation, and a strict boundary that helper tools provide source geometry but do not own machine artifacts or readiness claims.

The external `earthtojake/text-to-cad` repo contributes a STEP-first CAD-agent approach, including CAD generation/editing with STEP as a main output, optional STL/3MF/GLB exports, a CAD viewer for CAD/G-code/robot files, DXF-oriented workflows, build123d-style assembly modeling, and off-the-shelf STEP part discovery.

FabLab’s core architectural move is to treat all of these as provider capabilities under a larger fabrication-planning system.

FabLab’s second major architectural move is to treat purchased parts as first-class project constraints. Servos, bearings, screws, magnets, fans, switches, motors, shafts, electronics boards, and connectors must be represented as real components with dimensions, provenance, interface constraints, clearances, and validation requirements. They must not be treated as vague proxy blocks.

---

# 1. Mission

FabLab exists to turn a high-level project conversation into a complete, reviewable, manufacturable artifact package.

The agent should be able to discuss a project holistically, identify functional parts, reason about constraints, recommend which parts should be printed, laser-cut, CNC-routed, purchased, hand-fabricated, or modeled as STEP assemblies, and then generate the necessary files only after the user approves the proposed plan.

FabLab is not merely “text to CAD.” It is:

> **conversation to fabrication plan to validated artifact bundle.**

FabLab’s long-term purpose is to make this normal:

```text
project idea
  -> design conversation
  -> project brief
  -> part graph
  -> process and material recommendations
  -> purchased-part/component plan
  -> user approval
  -> provider generation
  -> validation
  -> output bundle
  -> fabricate
  -> assemble
  -> test
  -> revise
```

---

# 2. Design Philosophy

## 2.1 Project-first, not process-first

FabLab should not begin with “make an STL” or “make a laser file.” It should begin with the project’s purpose.

The agent should ask and reason about:

* What is the object for?
* What loads will it carry?
* Will it move?
* Will it get hot?
* Will it be outdoors?
* Does it need to be beautiful, cheap, strong, repairable, fast to produce, or modular?
* What tools and materials are available?
* Which parts are flat?
* Which parts are three-dimensional?
* Which parts need labels or engraving?
* Which parts need precision interfaces?
* Which parts should be bought rather than fabricated?
* Which parts need calibration coupons or test pieces?
* Which purchased parts define binding geometry?
* Which components need measured dimensions before fabrication?
* Which third-party providers are appropriate for the geometry or artifact type?

Only after this analysis should the agent recommend fabrication methods.

## 2.2 Parts, interfaces, and processes are first-class

FabLab must represent a project as a graph of parts and interfaces.

A part may be:

* 3D printed
* laser cut
* laser engraved
* CNC cut
* hand fabricated
* purchased off the shelf
* generated as STEP only
* generated as a jig, template, fixture, or inspection model
* generated by a third-party helper and then validated by FabLab
* represented as a component envelope used to constrain other fabricated parts

An interface may be:

* a fastener pattern
* a tab/slot joint
* a hinge
* a gear mesh
* an axle/bore relationship
* a magnet pocket
* a cable pass-through
* a board mounting pattern
* a thermal interface
* a human interaction surface
* an assembly alignment datum
* a manufacturing registration mark
* a servo horn receiver
* a bearing press fit
* a switch cutout
* a fan mounting pattern
* an electronics connector access window
* a removable service path

## 2.3 Generated is not the same as fabrication-ready

FabLab must preserve the distinction between:

* proposed
* recommended
* selected
* generated
* previewed
* validated
* calibration-only
* fabrication-ready
* physically verified

No artifact should be described as fabrication-ready merely because a file exists, a render succeeded, a mesh is manifold, a STEP file exports, a preview looks correct, or a G-code file was generated.

The existing `vibe-modeling` structural rule should generalize across FabLab: successful CAD rendering, a manifold STL, or a visually correct preview is not sufficient to claim structural safety or fabrication readiness. Structural joins, wall thicknesses, internal material widths, sections, and connectivity must be reviewed and recorded when relevant.

The existing `vibe-cutting` laser rule should also generalize across FabLab: machine code and helper-generated geometry do not become safe or ready merely because a file was produced. Machine limits, material recipes, operation ordering, calibration status, ventilation, focus, framing, and human supervision requirements must be documented.

## 2.4 Helpers are sources, not authorities

Third-party tools may produce source geometry, candidate CAD, inspection artifacts, viewer artifacts, component models, or helper outputs, but FabLab owns:

* project planning
* process selection
* material/tool recommendation
* purchased-part integration
* machine/material recipes
* operation ordering
* artifact manifests
* output documentation
* readiness claims
* safety disclaimers
* final generated fabrication artifacts

This follows the existing `vibe-cutting` model where helpers such as Boxes.py, CQ_Gears, BOSL2, and FreeCAD Gears provide source/provenance geometry or inspection artifacts, while the host pipeline validates mechanism graphs and owns the final job model.

## 2.5 Third-party submodules are not all temporary

FabLab must not use `third_party/` as a synonym for “temporary.”

Only these three repositories are temporary assimilation submodules:

```text
third_party/vibe-modeling
third_party/vibe-cutting
third_party/text-to-cad
```

Permanent provider/reference submodules remain part of FabLab’s architecture. They are the tools FabLab documents, wraps, validates, and exposes to agents.

## 2.6 Purchased parts are design truth, not afterthoughts

FabLab must treat purchased components as binding constraints.

Past agentic CAD failures have come from designs that looked plausible but did not fit real components. Examples include:

* servo shafts centered incorrectly
* servo horns blocked by printed geometry
* center screw access omitted
* wires pinched or trapped
* switch holes sized from memory
* fan mounting patterns guessed
* bearing clearances omitted
* fastener head clearances ignored
* heat-set insert dimensions invented
* electronics ports blocked by enclosure walls

FabLab must therefore maintain a component truth layer with provenance, status, fit risk, measurements, clearance rules, and required validation gates.

---

# 3. Initial Repository Strategy

FabLab’s repository strategy must distinguish:

1. the permanent agent framework,
2. temporary assimilation submodules,
3. permanent provider/reference submodules,
4. FabLab-native providers, docs, schemas, playbooks, and scripts.

The prior phrase “temporary vendoring phase” is too broad. The temporary part is limited to the three assimilation repos. Many `third_party/` modules are permanent.

## 3.1 Agent framework

FabLab should include the user’s agent framework as a core dependency:

```text
https://github.com/cjtrowbridge/agents
path: ./agents
status: permanent framework dependency
role: canonical agent policy, reusable playbooks, operating rules, and agent governance
```

The `agents` framework is not a temporary third-party helper. It is the foundation for FabLab’s agent behavior.

FabLab’s root `AGENTS.md` should instruct agents to read the local agent framework rules first, then use FabLab-specific playbooks, references, schemas, and scripts.

## 3.2 Temporary assimilation submodules

FabLab should initially add the following temporary assimilation submodules:

```text
https://github.com/cjtrowbridge/vibe-modeling
path: ./third_party/vibe-modeling
status: temporary assimilation submodule
role: source of additive/OpenSCAD workflow, structural CAD governance, revision/build conventions, servo references, and legacy projects

https://github.com/cjtrowbridge/vibe-cutting
path: ./third_party/vibe-cutting
status: temporary assimilation submodule
role: source of laser/subtractive workflow, provider-helper architecture, machine/material profiles, mechanism validation, third-party helper routing, and operational docs

https://github.com/earthtojake/text-to-cad
path: ./third_party/text-to-cad
status: temporary assimilation submodule
role: source of STEP-first CAD, build123d-style assembly patterns, CAD viewer patterns, DXF/CAD projection ideas, and off-the-shelf STEP part workflows
```

These temporary submodules exist so FabLab can inspect, wrap, assimilate, migrate, and eventually replace their relevant capabilities.

They should not become permanent runtime dependencies.

## 3.3 Permanent provider/reference submodules

FabLab must also bring over the important `third_party/` submodules from `vibe-cutting` and any useful third-party references from `vibe-modeling`.

These are not temporary. They are long-term capabilities that FabLab agents will use through provider boundaries, reference documentation, setup scripts, and validation gates.

Initial permanent provider/reference submodules should include at least:

```text
https://github.com/florianfesti/boxes
path: ./third_party/boxes
status: permanent provider submodule
role: laser-cut boxes, trays, shelves, fitted panels, finger joints, living hinges, and related flat-stock structures

https://github.com/arkypita/LaserGRBL
path: ./third_party/lasergrbl
status: permanent reference/operator submodule
role: GRBL laser preview/streaming reference and operator workflow reference; not imported or linked into FabLab runtime

https://github.com/cadquery/cadquery
path: ./third_party/cadquery
status: permanent provider dependency/submodule
role: Python parametric CAD and STEP/BREP-capable modeling foundation

https://github.com/meadiode/cq_gears
path: ./third_party/cq_gears
status: permanent provider submodule
role: CadQuery-based gear source geometry for spur gears, ring gears, racks, and mesh candidates

https://github.com/BelfrySCAD/BOSL2
path: ./third_party/bosl2
status: permanent OpenSCAD library/reference submodule
role: OpenSCAD helper library and comparison geometry source, especially for gears and advanced OpenSCAD operations

https://github.com/looooo/freecad.gears
path: ./third_party/freecad-gears
status: permanent inspection/provider submodule
role: FreeCAD gear inspection, STEP provenance, and non-authoritative geometry checks

https://github.com/earthtojake/step.parts
path: ./third_party/step.parts
status: permanent component/reference submodule
role: off-the-shelf STEP parts such as screws, bearings, motors, and connectors

https://github.com/earthtojake/cad-viewer
path: ./third_party/cad-viewer
status: permanent viewer/reference submodule
role: browser-based inspection of STEP, STL, 3MF, GLB, DXF, G-code, URDF, SDF, and SRDF-style artifacts
```

If any listed URL or repository name changes, the agent must verify the current upstream source before adding it, record the corrected URL, and update the submodule documentation.

## 3.4 Required third-party classification

Every submodule under `third_party/` must be classified.

Allowed classifications:

```text
temporary_assimilation_source
permanent_provider
permanent_reference
permanent_provider_dependency
manual_operator_reference
inspection_only_provider
component_source
viewer_reference
rejected_with_rationale
deprecated
```

Classification must be recorded in:

```text
docs/third-party-submodules.md
docs/temporary-assimilation-repos.md
docs/permanent-provider-submodules.md
tool_adapters/*.json
docs/assimilation/*.md
build_manifest.json
provider_versions.json
```

The classification must not depend on folder name alone.

## 3.5 Proposed initial layout

FabLab may either group third-party repositories by status:

```text
FabLab/
  README.md
  AGENTS.md
  LICENSE

  agents/

  third_party/
    temporary/
      vibe-modeling/
      vibe-cutting/
      text-to-cad/

    providers/
      boxes/
      cadquery/
      cq_gears/
      bosl2/
      freecad-gears/
      step.parts/

    references/
      lasergrbl/
      cad-viewer/

  docs/
  playbooks/
  references/
  schemas/
  scripts/
  providers/
  tool_adapters/
  catalogs/
  projects/
  output/
  tests/
```

Or keep all submodules directly under `third_party/`:

```text
FabLab/
  README.md
  AGENTS.md
  LICENSE

  agents/

  third_party/
    vibe-modeling/      # temporary assimilation
    vibe-cutting/       # temporary assimilation
    text-to-cad/        # temporary assimilation

    boxes/              # permanent provider
    lasergrbl/          # permanent reference/operator tool
    cadquery/           # permanent provider dependency
    cq_gears/           # permanent provider
    bosl2/              # permanent OpenSCAD library/provider
    freecad-gears/      # permanent inspection provider
    step.parts/         # permanent component source
    cad-viewer/         # permanent viewer/reference

  docs/
  playbooks/
  references/
  schemas/
  scripts/
  providers/
  tool_adapters/
  catalogs/
  projects/
  output/
  tests/
```

The second option is simpler, but it requires clear documentation so agents do not mistake permanent provider submodules for temporary assimilation repos.

## 3.6 Temporary assimilation repository rules

Temporary assimilation submodules are included to help build FabLab.

They are:

```text
third_party/vibe-modeling
third_party/vibe-cutting
third_party/text-to-cad
```

Rules:

* Treat them as read-only source references unless a task explicitly authorizes changes.
* Do not make FabLab’s long-term runtime depend on them.
* Use them to inspect and migrate docs, playbooks, schemas, scripts, tests, examples, and architectural patterns.
* Track every adopted capability in an assimilation report.
* Create FabLab-native replacements for their core workflows.
* Identify their internal third-party dependencies and decide which should become permanent FabLab provider/reference submodules.
* Remove these temporary submodules only after parity is demonstrated and approved.

## 3.7 Permanent provider/reference submodule rules

Permanent provider/reference submodules are long-term dependencies or references.

They may remain under `third_party/` indefinitely when they provide a real capability FabLab should not reimplement.

Rules:

* Do not casually modify upstream source.
* Keep each submodule pinned.
* Record license and source URL.
* Use provider wrappers, command-line adapters, or documented manual-operator workflows.
* Do not import GPL or incompatible code into FabLab core.
* Treat generated helper output as source/provenance unless FabLab validation promotes it.
* Provide agent-facing docs explaining when and how to use each helper.
* Provide tests or smoke checks when the helper is executable.
* Keep runtime state, caches, generated artifacts, and downloaded dependencies outside committed source.
* Preserve the distinction between reference-only tools and executable providers.

## 3.8 Provider boundary rules

Every permanent provider/reference submodule must have a FabLab-owned boundary.

Required files:

```text
tool_adapters/<tool>.json
docs/tools/<tool>.md
playbooks/how_to_use_<tool>.md
setup/tools/<tool>.py              # when executable/setup-managed
tests/test_<tool>_provider.py      # when automatable
```

The provider boundary must state:

* what the tool is for
* what it is not for
* whether it may be imported, invoked as a subprocess, or used only as reference
* whether it can generate authoritative fabrication artifacts
* what validation is required before helper output can be used
* what license restrictions apply
* what setup commands are allowed
* what outputs are expected
* what outputs are untrusted provenance only
* what readiness states are possible

## 3.9 Replacement phase

FabLab is considered ready to replace the prior two separate user repos only when it can demonstrate feature parity or better for:

* OpenSCAD additive design generation
* STL/3MF/preview generation
* numbered revisions
* immutable revision snapshots
* build manifests
* structural review reporting
* laser SVG/preview/G-code generation
* operation-stage G-code
* machine/material profiles
* setup documents
* helper adapters
* mechanism validation
* portable bootstrap
* agent playbooks
* output README generation
* process/material recommendation
* multi-process project plans
* STEP-first assembly-aware CAD
* off-the-shelf part provenance
* cross-artifact inspection
* permanent provider submodule governance
* third-party license boundary documentation
* provider setup/check/smoke-test workflows
* purchased-part/component truth layer
* servo integration safeguards
* output README explanations for purchased parts and validation status

After this point, only the temporary assimilation submodules should be removed:

```text
remove: ./third_party/vibe-modeling
remove: ./third_party/vibe-cutting
remove: ./third_party/text-to-cad
```

Permanent provider/reference submodules should remain unless individually replaced by a better provider or intentionally deprecated.

---

# 4. Target Architecture

FabLab should be organized around six layers.

## 4.1 Agent and conversation layer

Responsible for:

* reading project briefs
* asking clarifying questions when necessary
* identifying constraints
* decomposing the project into parts
* recommending processes
* identifying purchased components
* proposing a plan for user approval
* executing approved plans
* reporting validation status
* updating docs and playbooks

Key artifacts:

```text
project_brief.md
agent_plan.md
clarifying_questions.md
decision_log.md
```

## 4.2 Part graph layer

Responsible for turning a project into functional parts and interfaces.

Key artifacts:

```text
part_graph.json
interfaces.json
assembly_graph.json
bom.json
component_manifest.json
```

Example part categories:

```text
structural_frame
flat_panel
mounting_boss
fan_duct
gear
rack
linkage
label_plate
electronics_tray
access_hatch
alignment_jig
calibration_coupon
off_the_shelf_component
servo_mount
bearing_carrier
switch_panel
fan_mount
electronics_board_mount
```

## 4.3 Process recommendation layer

Responsible for analyzing which fabrication process fits each part.

Candidate processes:

```text
fdm_3d_print
sla_3d_print
laser_cut
laser_engrave
cnc_route
cnc_mill
sheet_metal
hand_fabricate
buy_off_the_shelf
step_model_only
template_only
hybrid_assembly
component_fit_test
calibration_coupon
```

Candidate recommendation factors:

```text
flatness
curvature
load
heat
outdoor_exposure
precision
motion
wear
friction
quantity
aesthetics
engraving_or_labeling
available_materials
available_machines
assembly_access
repairability
cost
time_to_fabricate
risk
component_fit_risk
measurement_confidence
provider_availability
```

Key artifacts:

```text
process_recommendations.md
process_recommendations.json
selected_process_plan.json
material_recommendations.md
tool_recommendations.md
component_recommendations.md
```

## 4.4 Provider layer

Responsible for invoking, wrapping, documenting, and validating specific generation, inspection, viewer, and helper systems.

The provider layer is not temporary. It is one of FabLab’s core long-term abstractions.

Initial providers and references:

```text
openscad_provider
native_vector_provider
laser_grbl_reference
build123d_step_provider
cad_projection_provider
boxes_provider
cq_gears_provider
bosl2_provider
freecad_gears_provider
step_parts_provider
cad_viewer_reference
```

Provider classifications:

```text
native_provider
wrapped_subprocess_provider
openscad_library_provider
python_environment_provider
system_application_provider
manual_operator_reference
inspection_only_provider
component_source_provider
viewer_reference
temporary_assimilation_source
```

Future providers:

```text
cnc_router_provider
sheet_metal_provider
pcb_provider
sewing_pattern_provider
casting_mold_provider
robot_description_provider
urdf_provider
sdf_provider
vendor_quote_provider
```

FabLab must clearly distinguish between:

* providers it owns natively
* providers it wraps
* references it uses for operator workflow
* component sources it uses for purchased parts
* viewers it uses for inspection
* temporary assimilation sources that should eventually be removed

## 4.5 Validation layer

Responsible for deciding what has been checked and what remains unverified.

Validation domains:

```text
geometry_validity
printability
structural_joins
minimum_wall_thickness
minimum_internal_material_width
laser_bounds
kerf_allowance
operation_order
duplicate_cut_overburn
machine_profile_validity
material_recipe_validity
mechanism_mesh
gear_ratio
phase_transfer
clearance
collision
stackup
registration
assembly_fit
off_the_shelf_part_fit
component_fit
servo_integration
bearing_fit
fastener_access
connector_access
wire_relief
thermal_risk
human_safety
```

Key artifacts:

```text
validation_report.json
validation_summary.md
structural_review.md
mechanism_validation.json
machine_readiness_report.json
material_readiness_report.json
component_validation_report.json
servo_validation_report.json
risk_register.md
```

## 4.6 Artifact bundle layer

Responsible for installing a complete, self-documenting output folder.

Key artifacts:

```text
output/<project>/
  README.md
  build_manifest.json
  artifact_manifest.json
  process_plan.json
  process_recommendations.md
  material_setup.md
  tool_setup.md
  assembly_guide.md
  validation_summary.md
  bom.csv
  previews/
  cad/
  print/
  laser/
  cnc/
  gcode/
  source_geometry/
  operation_artifacts/
  calibration/
  purchased_parts/
  third_party_provenance/
```

---

# 5. Required Capabilities

FabLab must include every major capability from the two existing user repos and the new hybrid approach.

## 5.1 Additive capabilities inherited from `vibe-modeling`

FabLab must support:

* OpenSCAD design authoring
* parameterized JSON configs
* numbered revisions
* generated STL artifacts
* generated 3MF artifacts where applicable
* multi-view PNG previews
* revision snapshots
* immutable revision folders
* scratch output folders
* complete build manifests
* source/config provenance
* multi-part design manifests
* structural join review
* minimum wall thickness review
* minimum internal edge/material width review
* sectional inspection workflow
* generated artifact audits
* agentic OpenSCAD playbooks
* per-design documentation
* commit/playbook workflow governance
* servo design references and servo-receiver rules
* Lovelace block patterns
* cyberdeck and pan/tilt mechanism lessons

## 5.2 Subtractive capabilities inherited from `vibe-cutting`

FabLab must support:

* laser-cut design configs
* native vector geometry
* SVG output
* preview PNG output
* GRBL G-code output
* operation-stage G-code
* job plans
* build manifests
* material setup docs
* machine profiles
* material profiles
* safety notes
* pass-aware operation artifacts
* engraving containment checks
* bounds validation
* helper adapters
* Boxes.py integration
* CQ_Gears integration
* BOSL2 comparison geometry
* FreeCAD Gears inspection
* host-owned mechanism validation
* gear mesh validation
* stackup validation
* channel/phase validation
* duplicate-cut and overburn checks
* portable bootstrap
* readiness reports
* cross-platform verification
* docs, plans, journal, kanban, and downtime report patterns
* third-party provider boundary patterns

## 5.3 New hybrid capabilities

FabLab must add:

* project-level part decomposition
* multi-process fabrication planning
* material and tool recommendation
* process scoring
* STEP-first assembly modeling
* build123d-style CAD generation
* CAD projection to DXF/SVG
* off-the-shelf STEP component sourcing
* assembly-aware artifact manifests
* cross-process output README generation
* project BOM generation
* mixed fabrication assembly guides
* reusable calibration coupon generation
* fabrication risk register
* “selected vs recommended” tracking
* “generated vs fabrication-ready” tracking
* provider-independent artifact bundle schema
* high-level agent playbooks for holistic project design

## 5.4 Third-party provider governance capabilities

FabLab must support:

* permanent third-party provider submodules
* temporary assimilation submodules
* provider classification
* provider adapter manifests
* helper setup/check/run commands
* license boundary documentation
* submodule pin tracking
* submodule cleanliness checks
* provider smoke tests
* provider readiness states
* helper output provenance
* provider-specific playbooks
* provider-specific docs
* safe failure behavior when providers are unavailable
* distinction between reference-only tools and executable providers

FabLab must preserve the `vibe-cutting` principle that helper submodules can provide specialized source geometry or inspection artifacts without becoming the authority for final fabrication jobs. Boxes.py, CQ_Gears, BOSL2, and FreeCAD Gears should be routed through adapters or inspection workflows while host-owned validation remains responsible for readiness claims.

## 5.5 Purchased-part and component capabilities

FabLab must support:

* component catalog entries
* project-specific component instances
* purchased-parts BOMs
* off-the-shelf part sourcing
* STEP component provenance
* manufacturer datasheet provenance
* measured component dimensions
* physical verification status
* component substitution rules
* fit-risk classification
* high-risk component interface validation
* servo profiles
* servo horn receiver validation
* test coupon generation
* fan/switch/bearing/fastener integration checks
* output README purchased-parts sections

---

# 6. Project Workflow

FabLab’s default agent workflow must follow this sequence.

## 6.1 Intake

The user describes a project in natural language.

The agent creates or updates:

```text
project_brief.md
constraints.md
known_inputs.md
open_questions.md
```

The agent should identify missing critical facts, but it should also make useful best-effort assumptions when the missing facts do not block progress.

The agent should also identify:

* likely purchased components
* available fabrication tools
* available materials
* components requiring measurement
* likely provider/tool needs
* safety or calibration risks

## 6.2 Functional decomposition

The agent decomposes the project into parts and interfaces.

Outputs:

```text
part_graph.json
interfaces.json
assembly_graph.json
component_manifest.json
```

Each part must include:

```json
{
  "id": "front_switch_panel",
  "name": "Front Switch Panel",
  "function": "Mounts power toggles and labels device power channels.",
  "interfaces": ["toggle_switch_cutouts", "case_front_mounting_holes"],
  "constraints": {
    "flat": true,
    "requires_engraving": true,
    "moderate_precision": true
  }
}
```

Each purchased component must include:

```json
{
  "id": "main_power_toggle",
  "component_type": "toggle_switch",
  "status": "proxy_unverified",
  "used_by_parts": ["front_switch_panel"],
  "critical_dimensions": ["panel_cutout_diameter", "thread_length", "body_depth", "terminal_clearance"],
  "requires_physical_measurement": true
}
```

## 6.3 Process and material recommendation

The agent evaluates each part and recommends one or more fabrication processes.

Example:

```json
{
  "part_id": "front_switch_panel",
  "recommended_processes": [
    {
      "process": "laser_cut_and_engrave",
      "material": "3mm acrylic or 3mm plywood",
      "confidence": "high",
      "reason": "The part is flat, contains repeated cutouts, and benefits from engraved labels."
    },
    {
      "process": "fdm_3d_print",
      "material": "PETG",
      "confidence": "medium",
      "reason": "Works if an integrated bezel is needed, but is slower and less clean for flat labeled panels."
    }
  ],
  "selected_process": null
}
```

Outputs:

```text
process_recommendations.md
process_recommendations.json
material_recommendations.md
tool_recommendations.md
component_recommendations.md
```

## 6.4 Approval gate

Before generating manufacturing artifacts, the agent must present:

* proposed part list
* purchased component list
* recommended processes
* proposed materials
* required tools/machines
* expected outputs
* known risks
* validation limits
* assumptions
* required measurements
* required test coupons
* third-party providers to be used

The agent must wait for project approval before producing fabrication artifacts unless the user has explicitly authorized immediate generation.

## 6.5 Artifact generation

After approval, FabLab invokes the selected providers.

Example provider mapping:

```text
fan_duct -> build123d_step_provider or openscad_provider -> STL/STEP/preview
front_switch_panel -> native_vector_provider -> SVG/preview/G-code
side_panels -> cad_projection_provider or laser provider -> DXF/SVG/G-code
gear_train -> cq_gears_provider + mechanism validation -> SVG/G-code
purchased_screws -> step_parts_provider -> STEP provenance + BOM row
servo_mount -> openscad_provider or build123d_step_provider + servo validation -> STL/STEP/preview
servo_horn_receiver -> provider + test coupon -> STL/coupon README
```

## 6.6 Validation

FabLab validates each artifact according to its process.

Example validation map:

```text
FDM part:
  - wall thickness
  - structural joins
  - overhang/print orientation notes
  - clearance checks
  - source/config provenance

Laser part:
  - sheet bounds
  - cut/engrave operation ordering
  - duplicate path risk
  - kerf assumptions
  - material/machine recipe status
  - setup checklist

Mechanism:
  - gear mesh
  - phase transfer
  - backlash
  - stackup
  - rotating clearance
  - axle/bore clearance
  - registration
  - helper provenance

STEP assembly:
  - named datums
  - component placement
  - collision checks where available
  - measurement report
  - purchased part provenance

Servo integration:
  - body envelope represented
  - shaft offset represented
  - horn sweep represented
  - center screw access preserved
  - wire relief preserved
  - service/removal path preserved
  - test coupon generated when needed
```

## 6.7 Output bundle installation

FabLab installs a self-contained output bundle.

Required output folder:

```text
output/<project>/
  README.md
  build_manifest.json
  artifact_manifest.json
  process_plan.json
  process_recommendations.md
  validation_summary.md
  assembly_guide.md
  bom.csv
  material_setup.md
  tool_setup.md
  previews/
  cad/
  print/
  laser/
  gcode/
  operation_artifacts/
  calibration/
  purchased_parts/
  third_party_provenance/
```

The output README is mandatory.

---

# 7. Output README Contract

Every generated project output folder must include:

```text
output/<project>/README.md
```

The README must explain:

1. What the project is.
2. Which revision/config generated the output.
3. Which parts are included.
4. Which parts are 3D printed.
5. Which parts are laser cut or engraved.
6. Which parts are CNC-routed or otherwise machined.
7. Which parts are purchased/off-the-shelf.
8. Which materials were selected.
9. Which tools or machines are assumed.
10. Which third-party providers were used.
11. Which files correspond to which physical parts.
12. Which artifacts are source geometry.
13. Which artifacts are fabrication artifacts.
14. Which artifacts are previews.
15. Which validation checks passed.
16. Which validation checks failed.
17. Which validation checks remain unverified.
18. Which outputs are calibration-only.
19. How to inspect the artifacts.
20. How to manufacture each part.
21. How to assemble the project.
22. What physical calibration or safety steps must happen before fabrication.
23. Which purchased components need measurement.
24. Which substitutions are allowed.
25. What changed from the prior revision, if applicable.

Example README outline:

```markdown
# Output: Portable Inference Cluster Rev 0001

## Summary

This folder contains the generated fabrication package for the approved Rev 0001 process plan.

## Parts

| Part | Process | Material | Artifact |
|---|---|---|---|
| Fan duct | FDM print | PETG | print/fan_duct.stl |
| Front panel | Laser cut/engrave | 3mm acrylic | laser/front_panel.svg |
| Side panel | Laser cut | 3mm plywood | laser/side_panel.svg |
| M3 screws | Purchased | Steel | bom.csv |

## Purchased Parts

| Component | Status | Used By | Verification |
|---|---|---|---|
| M3 screws | manufacturer_sourced | front_panel, side_panel | verify length and head clearance |
| 40mm fan | proxy_unverified | fan_mount | measure frame, screw spacing, thickness, wire exit |

## Manufacturing Steps

1. Review previews.
2. Measure purchased components marked unverified.
3. Print calibration coupons where required.
4. Print the PETG duct.
5. Cut and engrave the front panel.
6. Cut the side panels.
7. Deburr and test fit.
8. Assemble with M3 hardware.

## Validation Status

- Geometry generation: passed
- Structural review: unverified
- Laser bounds: passed
- Material recipe: calibration-only
- Purchased component fit: unverified until physical measurement
- Assembly fit: unverified until physical test

## Safety and Calibration

Do not run generated G-code until machine limits, focus, material settings, ventilation, and non-emitting framing are verified.
```

---

# 8. Proposed Final Repository Layout

```text
FabLab/
  README.md
  AGENTS.md
  LICENSE

  agents/

  docs/
    architecture.md
    process-selection.md
    material-selection.md
    output-bundle-contract.md
    provider-contract.md
    validation-contract.md
    third-party-submodules.md
    temporary-assimilation-repos.md
    permanent-provider-submodules.md
    helper-boundaries.md
    license-boundaries.md
    component-sourcing-policy.md
    purchased-parts-contract.md
    servo-integration-contract.md
    migration-from-vibe-modeling.md
    migration-from-vibe-cutting.md
    text-to-cad-assimilation.md

    tools/
      boxes.md
      lasergrbl.md
      cadquery.md
      cq-gears.md
      bosl2.md
      freecad-gears.md
      step-parts.md
      cad-viewer.md
      openscad.md
      build123d-step.md

    assimilation/
      vibe-modeling-assimilation.md
      vibe-cutting-assimilation.md
      text-to-cad-assimilation.md
      migration-parity-matrix.md
      third-party-license-boundaries.md

  playbooks/
    how_to_start_a_new_fabrication_project.md
    how_to_decompose_a_project_into_parts.md
    how_to_recommend_materials_and_processes.md
    how_to_prepare_a_process_plan_for_approval.md
    how_to_generate_approved_fabrication_artifacts.md
    how_to_build_and_audit_a_fabrication_bundle.md
    how_to_author_additive_parts.md
    how_to_author_laser_cut_parts.md
    how_to_author_step_assemblies.md
    how_to_author_hybrid_assemblies.md
    how_to_validate_structural_parts.md
    how_to_validate_laser_jobs.md
    how_to_validate_mechanisms.md
    how_to_create_output_readmes.md
    how_to_add_a_permanent_provider_submodule.md
    how_to_add_a_temporary_assimilation_submodule.md
    how_to_assimilate_a_temporary_source_repo.md
    how_to_write_provider_documentation.md
    how_to_wrap_a_third_party_helper.md
    how_to_validate_provider_outputs.md
    how_to_retire_a_temporary_assimilation_submodule.md
    how_to_define_a_purchased_part.md
    how_to_design_with_servos.md
    how_to_validate_purchased_part_interfaces.md
    how_to_migrate_legacy_vibe_modeling_projects.md
    how_to_migrate_legacy_vibe_cutting_projects.md
    how_to_commit_and_push_changes.md

  references/
    process-selection-rubric.md
    material-selection-rubric.md
    helper-provider-boundary.md
    fabrication-readiness-language.md
    component-sourcing-policy.md
    calibration-coupon-patterns.md
    manifest-patterns.md
    measured-component-provenance.md

  schemas/
    project.schema.json
    project_brief.schema.json
    part.schema.json
    part_graph.schema.json
    interface.schema.json
    process_recommendation.schema.json
    process_plan.schema.json
    material_profile.schema.json
    machine_profile.schema.json
    provider.schema.json
    artifact_manifest.schema.json
    build_manifest.schema.json
    validation_report.schema.json
    output_readme.schema.json
    assembly_plan.schema.json
    bom.schema.json
    component.schema.json
    component_catalog.schema.json
    component_instance.schema.json
    purchased_part.schema.json
    component_interface.schema.json
    component_measurement.schema.json
    servo_profile.schema.json
    servo_mount_validation.schema.json
    test_coupon.schema.json
    assimilation_report.schema.json
    third_party_module.schema.json
    provider_assimilation.schema.json

  catalogs/
    materials/
      pla.json
      petg.json
      abs.json
      basswood_3mm.json
      plywood_3mm.json
      acrylic_3mm.json
      aluminum_sheet.json

    machines/
      generic_fdm_printer.json
      creality_falcon_a1_pro.json
      hand_tools.json

    components/
      fasteners/
      bearings/
      magnets/
      switches/
      fans/
      servos/
        mg996r_standard_servo_profile_v1.json
      motors/
      shafts/
      electronics_boards/
      heat_set_inserts/
      connectors/

  providers/
    openscad/
    native_vector/
    laser_grbl/
    build123d_step/
    cad_projection/
    boxes/
    cq_gears/
    bosl2/
    freecad_gears/
    step_parts/
    cad_viewer/

  tool_adapters/
    openscad.json
    native_vector.json
    build123d_step.json
    boxes.json
    cq_gears.json
    bosl2.json
    freecad_gears.json
    step_parts.json
    cad_viewer.json

  scripts/
    fablab.py
    project_new.py
    project_plan.py
    process_recommend.py
    build_bundle.py
    audit_bundle.py
    provider_tool.py
    validate_project.py
    validate_components.py
    generate_output_readme.py
    migrate_vibe_modeling.py
    migrate_vibe_cutting.py
    classify_third_party.py

  setup/
    bootstrap.sh
    bootstrap.ps1
    bootstrap_host.py
    pixi.toml
    toolchain-manifest.json
    tools/
      boxes.py
      cadquery.py
      cq_gears.py
      bosl2.py
      freecad_gears.py
      step_parts.py
      cad_viewer.py

  projects/
    examples/
      hybrid_electronics_enclosure/
      lovelace_power_extender/
      laser_merit_badges/
      printable_cottage_case/
      servo_pan_tilt_coupon/

  output/
    .gitkeep

  tests/
    test_process_recommendation.py
    test_output_readme_contract.py
    test_provider_contracts.py
    test_manifest_generation.py
    test_migration_vibe_modeling.py
    test_migration_vibe_cutting.py
    test_hybrid_bundle.py
    test_third_party_classification.py
    test_component_manifest.py
    test_servo_integration_contract.py
    test_purchased_part_interfaces.py

  third_party/
    # Temporary assimilation submodules.
    # These exist only while FabLab is being constructed and migrated.
    vibe-modeling/
    vibe-cutting/
    text-to-cad/

    # Permanent provider/reference submodules.
    # These are long-term third-party capabilities exposed through FabLab provider boundaries.
    boxes/
    lasergrbl/
    cadquery/
    cq_gears/
    bosl2/
    freecad-gears/
    step.parts/
    cad-viewer/
```

---

# 9. Agentic Playbook Requirements

FabLab must include playbooks that guide agents through the full lifecycle.

## 9.1 `how_to_start_a_new_fabrication_project.md`

Must instruct agents to:

1. Read the user’s project request.
2. Identify the project goal.
3. Identify known constraints.
4. Identify available tools and materials.
5. Identify likely purchased components.
6. Create `project_brief.md`.
7. Create an initial project config.
8. Record assumptions.
9. Avoid generating fabrication artifacts before approval.

## 9.2 `how_to_decompose_a_project_into_parts.md`

Must instruct agents to:

1. Break the project into functional parts.
2. Identify interfaces.
3. Identify off-the-shelf parts.
4. Identify moving assemblies.
5. Identify calibration/test pieces.
6. Identify component fit risks.
7. Create `part_graph.json`.
8. Create `assembly_graph.json`.
9. Create or update `component_manifest.json`.

## 9.3 `how_to_recommend_materials_and_processes.md`

Must instruct agents to:

1. Score each part against process-selection criteria.
2. Recommend candidate materials.
3. Recommend candidate tools/machines.
4. Recommend purchased parts where fabrication is inappropriate.
5. Explain tradeoffs.
6. Mark confidence level.
7. Record rejected alternatives.
8. Produce `process_recommendations.md`.
9. Produce `process_recommendations.json`.

## 9.4 `how_to_prepare_a_process_plan_for_approval.md`

Must instruct agents to present:

1. Part list.
2. Purchased component list.
3. Recommended processes.
4. Recommended materials.
5. Expected generated artifacts.
6. Required machines/tools.
7. Required third-party providers.
8. Safety notes.
9. Validation limits.
10. Required measurements.
11. Required test coupons.
12. Questions or assumptions.
13. Approval request.

## 9.5 `how_to_generate_approved_fabrication_artifacts.md`

Must instruct agents to:

1. Confirm the approved process plan.
2. Create or update configs.
3. Invoke only the selected providers.
4. Generate source artifacts.
5. Generate fabrication artifacts.
6. Generate previews.
7. Run validations.
8. Generate manifests.
9. Generate output README.
10. Refuse to label unverified artifacts as fabrication-ready.

## 9.6 `how_to_build_and_audit_a_fabrication_bundle.md`

Must instruct agents to:

1. Stage artifacts in a temporary build directory.
2. Verify expected artifact list.
3. Verify no stale or unexpected artifacts.
4. Hash source/config/provider inputs.
5. Hash generated artifacts.
6. Write `build_manifest.json`.
7. Write `artifact_manifest.json`.
8. Install the output bundle atomically.
9. Run audit-only checks.

## 9.7 `how_to_create_output_readmes.md`

Must instruct agents to:

1. Read the selected process plan.
2. Read the artifact manifest.
3. Read validation summaries.
4. Read component manifest and BOM.
5. Generate a human-readable output README.
6. Explain every artifact.
7. Explain fabrication order.
8. Explain assembly order.
9. Explain purchased parts.
10. Explain calibration-only status.
11. Explain safety requirements.
12. Explain what is unverified.

## 9.8 `how_to_add_a_permanent_provider_submodule.md`

Must instruct agents to:

1. Identify the third-party tool and its upstream URL.
2. Confirm why the tool should remain a permanent provider/reference.
3. Add the submodule under `third_party/`.
4. Pin the submodule.
5. Record license and source URL.
6. Create or update `docs/third-party-submodules.md`.
7. Create `docs/tools/<tool>.md`.
8. Create `tool_adapters/<tool>.json` when the tool is executable or provider-routable.
9. Create setup/check/run scripts when appropriate.
10. Add tests or smoke checks when appropriate.
11. State whether the tool is authoritative, source-only, inspection-only, component-source, viewer, or reference-only.
12. State what validation is required before using outputs in a fabrication bundle.

## 9.9 `how_to_add_a_temporary_assimilation_submodule.md`

Must instruct agents to:

1. Identify the source repo being temporarily assimilated.
2. Add it under `third_party/`.
3. Mark it as temporary in `docs/temporary-assimilation-repos.md`.
4. Create an assimilation report.
5. Inventory docs, playbooks, schemas, tests, scripts, examples, and submodules.
6. Identify which parts should become FabLab-native.
7. Identify which submodules should become permanent provider/reference submodules.
8. Identify license and dependency boundaries.
9. Create migration/parity tasks.
10. Define removal criteria.

## 9.10 `how_to_assimilate_a_temporary_source_repo.md`

Must instruct agents to:

1. Read the source repo’s README, AGENTS instructions, docs, playbooks, schemas, scripts, and tests.
2. Inventory third-party submodules used by that repo.
3. Classify each item as:

   * adopt native
   * adapt into FabLab
   * wrap as provider
   * preserve as reference
   * migrate later
   * deprecate after parity
   * ignore with rationale
   * blocked by license
   * blocked by dependency
4. Create a migration/parity matrix.
5. Move reusable workflow knowledge into FabLab docs/playbooks.
6. Move provider knowledge into `docs/tools/`, `tool_adapters/`, `setup/tools/`, and tests.
7. Do not make the temporary source repo a runtime dependency.
8. Update removal criteria when parity is complete.

## 9.11 `how_to_write_provider_documentation.md`

Must instruct agents to document:

1. What the provider does.
2. What it should not be used for.
3. Whether it is executable, reference-only, inspection-only, or component-source.
4. How it is installed or checked.
5. How it is invoked.
6. What outputs it produces.
7. What license boundaries apply.
8. What validation gates apply.
9. How outputs appear in the final artifact bundle.

## 9.12 `how_to_define_a_purchased_part.md`

Must instruct agents to:

1. Identify the real component.
2. Search the existing component catalog.
3. Prefer manufacturer dimensions or measured dimensions.
4. Record source/provenance.
5. Record critical dimensions.
6. Record integration constraints.
7. Record substitution rules.
8. Classify fit risk.
9. Create component catalog entry if missing.
10. Create project component instance.
11. Add part to BOM.

## 9.13 `how_to_design_with_servos.md`

Must instruct agents to:

1. Select a known servo profile or create a new measured profile.
2. Never invent servo body geometry.
3. Never center the servo shaft unless the profile says it is centered.
4. Preserve horn sweep.
5. Preserve center screw access.
6. Preserve wire relief.
7. Prefer stock horn receiver pockets.
8. Avoid printed splines unless explicitly approved and tested.
9. Generate receiver test coupon when needed.
10. Validate servo removal/service path.
11. Include servo section in output README.

## 9.14 `how_to_validate_purchased_part_interfaces.md`

Must instruct agents to:

1. List all purchased parts.
2. List all fabricated parts that touch them.
3. Classify each interface risk.
4. Run appropriate fit checks.
5. Generate test coupons where required.
6. Record unverified dimensions.
7. Block fabrication-ready claims for high-risk unmeasured parts.
8. Update output README and BOM.

---

# 10. Process Recommendation Rubric

FabLab should begin with a deterministic rubric before attempting more complex optimization.

## 10.1 Additive/FDM is preferred when

* the part is non-planar
* the part contains ducts or curved passages
* the part contains bosses, standoffs, clips, or pockets
* the part has low-to-moderate load
* the part benefits from integrated 3D geometry
* the part is a jig, fixture, spacer, or enclosure body
* iteration speed matters more than surface finish
* internal voids are simple enough to print

## 10.2 Laser cutting is preferred when

* the part is flat
* the part is sheet-like
* the part requires engraving or labels
* the part is repeated many times
* the part is a panel, token, badge, linkage, gear, rack, or spacer
* the part can be assembled from layers
* the part benefits from precise 2D profiles
* material thickness is part of the design

## 10.3 STEP/build123d CAD is preferred when

* the project is an assembly
* multiple parts must share datums
* purchased parts must be represented
* geometry should be reusable across print and cut outputs
* CAD projection can generate 2D fabrication profiles
* named faces, edges, frames, or measurements matter
* the project may later need CNC, robotics, or simulation outputs

## 10.4 Off-the-shelf purchase is preferred when

* the part is a fastener, bearing, shaft, magnet, fan, servo, switch, motor, connector, bushing, or standard mechanical component
* fabrication would be less accurate than buying the part
* the part is safety-critical
* wear resistance matters
* material properties are hard to reproduce
* replacement availability matters
* the part requires precision manufacturing beyond available tools

## 10.5 Calibration coupons are required when

* the material recipe is unverified
* kerf is unknown
* press-fit tolerances matter
* gears or mechanisms are being fabricated
* engraving readability is uncertain
* thermal behavior is uncertain
* the machine profile is provisional
* the part is expensive or time-consuming
* a servo horn receiver is newly generated
* a bearing or shaft fit is high-risk
* a switch or connector fit depends on unverified component dimensions

---

# 11. Provider Contract

Every provider must declare:

```json
{
  "id": "openscad",
  "schema_version": 1,
  "role": "additive_geometry",
  "provider_classification": "native_provider",
  "inputs": ["project_part", "config"],
  "outputs": ["stl", "3mf", "preview_png", "source_scad"],
  "can_generate_machine_code": false,
  "owns_readiness_claims": false,
  "validation_required": ["structural_review", "artifact_audit"],
  "license": "declared_in_adapter"
}
```

Provider outputs must be classified as one of:

```text
source_geometry
preview
fabrication_artifact
machine_code
inspection_artifact
manifest
documentation
calibration_artifact
component_model
viewer_artifact
reference_only
```

Permanent third-party providers must additionally declare:

```json
{
  "upstream_url": "https://example.com/upstream/repo",
  "submodule_path": "third_party/example",
  "submodule_status": "permanent_provider",
  "invocation_mode": "subprocess",
  "license_boundary": "do_not_import_into_core",
  "output_authority": "source_geometry_only",
  "setup_command": "setup/bootstrap.sh run -- scripts/provider_tool.py setup example",
  "check_command": "setup/bootstrap.sh run -- scripts/provider_tool.py check example"
}
```

---

# 12. FabLab Command Model

Initial command interface:

```bash
setup/bootstrap.sh run -- scripts/fablab.py new --project <name>
setup/bootstrap.sh run -- scripts/fablab.py brief --project <name>
setup/bootstrap.sh run -- scripts/fablab.py decompose --project <name>
setup/bootstrap.sh run -- scripts/fablab.py recommend --project <name>
setup/bootstrap.sh run -- scripts/fablab.py plan --project <name>
setup/bootstrap.sh run -- scripts/fablab.py build --project <name>
setup/bootstrap.sh run -- scripts/fablab.py audit --project <name>
setup/bootstrap.sh run -- scripts/fablab.py output-readme --project <name>
```

Provider-specific commands should exist but remain subordinate:

```bash
setup/bootstrap.sh run -- scripts/provider_tool.py list
setup/bootstrap.sh run -- scripts/provider_tool.py validate
setup/bootstrap.sh run -- scripts/provider_tool.py check <provider>
setup/bootstrap.sh run -- scripts/provider_tool.py setup <provider>
setup/bootstrap.sh run -- scripts/provider_tool.py run <provider> -- <args>
```

Third-party classification commands:

```bash
setup/bootstrap.sh run -- scripts/classify_third_party.py list
setup/bootstrap.sh run -- scripts/classify_third_party.py check
setup/bootstrap.sh run -- scripts/classify_third_party.py audit
```

Component commands:

```bash
setup/bootstrap.sh run -- scripts/fablab.py components list
setup/bootstrap.sh run -- scripts/fablab.py components validate --project <name>
setup/bootstrap.sh run -- scripts/validate_components.py --project <name>
```

---

# 13. Migration Requirements

## 13.1 Migrating `vibe-modeling`

FabLab must be able to import a legacy `vibe-modeling` design and create:

```text
projects/<name>/
  project.json
  configs/rev_000N.json
  parts/<part>.part.json
  legacy/
    source_path_reference.json
```

It must preserve:

* source OpenSCAD
* configs
* revision numbers
* part IDs
* generated artifact expectations
* structural verification rules
* README context
* playbook-relevant notes
* servo reference notes
* component assumptions
* output/revision governance

## 13.2 Migrating `vibe-cutting`

FabLab must be able to import a legacy `vibe-cutting` design and create:

```text
projects/<name>/
  project.json
  configs/rev_000N.json
  parts/<part>.part.json
  process_plan.json
  legacy/
    source_path_reference.json
```

It must preserve:

* project config
* machine profile
* material profile
* design config
* output artifact expectations
* helper requests
* mechanism graphs
* operation-stage semantics
* safety/calibration status
* README context
* provider/helper boundaries
* relevant permanent third-party submodules

## 13.3 Assimilating `text-to-cad`

FabLab must inspect and assimilate the useful patterns from `text-to-cad` without making the temporary submodule a long-term runtime dependency.

It must preserve or adapt:

* STEP-first CAD workflow patterns
* build123d-style source patterns
* assembly-aware modeling conventions
* DXF/CAD projection ideas
* CAD viewer patterns
* off-the-shelf STEP part lookup patterns
* inspection and measurement conventions
* topology/reference/datum concepts

Where useful capabilities depend on external repos or tools, those should be represented as permanent provider/reference submodules or FabLab-native provider wrappers.

## 13.4 Retirement criteria for temporary assimilation repos

Only these repos are subject to planned retirement:

```text
third_party/vibe-modeling
third_party/vibe-cutting
third_party/text-to-cad
```

They must not be removed until:

* migrated example projects build successfully
* output bundles pass audit
* existing major workflows have FabLab equivalents
* agent playbooks cover the new workflows
* generated output READMEs are complete
* old repo capability parity is documented
* third-party provider submodules from the old repos have been brought over or intentionally rejected
* provider docs and tool adapters exist for permanent helpers
* license boundaries are documented
* purchased-part/component contracts exist
* servo integration safeguards are tested
* the user approves retirement

Permanent provider/reference submodules are not removed as part of this retirement. They remain under `third_party/` unless a specific provider replacement/deprecation plan says otherwise.

---

# 14. Purchased Parts and Component Truth Layer

## 14.1 Component catalog

FabLab must include a component catalog:

```text
catalogs/
  components/
    servos/
    motors/
    bearings/
    fasteners/
    magnets/
    fans/
    switches/
    connectors/
    electronics_boards/
    heat_set_inserts/
    threaded_inserts/
    shafts/
    belts/
    pulleys/
    springs/
```

Each component entry must include:

```json
{
  "schema_version": 1,
  "id": "mg996r_standard_servo_profile_v1",
  "component_type": "servo",
  "manufacturer": "generic_mg996r_compatible",
  "status": "reference_profile",
  "source_confidence": "medium",
  "requires_physical_verification": true,
  "dimensions_mm": {},
  "interfaces": {},
  "clearance_rules": [],
  "mounting_rules": [],
  "artifact_references": [],
  "notes": []
}
```

## 14.2 Component status values

Every component must have a status:

```text
proxy_unverified
reference_profile
manufacturer_sourced
measured_by_user
physically_tested
fit_verified
deprecated
```

Agents must not treat `proxy_unverified` or `reference_profile` components as fully reliable.

## 14.3 Required component provenance

Every purchased part used in a project must record at least one provenance source:

```text
manufacturer datasheet
vendor listing
STEP file
caliper measurement
photo with scale
prior verified project
user supplied dimensions
FabLab reference profile
```

For high-risk components, FabLab should prefer:

```text
actual measured part
actual STEP model
manufacturer mechanical drawing
test coupon
```

## 14.4 Purchased part output artifacts

For every purchased part, the output bundle must include a purchased-parts section:

```text
output/<project>/purchased_parts/
  purchased_parts.md
  purchased_parts.csv
  component_manifest.json
  step/
  datasheets/
  measurement_notes/
```

The output README must explain:

* what to buy
* why it was selected
* which generated parts depend on it
* which dimensions are binding
* which dimensions are unverified
* what to measure before fabrication
* what test coupons to print/cut
* what access/maintenance constraints matter
* which substitutions are allowed

---

# 15. Servo Integration Contract

## 15.1 Why servos need a special contract

Servos are a known failure point because they combine:

```text
body mounting geometry
shaft offset
spline/horn interface
screw access
wire strain relief
horn sweep volume
moving load
torque limits
clearance envelopes
replaceable hardware
```

FabLab must import and generalize the existing servo guidance from `vibe-modeling`.

The agent must not invent servo geometry. It must not center the shaft unless the component profile says the shaft is centered. It must preserve horn sweep, center screw access, wire relief, and service/removal paths.

## 15.2 Default MG996R profile

FabLab must include a default component profile:

```text
catalogs/components/servos/mg996r_standard_servo_profile_v1.json
```

Minimum required fields:

```json
{
  "schema_version": 1,
  "id": "mg996r_standard_servo_profile_v1",
  "component_type": "servo",
  "profile_family": "MG996R / MG995 standard-size hobby servo",
  "status": "reference_profile",
  "requires_physical_verification": true,

  "body": {
    "approx_x_mm": 40.7,
    "approx_y_mm": 19.7,
    "approx_z_mm": 42.9
  },

  "flange": {
    "width_mm": 54.0,
    "depth_mm": 20.0
  },

  "body_cutout": {
    "x_mm": 40.3,
    "y_mm": 20.0,
    "clearance_required": true
  },

  "mounting_holes": {
    "pattern_x_mm": 50.0,
    "pattern_y_mm": 10.0,
    "hole_diameter_mm": 4.0,
    "default_screw": "M3",
    "printed_clearance_diameter_mm": 3.3
  },

  "screw_boss": {
    "default_outer_diameter_mm": 9.0
  },

  "shaft": {
    "do_not_center_in_body": true,
    "offset_from_flange_center_mm": 11.0,
    "distance_from_nearest_flange_end_mm": 16.0
  },

  "rules": [
    "Do not invent servo mounting geometry.",
    "Do not center the shaft in the servo body unless the profile says it is centered.",
    "Do not block horn sweep.",
    "Do not block center screw access.",
    "Do not crush or trap the wire.",
    "Prefer stock horn receiver pockets over printed splines.",
    "Require a test coupon for first receiver pocket."
  ]
}
```

These values should be treated as a reference profile until physically verified against the exact servo being used.

## 15.3 Servo horn receiver rule

FabLab must import the existing rule:

> Prefer designing the fabricated part to receive a stock servo horn. Do not directly print a custom internal servo spline unless explicitly required and a tested spline profile is available.

For MG996R-class servos, the stock horn should be treated as the torque-transfer insert because the spline is small, highly loaded, and difficult to print accurately.

## 15.4 Servo design validation

Any part that mounts or interfaces with a servo must run servo-specific validation.

Required validation checks:

```text
servo body envelope represented
servo flange represented
shaft offset represented
mounting holes placed from component profile
wire exit clearance represented
horn sweep envelope represented
center screw access preserved
horn receiver pocket defined or omitted with rationale
stock horn dimensions recorded as measured or assumed
fastener access preserved
servo removal path preserved
rotation limits recorded
torque/load assumption recorded
test coupon generated when receiver pocket is new
```

## 15.5 Servo test coupon requirement

If a generated design includes a servo horn receiver pocket, FabLab must generate or recommend a test coupon unless the exact horn receiver has already been physically verified.

Example output:

```text
output/<project>/calibration/
  mg996r_horn_receiver_coupon.stl
  mg996r_horn_receiver_coupon_readme.md
```

The coupon README must explain:

```text
which horn it fits
which clearance is being tested
which screws are required
what successful fit means
what failure modes to check
how to update the component profile after measurement
```

## 15.6 Servo integration in output README

The output README must include a servo section when relevant:

```markdown
## Servo Integration

This project uses `mg996r_standard_servo_profile_v1`.

### Servo Status

- Component profile: reference profile
- Physical measurements: not yet verified
- Horn receiver: generated
- Horn receiver coupon: required before final fabrication

### Critical Checks

- Do not center the shaft in the body.
- Confirm the horn sweep is unobstructed.
- Confirm the center screw can be accessed after assembly.
- Confirm the servo wire is not pinched.
- Confirm the stock horn fits the receiver pocket.
```

---

# 16. Initial Milestones

## Milestone 0: Repository Bootstrap

* Create FabLab repo.
* Add `agents` framework at `./agents`.
* Add temporary assimilation submodules:

  * `third_party/vibe-modeling`
  * `third_party/vibe-cutting`
  * `third_party/text-to-cad`
* Add permanent provider/reference submodules initially inherited from the source repos:

  * `third_party/boxes`
  * `third_party/lasergrbl`
  * `third_party/cadquery`
  * `third_party/cq_gears`
  * `third_party/bosl2`
  * `third_party/freecad-gears`
  * `third_party/step.parts`
  * `third_party/cad-viewer`
* Add root README and AGENTS.
* Add `docs/third-party-submodules.md`.
* Add `docs/temporary-assimilation-repos.md`.
* Add `docs/permanent-provider-submodules.md`.
* Add provider boundary documentation.
* Confirm all submodules are pinned and recursively clean.

## Milestone 1: Third-Party Classification and Assimilation Inventory

* Inventory `vibe-modeling`.
* Inventory `vibe-cutting`.
* Inventory `text-to-cad`.
* Inventory all third-party submodules used by those repos.
* Classify every submodule as temporary assimilation, permanent provider, permanent reference, or rejected with rationale.
* Produce:

  * `docs/assimilation/vibe-modeling-assimilation.md`
  * `docs/assimilation/vibe-cutting-assimilation.md`
  * `docs/assimilation/text-to-cad-assimilation.md`
  * `docs/assimilation/migration-parity-matrix.md`
  * `docs/third-party-submodules.md`

## Milestone 2: Provider Documentation and Wrapper Baseline

* Create docs/tools pages for every permanent provider/reference submodule.
* Create provider manifests for executable helpers.
* Create setup/check/run command contracts where applicable.
* Create smoke tests where applicable.
* Define readiness states.
* Preserve the rule that helper output is not automatically authoritative fabrication output.
* Confirm provider docs explain when agents should use each third-party tool.

## Milestone 3: Common Project Schema

* Define project schema.
* Define part schema.
* Define component schema.
* Define component instance schema.
* Define process recommendation schema.
* Define process plan schema.
* Define artifact manifest schema.
* Define output README contract.

## Milestone 4: Process Recommendation MVP

* Implement deterministic part/process scoring.
* Generate `process_recommendations.md`.
* Generate `process_recommendations.json`.
* Support additive, laser, STEP, purchased, and calibration-only recommendations.
* Include component-fit risk in recommendations.

## Milestone 5: Output Bundle MVP

* Generate output folder.
* Generate README.
* Generate artifact manifest.
* Generate build manifest.
* Generate BOM.
* Generate component manifest.
* Support at least one dummy provider artifact.

## Milestone 6: Additive Provider MVP

* Wrap or port OpenSCAD build flow.
* Generate STL and preview artifacts.
* Preserve structural review block.
* Audit output bundle.

## Milestone 7: Laser Provider MVP

* Wrap or port laser build flow.
* Generate SVG, preview, G-code, operation artifacts, setup docs.
* Preserve machine/material profile semantics.
* Audit output bundle.

## Milestone 8: STEP Provider MVP

* Add build123d/STEP provider wrapper.
* Generate STEP, STL, GLB or preview where available.
* Record CAD measurements and source provenance.
* Add STEP artifacts to output README.

## Milestone 9: Purchased Component MVP

* Add component catalog schema.
* Add project component instance schema.
* Add MG996R servo reference profile.
* Add fastener, fan, switch, bearing, and heat-set insert examples.
* Generate purchased parts section in output README.
* Add servo horn receiver coupon example.
* Add component validation tests.

## Milestone 10: Hybrid Project MVP

Create one non-Lovelace hybrid example:

```text
hybrid_electronics_enclosure
  printed fan duct
  laser-cut front panel
  engraved labels
  purchased M3 screws
  purchased 40mm fan
  purchased toggle switch
  STEP assembly preview
  output README
```

This proves FabLab is general and not just a Lovelace-specific refactor.

## Milestone 11: Lovelace Pilot

Create a Lovelace hybrid primitive:

```text
lovelace_power_extender
  printed cube shell
  laser-cut gear layer
  purchased fasteners/axles
  STEP assembly
  mechanism validation
  output README
```

## Milestone 12: Servo/Pan-Tilt Regression Pilot

Create a servo-based regression example:

```text
servo_pan_tilt_coupon
  MG996R component profile
  servo body mount
  horn receiver coupon
  center screw access check
  horn sweep check
  wire relief check
  output README
```

This test must prevent FabLab from repeating the prior failure mode where a design uses plausible but physically wrong servo geometry.

## Milestone 13: Temporary Assimilation Repo Retirement

* Migrate representative `vibe-modeling` designs.
* Migrate representative `vibe-cutting` designs.
* Migrate or reimplement the useful `text-to-cad` patterns.
* Compare outputs and capability parity.
* Confirm permanent provider/reference submodules remain independently documented.
* Confirm provider wrappers do not rely on temporary assimilation repos.
* Remove only:

  * `third_party/vibe-modeling`
  * `third_party/vibe-cutting`
  * `third_party/text-to-cad`
* Keep permanent provider/reference submodules.
* Document retirement decision and user approval.

---

# 17. Acceptance Criteria

FabLab is successful when a user can say:

```text
I want to build a modular enclosure for these compute boards with ventilation,
labeled switches, removable panels, and future robot mounting points.
```

And the agent can produce:

1. A project brief.
2. A part graph.
3. A component manifest.
4. A process recommendation report.
5. A user-approvable process plan.
6. A selected material/tool plan.
7. Generated artifacts for each selected process.
8. A validation summary.
9. A BOM.
10. A purchased-parts report.
11. A self-documenting output folder.
12. A README explaining how to fabricate and assemble everything.

The final output should clearly state which pieces are ready to fabricate, which are calibration-only, which need human verification, which purchased components need measurement, and which assumptions were made.

## 17.1 Third-party classification acceptance

FabLab is not aligned unless it can clearly answer:

```text
Which third_party repos are temporary assimilation sources?
Which third_party repos are permanent provider/reference capabilities?
Which providers are executable?
Which providers are reference-only?
Which providers are inspection-only?
Which outputs are source geometry?
Which outputs are authoritative fabrication artifacts?
Which validation gates promote helper output into a build bundle?
Which temporary repos can be removed?
Which permanent provider submodules must remain?
```

Required acceptance test:

```text
test_third_party_classification.py
```

This test should fail if:

* `vibe-modeling`, `vibe-cutting`, or `text-to-cad` are not marked temporary.
* Boxes.py, LaserGRBL, CadQuery, CQ_Gears, BOSL2, FreeCAD Gears, `step.parts`, or CAD viewer tooling are incorrectly marked temporary.
* a permanent provider lacks documentation.
* an executable provider lacks an adapter or explicit reason for no adapter.
* a reference-only provider is imported or linked into FabLab runtime.
* helper output is treated as fabrication-ready without FabLab validation.
* retirement criteria remove permanent provider submodules.

## 17.2 Purchased-part acceptance

FabLab is not aligned unless it can:

* represent purchased components as first-class project objects
* classify component fit risk
* record component provenance
* generate component manifests
* generate BOM rows
* identify required measurements
* generate calibration coupons when needed
* block fabrication-ready claims for unverified high-risk component interfaces
* explain purchased parts in the output README

Required acceptance test:

```text
test_purchased_part_interfaces.py
```

This test should use at least:

```text
M3 screws
MG996R servo
40mm fan
toggle switch
heat-set insert
bearing or shaft
```

The test must confirm that FabLab produces:

```text
component instances
BOM rows
critical dimensions
fit-risk classifications
validation requirements
output README purchased-parts section
```

## 17.3 Servo regression acceptance

FabLab must include a regression test based on an MG996R pan/tilt scenario.

Required acceptance test:

```text
test_servo_integration_contract.py
```

The test must fail if the generated or planned design:

```text
centers the shaft in the servo body
omits wire relief
blocks horn sweep
blocks center screw access
uses a printed spline by default
omits component provenance
omits test coupon requirement
claims fabrication-ready without physical verification
```

---

# 18. Long-Term Vision

FabLab should become a general-purpose agentic fabrication operating system.

It should support projects like:

* Lovelace mechanical computing blocks
* cyberdeck enclosures
* portable inference clusters
* community garden signage and tool systems
* laser-cut tokens and badges
* robot chassis modules
* pan/tilt camera domes
* weather station enclosures
* antenna mounts
* mechanical linkages
* furniture-scale flat-pack designs
* hybrid printed/laser-cut educational kits
* servo-driven camera/sensor modules
* mixed purchased/fabricated assemblies

The goal is not to force every project into one CAD tool or one manufacturing process.

The goal is to let the agent reason across tools and processes, recommend an appropriate fabrication strategy, and produce the right artifacts with explicit validation and documentation.

FabLab should eventually make this workflow normal:

```text
conversation
  -> project brief
  -> part graph
  -> component manifest
  -> process/material recommendations
  -> user approval
  -> provider generation
  -> validation
  -> output bundle
  -> fabricate
  -> assemble
  -> test
  -> revise
```

The final system should feel like talking to a careful fabrication collaborator: one that understands CAD, CAM, materials, third-party tools, purchased components, machine limitations, safety, assembly, documentation, and revision control.

FabLab’s core principle is:

> A fabrication project is not a set of generated files. It is a set of functional parts, real components, interfaces, materials, processes, validation gates, provenance records, and assembly instructions.

The agent’s job is not merely to draw parts.

The agent’s job is to preserve the truth of the project across conversation, design, purchased components, fabrication processes, generated artifacts, validation, and physical assembly.
