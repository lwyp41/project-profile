# Module Registry

Project types recommend modules; user configuration selects their effective depth. Explicit module overrides win over a preset. Unknown module IDs or depths require clarification before investigation.

| ID | Purpose | Guidance |
|---|---|---|
| `project-overview` | Shape, lifecycle, main capability, and observable boundary. | `modules/project-overview.md` |
| `background-problem` | Triggering context, problem, and risk. | `modules/background-problem.md` |
| `users-stakeholders` | Intended/actual users and affected parties. | `modules/users-stakeholders.md` |
| `goals-success` | Goals, success conditions, and unverified targets. | `modules/goals-success.md` |
| `requirements-constraints` | Functional, operational, privacy, cost, policy, and compatibility constraints. | `modules/requirements-constraints.md` |
| `product-workflow` | Inputs, routing, human gates, handoffs, and outputs. | `modules/product-workflow.md` |
| `technical-architecture` | System boundaries, runtime, interfaces, integrations, and deterministic components. | `modules/technical-architecture.md` |
| `ai-agent-design` | LLM/prompt/tool/context/HITL/evaluation design. | `modules/ai-agent-design.md` |
| `information-data` | Sources of truth, provenance, data boundaries, and generated-output policy. | `modules/information-data.md` |
| `decisions-tradeoffs` | Constraints, alternatives, choices, rationale, and consequences. | `modules/decisions-tradeoffs.md` |
| `ownership-contribution` | Personal work, collaboration, maintenance, and AI-assistance boundary. | `modules/ownership-contribution.md` |
| `validation-qa` | Automated/manual validation, regression, and untested boundary. | `modules/validation-qa.md` |
| `outcomes-metrics` | Usage, scale, efficiency, quality, and measurement caveats. | `modules/outcomes-metrics.md` |
| `evolution-history` | Initial state, changes, migrations, and current state. | `modules/evolution-history.md` |
| `risks-limitations` | Failure modes, unresolved issues, risks, and evidence boundaries. | `modules/risks-limitations.md` |

## Presets

All applicable modules not listed below use `standard`; explicit user overrides win.

```yaml
resume:
  project-overview: brief
  users-stakeholders: brief
  background-problem: deep
  product-workflow: deep
  technical-architecture: standard
  ai-agent-design: deep
  information-data: standard
  decisions-tradeoffs: deep
  ownership-contribution: deep
  validation-qa: standard
  outcomes-metrics: deep
  evolution-history: deep
  risks-limitations: brief
technical:
  project-overview: brief
  background-problem: standard
  users-stakeholders: brief
  requirements-constraints: deep
  product-workflow: standard
  technical-architecture: deep
  ai-agent-design: deep
  information-data: deep
  decisions-tradeoffs: deep
  ownership-contribution: standard
  validation-qa: deep
  outcomes-metrics: standard
  evolution-history: standard
  risks-limitations: deep
balanced:
  project-overview: brief
  risks-limitations: brief
```
