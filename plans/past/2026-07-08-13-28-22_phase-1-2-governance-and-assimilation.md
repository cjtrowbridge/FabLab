---
plan_id: 2026-07-08-13-28-22_phase-1-2-governance-and-assimilation
title: Phase 1-4 Governance Assimilation And Skeleton
summary: Execute Roadmap Phase 1 and Phase 2 fully, then complete a bounded first pass through most Phase 3 schemas and Phase 4 command/runtime skeleton work.
status: past
created_at: 2026-07-08-13-28-22
---

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

## Scope

This plan covers the consecutive work I can complete with high confidence before stopping for review of long-lived contracts:

- Roadmap Phase 1: Third-Party Inventory And Governance.
- Roadmap Phase 2: Assimilation Audit And Parity Matrix.
- Roadmap Phase 3: Core Data Model And Schemas, through a reviewable first-pass schema/doc set.
- Roadmap Phase 4: Command Model, Bootstrap, And Runtime Skeleton, through a lightweight non-provider-executing skeleton.

The plan intentionally stops before deep provider execution, generated fabrication artifacts, or irreversible schema lock-in. Phase 3 and Phase 4 outputs should be treated as first-pass contracts and skeletons that are ready for user review before downstream phases depend on them.

## Execution Checklist

### Phase 1: Third-Party Inventory And Governance

- [x] Verify the currently staged bootstrap state and confirm no unrelated user changes are present.
- [x] Add the README-listed permanent provider/reference submodule `third_party/step.parts`, unless the upstream URL is unavailable or has changed.
- [x] Add the README-listed permanent provider/reference submodule `third_party/cad-viewer`, unless the upstream URL is unavailable or has changed.
- [x] Record any corrected upstream URLs in the relevant docs if either README-listed URL needs adjustment.
- [x] Create `docs/third-party-submodules.md` with every `third_party/` submodule, upstream URL, path, pinned commit, classification, role, and status.
- [x] Create `docs/temporary-assimilation-repos.md` documenting `vibe-modeling`, `vibe-cutting`, and `text-to-cad` as temporary assimilation sources.
- [x] Create `docs/permanent-provider-submodules.md` documenting permanent providers and references separately from temporary repos.
- [x] Create `docs/assimilation/third-party-license-boundaries.md` with initial license/import/copy boundaries for all third-party repos.
- [x] Create `docs/assimilation/migration-parity-matrix.md` with an initial README capability matrix.
- [x] Create `provider_versions.json` from the pinned submodule state.
- [x] Create root `build_manifest.json` for the repository bootstrap/toolchain provenance snapshot.
- [x] Create `tool_adapters/` manifest stubs for each permanent provider/reference that needs a FabLab boundary.
- [x] Create `scripts/classify_third_party.py` with a lightweight `list`, `check`, and `audit` interface.
- [x] Verify `scripts/classify_third_party.py check` passes against the docs/manifests created in this phase.
- [x] Update `ROADMAP.md` Phase 1 checkboxes as completed where the exit gate evidence exists.

### Phase 2: Assimilation Audit And Parity Matrix

- [x] Read the temporary repos' root READMEs and agent/runtime instruction files.
- [x] Inventory temporary repo docs, playbooks, schemas, scripts, tests, examples, and submodules.
- [x] Create `docs/assimilation/vibe-modeling-assimilation.md`.
- [x] Create `docs/assimilation/vibe-cutting-assimilation.md`.
- [x] Create `docs/assimilation/text-to-cad-assimilation.md`.
- [x] Expand `docs/assimilation/migration-parity-matrix.md` with source locations, FabLab target paths, implementation status, validation evidence, and retirement evidence.
- [x] Identify reusable docs/playbooks to migrate into FabLab-native files.
- [x] Identify scripts to port, wrap, replace, or reject with rationale.
- [x] Identify representative legacy examples that should become parity fixtures.
- [x] Identify internal third-party dependencies that should become permanent providers, references, or rejected-with-rationale entries.
- [x] Mark all temporary-repo runtime dependencies as migration debt.
- [x] Update `ROADMAP.md` Phase 2 checkboxes as completed where the exit gate evidence exists.

