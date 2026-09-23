# Decisions and Trade-offs

## Goal

Reconstruct consequential choices as `constraint → alternatives → choice → rationale → consequence`, not as implementation inventory.

## Applicability and depth

Enable for architecture, workflow, safety, cost, compatibility, scope, or quality choices. Missing rationale is a clarification need, never N/A.

- **Brief:** inspect architecture/overview docs for the most consequential visible choice.
- **Standard:** inspect ADRs, commits, comments, tests, configuration, and releases; recover constraint, choice, and consequence.
- **Deep:** trace predecessor variants and rejected paths; compare history and docs; identify rationale requiring owner confirmation.

## Facts, interview, and rendering

Record constraint, alternatives, choice, rationale, consequence, source, ownership, caveat, and conflict. Ask which alternatives were serious, why this was chosen, and what followed. Never invent alternatives from common practice or a measured benefit from a mechanism; render only supported rationale.

## Render by depth

- **Brief render:** the most consequential supported choice and its immediate context.
- **Standard render:** preserve Brief; render constraint → choice → consequence, plus supported rationale or an explicit evidence boundary.
- **Deep render:** preserve Standard; add serious alternatives, supported rationale, later validation or revision, conflicts, and `CLARIFICATION_REQUIRED` for material missing rationale rather than inventing it.
