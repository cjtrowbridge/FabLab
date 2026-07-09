# Provider Contract

Providers are tools, libraries, references, or source repositories that help generate or inspect fabrication-related artifacts.

Every provider manifest must declare:

- `id`
- `classification`
- `submodule_path`
- `invocation_mode`
- `license_boundary`
- `output_authority`
- `expected_outputs`
- `validation_required`
- setup/check command status

## Output Authority

Provider outputs are provenance until FabLab validation promotes them. A helper may provide source geometry, previews, inspection artifacts, component models, or reference information, but it does not own fabrication readiness.

## Safe Defaults

- Reference-only tools are never invoked as generators.
- `setup` and `run` commands are disabled unless a manifest explicitly declares safe commands.
- License boundaries default to review-required when unclear.
