# Temporary Assimilation Repositories

These repositories exist only while FabLab absorbs their useful behavior. They must not become long-term runtime dependencies.

| Repo | Path | Retirement Target | Assimilation Report |
|---|---|---|---|
| `cjtrowbridge/vibe-modeling` | `third_party/vibe-modeling` | Remove after additive parity and legacy migration evidence are approved. | `docs/assimilation/vibe-modeling-assimilation.md` |
| `cjtrowbridge/vibe-cutting` | `third_party/vibe-cutting` | Remove after subtractive/laser parity and legacy migration evidence are approved. | `docs/assimilation/vibe-cutting-assimilation.md` |
| `earthtojake/text-to-cad` | `third_party/text-to-cad` | Remove after useful STEP, viewer, DXF, and component-source patterns are assimilated or wrapped. | `docs/assimilation/text-to-cad-assimilation.md` |

## Operating Rules

- Treat these repositories as source references.
- Track every adopted capability in the parity matrix.
- Route long-term external helpers through permanent provider/reference submodules.
- Keep runtime commands pointed at FabLab-native paths.
- Remove temporary submodules only after parity evidence is complete and approved.
