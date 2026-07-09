# Decision 0001: Phase 3-4 Working Defaults

Status: accepted working defaults

Date: 2026-07-08

## Context

FabLab has completed a first-pass governance, schema, and command skeleton. The next work needs clear defaults so agents can continue without repeatedly re-opening settled early decisions, while still avoiding premature lock-in for schemas, dependencies, provider execution, and fabrication readiness.

## Decisions

- Keep Phase 3 schemas as reviewable draft contracts, not frozen APIs.
- Use lightweight standard-library validation for first-pass schema and fixture checks.
- Keep provider `setup` and `run` disabled unless each provider manifest declares reviewed safe commands.
- Keep bootstrap local-only by default; downloads must require an explicit future `--allow-downloads` path.
- Keep `cad-viewer` as `review_required` until its upstream license is verified.
- Select parity fixtures by capability coverage and small size rather than project size or popularity.
- Treat Phase 3/4 as a skeleton and contract baseline, not real provider execution or fabrication parity.

## Consequences

- Future schema changes are allowed, but must update fixtures, docs, and validation scripts together.
- Provider execution must be added provider-by-provider through explicit setup/check/smoke workflows.
- Real fabrication artifact generation starts in later parity phases, after reviewed contracts exist.
- Roadmap checkboxes must reflect evidence actually present in the repository, not intended scope.
