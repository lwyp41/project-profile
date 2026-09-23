# Risks and Limitations

## Goal and applicability

Record failure modes, unresolved issues, unsupported assumptions, conflicts, privacy/security limits, and evidence boundaries. N/A never substitutes for missing evidence.

## Investigation by depth

- **Brief:** inspect known limitations, warnings, and issue summaries.
- **Standard:** inspect failure paths, tests, policies, changelog, and unresolved documentation.
- **Deep:** trace incidents, regressions, conflicts, mitigation history, and residual risk across sources.

## Facts, interview, and rendering

Record risk, trigger, affected scope, mitigation, residual risk, source, and status. Ask about material known failures absent from artifacts. Do not convert a documented guardrail into proof the risk never occurs; render uncertainty and conflict explicitly.

## Render by depth

- **Brief render:** highest-impact known risk or evidence boundary.
- **Standard render:** preserve Brief; add trigger, affected scope, mitigation, residual risk, and unresolved limitation.
- **Deep render:** preserve Standard; add incidents or regressions, mitigation history, conflicts, privacy/security boundaries, and uncertainty about what controls cannot establish where evidenced.
