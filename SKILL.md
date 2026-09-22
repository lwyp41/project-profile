---
name: project-profile
description: Reconstruct a completed project's evidence-backed facts, decisions, evolution, contribution, validation, outcomes, and boundaries into a configurable PROJECT_PROFILE.md that downstream Skills can reuse. Use for repositories, Agent Skills, prompts, AI agents, software, data, research, documentation, or sparse artifacts. Do NOT use for resume bullets, marketing copy, invented impact, or unsupported claims.
---

# Project Profile v2

Reconstruct facts first; render prose second. Produce a native-language, evidence-disciplined `PROJECT_PROFILE.md` that downstream Skills can reuse. Markdown is canonical; DOCX is outside v2's core scope and may only be a derivative.

## Boundary

- Do not write resume bullets or promotional claims, or invent ownership, users, adoption, rationale, alternatives, metrics, impact, or outcomes.
- Preserve `VERIFIED`, `INFERRED`, `CLARIFICATION_REQUIRED`, `UNKNOWN`, `NOT_APPLICABLE`, and `CONFLICTING`; classify material claims as `fact`, `design_intent`, `mechanism`, `observed_outcome`, or `measured_outcome`.
- A material, user-answerable gap must be `CLARIFICATION_REQUIRED` and asked before it becomes `UNKNOWN`; a disabled module or missing evidence is not N/A.
- Write and interview directly in the request language. Localize headings; do not translate a rigid template.

## Load references progressively

Read [evidence-policy.md](references/evidence-policy.md), [module-registry.md](references/module-registry.md), [depth-policy.md](references/depth-policy.md), [interview-policy.md](references/interview-policy.md), and [rendering-policy.md](references/rendering-policy.md) before their respective decisions. After classification, load only relevant `references/project-types/<type>.md` and enabled `references/modules/<module>.md` files. [templates/profile-config.yaml](templates/profile-config.yaml) is optional; natural-language configuration is equivalent.

## Runtime state contract

Treat the workflow as explicit states, not as an internal checklist. Do not skip forward because the project looks simple.

```text
PROFILE_MODE_SELECTED
→ DISCOVERED
→ CONFIGURED
→ FACTS_RECONSTRUCTED
→ INTERVIEW_RESOLVED_OR_JUSTIFIED_SKIP
→ REVIEW_APPROVED
→ RENDERED
```

A run is incomplete until every state transition above is satisfied.

### Mandatory profile-mode selection

Before inspecting the project, the user must select one profile mode. Do not infer, auto-select, or silently default a mode.

If the user's request already explicitly names one of these modes, that explicit request satisfies the gate. Otherwise stop and ask one short question that explains what the choice controls:

- **Balanced** — general-purpose project reconstruction across applicable modules.
- **Resume** — deeper career-evidence reconstruction, especially Ownership, Scale, Complexity, Decision, Impact, and Iteration.
- **Technical** — deeper architecture, constraints, AI/agent design, information boundaries, validation, and risks.
- **Custom** — control all 15 modules and four investigation depths; after selection, the Skill shows the complete option set and a compact configuration example.

Keep this explanation brief. The purpose of the question is to choose investigation priorities, not writing style.

For **Custom**, complete an explicit onboarding exchange before discovery. Immediately after Custom is selected, proactively show the four depth levels, all 15 canonical module IDs with short descriptions localized to the user's language, and at least one compact configuration example. State that unspecified applicable modules use a visible `standard` baseline unless the user explicitly chooses another default depth. Explain that the user does not need to configure all 15 modules individually, may provide only exception overrides, and may use natural-language configuration. Accept compact instructions such as "deep decisions + ownership, standard architecture, off outcomes". Clarify only unknown module IDs, invalid depths, or an ambiguity that would materially change investigation.

