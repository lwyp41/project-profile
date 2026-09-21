# Validation and QA

## Goal and applicability

Recover automated/manual checks, CI, evals, validators, visual/structural QA, and untested boundary. Documentation-only claims are not execution evidence.

## Investigation by depth

- **Brief:** inspect test commands, CI definition, and validator entry points.
- **Standard:** inspect test cases, fixtures, scripts, checklists, and recent results.
- **Deep:** trace coverage gaps, regression history, failure logs, manual-review gates, and what each check cannot establish.

## Facts, interview, and rendering

Record check, command, scope, result, source, limitation, and claim type. Ask which checks actually ran when material. Do not claim visual or end-to-end QA from a static checker; render verified execution separately from designed gates.
