# Project Profile Schema

Use an adaptive narrative schema. The main body should read as a coherent project account in the user's language, not as a completed questionnaire. Use headings that sound native in that language; do not translate this file's headings word-for-word. Keep the evidence appendix structured enough for a later Skill to inspect.

## Main narrative

Use only the blocks that materially improve understanding. Merge blocks when that produces a clearer story.

1. **Project snapshot**: name, status, project shape, one-sentence purpose, and what is directly observable.
2. **Starting point and problem**: the triggering context, user problem, or constraint. Distinguish documented motivation from an inference.
3. **What was designed and how it works**: the essential capability, operating model, information flow, modules, artifacts, or decision sequence. For a Skill, explain the trigger, routing, guardrails, and output contract rather than listing every reference file.
4. **Key choices and trade-offs**: only choices supported by artifacts or user testimony; connect each one to the risk or constraint it addresses.
5. **Contribution evidence**: what the project owner demonstrably built, investigated, coordinated, decided, or validated. State ownership and collaborators only when known.
6. **Validation, outcomes, and boundaries**: tests, usage observations, outputs, quality gates, metrics, limitations, and risks. Attribute personal observations and do not convert them into generalized performance claims.
7. **Next steps or open questions**: include only consequential work that is documented or explicitly proposed by the user.

For compact projects, a strong profile may use only “Project snapshot”, “How it works”, “Contribution evidence”, and “Boundaries”. Do not add empty sections merely to look complete.

## Downstream fact pack

After the narrative, add a localized section whose title means “Reusable facts for downstream use”. Its purpose is to let a later resume, portfolio, or interview Skill select evidence without reverse-engineering prose again.

Include only high-signal units. Each unit should contain:

| Field | Meaning |
|---|---|
| Situation / problem | The concrete context or risk addressed |
| Work or decision | The source-backed action, design, or responsibility |
| Artifact / mechanism | What was produced or how it was implemented |
| Observed result | A measured result or clearly attributed observation; otherwise `Unknown` |
| Scope and ownership | What is known about scale, role, and collaborators |
| Evidence locator | A concise file, section, commit, or user-answer pointer |
| Caveat | Missing evidence, confidence boundary, or wording restriction |

These are neutral fact units, not accomplishment bullets. Do not start them with “I”, choose promotional verbs, or combine separate facts into an inflated outcome.

## Evidence appendix

Put the detailed status model, coverage summary, material conflicts, and claim-level ledger after the main narrative and fact pack. This appendix makes the profile auditable without making the story sound mechanical.

## Conditional analysis prompts

### AI / Agent / Prompt

Include Why AI, AI capability, AI versus traditional approach, model/LLM strategy, prompt/agent/RAG design, human-in-the-loop, AI evaluation and reliability, cost, AI risks, and business/product value when applicable.

### Skill / Documentation

Include Purpose, Trigger Conditions, Workflow, Instructions, Decision Logic, References, Examples, Expected Outputs, and Failure Modes. Treat the skill’s actual instructions and artifacts as primary evidence.

### Software / Library

Include runtime and deployment, package boundaries, API contracts, dependencies, testing, observability, and integration constraints when applicable.

### Data / Research

Include research question, data provenance, sampling or selection, method, analysis, reproducibility, findings, uncertainty, and limitations when applicable.

### Sparse / Artifact

Include artifact inventory, observable behavior or structure, plausible use contract, evidence boundary, missing materials, and interview-derived context.

## Evidence-ledger format

For each material claim, record:

| Field | Meaning |
|---|---|
| Claim | The concise statement used in the profile |
| Status | One allowed status label |
| Evidence | Source kind plus locator |
| Rationale | Why the evidence supports the claim, especially for inference |
| Gaps / conflict | What remains unresolved |

Use `N/A` in the prose when a conditional concept does not apply, and `Unknown` when it applies but cannot be established. The ledger must preserve the exact status label.
