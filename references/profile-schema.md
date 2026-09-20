# Project Profile Schema

Use a Core + Conditional schema. Keep the headings stable enough for comparison, but do not force irrelevant sections into a project.

## Core

1. Project identity and status
2. Project background
3. Problem / Motivation
4. Product or project goals
5. Users and usage scenarios
6. Core capabilities / functions
7. Project type and analysis mode
8. Technology, tools, and artifacts
9. Architecture or operating model
10. Data and information flow
11. APIs, modules, interfaces, or document/skill surfaces
12. Technical or methodological challenges
13. Key design decisions
14. Trade-offs
15. Performance, quality, or other metrics
16. Results / project outcomes
17. Limitations and risks
18. Future work
19. Evidence Coverage
20. Evidence ledger
21. Career-Relevant Signals

## Conditional sections

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

## Field format

For each material claim, record:

| Field | Meaning |
|---|---|
| Claim | The concise statement used in the profile |
| Status | One allowed status label |
| Evidence | Source kind plus locator |
| Rationale | Why the evidence supports the claim, especially for inference |
| Gaps / conflict | What remains unresolved |

Use `N/A` in the prose when a conditional concept does not apply, and `Unknown` when it applies but cannot be established. The ledger must preserve the exact status label.
