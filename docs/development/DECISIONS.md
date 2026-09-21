# v2 Decision Log

## Approved architecture

- v2 reconstructs a canonical fact model before rendering prose. `PROJECT_PROFILE.md` remains the canonical user-facing artifact; no separate sensitive fact store is created by default.
- Project types route investigation. They do not select a rigid output template.
- Module depth controls investigation behavior (`off`, `brief`, `standard`, `deep`), not just output length.
- Profile-mode selection is a mandatory user-visible gate before discovery. The user must explicitly select `balanced`, `resume`, `technical`, or `custom`; the Skill must not silently default or infer a mode.
- `custom` is a first-class profile mode so users can explicitly choose module emphasis, reductions, disables, and depths without being collapsed into a preset.
- The `resume`, `technical`, and `balanced` presets alter investigation priorities only. They never authorize promotional claims or weaker evidence rules.
- The existing six evidence states and the mandatory clarification-before-unknown transition remain intact.
- The interview state is conditional but binding: every run performs a material-gap scan, asks all material user-answerable gaps before `UNKNOWN`, or records why no interview was needed.
- The review state is a hard user-visible gate before final rendering unless the user explicitly requested an unattended/no-review run in advance.

## Deferred decisions

- Public regression uses a fully synthetic fixture; it must not be presented as evidence about any real project, person, or outcome.
