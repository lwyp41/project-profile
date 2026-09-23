# Branch-loaded manual acceptance — PR #6

## Scope and method

This is a branch-loaded manual acceptance record for `fix/depth-observable-output`, using the frozen `SignalTriage` synthetic project and testimony fixture already committed under `evals/synthetic-agent-skill/`. It is **not an automated or model-runtime evaluation**: an operator loads the branch's `SKILL.md`, depth policy, rendering policy, module contracts, and fixture evidence, then checks the Review and final-render obligations below. The deterministic fixture remains a separate regression contract.

## Balanced

**Input:** select `Balanced` for the frozen synthetic project.

**Expected Standard behavior:** applicable modules remain Standard (except Brief overview and risks). The workflow is not reduced to an orientation: it exposes actors, the happy path, the approval handoff, the guarded path, and the evidence boundary. The available synthetic evidence supports an ordered intake → diagnosis → strategy approval → remediation-draft flow, but does not support adoption or outcome claims.

### Review disposition

| Module | Effective depth | Recovered coverage | Proposed render destination |
|---|---|---|---|
| product-workflow | standard | actors, happy path, approval handoff, guarded path, evidence boundary | Workflow and controls |
| decisions-tradeoffs | standard | constraint, choice, intended consequence, rationale boundary | Decisions and evidence limits |
| validation-qa | standard | approval control, verification boundary, unmeasured quality | Validation boundaries |

### Final rendering

#### Workflow and controls

SignalTriage screens intake before deeper diagnosis, then requires strategy approval before a remediation draft. The approval handoff is the guard against drafting before review; the fixture does not establish a quality or efficiency outcome.

#### Decisions and evidence limits

The ordering is an evidenced design intent to focus deeper diagnosis. No measured consequence is supplied, so the final profile preserves that boundary rather than claiming improvement.

#### Validation boundaries

The approval gate is an implemented control. It proves the workflow requirement, not whether the control improved outcomes in use.

## Custom

**Input:** `全部 standard；6,7,8,10,12,14 deep；11 brief`.

The numeric selectors normalize to `product-workflow`, `technical-architecture`, `ai-agent-design`, `decisions-tradeoffs`, `validation-qa`, and `evolution-history` at Deep; `ownership-contribution` is Brief; other applicable modules are Standard. Canonical IDs are not required for this input.

### Review disposition

| Module | Effective depth | Recovered coverage | Proposed render destination |
|---|---|---|---|
| technical-architecture | deep | boundary, deterministic control, runtime limitation, validation boundary | Architecture and runtime |
| product-workflow | deep | public entry, state handoff, approval gate, guarded path | Workflow and controls |
| ai-agent-design | deep | deterministic instruction route, context boundary, approval gate, model-detail gap | Agent controls and limits |
| decisions-tradeoffs | deep | constraint, choice, supported design intent, missing measured consequence | Decisions and evidence limits |
| validation-qa | deep | automated contract checks, approval control, unmeasured quality, validation boundary | Validation boundaries |
| evolution-history | deep | initial profile state, v2 migration, current evidence-ledger state, pre-repository uncertainty | Evolution and current state |

### Final rendering

#### Architecture and runtime

The branch's profile workflow has a deterministic validator and an evidence ledger boundary. It validates profile structure and evidence states, but does not establish a runtime service, deployment behavior, adoption, or reliability outcome.

#### Workflow and controls

The public mode-selection path hands recovered facts through review approval before final rendering. A missing user-answerable rationale takes the guarded `CLARIFICATION_REQUIRED` path rather than being added as prose.

#### Agent controls and limits

SignalTriage's declared route is an instruction-driven intake, diagnosis, approval, and drafting workflow with deterministic evidence controls. The frozen fixture does not identify a model, autonomy level, or production runtime, so those remain explicit evidence gaps rather than inferred AI behavior.

#### Decisions and evidence limits

The evidence-first workflow chooses review before final prose to prevent unsupported downstream claims. The frozen fixture supports the intent and approval control; it provides no measured outcome, which remains visible as a boundary.

#### Validation boundaries

The branch's unit tests and profile validator check the profile contract, while the workflow approval gate controls drafting. These checks do not establish end-to-end quality, adoption, or a measured failure rate, so the Deep render preserves their verification boundary.

#### Evolution and current state

The current v2 state uses explicit evidence statuses and a canonical ledger. The available synthetic fixture does not establish pre-repository project history, so that earlier state remains uncertain instead of being reconstructed from commit count.

## Acceptance result

The branch-loaded manual run confirms that Balanced Standard produces a substantive workflow/decision/validation account; Custom Deep makes architecture, workflow, Agent controls, decisions, validation, and evolution individually visible in both Review and final sections; and every material destination above resolves to a final rendered heading. This is a manual behavior acceptance supplement, not a substitute for future live/model-output evaluation.
