# FabLab Roadmap

This roadmap turns the current README into phased execution plans with explicit exit gates. Its purpose is to get FabLab from the initial repository shell to a complete replacement for the separate `vibe-modeling` and `vibe-cutting` repositories, while preserving permanent third-party provider capabilities under documented FabLab boundaries.

The temporary assimilation repositories are:

- `third_party/vibe-modeling`
- `third_party/vibe-cutting`
- `third_party/text-to-cad`

The first two are the prior user repositories FabLab must replace directly. `text-to-cad` is also temporary under the README contract and should be removed once its useful STEP-first, viewer, projection, and component-source patterns have been assimilated or wrapped through permanent providers.

Permanent provider/reference submodules, such as Boxes.py, LaserGRBL, CadQuery, CQ_Gears, BOSL2, FreeCAD Gears, `step.parts`, and CAD viewer tooling, are not retirement targets. They remain as long-term capabilities when they have FabLab-owned docs, manifests, setup paths, and validation gates.

## Checkbox Legend

- `[ ]` Planned or not started.
- `[x]` Complete in the current repository state.
- `[?]` Needs validation before it can be marked complete.
- `[-]` Intentionally closed, deferred, or superseded.

## Completion Definition

FabLab is complete enough to retire the temporary assimilation repos when it can do all of the following without depending on `third_party/vibe-modeling`, `third_party/vibe-cutting`, or `third_party/text-to-cad` at runtime:

- [ ] Start a fabrication project from a high-level conversation or brief.
- [ ] Decompose the project into parts, interfaces, purchased components, and assemblies.
- [ ] Recommend processes, materials, tools, providers, and calibration coupons.
- [ ] Wait for approval before manufacturing artifact generation unless explicitly authorized.
- [ ] Generate additive artifacts with OpenSCAD-compatible revision, preview, manifest, and structural-review parity.
- [ ] Generate subtractive/laser artifacts with SVG, preview PNG, GRBL G-code, operation-stage G-code, machine/material profiles, and laser validation parity.
- [ ] Generate STEP-first and assembly-aware CAD artifacts where appropriate.
- [ ] Represent purchased parts as binding component constraints with provenance, status, measurements, fit risk, and validation rules.
- [ ] Route permanent third-party helpers through provider boundaries instead of treating them as authorities.
- [ ] Produce complete output bundles with READMEs, manifests, BOMs, validation summaries, assembly guides, setup docs, provenance, previews, and calibration artifacts.
- [ ] Audit generated bundles and clearly distinguish proposed, selected, generated, previewed, validated, calibration-only, fabrication-ready, and physically verified states.
- [ ] Migrate representative legacy projects from both prior user repos and demonstrate equal or better outputs.
- [ ] Document capability parity and obtain explicit user approval for temporary submodule removal.

## Gate Levels

Each phase has an exit gate. A gate is not passed because files exist; it is passed when the listed evidence is present and reviewable.

- **Documented**: design decisions, contracts, and boundaries are written down in the repo.
- **Modeled**: schemas and manifests can represent the required concepts.
- **Executable**: commands or scripts can run the workflow on fixtures or examples.
- **Validated**: tests, smoke checks, audits, or generated reports prove the workflow behaves as intended.
- **Migrated**: legacy examples or capabilities have FabLab-native equivalents.
- **Approved**: the user has reviewed the evidence and accepted the phase result.


## Phase 0: Repository Bootstrap

Goal: Establish the repo as a plan-governed FabLab host with the initial submodules and a shared execution roadmap.

Current status: complete from the initial bootstrap checkpoint.

Work packages:

- [x] Add the `agents` framework at `./agents`.
- [x] Add temporary assimilation submodules under `third_party/`.
- [x] Add inherited permanent provider/reference submodules already present in `vibe-cutting`.
- [x] Copy host-managed framework playbooks, references, templates, scripts, and shim files.
- [x] Create plan, journal, kanban, and downtime report directories.
- [x] Create this roadmap.

Exit gate:

