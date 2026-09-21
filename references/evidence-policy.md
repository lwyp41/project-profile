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

## Required gap transition

For every material field with missing repository or documentation evidence, apply this order:

```text
Missing evidence
  → Can a focused user answer resolve it?
    → yes: CLARIFICATION_REQUIRED → Progressive User Interview
    → no: UNKNOWN
```

After the interview, update `CLARIFICATION_REQUIRED` as follows:

- user gives a direct answer → `VERIFIED` (source kind: `user`);
- user gives a qualified answer → `INFERRED` or keep `CLARIFICATION_REQUIRED` when more precision is needed;
- user says “no” → `VERIFIED` negative fact (source kind: `user`);
- user says “I don't know” or “I don't remember” → `UNKNOWN`;
- user says “not applicable” → `NOT_APPLICABLE`;
- user declines or cannot be reached → `UNKNOWN`, with the reason recorded.

Do not bypass this transition because the profile can still be drafted without the answer. The purpose of `CLARIFICATION_REQUIRED` is to make important, answerable gaps visible to the user before they become unknown.

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
- Every material v2 fact also records its module and, where applicable, time context, ownership, metric, caveat, conflict, and review state in the Canonical Fact Model.
- Ownership is not inferred from repository location, commits alone, or possession of the repository. Attribute only directly evidenced or explicitly confirmed scope.
- A material metric requires value, unit, scope, time window, and source. User testimony can verify a personal observation, but does not make it a general benchmark.

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