### Phase 3: Core Data Model And Schemas First Pass

- [x] Create `schemas/` if missing.
- [x] Create first-pass JSON schemas for project, project brief, part, part graph, interface, assembly graph, process recommendation, selected process plan, material profile, machine profile, provider, artifact manifest, build manifest, validation report, BOM, component catalog entry, component instance, component measurement, servo profile, test coupon, assimilation report, and third-party module.
- [x] Create `docs/architecture.md` describing the Phase 3 model boundaries and how schemas relate to README artifacts.
- [x] Create `docs/provider-contract.md` describing provider classifications, invocation modes, output authority, and readiness limitations.
- [x] Create `docs/validation-contract.md` describing validation domains, validation result states, and readiness claims.
- [x] Create `docs/output-bundle-contract.md` describing bundle structure, manifests, README requirements, and audit expectations.
- [x] Create `docs/purchased-parts-contract.md` describing component provenance, measurement status, fit risk, and BOM requirements.
- [x] Create `docs/servo-integration-contract.md` describing servo-specific shaft, horn, screw, wire, and service-path rules.
- [x] Define status vocabularies for component status, artifact type, validation result, readiness state, provider classification, and selected vs recommended process state.
- [x] Create representative schema fixtures under `tests/fixtures/` or `schemas/examples/`.
- [x] Add a lightweight schema validation test or script that can validate the representative fixtures using only available standard tooling where possible.
- [x] Update `ROADMAP.md` Phase 3 checkboxes as completed only where evidence exists.

### Phase 4: Command Model And Runtime Skeleton First Pass

- [x] Create `setup/` and `setup/tools/` if missing.
- [x] Create `setup/bootstrap.sh` with lightweight `doctor` and `run` entry points that do not download dependencies by default.
- [x] Create `setup/bootstrap.ps1` as a documented Windows placeholder or minimal equivalent.
- [x] Create `setup/toolchain-manifest.json` recording expected command/runtime assumptions.
- [x] Create `scripts/fablab.py` with subcommand parsing for `new`, `brief`, `decompose`, `recommend`, `plan`, `build`, `audit`, `output-readme`, and `components`.
- [x] Implement safe placeholder behavior for unimplemented `scripts/fablab.py` commands so they explain the missing implementation without producing fabrication artifacts.
- [x] Create `scripts/provider_tool.py` with `list`, `validate`, `check`, `setup`, and `run` subcommands.
- [x] Wire `scripts/provider_tool.py list` and `validate` to the Phase 1 adapter manifests.
- [x] Keep provider `setup` and `run` conservative: report unsupported/future provider execution unless a manifest explicitly declares a safe check command.
- [x] Create or update `scripts/validate_project.py` for schema/fixture validation.
- [x] Create or update `scripts/validate_components.py` for component-manifest placeholder validation.
- [x] Create `scripts/generate_output_readme.py` with a contract-aware placeholder or template generator that does not claim fabrication readiness.
- [x] Add basic tests for command parsing, provider manifest validation, missing-provider failure behavior, and schema fixture validation where feasible without additional dependencies.
- [x] Update `ROADMAP.md` Phase 4 checkboxes as completed only where evidence exists.

### Verification And Checkpoint

- [x] Run `python3 agents/scripts/regenerate_plan_indexes.py --repo-root .`.
- [x] Run `python3 agents/scripts/regenerate_plan_indexes.py --check --repo-root .`.
- [x] Run `python3 scripts/classify_third_party.py check`.
- [x] Run the Phase 3 schema/fixture validation command.
- [x] Run the Phase 4 command skeleton smoke checks.
- [x] Run `git diff --check`.
- [x] Run `git diff --cached --check` after staging.
- [x] Review `git status -sb`.
- [x] Update `journal/2026-07-08.md` with the Phase 1-4 checkpoint.
- [x] Stage all Phase 1-4 work for review.
- [x] Provide a completion summary with remaining risks, skipped items, and a suggested commit message.

## Exit Gates

Phase 1 is complete when:

- [x] Every `third_party/` submodule is classified using README-approved classification values.
- [x] Temporary assimilation repos are documented separately from permanent provider/reference repos.
- [x] Permanent helpers have at least stub provider manifests and docs placeholders.
- [x] License and import boundaries are documented well enough that agents know what not to copy into FabLab core.
- [x] A classification check command exists and passes.

Phase 2 is complete when:

- [x] Each temporary repo has an assimilation report.
- [x] Every README-required capability is mapped to an implementation disposition.
- [x] Representative legacy projects are selected for migration tests.
- [x] The parity matrix names the evidence required to retire `vibe-modeling` and `vibe-cutting`.
- [x] `text-to-cad` retirement evidence is also represented because the README classifies it as temporary.

Phase 3 first pass is complete when:

- [x] README-required core artifacts have first-pass schemas or documented schema placeholders.
- [x] Provider, validation, output bundle, purchased-part, and servo contracts exist as docs.
- [x] Status vocabularies are documented consistently across schemas/docs.
- [x] Representative fixtures exist and pass the lightweight validation command.
- [x] Any schema uncertainty is listed as a Phase 3 review item rather than silently frozen.

Phase 4 first pass is complete when:

- [x] Bootstrap scripts exist and default to local, non-downloading checks.
- [x] `scripts/fablab.py` exposes the README command surface with safe placeholder behavior.
- [x] `scripts/provider_tool.py` can list and validate provider manifests.
- [x] Provider setup/run behavior does not execute untrusted helpers unless explicitly supported by a manifest.
- [x] Basic command and manifest smoke checks pass.

## Decision Proposals

These are the proposed defaults I will use unless you amend the plan before execution.

### Repository Layout

- [x] **Proposal**: Keep all submodules directly under `third_party/`, matching the simpler README layout already used by the bootstrap.
- [x] **Rationale**: The repo already has direct `third_party/<name>` paths, and the README allows this layout as long as documentation prevents temporary/permanent confusion.
- [x] **Alternative**: Move to grouped paths such as `third_party/temporary/`, `third_party/providers/`, and `third_party/references/`.
- [x] **Default decision**: Use direct paths and make status explicit in docs/manifests.

### Missing Permanent Submodules

- [x] **Proposal**: Add `https://github.com/earthtojake/step.parts` at `third_party/step.parts`.
- [x] **Proposal**: Add `https://github.com/earthtojake/cad-viewer` at `third_party/cad-viewer`.
- [x] **Rationale**: Both are explicitly listed in the README as initial permanent provider/reference submodules.
- [x] **Default decision**: Add them unless `git submodule add` fails due to changed upstream location, in which case verify the URL before proceeding.

### Classification Source Of Truth

- [x] **Proposal**: Use `docs/third-party-submodules.md` as the human-readable index and `provider_versions.json` plus `tool_adapters/*.json` as machine-readable source data.
- [x] **Rationale**: The README requires all of these files; this split keeps docs useful for humans and scripts useful for checks.
- [x] **Alternative**: Make a single JSON registry the sole authority and generate docs from it later.
- [x] **Default decision**: Maintain both manually for now, with `scripts/classify_third_party.py check` verifying consistency.

### Provider Manifest Stub Depth

- [x] **Proposal**: Create lightweight adapter stubs with stable fields: `id`, `name`, `classification`, `upstream_url`, `submodule_path`, `invocation_mode`, `license_boundary`, `output_authority`, `expected_outputs`, `validation_required`, `setup_command`, `check_command`, and `notes`.
- [x] **Rationale**: Phase 1 should define boundaries without pretending executable setup is complete.
- [x] **Alternative**: Delay adapter files until provider implementation phases.
- [x] **Default decision**: Create stubs now and mark executable commands as `null` or `future`.

### License Boundaries

- [x] **Proposal**: Classify unknown or unreviewed licenses conservatively as `review_required` until the exact upstream license file is recorded.
- [x] **Rationale**: This avoids false confidence and protects FabLab core from accidental license contamination.
- [x] **Default decision**: Do not copy third-party implementation code into FabLab core during Phase 1-2.