- [x] `AGENTS.md` and runtime shims point agents to `./agents/RULES.md`.
- [x] `plans/`, `journal/`, `kanban/`, and `downtime/reports/` exist.
- [x] `.gitmodules` contains the initial temporary assimilation submodules and inherited provider/reference submodules.
- [x] Plan indexes verify with `python3 agents/scripts/regenerate_plan_indexes.py --check --repo-root .`.
- [x] The initial bootstrap checkpoint is staged or committed.

## Phase 1: Third-Party Inventory And Governance

Goal: Make every third-party repository explicit, classified, licensed, and bounded before any deeper migration work relies on it.

Work packages:

- [x] Add missing README-listed permanent provider/reference submodules that are not present yet:
- [x] `third_party/step.parts`
- [x] `third_party/cad-viewer`
- [x] Create `docs/third-party-submodules.md`.
- [x] Create `docs/temporary-assimilation-repos.md`.
- [x] Create `docs/permanent-provider-submodules.md`.
- [x] Create `docs/assimilation/migration-parity-matrix.md`.
- [x] Create `docs/assimilation/third-party-license-boundaries.md`.
- [x] Create `provider_versions.json`.
- [x] Create an initial root `build_manifest.json` for repository/toolchain provenance.
- [x] Create `tool_adapters/*.json` stubs for each permanent provider/reference that will be wrapped, inspected, or invoked.
- [x] Record for every submodule:
- [x] upstream URL
- [x] local path
- [x] pinned commit
- [x] classification
- [x] role
- [x] license boundary
- [x] invocation mode
- [x] whether outputs are source geometry, inspection artifacts, previews, machine code, component models, or reference-only
- [x] retirement status, if temporary

Exit gate:

- [x] Every `third_party/` submodule is classified using the README-approved classification values.
- [x] Temporary assimilation repos are documented separately from permanent provider/reference repos.
- [x] Permanent helpers have at least stub provider manifests and docs placeholders.
- [x] License and import boundaries are documented well enough that agents know what not to copy into FabLab core.
- [x] A classification check command or script exists, even if initially simple.

## Phase 2: Assimilation Audit And Parity Matrix

Goal: Inventory what must be absorbed from `vibe-modeling`, `vibe-cutting`, and `text-to-cad` before implementation begins in earnest.

Work packages:

- [x] Read and summarize each temporary repo's README, agent instructions, docs, scripts, tests, schemas, examples, and playbooks.
- [x] Create `docs/assimilation/vibe-modeling-assimilation.md`.
- [x] Create `docs/assimilation/vibe-cutting-assimilation.md`.
- [x] Create `docs/assimilation/text-to-cad-assimilation.md`.
- [x] Expand `docs/assimilation/migration-parity-matrix.md` into a checklist of capabilities, source locations, FabLab destination paths, tests, and retirement evidence.
- [x] Identify reusable docs/playbooks to migrate into FabLab-native files.
- [x] Identify scripts to port, wrap, or replace.
- [x] Identify examples that will become parity fixtures.
- [x] Identify internal third-party dependencies that should become permanent providers, references, or rejected-with-rationale entries.
- [x] Mark all temporary-repo runtime dependencies as migration debt.

Exit gate:

- [x] Each temporary repo has an assimilation report.
- [x] Every README-required capability is mapped to one of:
- [x] implemented
- [x] planned FabLab-native implementation
- [x] permanent provider boundary
- [x] reference-only
- [x] rejected with rationale
- [x] blocked
- [x] Representative legacy projects are selected for migration tests.
- [x] The parity matrix names the evidence required to retire `vibe-modeling` and `vibe-cutting`.

## Phase 3: Core Data Model And Schemas

Goal: Define the stable contracts that every provider, validator, project workflow, and output bundle will use.

Work packages:

