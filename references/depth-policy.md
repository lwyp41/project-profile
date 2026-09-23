# Depth Policy

Depth is both an investigation commitment and a rendered substance commitment for one module, not a word-count setting. Every depth obeys the evidence policy and records inspected sources, recovered facts, recovered semantic coverage, and material gaps in the Module Coverage Map. Rendered coverage must preserve recovered coverage where facts exist; longer prose that does not add semantic categories is not deeper.

| Depth | Investigation contract | Render contract |
|---|---|---|
| `off` | Do not investigate independently, except facts required to interpret an enabled module. | Do not render it. Disabling a module is not `NOT_APPLICABLE`. |
| `brief` | Inspect obvious high-signal sources and recover 2–4 high-value facts. Inspect history only to resolve a material conflict. | Render orientation, the highest-value evidenced facts, and a necessary boundary. It is intentionally selective. |
| `standard` | Inspect primary artifacts plus related documentation, examples, and tests. Recover mechanism, a major choice, result, and limitation where applicable. | Render a complete project summary: what exists/covers, how the core mechanism or workflow works, at least one relevant constraint/choice/result/limitation, and an evidence boundary. Standard must preserve Brief coverage and must not collapse to a one-line orientation. |
| `deep` | Inspect implementation, references, examples, tests, generated artifacts, Git history, older variants, changelog, and conflicting sources when available. | Preserve Standard coverage and additionally render relevant evidenced categories—structure, runtime/data/control flow, failure/degradation, alternatives/rationale/consequence, evolution, validation boundaries, conflicts, and material gaps. Unsupported user-answerable categories are `CLARIFICATION_REQUIRED`, never invented. |

The module-specific contract defines which semantic categories are relevant. Evaluation compares inspected-source set, fact set, question set, and rendered semantic coverage for the same frozen fixture at each depth. Where evidence exists, coverage is monotonic: Deep must preserve Standard and Standard must preserve Brief. A difference in prose length alone is a failure.

For Custom, `standard` is the visible default depth for unspecified applicable modules unless the user explicitly chooses another default depth. A per-module override always takes precedence over that baseline. The effective depth and the rule used to derive it must be recorded in the Module Coverage Map; no Custom baseline may remain hidden.
