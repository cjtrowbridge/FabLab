# Output Bundle Contract

Every generated project output folder must be self-documenting and auditable.

Required bundle concepts:

- `README.md`
- `build_manifest.json`
- `artifact_manifest.json`
- `process_plan.json`
- `process_recommendations.md`
- `material_setup.md`
- `tool_setup.md`
- `assembly_guide.md`
- `validation_summary.md`
- `bom.csv`
- previews
- CAD, print, laser, G-code, source geometry, operation, calibration, purchased-part, and provenance artifacts as applicable

## README Requirements

The output README must explain what each artifact is, which physical part it corresponds to, what validation passed, what remains unverified, and what calibration or safety steps are required.

## Audit Rule

A bundle audit must reject stale, missing, unexpected, or unmanifested artifacts before FabLab describes a bundle as complete.