- [x] Create `schemas/` for:
- [x] project
- [x] project brief
- [x] part
- [x] part graph
- [x] interface
- [x] assembly graph
- [x] process recommendation
- [x] selected process plan
- [x] material profile
- [x] machine profile
- [x] provider
- [x] artifact manifest
- [x] build manifest
- [x] validation report
- [x] output README contract
- [x] BOM
- [x] component catalog entry
- [x] component instance
- [x] component measurement
- [x] servo profile
- [x] test coupon
- [x] assimilation report
- [x] third-party module
- [x] Create docs for:
- [x] `docs/architecture.md`
- [x] `docs/provider-contract.md`
- [x] `docs/validation-contract.md`
- [x] `docs/output-bundle-contract.md`
- [x] `docs/purchased-parts-contract.md`
- [x] `docs/servo-integration-contract.md`
- [x] Define status vocabularies for:
- [x] component status
- [x] artifact type
- [x] validation result
- [x] readiness state
- [x] provider classification
- [x] selected vs recommended process state
- [x] Add schema validation tests.

Exit gate:

- [x] The README's key artifacts can be represented by schemas.
- [x] Example JSON fixtures validate for project, part graph, process plan, provider manifest, component manifest, validation report, artifact manifest, and output bundle.
- [x] The readiness-state vocabulary prevents generated files from being called fabrication-ready without the required evidence.

## Phase 4: Command Model, Bootstrap, And Runtime Skeleton

Goal: Create the executable spine of FabLab before porting full generation behavior.

Work packages:

- [x] Create `setup/bootstrap.sh`, `setup/bootstrap.ps1`, and bootstrap/toolchain manifests.
- [x] Create `scripts/fablab.py` with subcommands:
- [x] `new`
- [x] `brief`
- [x] `decompose`
- [x] `recommend`
- [x] `plan`
- [x] `build`
- [x] `audit`
- [x] `output-readme`
- [x] `components`
- [x] Create `scripts/provider_tool.py` with subcommands:
- [x] `list`
- [x] `validate`
- [x] `check`
- [x] `setup`
- [x] `run`
- [x] Create `scripts/classify_third_party.py`.
- [x] Create `scripts/validate_project.py`.
- [x] Create `scripts/validate_components.py`.
- [x] Create `scripts/generate_output_readme.py`.
- [x] Establish logging, deterministic output paths, dry-run behavior, and audit-only modes.
- [x] Ensure generated caches and runtime state stay outside committed source.

Exit gate:

- [x] `setup/bootstrap.sh doctor` or equivalent reports the repo's basic readiness.
- [x] `scripts/fablab.py new --project <example>` creates a valid project skeleton.
- [x] `scripts/provider_tool.py list` reads provider manifests.
- [x] `scripts/classify_third_party.py check` verifies submodule classifications.
- [x] Tests cover command parsing, schema validation, and failure behavior for missing providers.

## Phase 5: Contract Review And Schema Hardening

Goal: Turn first-pass Phase 3 schemas and contracts into reviewed, dependable foundations before real generator work depends on them.

Work packages:

- [ ] Review all first-pass schemas against the README artifact list and assimilation reports.
- [ ] Decide which schemas are stable enough for Phase 9 implementation and which remain draft.
- [ ] Expand schemas beyond top-level smoke fields where downstream code needs stronger validation.
- [ ] Add explicit schema examples for output bundles, process plans, component manifests, servo profiles, provider manifests, and validation reports.
- [ ] Document schema versioning rules and backward-compatibility expectations.
- [ ] Create a schema change checklist for future agents.
- [ ] Update `docs/architecture.md`, `docs/provider-contract.md`, and `docs/validation-contract.md` with any reviewed schema decisions.

Exit gate:

- [ ] Schema review decisions are recorded in `docs/decisions/`.
- [ ] Required Phase 9 schemas are marked stable enough for implementation.
- [ ] Fixture validation covers every schema that Phase 5 will consume.
- [ ] Remaining schema uncertainty is listed as explicit follow-up work.

## Phase 6: Validation Tooling And Dependency Policy

Goal: Decide and implement the validation/dependency path that replaces the first-pass standard-library smoke checks when stronger validation is needed.

