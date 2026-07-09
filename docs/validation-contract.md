# Validation Contract

FabLab validation records what has been checked, what failed, and what remains unverified.

Validation results use:

- `passed`
- `failed`
- `unverified`
- `not_applicable`
- `blocked`

Readiness states use:

- `proposed`
- `recommended`
- `selected`
- `generated`
- `previewed`
- `validated`
- `calibration_only`
- `fabrication_ready`
- `physically_verified`

## Readiness Rule

Generated files, successful renders, valid meshes, previews, and G-code are not fabrication-ready by themselves. Readiness requires process-specific validation evidence and any required physical calibration or measurement.

## Provider Rule

Helper-generated output is source/provenance until FabLab validation records it as usable for a selected process.
