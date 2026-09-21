# 项目画像：`incident-triage`

> 状态：完整的 Skill 包<br>
> 主要类型：`AGENT_SKILL`<br>
> 证据日期：示例样本

这是一份用于校验中文表达的虚构示例，不对应真实项目，也不用于证明任何实际成果。

> 配置：`purpose: balanced`；`project-overview: brief`；`product-workflow: standard`；`validation-qa: standard`；`outcomes-metrics: brief`。

## 它解决的不是“把工单写得更漂亮”

`incident-triage` 的目标是在问题被交给开发前，先把范围和复现信息核实清楚，再输出可继续处理的分诊摘要。这样做的重点不在于自动生成更多文字，而在于把“先验证、后交接”的顺序固定下来。[事实：`SKILL.md` 的目标与工作流]

现有材料可以证明这套流程被写进了 Skill，但无法证明团队是否采用过它，也无法证明它缩短了分诊时间。这两项保留为未知，不把合理期待写成已发生的收益。

## 工作流如何落地

Skill 会收集报障信息，检查范围和复现细节，完成分类后再生成结构化摘要。参考资料定义了摘要需要包含的字段，示例展示了预期交付物；约束同时要求不要接受未经验证的复现结论，也不要把超出范围的请求直接当作实施授权。[事实：`SKILL.md`、`references/`、`examples/`]

从流程顺序可以推断，它试图减少“尚未确认就开始实现”的情况；但没有效果数据，因此这一点只能作为设计意图，而不能写成实际改进。[推断：工作流顺序；缺少结果指标]

## 供下游使用的事实包

| 情境 / 问题 | 工作或决策 | 产物 / 机制 | 已观察到的结果 | 范围与归属 | 证据位置 | 使用限制 |
|---|---|---|---|---|---|---|
| 问题报告可能在范围和复现情况尚未核实前就进入开发。 | 将分类和验证设为交接前置条件。 | 有序的 Skill 工作流与结构化分诊摘要。 | 未知：没有采用率或耗时数据。 | 此示例未说明作者归属。 | `SKILL.md` 的工作流标题。 | 不能据此写“缩短分诊时间”或“被团队采用”。 |
| 报告可能包含未验证的复现结论，或本身超出处理范围。 | 增加显式的拒绝边界。 | 约束与停止条件。 | 未知：没有误判率或失败率数据。 | 此示例未说明作者归属。 | `SKILL.md` 的约束。 | 它证明的是预期行为，不是实际效果。 |

---

## 证据附录

### 证据覆盖情况

| 类别 | 数量 | 说明 |
|---|---:|---|
| VERIFIED | 1 | 示例台账中的流程主张 |
| INFERRED | 1 | 流程顺序可能减少过早实施 |
| CLARIFICATION_REQUIRED | 0 | 这是虚构样例，未发起用户访谈 |
| UNKNOWN | 1 | 采用与结果证据无法建立 |
| NOT_APPLICABLE | 1 | 运行时 API 延迟指标 |
| CONFLICTING | 0 | 未发现冲突来源 |

覆盖度说明证据是否可得，不代表项目质量或实际影响。

### 模块覆盖情况

| 模块 | 适用性 | 深度 | 已检查来源 | 事实编号 | 渲染决定 |
|---|---|---|---|---|---|
| project-overview | 适用 | brief | `SKILL.md` | E1 | 已渲染 |
| product-workflow | 适用 | standard | `SKILL.md`、`references/`、`examples/` | E1–E2 | 已渲染 |
| outcomes-metrics | 适用 | brief | 示例叙述 | E3 | 仅渲染边界 |
| technical-architecture | 不适用 | off | 无 | E4 | 已省略 |

### 证据记录

<!-- project-profile-ledger: v2 -->

| ID | 模块 | 结论 / 字段 | 主张类型 | 状态 | 来源类型 | 证据位置 | 时间语境 | 归属 | 指标 | 理由 | 限制 | 冲突 | 审阅状态 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E1 | product-workflow | Skill 在完成分类和复现检查后输出分诊摘要。 | mechanism | VERIFIED | repository | `SKILL.md` 的目标与工作流 | 示例样本 | 未说明 | 无 | — | 流程直接陈述。 | 无 | controlled-reviewed |
| E2 | decisions-tradeoffs | 此顺序意在减少未验证就实施的情况。 | design_intent | INFERRED | inference | 有序检查 | 示例样本 | 未说明 | 无 | — | 流程可支持设计意图，不能证明实际效果。 | 无 | controlled-reviewed |
| E3 | outcomes-metrics | 采用情况和耗时变化。 | observed_outcome | UNKNOWN | repository | 没有指标或用户证词 | 示例样本 | 不适用 | 无 | — | 相关但无法建立。 | 无 | unresolved |
| E4 | technical-architecture | 运行时 API 延迟目标。 | mechanism | NOT_APPLICABLE | repository | 仅有 Skill 产物 | 示例样本 | 不适用 | 无 | — | 没有运行时 API。 | 无 | controlled-reviewed |

### 审阅记录

- 用户审阅状态：示例样本；无需批准。
- 已接受的修正：无。
- 明确的 Unknown / N/A 决定：采用和耗时为 UNKNOWN；API 延迟为 NOT_APPLICABLE。
- 剩余冲突：无。
