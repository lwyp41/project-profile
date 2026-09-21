# Project Profile: `incident-triage`

> Status: complete Skill package<br>
> Primary type: `AGENT_SKILL`<br>
> Evidence date: illustrative fixture

This illustrative English profile shows the intended narrative shape and evidence boundary. It is not evidence about a real project.

> Configuration: `purpose: balanced`; `project-overview: brief`; `product-workflow: standard`; `validation-qa: standard`; `outcomes-metrics: brief`.

## What this project does

`incident-triage` is a Skill that turns an incoming issue report into a structured triage brief. Its stated purpose is to make classification and reproduction checks happen before a report is handed to implementation. [Fact: `SKILL.md`, purpose and workflow sections]

The package can verify its own instruction surface, but it cannot establish whether a team adopted it or whether it reduced triage time. Those are therefore left unknown rather than presented as benefits.

## How the workflow addresses the problem

The Skill collects the report, checks scope and reproduction details, classifies the request, and produces a brief with the information an implementer needs. The sequence makes verification a prerequisite for preparation. [Fact: ordered workflow headings]

It is reasonable to infer that this ordering is meant to reduce premature implementation, but no observed reduction is available. [Inference: workflow order; no outcome metric]

References define required fields and examples show the expected brief. The instructions also name two boundaries: do not accept an unverified reproduction claim, and do not treat an out-of-scope request as authorization to implement. [Fact: `references/`, `examples/`, constraints]

## Reusable facts for downstream use

| Situation / problem | Work or decision | Artifact / mechanism | Observed result | Scope and ownership | Evidence locator | Caveat |
|---|---|---|---|---|---|---|
| An incoming report can be sent to implementation before its scope or reproduction is checked. | Required classification and verification before preparing the handoff. | Ordered Skill workflow and structured triage brief. | Unknown; no adoption or time data. | Artifact ownership is not stated in this fixture. | `SKILL.md`, workflow headings. | Do not claim reduced triage time or team adoption. |
| A report may contain an unverified reproduction claim or be outside scope. | Added explicit refusal boundaries. | Constraints and stop conditions. | Unknown; no false-positive or failure-rate data. | Artifact ownership is not stated in this fixture. | `SKILL.md`, constraints. | The package documents intended behavior, not real-world effectiveness. |

---

## Evidence appendix

### Evidence coverage

| Category | Count | Notes |
|---|---:|---|
| VERIFIED | 1 | Workflow claim in the illustrative ledger |
| INFERRED | 1 | Intended reduction of premature implementation |
| CLARIFICATION_REQUIRED | 0 | No user interview for this illustrative fixture |
| UNKNOWN | 1 | Adoption and outcome evidence cannot be established |
| NOT_APPLICABLE | 1 | Runtime API latency target |
| CONFLICTING | 0 | No conflicting source identified |

Coverage measures evidence availability, not project quality or impact.

### Module coverage

| Module | Applicability | Depth | Inspected sources | Fact IDs | Render decision |
|---|---|---|---|---|---|
| project-overview | applicable | brief | `SKILL.md` | E1 | rendered |
| product-workflow | applicable | standard | `SKILL.md`, `references/`, `examples/` | E1–E2 | rendered |
| outcomes-metrics | applicable | brief | fixture narrative | E3 | rendered as boundary only |
| technical-architecture | not applicable | off | none | E4 | omitted |

### Unknown / N/A / conflicts

Adoption and time reduction are `UNKNOWN`; a runtime API latency target is `NOT_APPLICABLE`; no conflicting source is known. This fixture has no pending `CLARIFICATION_REQUIRED` fact.

### Career-relevant signals

The artifact demonstrates a structured decision workflow, explicit source/verification boundaries, and a defined handoff contract. It does not establish the author's individual role, business impact, or adoption level.

### Evidence ledger

<!-- project-profile-ledger: v2 -->

| ID | Module | Claim / field | Claim type | Status | Source kind | Locator | Time context | Ownership | Metric | Rationale | Caveat | Conflict | Review state |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E1 | product-workflow | The Skill creates a triage brief after classification and reproduction checks. | mechanism | VERIFIED | repository | `SKILL.md`, purpose and workflow | illustrative fixture | unstated | none | — | Directly stated workflow. | 无 | controlled-reviewed |
| E2 | decisions-tradeoffs | The order is intended to reduce premature implementation. | design_intent | INFERRED | inference | Ordered checks in `SKILL.md` | illustrative fixture | unstated | none | — | Sequence supports intent, not measured effect. | 无 | controlled-reviewed |
| E3 | outcomes-metrics | Adoption and time reduction. | observed_outcome | UNKNOWN | repository | No metric or user statement | illustrative fixture | N/A | none | — | Relevant outcome cannot be established. | 无 | unresolved |
| E4 | technical-architecture | Runtime API latency target. | mechanism | NOT_APPLICABLE | repository | Skill-only artifact | illustrative fixture | N/A | none | — | No runtime API is present. | 无 | controlled-reviewed |

### Review record

- User review status: illustrative fixture; no approval required.
- Corrections accepted: none.
- Explicit unknown / N/A decisions: adoption and time reduction are unknown; API latency is N/A.
- Remaining conflicts: none.