Work packages:

- [ ] Decide whether to adopt a JSON Schema validator dependency.
- [ ] Define where Python dependencies are declared and how bootstrap installs them.
- [ ] Implement dependency-backed schema validation if approved.
- [ ] Keep a no-download fallback path for basic local checks.
- [ ] Update `setup/bootstrap.sh` and `setup/bootstrap.ps1` to reflect the accepted dependency policy.
- [ ] Add validation tests for invalid fixtures, not only happy-path fixtures.

Exit gate:

- [ ] Dependency policy is recorded in `docs/decisions/`.
- [ ] Bootstrap behavior is explicit about local-only checks versus downloads.
- [ ] Schema validation catches both valid and invalid fixtures.
- [ ] Verification works on a clean checkout without hidden global dependencies.

## Phase 7: License Verification And Provider Risk Review

Goal: Resolve unknown license/provenance boundaries before provider execution or code reuse expands.

Work packages:

- [ ] Verify the `cad-viewer` upstream license and update its classification from `review_required` when resolved.
- [ ] Review each permanent provider license file and summarize allowed use, import, subprocess, and generated-output implications.
- [ ] Add rejected-with-rationale entries for any provider behavior that should not be used.
- [ ] Update `docs/assimilation/third-party-license-boundaries.md`.
- [ ] Update each affected `tool_adapters/*.json` license boundary.
- [ ] Add a license-boundary check to `scripts/classify_third_party.py` or a dedicated script.

Exit gate:

- [ ] No provider has an unexplained license boundary.
- [ ] `cad-viewer` is either verified or explicitly blocked with rationale.
- [ ] Agents can tell whether a provider may be imported, invoked, referenced, or only inspected.

## Phase 8: Safe Provider Execution Enablement

Goal: Turn disabled provider setup/run placeholders into reviewed provider-specific setup, check, and smoke workflows without granting blanket execution authority.

Work packages:

- [ ] Define provider setup/check/smoke command schema fields.
- [ ] Add reviewed safe `check_command` values for providers that can be checked locally.
- [ ] Add setup scripts under `setup/tools/` one provider at a time.
- [ ] Implement `scripts/provider_tool.py check <provider>` for manifest-declared safe checks.
- [ ] Keep `setup` and `run` disabled for providers without explicit reviewed commands.
- [ ] Add provider smoke tests that produce provenance-only outputs in temporary directories.
- [ ] Ensure provider smoke outputs are never described as fabrication-ready.

Exit gate:

- [ ] At least one provider has a reviewed safe check command and smoke test.
- [ ] Provider commands fail closed when manifests omit safe commands.
- [ ] Runtime state and smoke outputs stay outside committed source.
- [ ] Provider execution policy is documented in `docs/provider-contract.md`.

## Phase 9: Additive Parity With `vibe-modeling`

Goal: Replace the additive/OpenSCAD workflow with FabLab-native project structure, commands, playbooks, and validation.

Work packages:

- [ ] Create `providers/openscad/`.
- [ ] Create `tool_adapters/openscad.json`.
- [ ] Create `docs/tools/openscad.md`.
- [ ] Create playbooks:
- [ ] `playbooks/how_to_author_additive_parts.md`
- [ ] `playbooks/how_to_validate_structural_parts.md`
- [ ] `playbooks/how_to_migrate_legacy_vibe_modeling_projects.md`
- [ ] Implement parameterized JSON config support.
- [ ] Implement numbered revisions and immutable revision snapshots.
- [ ] Generate STL artifacts.
- [ ] Generate 3MF artifacts where available.
- [ ] Generate multi-view PNG previews.
- [ ] Generate source/config provenance records.
- [ ] Generate build manifests and artifact manifests.
- [ ] Support multi-part design manifests.
- [ ] Implement structural join review, minimum wall thickness review, minimum internal material width review, and sectional inspection reports.
- [ ] Port servo design references and servo-receiver rules into FabLab docs and component contracts.
- [ ] Add migration support in `scripts/migrate_vibe_modeling.py`.
- [ ] Migrate at least one representative `vibe-modeling` project into `projects/examples/`.

