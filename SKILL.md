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

## Workflow

1. **Understand intent:** identify `purpose` (`resume`, `technical`, `balanced`), language, explicit module/depth overrides, and unresolved-field preference. Default to `balanced`; ask only about a material ambiguity.
2. **Discover:** inventory repository, docs, configuration, examples, outputs, tests, metadata, and Git history; record inspected and unavailable sources.
3. **Classify:** select evidence-backed primary/secondary types from `SOFTWARE`, `AI_AGENT`, `AGENT_SKILL`, `PROMPT_SYSTEM`, `LIBRARY`, `DATA_PROJECT`, `RESEARCH_PROJECT`, `DOCUMENTATION_PROJECT`, `SPARSE_ARTIFACT`. Types route investigation, not a fixed template.
4. **Configure:** apply preset, type recommendations, and explicit overrides. Build a Module Coverage Map: applicability, effective depth, priority/inspected sources, fact IDs, gaps, interview candidates, and render decision.
5. **Extract:** investigate enabled modules at their effective depth. Before prose, build a Canonical Fact Model with `id`, `module`, `claim`, `claim_type`, `status`, `source_kind`, `source_locator`, `time_context`, `ownership`, `metric`, `rationale`, `caveat`, `conflict`, and `review_state` where applicable.
6. **Reconstruct:** independently recover timeline/evolution; decisions as constraint → alternatives → choice → rationale → consequence; ownership/contribution; and outcomes/scale. A visible choice without supported rationale is a clarification need.
7. **Interview:** rank material gaps and ask 3–5 focused questions per round after investigation. For `resume`, explicitly assess Ownership, Scale, Complexity, Decision, Impact, and Iteration before review.
8. **Validate:** check every consequential fact, metric, ownership assertion, inference, conflict, and Unknown/N/A choice against the evidence policy.
9. **Review:** show facts/states, coverage, fact pack, unresolved items, conflicts, proposed Unknown/N/A decisions, and resume-signal coverage. Wait for approval or explicit authorization to preserve unresolved labels.
10. **Render:** use [templates/PROJECT_PROFILE.md](templates/PROJECT_PROFILE.md); render only enabled, applicable modules, neutral downstream facts, and a complete evidence appendix.

## Completion checklist

- [ ] Sources, classification, module configuration, and depths are recorded.
- [ ] Fact model and coverage map precede prose; evolution, decisions, ownership, and outcomes were investigated where applicable.
- [ ] Every material answerable gap was asked before `UNKNOWN`.
- [ ] Metrics retain value, unit, scope, time window, source, and caveat.
- [ ] The profile is natural documentation, not a ledger or resume; its fact pack is neutral and its appendix retains coverage, conflicts, ledger, and review record.
