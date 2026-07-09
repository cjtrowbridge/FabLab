# Purchased Parts Contract

Purchased parts are design truth. They define real dimensions, interfaces, substitutions, and validation gates.

Every purchased component should record:

- catalog identity
- project instance identity
- provenance
- status
- critical dimensions
- fit risk
- required measurements
- used-by parts
- substitution rules

## Status Rule

`proxy_unverified` and `reference_profile` components are not reliable enough for fabrication-ready claims on high-risk interfaces. Physical measurement, manufacturer drawings, STEP models, or test coupons are preferred.

## Output Rule

Output bundles must include purchased-part documentation and must tell the builder what to measure before fabrication.