Exit gate:

- [ ] A migrated additive example can be built from FabLab commands without reading runtime code from `third_party/vibe-modeling`.
- [ ] The output contains STL, optional 3MF, previews, manifests, source/config provenance, and an output README.
- [ ] Structural review output exists and uses FabLab readiness language.
- [ ] Revision behavior is immutable and auditable.
- [ ] The parity matrix marks additive workflow parity as passed or names remaining gaps with owners.

## Phase 10: Subtractive And Laser Parity With `vibe-cutting`

Goal: Replace the laser/subtractive workflow with FabLab-native providers, profiles, validators, and output bundles.

Work packages:

- [ ] Create `providers/native_vector/`.
- [ ] Create `providers/laser_grbl/` or a reference/operator boundary for LaserGRBL.
- [ ] Create `tool_adapters/native_vector.json`.
- [ ] Create docs:
- [ ] `docs/tools/lasergrbl.md`
- [ ] `docs/process-selection.md`
- [ ] `docs/material-selection.md`
- [ ] Create playbooks:
- [ ] `playbooks/how_to_author_laser_cut_parts.md`
- [ ] `playbooks/how_to_validate_laser_jobs.md`
- [ ] `playbooks/how_to_migrate_legacy_vibe_cutting_projects.md`
- [ ] Implement laser design configs.
- [ ] Implement machine profiles and material profiles.
- [ ] Generate SVG output.
- [ ] Generate preview PNG output.
- [ ] Generate GRBL G-code output.
- [ ] Generate operation-stage G-code.
- [ ] Generate material setup docs and safety notes.
- [ ] Preserve pass-aware operation artifacts.
- [ ] Implement bounds validation.
- [ ] Implement engraving containment checks.
- [ ] Implement duplicate-cut and overburn checks.
- [ ] Implement host-owned mechanism validation:
- [ ] gear mesh
- [ ] stackup
- [ ] channel/phase
- [ ] rotating clearance
- [ ] registration
- [ ] Add migration support in `scripts/migrate_vibe_cutting.py`.
- [ ] Migrate at least one representative `vibe-cutting` project into `projects/examples/`.

Exit gate:

- [ ] A migrated laser example can be built from FabLab commands without reading runtime code from `third_party/vibe-cutting`.
- [ ] The output contains SVG, preview PNG, G-code, operation-stage artifacts, profiles, manifests, setup docs, validation reports, and an output README.
- [ ] Machine/material readiness is separate from file-generation success.
- [ ] Mechanism validation is host-owned and does not delegate readiness claims to helper repos.
- [ ] The parity matrix marks subtractive workflow parity as passed or names remaining gaps with owners.

## Phase 11: Permanent Provider Boundaries

Goal: Make permanent helpers usable through FabLab-owned manifests, docs, setup paths, smoke checks, and validation rules.

Work packages:

- [ ] Create provider docs and adapters for:
- [ ] Boxes.py
- [ ] CadQuery
- [ ] CQ_Gears
- [ ] BOSL2
- [ ] FreeCAD Gears
- [ ] `step.parts`
- [ ] CAD viewer tooling
- [ ] LaserGRBL reference workflow
- [ ] Create setup/check scripts under `setup/tools/` where executable setup is appropriate.
- [ ] Create provider-specific tests or smoke checks for executable providers.
- [ ] Define for each provider:
- [ ] allowed invocation mode
- [ ] forbidden import/copy behavior
- [ ] license boundary
- [ ] output authority
- [ ] expected outputs
- [ ] untrusted provenance outputs
- [ ] validation gates
- [ ] safe failure behavior
- [ ] Implement provider setup/check/run routing in `scripts/provider_tool.py`.
- [ ] Ensure provider output can be included in artifact manifests without being treated as automatically fabrication-ready.

Exit gate:

