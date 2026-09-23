# Module Registry

Project types recommend modules; the user-selected profile mode determines the preset or Custom baseline, and explicit module overrides select effective depth. Unknown module IDs or depths require clarification before investigation.

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

## Custom selector normalization

Canonical IDs are valid but optional user input. During Custom onboarding, resolve a number, localized label, accepted alias, or canonical ID to the ID below before applying the depth. Accept localized natural-language group expressions (for example, `架构、流程、Agent、决策、验证、演进`) and `全部` / `其他` as default-plus-overrides. Ask only if a reference remains ambiguous after this normalization.

| Numeric selector | Chinese label | Accepted aliases | Canonical ID |
|---|---|---|---|
| 1 | 项目概览 | 概览, overview | `project-overview` |
| 2 | 背景与问题 | 背景, 问题 | `background-problem` |
| 3 | 用户与相关方 | 用户, 相关方 | `users-stakeholders` |
| 4 | 目标与成功标准 | 目标, 成功标准 | `goals-success` |
| 5 | 需求与约束 | 需求, 约束 | `requirements-constraints` |
| 6 | 产品与流程 | 流程, 工作流 | `product-workflow` |
| 7 | 技术架构 | 架构 | `technical-architecture` |
| 8 | AI / Agent 设计 | Agent, AI, 智能体 | `ai-agent-design` |
| 9 | 信息与数据 | 信息, 数据 | `information-data` |
| 10 | 决策与取舍 | 决策, 取舍 | `decisions-tradeoffs` |
| 11 | 个人贡献 | 贡献, 所有权 | `ownership-contribution` |
| 12 | 验证与 QA | 验证, QA, 测试 | `validation-qa` |
| 13 | 成果与指标 | 成果, 指标 | `outcomes-metrics` |
| 14 | 项目演进 | 演进, 历史 | `evolution-history` |
| 15 | 风险与限制 | 风险, 限制 | `risks-limitations` |

Normalize depth clauses in user order; an explicit module override wins over `全部`/`其他` defaults. Equivalent tables and aliases must be localized for other request languages.

## Profile modes

A profile mode must be selected explicitly before discovery begins.

- `balanced`: general-purpose reconstruction across applicable modules.
- `resume`: deeper career-evidence reconstruction, especially Ownership, Scale, Complexity, Decision, Impact, and Iteration.
- `technical`: deeper architecture, constraints, AI/agent design, information boundaries, validation, and risks.
- `custom`: user-defined module/depth configuration. Custom is first-class and must never be silently rewritten as Balanced.

## Preset depths

For preset modes, all applicable modules not listed below use `standard`; explicit user overrides win.

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

For `custom`, do not apply one of the preset maps first. The visible default baseline is `standard` unless the user explicitly sets another `default depth`; apply that baseline to unspecified applicable modules, then apply explicit per-module overrides (which always win). Do not hide this baseline during onboarding. Clarify only unknown module IDs, invalid depths, or ambiguities that materially change investigation.
