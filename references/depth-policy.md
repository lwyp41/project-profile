# Depth Policy

Depth is an investigation commitment for one module, not a word-count setting. Every depth obeys the evidence policy and records inspected sources, recovered facts, and material gaps in the Module Coverage Map.

| Depth | Investigation contract | Interview and rendering contract |
|---|---|---|
| `off` | Do not investigate independently, except facts required to interpret an enabled module. | Do not render it. Disabling a module is not `NOT_APPLICABLE`. |
| `brief` | Inspect obvious high-signal sources and recover 2–4 high-value facts. Inspect history only to resolve a material conflict. | Ask only when a missing fact blocks correct interpretation; render the core facts and necessary boundary. |
| `standard` | Inspect primary artifacts plus related documentation, examples, and tests. Recover mechanism, a major choice, result, and limitation where applicable. | Ask focused questions for remaining material gaps; render mechanism and evidence boundary. |
| `deep` | Inspect implementation, references, examples, tests, generated artifacts, Git history, older variants, changelog, and conflicting sources when available. | Actively recover evolution, alternatives, rationale, ownership, usage, scale, outcomes, and failures; ask user-answerable gaps. |

Evaluation compares the inspected-source set, fact set, and question set for the same module at each depth. A difference in prose length alone is a failure.

For Custom, `standard` is the visible default depth for unspecified applicable modules unless the user explicitly chooses another default depth. A per-module override always takes precedence over that baseline. The effective depth and the rule used to derive it must be recorded in the Module Coverage Map; no Custom baseline may remain hidden.