- [ ] `scripts/provider_tool.py validate` passes for every provider manifest.
- [ ] Executable providers have check or smoke commands.
- [ ] Reference-only providers clearly cannot be invoked as authoritative generators.
- [ ] Generated helper output is tracked as source/provenance unless FabLab validation promotes it.
- [ ] Provider docs are complete enough for agents to choose the correct helper and explain its limits in output READMEs.

## Phase 12: Hybrid Planning, STEP, And Component Truth Layer

Goal: Build the new FabLab-specific capability layer that neither legacy repo fully provides alone.

Work packages:

- [ ] Create playbooks:
- [ ] `playbooks/how_to_start_a_new_fabrication_project.md`
- [ ] `playbooks/how_to_decompose_a_project_into_parts.md`
- [ ] `playbooks/how_to_recommend_materials_and_processes.md`
- [ ] `playbooks/how_to_prepare_a_process_plan_for_approval.md`
- [ ] `playbooks/how_to_author_step_assemblies.md`
- [ ] `playbooks/how_to_author_hybrid_assemblies.md`
- [ ] `playbooks/how_to_define_a_purchased_part.md`
- [ ] `playbooks/how_to_design_with_servos.md`
- [ ] `playbooks/how_to_validate_purchased_part_interfaces.md`
- [ ] Implement project intake artifacts:
- [ ] `project_brief.md`
- [ ] `constraints.md`
- [ ] `known_inputs.md`
- [ ] `open_questions.md`
- [ ] `decision_log.md`
- [ ] Implement functional decomposition artifacts:
- [ ] `part_graph.json`
- [ ] `interfaces.json`
- [ ] `assembly_graph.json`
- [ ] `component_manifest.json`
- [ ] Implement process/material/tool recommendation artifacts.
- [ ] Implement deterministic process scoring from the README rubric.
- [ ] Implement selected vs recommended tracking.
- [ ] Add `catalogs/materials/`, `catalogs/machines/`, and `catalogs/components/`.
- [ ] Add the default MG996R servo profile.
- [ ] Implement component status, provenance, measurement, substitution, and fit-risk fields.
- [ ] Implement STEP-first assembly patterns using FabLab-owned provider boundaries.
- [ ] Assimilate useful `text-to-cad` patterns into docs, providers, and examples.
- [ ] Add component validation and servo validation reports.

Exit gate:

- [ ] A hybrid example can be decomposed into parts, interfaces, process recommendations, purchased components, and selected process plans.
- [ ] The agent workflow blocks artifact generation until approval unless immediate generation is explicitly authorized.
- [ ] Purchased parts with unverified dimensions block fabrication-ready claims for dependent high-risk interfaces.
- [ ] Servo integration checks verify shaft offset, horn sweep, center screw access, wire relief, and service/removal path.
- [ ] Useful `text-to-cad` patterns are represented in FabLab-native docs/providers, not as a runtime dependency.

## Phase 13: Output Bundle, Audit, And Documentation Generation

Goal: Produce complete, self-documenting fabrication packages that can be reviewed by a human before fabrication.

Work packages:

- [ ] Implement `scripts/build_bundle.py`.
- [ ] Implement `scripts/audit_bundle.py`.
- [ ] Implement output README generation from manifests, validation reports, BOMs, components, and process plans.
- [ ] Create `playbooks/how_to_generate_approved_fabrication_artifacts.md`.
- [ ] Create `playbooks/how_to_build_and_audit_a_fabrication_bundle.md`.
- [ ] Create `playbooks/how_to_create_output_readmes.md`.
- [ ] Ensure output bundles include:
- [ ] `README.md`
- [ ] `build_manifest.json`
- [ ] `artifact_manifest.json`
- [ ] `process_plan.json`
- [ ] `process_recommendations.md`
- [ ] `material_setup.md`
- [ ] `tool_setup.md`
- [ ] `assembly_guide.md`
- [ ] `validation_summary.md`
- [ ] `bom.csv`
- [ ] previews
- [ ] CAD files
- [ ] print files
- [ ] laser files
- [ ] G-code
- [ ] source geometry
- [ ] operation artifacts
- [ ] calibration artifacts
- [ ] purchased part docs
- [ ] third-party provenance
- [ ] Add audit checks for stale artifacts, missing artifacts, mismatched manifests, missing validation status, and missing provenance.
- [ ] Ensure output README language distinguishes unverified, calibration-only, and fabrication-ready states.

