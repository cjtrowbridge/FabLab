# FabLab Architecture

FabLab is organized around six layers:

- agent and conversation
- part graph
- process recommendation
- provider
- validation
- artifact bundle

The first-pass schemas in `schemas/` model the contracts between these layers. They are intentionally conservative and reviewable; they establish required identifiers, status fields, provenance fields, and manifest relationships without freezing all implementation details.

## Runtime Boundaries

- Temporary assimilation repos are references only.
- Permanent provider/reference repos are accessed through FabLab-owned adapters and docs.
- FabLab owns project planning, manifests, validation, output README generation, and readiness claims.
- Generated artifacts are not fabrication-ready without validation evidence.

## First-Pass Contract Status

These contracts are suitable for fixture validation and command skeletons. They should be reviewed before Phase 5 provider implementation depends on them deeply.
