# Evidence Policy

## Status model

| Status | Use when | Prohibited shortcut |
|---|---|---|
| `VERIFIED` | Directly supported by a reliable project source or explicit user statement | Do not upgrade from plausibility alone |
| `INFERRED` | Reasonable interpretation supported by observed evidence | Must name observation and reasoning |
| `CLARIFICATION_REQUIRED` | A material claim could be resolved by a focused user answer | Do not hide it as a fact |
| `UNKNOWN` | Relevant, but evidence cannot establish it | Do not convert absence into N/A |
| `NOT_APPLICABLE` | The concept does not apply to this project | Do not use merely because evidence is missing |
| `CONFLICTING` | Credible sources disagree | Preserve both sources and explain the conflict |

## Source kinds

- `repository`: source files, configuration, tests, assets, package metadata, generated artifacts.
- `documentation`: README, design notes, issue notes, guides, release notes, embedded comments.
- `git_history`: commits, branches, tags, blame, diffs, chronology.
- `user`: explicit answers, corrections, memories, or review decisions.
- `inference`: agent reasoning from one or more observations; never a primary source.
- `external_reference`: external documentation or comparison material, used only with permission and clearly separated from project evidence.

## Claim discipline

- Metrics require a value, unit, scope, time window, and source. If any material part is absent, mark the metric unknown or partial rather than estimating.
- Business impact, users, adoption, rationale, alternatives, and success criteria require direct evidence or an explicit user statement.
- “The code suggests” is an inference, not verification.
- A missing README does not prove there was no goal; a missing test does not prove poor quality.
- Contradictions are first-class findings. Do not resolve them by choosing the more convenient source without explaining why.

## Evidence Coverage

Report objective counts or categories, such as:

- core fields with verified support;
- core fields supported only by inference;
- fields requiring clarification;
- unknown fields;
- not-applicable fields;
- conflicting claims;
- conditional fields not activated by project type.

Do not turn these counts into a single quality score. Coverage describes evidence availability, not project quality or impact.
