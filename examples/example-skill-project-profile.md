# Project Profile: `incident-triage`

> Status: complete Skill package<br>
> Primary type: `AGENT_SKILL`<br>
> Evidence date: illustrative fixture

This illustrative English profile shows the intended narrative shape and evidence boundary. It is not evidence about a real project.

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
| Verified | 4 | Purpose, workflow, references/examples, refusal boundaries |
| Inferred | 1 | Intended reduction of premature implementation |
| Clarification required | 0 | No user interview for this illustrative fixture |
| Unknown | 3 | Adoption, time reduction, failure rate |
| Not applicable | 1 | Runtime API latency target |
| Conflicting | 0 | No conflicting source identified |

Coverage measures evidence availability, not project quality or impact.

### Career-relevant signals

The artifact demonstrates a structured decision workflow, explicit source/verification boundaries, and a defined handoff contract. It does not establish the author's individual role, business impact, or adoption level.

### Evidence ledger

| ID | Claim / field | Status | Source kind | Locator | Rationale / gap |
|---|---|---|---|---|---|
| E1 | The Skill creates a triage brief after classification and reproduction checks. | VERIFIED | repository | `SKILL.md`, purpose and workflow | Directly stated workflow. |
| E2 | The order is intended to reduce premature implementation. | INFERRED | inference | Ordered checks in `SKILL.md` | Sequence supports intent, not measured effect. |
| E3 | Adoption and time reduction. | UNKNOWN | repository | No metric or user statement | Relevant outcome cannot be established. |
| E4 | Runtime API latency target. | NOT_APPLICABLE | repository | Skill-only artifact | No runtime API is present. |

### Review record

- User review status: illustrative fixture; no approval required.
- Corrections accepted: none.
- Explicit unknown / N/A decisions: adoption and time reduction are unknown; API latency is N/A.
- Remaining conflicts: none.
