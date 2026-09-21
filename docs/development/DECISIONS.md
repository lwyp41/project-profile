# v2 Decision Log

## Approved architecture

- v2 reconstructs a canonical fact model before rendering prose. `PROJECT_PROFILE.md` remains the canonical user-facing artifact; no separate sensitive fact store is created by default.
- Project types route investigation. They do not select a rigid output template.
- Module depth controls investigation behavior (`off`, `brief`, `standard`, `deep`), not just output length.
- The `resume`, `technical`, and `balanced` presets alter investigation priorities only. They never authorize promotional claims or weaker evidence rules.
- The existing six evidence states and the mandatory clarification-before-unknown transition remain intact.

## Deferred decisions

- Public regression uses a fully synthetic fixture; it must not be presented as evidence about any real project, person, or outcome.
