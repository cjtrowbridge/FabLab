---
plan_id: 2026-07-08-12-55-35_bootstrap-agent-framework-and-submodules
title: Bootstrap Agent Framework And Submodules
summary: Add the initial FabLab submodules and integrate the agents framework into the host repository.
status: past
created_at: 2026-07-08-12-55-35
---

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

## Checklist

- [x] Read the FabLab README for initial submodule and agent-framework directions.
- [x] Add the `agents` framework submodule at `./agents`.
- [x] Add the three temporary assimilation submodules under `./third_party/`.
- [x] Read the agent framework bootstrap instructions and canonical rules.
- [x] Create required host operational directories for plans, journal, kanban, and downtime reports.
- [x] Create host shim files that direct runtimes to `./agents/RULES.md`.
- [x] Copy missing host-managed framework directories from `./agents/`.
- [x] Add any nested `third_party` submodules required from `vibe-modeling` and `vibe-cutting`.
- [x] Run agent-framework plan index verification from the host root.
- [x] Review git status and summarize the checkpoint.
