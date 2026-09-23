# Synthetic Agent Skill — Resume Preset

> This is a fictional public regression artifact, not a project claim.

## Project overview

SignalTriage is a synthetic Agent Skill that turns incoming reports into a screened triage brief before deeper diagnosis or remediation drafting.

## Reusable facts

| Situation | Decision | Mechanism | Outcome boundary |
|---|---|---|---|
| Broad reports can consume investigation effort prematurely. | Screen intake before deeper diagnosis. | Ordered triage workflow. | No adoption or efficiency result is established. |
| A remediation draft may be unsuitable before strategy review. | Require approval before drafting. | Approval gate. | No quality improvement is established. |

## Evidence appendix

### Evidence coverage

| Category | Count | Notes |
|---|---:|---|
| VERIFIED | 2 | Workflow and synthetic design facts |
| INFERRED | 1 | The ordering's intended benefit |
| CLARIFICATION_REQUIRED | 0 | No interview gap in this synthetic fixture |
| UNKNOWN | 1 | Adoption and outcomes |
| NOT_APPLICABLE | 1 | Runtime latency target |
| CONFLICTING | 0 | No conflicting synthetic source |

### Module coverage

<!-- project-profile-module-coverage: v2 -->

| Module | Applicability | Depth | Inspected sources | Fact IDs | Recovered semantic coverage | Material gaps / clarification state | Render destination |
|---|---|---|---|---|---|---|---|
| project-overview | applicable | brief | synthetic repository description | F01 | shape, capability, boundary | none | Project overview |
| decisions-tradeoffs | applicable | standard | T02, T03 | F02, F04 | constraint, choice, intended consequence | actual outcome UNKNOWN | Reusable facts |
| outcomes-metrics | applicable | brief | absence of metrics | F03 | measurement absence | adoption and outcome metrics UNKNOWN | Reusable facts |

### Evidence ledger

<!-- project-profile-ledger: v2 -->

| ID | Module | Claim | Claim type | Status | Source kind | Locator | Time context | Ownership | Metric | Rationale | Caveat | Conflict | Review state |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | product-workflow | SignalTriage screens intake before deeper diagnosis. | mechanism | VERIFIED | repository | Synthetic fixture README | synthetic fixture | fictional owner | none | Directly specified workflow. | Not evidence of real use. | none | controlled-reviewed |
| F02 | decisions-tradeoffs | Approval precedes remediation drafting. | design_intent | VERIFIED | user | T03 | synthetic fixture | fictional owner | none | Stated synthetic rationale. | No measured result. | none | controlled-reviewed |
| F03 | outcomes-metrics | Adoption and outcome metrics. | observed_outcome | UNKNOWN | repository | No metric supplied | synthetic fixture | N/A | none | Relevant boundary. | Cannot establish impact. | none | unresolved |
| F04 | decisions-tradeoffs | The order is intended to focus deeper diagnosis. | design_intent | INFERRED | inference | T02 | synthetic fixture | fictional owner | none | Sequence supports intent. | Not measured. | none | controlled-reviewed |
| F05 | technical-architecture | Runtime latency target. | mechanism | NOT_APPLICABLE | repository | Skill-only fixture | synthetic fixture | N/A | none | No runtime service. | Not applicable. | none | controlled-reviewed |

### Review record

All claims are synthetic; no real-world adoption, impact, or ownership is asserted.