The Custom onboarding must include this complete choice space (use the module-registry descriptions, translated into the user's language):

| Depth | Meaning |
|---|---|
| `off` | Do not independently investigate or render the module. |
| `brief` | Inspect only obvious high-signal sources. |
| `standard` | Inspect primary artifacts plus relevant documentation, examples, and tests. |
| `deep` | Also investigate history, alternatives, conflicts, outcomes, failures, and user-answerable gaps. |

| Module ID | Short description |
|---|---|
| `project-overview` | Shape, lifecycle, main capability, and observable boundary. |
| `background-problem` | Triggering context, problem, and risk. |
| `users-stakeholders` | Intended or actual users and affected parties. |
| `goals-success` | Goals, success conditions, and unverified targets. |
| `requirements-constraints` | Functional, operational, privacy, cost, policy, and compatibility constraints. |
| `product-workflow` | Inputs, routing, human gates, handoffs, and outputs. |
| `technical-architecture` | System boundaries, runtime, interfaces, integrations, and deterministic components. |
| `ai-agent-design` | LLM, prompt, tool, context, human-in-the-loop, and evaluation design. |
| `information-data` | Sources of truth, provenance, data boundaries, and generated-output policy. |
| `decisions-tradeoffs` | Constraints, alternatives, choices, rationale, and consequences. |
| `ownership-contribution` | Personal work, collaboration, maintenance, and AI-assistance boundary. |
| `validation-qa` | Automated or manual validation, regression, and untested boundary. |
| `outcomes-metrics` | Usage, scale, efficiency, quality, and measurement caveats. |
| `evolution-history` | Initial state, changes, migrations, and current state. |
| `risks-limitations` | Failure modes, unresolved issues, risks, and evidence boundaries. |

Show a compact example such as:

```text
default depth: standard
deep: technical-architecture, decisions-tradeoffs, validation-qa
brief: outcomes-metrics
off: ownership-contribution
```

Natural-language equivalents are valid. A complete configuration can be confirmed concisely and then proceed to discovery without repeating the full onboarding. A partial override is interpreted against the visible baseline and confirmed; for example, `deep decisions and architecture; off outcomes` means standard for every other applicable module, deep for `decisions-tradeoffs` and `technical-architecture`, and off for `outcomes-metrics`. Explicit module overrides always take precedence over the default depth. Do not begin new repository discovery until Custom configuration is resolved.

## Workflow

1. **Select profile mode — hard gate:** satisfy the mandatory profile-mode selection above. No repository investigation begins before this state is complete. For Custom, the onboarding/configuration exchange is part of this gate; `PROFILE_MODE_SELECTED` alone is insufficient.
2. **Discover:** inventory repository, docs, configuration, examples, outputs, tests, metadata, and Git history; record inspected and unavailable sources.
3. **Classify:** select evidence-backed primary/secondary types from `SOFTWARE`, `AI_AGENT`, `AGENT_SKILL`, `PROMPT_SYSTEM`, `LIBRARY`, `DATA_PROJECT`, `RESEARCH_PROJECT`, `DOCUMENTATION_PROJECT`, `SPARSE_ARTIFACT`. Types route investigation, not a fixed template.
4. **Configure:** apply the user-selected mode, type recommendations, and explicit overrides. Build a Module Coverage Map: applicability, effective depth, priority/inspected sources, fact IDs, gaps, interview candidates, and render decision. For `custom`, unspecified applicable modules use the explicitly confirmed default depth (`standard` unless the user chose another one), and user-selected module overrides are authoritative.
5. **Extract:** investigate enabled modules at their effective depth. Before prose, build a Canonical Fact Model with `id`, `module`, `claim`, `claim_type`, `status`, `source_kind`, `source_locator`, `time_context`, `ownership`, `metric`, `rationale`, `caveat`, `conflict`, and `review_state` where applicable.
6. **Reconstruct:** independently recover timeline/evolution; decisions as constraint → alternatives → choice → rationale → consequence; ownership/contribution; and outcomes/scale. A visible choice without supported rationale is a clarification need.
7. **Interview — conditional but binding:** after investigation, run the gap scan in [interview-policy.md](references/interview-policy.md). If any material, user-answerable gap exists, ask 3–5 focused questions per round. If none exist, explicitly record why the interview is skipped. For `resume`, assess Ownership, Scale, Complexity, Decision, Impact, and Iteration before review.
8. **Validate:** check every consequential fact, metric, ownership assertion, inference, conflict, and Unknown/N/A choice against the evidence policy.
9. **Review — hard gate:** show the selected mode, effective module/depth configuration, material facts/states, fact pack, unresolved items, conflicts, proposed Unknown/N/A decisions, interview outcome, and resume-signal coverage when applicable. Stop and wait for user approval or correction. Do not render the final profile in the same turn unless the user explicitly requested an unattended/no-review run before the review state was reached.
10. **Render:** only after `REVIEW_APPROVED`, use [templates/PROJECT_PROFILE.md](templates/PROJECT_PROFILE.md); render only enabled, applicable modules, neutral downstream facts, and a complete evidence appendix.

## Anti-rationalization rules

| Tempting shortcut | Binding rule |
|---|---|
| "Balanced is probably fine." | Never auto-select a profile mode. Require an explicit user choice. |
| "The project is simple, so configuration is unnecessary." | Still require profile-mode selection; simplicity may reduce investigation, not remove the gate. |
| "I found enough facts, so there is no need to consider an interview." | Run the material-gap scan. Interview if any user-answerable material gap exists; otherwise record the skip reason. |
| "I can infer ownership or rationale from the repository." | Repository location or a visible choice does not establish personal ownership or rationale. |
| "The user probably wants the final file immediately." | The review gate is mandatory unless the user explicitly requested a no-review/unattended run. |
| "Custom can be represented by Balanced plus a few internal tweaks." | Custom is a first-class user-selected mode; preserve the user's module/depth choices explicitly. |

## Completion checklist

- [ ] The user explicitly selected `balanced`, `resume`, `technical`, or `custom`; no silent default was used.
- [ ] Sources, classification, module configuration, and depths are recorded.
- [ ] Fact model and coverage map precede prose; evolution, decisions, ownership, and outcomes were investigated where applicable.
- [ ] The interview gap scan ran; every material answerable gap was asked before `UNKNOWN`, or a no-interview reason was recorded.
- [ ] Metrics retain value, unit, scope, time window, source, and caveat.
- [ ] Review showed selected mode, configuration, facts/states, unresolved items, and interview outcome, and user approval was obtained unless explicitly waived in advance.
- [ ] The profile is natural documentation, not a ledger or resume; its fact pack is neutral and its appendix retains coverage, conflicts, ledger, and review record.
