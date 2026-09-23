# Requirements and Constraints

## Goal and applicability

Recover functional, operational, policy, privacy, compatibility, cost, and time constraints. A missing operational artifact is not a quality judgment.

## Investigation by depth

- **Brief:** inspect specifications, policy text, and configuration.
- **Standard:** inspect compatibility layers, privacy rules, failure paths, and tests.
- **Deep:** trace constraint changes, enforcement mechanisms, exceptions, and conflicts in history.

## Facts, interview, and rendering

Record constraint, source, enforcement, status, time, and caveat. Ask whether a visible restriction is intentional when it materially affects interpretation. Do not infer requirements from implementation convenience; render verified constraints and unresolved intent separately.

## Render by depth

- **Brief render:** highest-impact verified constraint and its affected scope.
- **Standard render:** preserve Brief; add enforcement mechanism, operational or compatibility effect, and unresolved intent/limitation.
- **Deep render:** preserve Standard; add constraint changes, exceptions, failure-path enforcement, policy conflicts, and material clarification gaps where evidenced.