### Assimilation Report Format

- [x] **Proposal**: Use one Markdown report per temporary repo with sections for source overview, inventory, capabilities, provider dependencies, migration targets, rejected items, risks, and parity evidence.
- [x] **Rationale**: Markdown is reviewable and easy to evolve before schemas are finalized in Phase 3.
- [x] **Default decision**: Keep reports human-readable and link into the parity matrix.

### Parity Matrix Format

- [x] **Proposal**: Use a Markdown table in `docs/assimilation/migration-parity-matrix.md` for Phase 2.
- [x] **Rationale**: It is easier to review and edit while the categories are still being discovered.
- [x] **Alternative**: Use JSON immediately.
- [x] **Default decision**: Markdown first; Phase 3 may introduce a schema-backed matrix if useful.

### Capability Dispositions

- [x] **Proposal**: Use these disposition values: `implemented`, `planned_fablab_native`, `permanent_provider_boundary`, `reference_only`, `rejected_with_rationale`, `blocked`, `migration_debt`.
- [x] **Rationale**: They map directly to README intent and roadmap language.
- [x] **Default decision**: Apply these values consistently across reports and the parity matrix.

### Example Fixture Selection

- [x] **Proposal**: Select examples by capability coverage rather than popularity or size.
- [x] **Rationale**: The purpose of Phase 2 examples is parity proof: additive revisions, structural checks, laser operations, mechanisms, provider helpers, STEP/hybrid patterns, and purchased-part constraints.
- [x] **Default decision**: Pick the smallest representative examples that cover the most retirement evidence.

### Roadmap Checkbox Updates

- [x] **Proposal**: Mark roadmap boxes complete only when the corresponding repo evidence exists, not when work is merely planned.
- [x] **Rationale**: The roadmap should remain a truthful dashboard.
- [x] **Default decision**: Update Phase 1 through Phase 4 boxes during execution only when each item has concrete repo evidence.

### Phase 3 Schema Depth

- [x] **Proposal**: Implement first-pass schemas that are useful enough for fixtures and command validation, but keep them deliberately conservative and reviewable.
- [x] **Rationale**: The repo needs concrete schemas to move, but schema lock-in should wait until the user can review a working draft.
- [x] **Alternative**: Keep Phase 3 as proposals only.
- [x] **Default decision**: Create schemas and fixtures, then label unresolved schema choices clearly in docs and completion notes.

### Schema Validation Tooling

- [x] **Proposal**: Prefer Python standard-library validation for structural smoke checks in this phase, and avoid adding package dependencies until bootstrap/tooling policy is reviewed.
- [x] **Rationale**: This keeps Phase 3-4 executable in the current environment and avoids premature dependency management decisions.
- [x] **Alternative**: Adopt a JSON Schema validator dependency immediately.
- [x] **Default decision**: Use lightweight validation now; list dependency-based validation as a Phase 4/5 improvement if needed.

### Command Skeleton Behavior

- [x] **Proposal**: Commands should exist and parse arguments, but unimplemented fabrication actions should produce explicit "not implemented yet" responses and never emit fabrication-ready artifacts.
- [x] **Rationale**: This proves command shape while preserving the README safety distinction between generated and fabrication-ready.
- [x] **Default decision**: Build safe placeholders, provider listing, manifest validation, and project skeleton creation before any real generator execution.

### Bootstrap Defaults

- [x] **Proposal**: `setup/bootstrap.sh doctor` should be local and read-only by default, while dependency downloads require an explicit future `--allow-downloads` path.
- [x] **Rationale**: This mirrors the repo's safety posture and avoids hidden network/dependency changes.
- [x] **Default decision**: Implement a no-download bootstrap skeleton.

### Phase 4 Stop Point

- [x] **Proposal**: Stop after command skeletons, validation stubs, provider manifest validation, and smoke checks pass.
- [x] **Rationale**: Real provider execution and artifact generation enter Phase 5+ risk territory and should be driven by reviewed schemas/provider contracts.
- [x] **Default decision**: Do not implement OpenSCAD, laser, STEP, or helper-provider generation in this plan.