Exit gate:

- [ ] Every generated example output bundle passes `audit_bundle`.
- [ ] Output READMEs explain every file, every process, every purchased part, validation status, fabrication sequence, assembly sequence, calibration needs, and safety limits.
- [ ] Build manifests and artifact manifests are deterministic enough for review and regression tests.
- [ ] No generated bundle claims fabrication readiness unless the required validation evidence is present.

## Phase 14: Migration Fixtures And Parity Demonstration

Goal: Prove FabLab can replace the old repos by migrating real examples and comparing outputs, docs, and behavior.

Work packages:

- [ ] Select additive parity fixtures from `vibe-modeling`.
- [ ] Select laser/subtractive parity fixtures from `vibe-cutting`.
- [ ] Select STEP/hybrid/component fixtures from `text-to-cad` patterns or new FabLab examples.
- [ ] Create examples under `projects/examples/`, including:
- [ ] an additive/OpenSCAD project
- [ ] a laser-cut project
- [ ] a mechanism or gear project
- [ ] a servo integration/test coupon project
- [ ] a mixed print-and-laser enclosure
- [ ] a purchased-component-heavy project
- [ ] a STEP-first assembly project
- [ ] Run migration scripts and record source references.
- [ ] Build and audit all examples.
- [ ] Update the parity matrix with evidence paths.
- [ ] Document any intentionally rejected or changed behavior.

Exit gate:

- [ ] Representative legacy projects build successfully in FabLab.
- [ ] Output bundles pass audit.
- [ ] Existing major workflows have FabLab-native equivalents.
- [ ] Agent playbooks cover the new workflows.
- [ ] Output READMEs are complete.
- [ ] Third-party provider submodules from the old repos have been brought over or rejected with rationale.
- [ ] Provider docs and tool adapters exist for permanent helpers.
- [ ] License boundaries are documented.
- [ ] Purchased-part/component contracts exist.
- [ ] Servo integration safeguards are tested.
- [ ] The user can review a single parity matrix and see the status of every README-required capability.

## Phase 15: Temporary Repo Retirement

Goal: Remove temporary assimilation submodules only after parity is demonstrated and approved.

Work packages:

- [ ] Search for runtime references to:
- [ ] `third_party/vibe-modeling`
- [ ] `third_party/vibe-cutting`
- [ ] `third_party/text-to-cad`
- [ ] Replace remaining runtime references with FabLab-native paths, provider manifests, or docs links.
- [ ] Keep historical source references in assimilation docs only where useful.
- [ ] Run all tests, smoke checks, provider checks, example builds, and bundle audits.
- [ ] Update docs to state that the temporary repos have been retired.
- [ ] Remove temporary submodules from `.gitmodules`.
- [ ] Remove temporary submodule directories.
- [ ] Regenerate provider versions and third-party classification docs.
- [ ] Request explicit user approval before the removal commit.

Exit gate:

- [ ] No FabLab runtime command depends on a temporary assimilation repo.
- [ ] No provider manifest points to a temporary assimilation repo as an executable dependency.
- [ ] No playbook instructs agents to use temporary repo files for normal project execution.
- [ ] The parity matrix is complete and approved.
- [ ] The user approves removal.
- [ ] `third_party/vibe-modeling`, `third_party/vibe-cutting`, and `third_party/text-to-cad` are removed while permanent provider/reference submodules remain.

## Phase 16: Post-Retirement Hardening

Goal: Stabilize FabLab after the temporary sources are gone.

Work packages:

- [ ] Run full verification on a fresh clone.
- [ ] Confirm submodule initialization only pulls permanent providers/references.
- [ ] Confirm examples still build and audit without temporary repos.
- [ ] Add regression tests for known failures from the old repos:
- [ ] weak structural joins
- [ ] thin internal material
- [ ] stale revision artifacts
- [ ] unsafe laser readiness claims
- [ ] missing operation-stage artifacts
- [ ] duplicate cut paths
- [ ] unverified servo geometry
- [ ] unmeasured purchased-part interfaces
- [ ] incomplete output READMEs
- [ ] Update `README.md` if the project spec has moved from initial spec to implemented architecture.
- [ ] Create a release/checkpoint tag or milestone commit if desired.

Exit gate:

- [ ] A fresh clone can bootstrap, check providers, run tests, build examples, and audit outputs without temporary repos.
- [ ] The README and ROADMAP agree about the implemented architecture and remaining future work.
- [ ] Regression tests cover the critical lessons learned during assimilation.

## Cross-Phase Workstreams

These workstreams run throughout multiple phases and should be tracked in plans as they become active.


### Documentation

- [ ] Keep README, ROADMAP, docs, playbooks, and provider references consistent.
- [ ] Record adopted and rejected behavior in assimilation reports.
- [ ] Prefer FabLab-native docs over links into temporary repos.

### Testing

- [ ] Add tests when schemas, command behavior, provider routing, validation logic, migration scripts, or output contracts are introduced.
- [ ] Treat examples as regression fixtures once migrated.
- [ ] Keep smoke tests lightweight enough for frequent agent use.

### Safety And Readiness Language

- [ ] Never equate generated files with fabrication readiness.
- [ ] Require validation evidence before readiness claims.
- [ ] Preserve the distinction between helper provenance and FabLab-owned readiness.
- [ ] Put machine, material, calibration, ventilation, and supervision caveats into output READMEs.

### Component Truth

- [ ] Prefer manufacturer drawings, measured dimensions, known STEP models, or test coupons over guessed dimensions.
- [ ] Block fabrication-ready claims for high-risk unmeasured purchased-part interfaces.
- [ ] Treat servos as a special high-risk component family with explicit shaft, horn, wire, screw, and service constraints.

### Provider Governance

- [ ] Every permanent provider/reference needs a manifest, docs, classification, license boundary, and validation statement.
- [ ] Helper repos may produce useful geometry or inspection artifacts, but FabLab owns project planning, final manifests, validation, and readiness language.

## Suggested Milestones


Milestone 1: governed repository baseline.

- [x] Phases 0 and 1 complete.
- [x] All submodules classified.
- [x] Missing permanent providers added.
- [x] Provider manifest stubs exist.

Milestone 2: assimilation plan complete.

- [x] Phase 2 complete.
- [x] Parity matrix covers every README-required capability.
- [x] Migration fixtures selected.

Milestone 3: executable skeleton.

- [x] Phases 3 and 4 first-pass skeleton complete.
- [x] Schemas, commands, bootstrap, provider listing, and validation scaffolding work.

Milestone 4: reviewed contracts and safe providers.

- [ ] Phases 5, 6, 7, and 8 complete.
- [ ] Schema contracts are reviewed and stable enough for additive parity work.
- [ ] Dependency and bootstrap policy is accepted and implemented.
- [ ] Provider license boundaries and safe execution checks are resolved.

Milestone 5: legacy parity.

- [ ] Phases 9 and 10 complete.
- [ ] Additive and subtractive examples build under FabLab.

Milestone 6: hybrid FabLab.

- [ ] Phases 11, 12, and 13 complete.
- [ ] Permanent providers, components, STEP/hybrid planning, validation, and output bundles work together.

Milestone 7: retirement approval.

- [ ] Phase 14 complete.
- [ ] The parity matrix proves replacement readiness.
- [ ] User approves temporary repo removal.

Milestone 8: clean FabLab.

- [ ] Phases 15 and 16 complete.
- [ ] Temporary repos are gone.
- [ ] Permanent providers remain.
- [ ] Fresh clone verification passes.
