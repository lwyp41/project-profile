# Project Profile v2 设计方案

> 阶段：Phase 1 — 待批准的设计
>
> 设计依据优先级：用户当前指令 → `docs/development/MASTER_PLAN.md` → `evals/GOLDEN_EVAL_SPEC.md` → 本文档 → 当前 v1 实现。
>
> 本文档只定义实施方案；除新增本文档外，未修改现有 Skill、参考资料、模板、示例或测试。

## 1. 设计结论

v2 应从“证据优先的项目叙事生成器”升级为“可配置的项目事实重建系统”。核心变化不是增加固定章节或延长正文，而是在写作前完成有来源、状态、时间、归属和边界的模块化事实重建。`PROJECT_PROFILE.md` 仍是唯一的正式交付物与下游接口；它要包含易读的选择性模块正文、可复用事实包和完整证据附录。

v1 的证据纪律必须原样保留：六种状态、证据定位、负面证据、冲突、`UNKNOWN`/`NOT_APPLICABLE` 区分、先调查后访谈、用户复核后生成。v2 补足的能力是：模块和深度控制、时间线、决策链、归属、真实使用/结果、面向简历用途的六项职业信号，以及跨预设的可验证差异。

## 2. 当前状态诊断

### 已验证的 v1 基础

| 现有能力 | 证据 | v2 处置 |
|---|---|---|
| 十一步调查—访谈—审阅工作流 | `SKILL.md` 的 Operating contract 与 Workflow | 保留顺序约束，扩展为模块化重建流水线。 |
| 六种证据状态和强制缺口转换 | `references/evidence-policy.md` | 原样保留为跨所有模块的硬性政策。 |
| 自适应项目类型与条件分析 | `SKILL.md`、`references/extraction-patterns.md` | 改为“项目类型路由器”，不再隐式决定正文模板。 |
| 可读叙事 + 事实包 + 审计附录 | `references/profile-schema.md`、模板 | 保留，改为从事实模型和启用模块渲染。 |
| 原生语言写作与本地化标题 | `SKILL.md` | 保留，且适用于访谈、模块标题和评审。 |
| 以文档为主的最低回归检查 | `tests/README.md` | 迁移为可执行静态检查加 fixture/eval 断言。 |

### 当前限制及其根因

| 症状 | 根因 | v2 的设计回应 |
|---|---|---|
| 产物可审计但可能“正确而单薄” | 单一叙事 schema 在事实重建前就引导压缩 | 先建立模块覆盖图和规范化事实模型，再渲染。 |
| 演进、决策、归属、结果不是独立调查对象 | 现有 workflow 只有泛化的知识提取/缺口发现 | 增加四个明确的重建步骤和相应模块指导。 |
| 访谈只围绕一般缺口 | 没有与用途相连的信号清单 | `resume` 必查 Ownership、Scale、Complexity、Decision、Impact、Iteration。 |
| 项目类型同时影响“看什么”和“写什么” | 条件 schema 与项目类型耦合 | 类型只选择高信号来源、模块推荐和访谈路由。 |
| 深度不可配置、也无法验证调查差异 | 没有调查预算/来源范围语义 | 定义 `off`/`brief`/`standard`/`deep` 的检索与访谈行为。 |
| 下游事实包过于扁平 | 它既是重用数据又承担全部知识承载 | 将其降为从 Canonical Fact Model 投影出的精选接口，完整事实仍由模块正文和 ledger 保留。 |
| 回归只检查规则存在 | 没有受控 fixture、覆盖矩阵或基线差异 | 建立合成 Agent Skill 黄金场景及软件、稀疏项目矩阵。 |

### 当前仓库边界

设计阶段的仓库只有 Markdown Skill 包、参考资料、模板、双语示例及说明性测试；当时未发现运行脚本或 fixture 项目。设计输入现归档在 `docs/development/` 与 `evals/`，须保留而不由运行实现覆盖。历史版本显示 v1 最近演进集中在本地化写作、安装文档与 `UNKNOWN` 前的访谈闸门。

## 3. v1 → v2 架构映射

```text
用户意图 / 可选配置
        ↓
来源发现 → 类型路由 → 模块 + 深度选择 → 模块覆盖图
        ↓
按模块提取 artifact evidence
        ↓
时间线 ─┬─ 决策链 ─┬─ 归属 ─┬─ 结果/规模
        ↓          ↓         ↓
Canonical Fact Model（唯一的事实重建层）
        ↓
缺口排序 → 模块/用途驱动的渐进访谈 → 事实模型更新
        ↓
证据验证 → 用户复核闸门
        ↓
选择的知识模块正文 + 下游事实包 + 证据附录
        ↓
PROJECT_PROFILE.md
```

| v1 概念 | v2 对应物 | 关键变化 |
|---|---|---|
| Adaptive Analysis Mode | 项目类型路由 + Module Registry | 由类型推荐调查路线，不强制展示章节。 |
| Evidence Map | Module Coverage Map + Canonical Fact Model | 前者管理调查范围和缺口，后者保留全部可重用事实。 |
| Extract Verified Knowledge | 模块化证据提取 + 四项横向重建 | 每个事实必须归入模块；时间、决策、归属、结果可跨模块关联。 |
| Progressive Interview | gap-driven + module-driven + purpose-driven interview | 简历预设将六项职业信号作为必查队列。 |
| Adaptive narrative | Canonical Profile Rendering | 只渲染启用且适用的模块，但绝不因正文精简丢弃已重建事实。 |
| Career-relevant signals | `resume` 用途的受证据约束检查 | 不产生简历文案，也不推定作者归属。 |

## 4. 配置、模块注册表与类型路由

### 4.1 配置解析规则

v2 接受自然语言请求或可选的 `profile-config.yaml`。解析结果按下列优先级合并：

1. 用户显式模块/深度覆盖；
2. 用户显式 `purpose`；
3. 与已分类项目类型相匹配的预设推荐；
4. `balanced` 默认值。

`purpose` 仅影响调查优先级和默认深度，不能改变事实状态、证据规则、正文语言或非宣传性边界。未知模块 ID、未知深度、或互相矛盾的覆盖必须在开始调查前以一条简洁问题澄清；不能静默猜测。`off` 明确优先于预设。类型不适用的模块不会被强行打开；若用户显式要求，保留为 `NOT_APPLICABLE` 或解释受限调查范围。

建议配置契约：

```yaml
purpose: balanced # resume | technical | balanced
default_depth: standard
modules:
  decisions-tradeoffs: deep
  outcomes-metrics: off
```

### 4.2 Module Registry

每项模块指导都必须定义：调查目标、适用性线索、brief/standard/deep 的来源范围、要产生的事实字段、访谈触发器、`NOT_APPLICABLE` 判定、渲染建议和常见不当推断。模块不等于固定标题；它是事实重建的工作单元。

| ID | 目标与主要事实 | 典型高信号证据 |
|---|---|---|
| `project-overview` | 项目形态、生命周期、主要能力、可观察边界 | README、入口、元数据、版本记录 |
| `background-problem` | 触发背景、要解决的风险/问题 | README、需求/设计文档、用户说明、历史 |
| `users-stakeholders` | 目标/实际使用者、受影响方、权限边界 | 文档、配置、用户证词；无证据不推定采用 |
| `goals-success` | 目标、成功条件、未验证目标 | 需求、验收、评估、用户证词 |
| `requirements-constraints` | 功能、非功能、隐私、成本、兼容性、政策约束 | 规则、配置、错误/降级路径、历史 |
| `product-workflow` | 输入、步骤、路由、交接、人工闸门、输出 | 入口指令、流程图、示例、测试 |
| `technical-architecture` | 模块/边界、运行时、接口、集成、确定性组件 | 源码、manifest、配置、脚本、测试 |
| `ai-agent-design` | LLM/Prompt/工具/上下文/HITL/评估及 AI 与确定性职责划分 | prompts、工具定义、路由、评估与安全规则 |
| `information-data` | 来源、数据/事实边界、存储/检索、生成物政策 | schemas、来源清单、数据文档、隐私规则 |
| `decisions-tradeoffs` | constraint → alternatives → choice → rationale → consequence | ADR、历史、注释、用户证词；缺 rationale 则提问 |
| `ownership-contribution` | 个人设计、实现、维护、协作边界 | 提交历史、署名、用户证词；仓库归属不足以证明个人贡献 |
| `validation-qa` | 自动/人工验证、回归、结构/视觉检查及未覆盖处 | 测试、eval、CI、脚本、QA 文档 |
| `outcomes-metrics` | 使用、规模、效率、质量、业务/运营结果及测量限制 | 指标、日志、报告、用户证词；指标需完整上下文 |
| `evolution-history` | 初始状态 → 首版 → 问题 → 变化/迁移 → 当前状态 | Git、changelog、旧文件、旧 prompts、用户证词 |
| `risks-limitations` | 已知故障、未解问题、证据边界、风险控制 | issue、限制说明、失败路径、缺口/冲突 ledger |

### 4.3 项目类型路由

保留九种类型：`SOFTWARE`、`AI_AGENT`、`AGENT_SKILL`、`PROMPT_SYSTEM`、`LIBRARY`、`DATA_PROJECT`、`RESEARCH_PROJECT`、`DOCUMENTATION_PROJECT`、`SPARSE_ARTIFACT`。允许多标签，但要求记录主/次类型、证据和置信边界。

类型路由文件只给出三件事：推荐模块、优先检查的来源、常见访谈问题。例如 `AGENT_SKILL` 强调 `product-workflow`、`ai-agent-design`、`information-data`、`decisions-tradeoffs`、`validation-qa`、`evolution-history` 与 `ownership-contribution`；`SOFTWARE` 强调 constraints、architecture、integrations、QA 与运营边界。类型不得生成固定模板，也不能使不适用模块看起来像缺失。

## 5. 深度政策

深度是每个模块的调查承诺，不是篇幅开关。所有等级都要遵守证据政策；差异只在搜索广度、交叉验证、历史考古和访谈主动性。

| 深度 | 调查行为 | 访谈与渲染 |
|---|---|---|
| `off` | 不独立调查；仅在解释其他已启用模块不可避免时记录交叉事实。 | 不渲染该模块；不因关闭而错误标为 `UNKNOWN`。 |
| `brief` | 查明显高信号来源，恢复 2–4 个最高价值事实；仅为实质冲突检查历史。 | 只有缺失信息阻碍正确解释时才提问；正文只保留核心事实和必要边界。 |
| `standard` | 查主来源、相关 docs/examples/tests；恢复机制、主要选择、结果和限制（适用时）。 | 对仍缺的实质事实发起聚焦访谈；渲染机制与证据边界。 |
| `deep` | 查实现、参考、示例、测试、生成物、Git、旧版本/变更记录、冲突来源与替换方案。 | 系统性追问可由用户回答的演进、替代、理由、归属、规模、结果与失败模式；正文保留可解释的因果链。 |

可验证性：eval 必须在同一项目的 `ai-agent-design`、`outcomes-metrics`、`evolution-history` 三模块比较三个深度的“查阅来源集合、提取事实集合、提出的问题集合”，而非仅比较字符数。

## 6. 预设定义

所有未列出且适用的模块使用 `default_depth: standard`；项目类型不适用时关闭或注明 N/A。显式覆盖永远优先。

### `resume`

```yaml
purpose: resume
default_depth: standard
modules:
  project-overview: brief
  background-problem: deep
  users-stakeholders: brief
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
```

额外硬闸门：在最终复核前检查 Ownership、Scale、Complexity、Decision、Impact、Iteration 六项信号。每项先搜证据；若实质且可由用户回答，进入 `CLARIFICATION_REQUIRED` 问题队列；未问不能降为 `UNKNOWN`。输出仍是中性项目事实，不是候选人简历 bullet。

### `technical`

```yaml
purpose: technical
default_depth: standard
modules:
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
```

重点是架构、来源边界、AI/确定性责任切分、验证、人机闸门、失败处理、兼容性和隐私；不能只是 Resume 版本扩写技术段落。

### `balanced`

```yaml
purpose: balanced
default_depth: standard
modules:
  project-overview: brief
  risks-limitations: brief
```

其余适用模块为 `standard`。此预设不额外开启简历六信号闸门，但仍对所有实质可回答缺口执行现有访谈政策。

## 7. Canonical Fact Model 与渲染契约

### 7.1 事实模型

在任何正文起草前，Agent 必须维护每条实质事实的结构化记录。它是工作流的内部权威模型；正式交付时完整地投影到 `PROJECT_PROFILE.md` 的 evidence ledger，精选地投影到正文和下游事实包。默认不另存含用户敏感信息的原始事实文件，避免扩大项目资料暴露面；eval 可另存简化的 `claims.json`。

```yaml
id: F-001
module: decisions-tradeoffs
claim: 候选人事实与岗位研究被分离管理。
status: VERIFIED
source_kind: repository # repository | documentation | git_history | user | inference | external_reference
source_locator: references/source-policy.md#candidate-facts
observed_fact: 来源清单限制岗位研究不能作为候选人事实。
time_context: local-agent-stage
ownership: UNKNOWN
metric: null # {value, unit, scope, time_window, measurement_method}
rationale: 直接规则；不推定实际执行效果。
caveat: 设计机制不等于已测量的错误率下降。
conflict: null
related_fact_ids: [F-018]
review_state: pending # pending | user-confirmed | user-corrected | accepted-unresolved
```

规则：

- `status` 是事实状态，不能由 prose 的修辞替代；
- `source_kind` 与 `source_locator` 对所有 `VERIFIED` 事实必填；用户事实要标明访谈轮次/回答；
- `INFERRED` 必须保留观察和推理；
- metric 若有，必须带 value、unit、scope、time window 和 source；缺项须作为不完整/未知处理；
- `ownership` 是单独字段，不能从代码库位置反推；
- `conflict` 记录相互矛盾的事实 ID/来源，不能静默选边；
- 模块的 `NOT_APPLICABLE` 是有理由的适用性结论；关闭模块不等于 N/A。

### 7.2 Module Coverage Map

事实模型之前维护一张调查控制表：模块、适用性、有效深度、优先来源、已检查来源、已获得事实 ID、实质缺口、访谈候选、渲染决定。它允许评估“deep 是否真的查得更多”，也使遗漏对用户复核可见。

### 7.3 输出投影

`PROJECT_PROFILE.md` 由以下投影组成：

1. 项目概览；
2. 已启用且适用的知识模块（可合并、可本地化、不可出现空占位）；
3. 中性下游事实包：Situation/problem、Work/decision、Artifact/mechanism、Observed result、Scope/ownership、Evidence locator、Caveat；
4. 证据附录：Coverage、Unknown/N/A/Conflicts、完整 claim ledger、Review record。

事实包是接口而非主数据库：任何单元不能混合无关事实，也不能将机制写成影响、将项目存在写成个人贡献，或改写成第一人称营销文案。

## 8. 访谈与复核重设计

### 8.1 调查—访谈顺序

```text
调查模块来源 → 记录事实及缺口 → 按材料价值排序问题
→ 每轮 3–5 个问题（说明原因）→ 更新事实模型
→ 再调查/处理冲突（必要时）→ 用户复核 → 渲染最终档案
```

问题选择排序：是否改变实质解释/安全性/下游可用性 → 是否无法由资料恢复 → 用户是否易准确回答 → 是否解决冲突。接受“不知道”“不记得”“不适用”“否”；分别按既有 evidence policy 转换状态。

### 8.2 模块特异性

- `decisions-tradeoffs` 按“constraint → alternatives → chosen approach → rationale → consequence”提取；机制存在但原因缺失时，不造理由，标 `CLARIFICATION_REQUIRED`。
- `evolution-history` 强制尝试“初始状态 → 首版 → 发现的问题 → 重大变化/迁移 → 当前状态”；不能只描述当前目录。
- `ownership-contribution` 区分作者、维护者、协作者和模型辅助；缺失时问而不归因。
- `outcomes-metrics` 区分目标、用户主观观察、已测量结果和业务影响；没有可靠测量不能被升级。
- `resume` 追加六信号问题队列；`technical` 追加运行时、来源、验证、失败处理、隐私和兼容性问题队列。

### 8.3 用户复核闸门

复核材料必须展示：主要事实与状态、模块覆盖/关闭原因、下游事实包、待澄清项、拟定 Unknown/N/A、冲突、对简历预设的六信号覆盖。用户确认、纠正或明确接受未解决标签后，才可生成最终档案。用户明确要求保留未解决项时，记录为 `accepted-unresolved`，不能伪装为已验证。

## 9. 黄金评估设计

### 9.1 评估矩阵

| Fixture | `resume` | `technical` | 主要验证 |
|---|---|---|---|
| Synthetic Agent Skill | 必须 | 必须 | 受控基线覆盖、工作流/来源/QA 差异 |
| Software fixture | 必须 | 必须 | 代码/测试/架构丰富，但业务证据可稀少 |
| Sparse fixture | 必须 | 必须 | 聚焦访谈、防幻觉、Unknown/N/A 正确性 |

合成 Agent Skill 是第一门槛，不取代后两个 fixture。执行阶段必须将合成基线与任何真实仓库证据分开：合成内容仅用于覆盖回归，不是自动验证来源，也不得升级为真实项目事实。

### 9.2 合成 Agent Skill 产物

```text
evals/synthetic-agent-skill/
  README.md
  input/testimony-fixture.md
  resume-profile-v2.md
  technical-profile-v2.md
  coverage-matrix.md
  baseline-diff.md
  unresolved-facts.md
  coverage.json              # optional
  claims.json                # optional
```

`coverage-matrix.md` 按 100 分 instrumentation 权重追踪背景、定位、需求、工作流、AI、技术、信息边界、演进、归属、决策、QA、结果；不得将此分数展示为项目质量。每个旧基线事实在 `baseline-diff.md` 标为 `PRESERVED`、`IMPROVED`、`PARTIALLY_PRESERVED`、`LOST` 或 `CORRECTLY_REMOVED_AS_UNSUPPORTED`，并附 v2 位置和理由。任一有证据且高价值的 `LOST` 即失败。

### 9.3 关键断言

- 支持的合成基线覆盖不下降；Ownership 与 Decisions 必须优于基线；不支持的实质声明为零。
- 合成 fixture 的用户证词只用于验证来源、状态和定位规则；不得产生或暗示真实项目的使用、效率或结果。
- 捕捉候选人事实/岗位研究/生成物的三类边界，以及 employer research、策略确认、结构验证、视觉 QA、语义职位路由、角色规范、隐私/可分享性和兼容性（均以实际仓库证据为条件）。
- Resume 与 Technical 输出的有效深度、检查来源、问题队列、事实重点和正文必须可见不同。
- 对至少三模块验证 `brief`/`standard`/`deep` 的来源、事实和问题集合递进；仅文本变长为失败。
- 下游就绪审查：Resume 无须重查仓库即可开始产生准确候选人表述；Technical 无须逐文件重开即可理解结构、AI/确定性分工、来源控制、验证和技术边界。

### 9.4 自动化与人工审查分工

静态/结构校验可检查：六状态、配置合法性、启用模块的 coverage 行、ledger 必填列、指标字段、review record、禁止字词/无来源声明的候选提示、预设和深度选择记录。它们不能单独判断事实是否真实或叙事是否有用。

人工/agent 评审必须检查：逐项 baseline diff、来源与主张是否匹配、推断是否越界、采访是否遗漏可回答问题、预设差异、深度调查证据、自然语言质量和下游独立性。

## 10. 拟议仓库结构

```text
SKILL.md
references/
  evidence-policy.md
  depth-policy.md
  module-registry.md
  interview-policy.md
  rendering-policy.md
  modules/
    project-overview.md
    background-problem.md
    users-stakeholders.md
    goals-success.md
    requirements-constraints.md
    product-workflow.md
    technical-architecture.md
    ai-agent-design.md
    information-data.md
    decisions-tradeoffs.md
    ownership-contribution.md
    validation-qa.md
    outcomes-metrics.md
    evolution-history.md
    risks-limitations.md
  project-types/
    agent-skill.md
    ai-agent.md
    software.md
    prompt-system.md
    library.md
    data-project.md
    research-project.md
    documentation-project.md
    sparse-artifact.md
templates/
  PROJECT_PROFILE.md
  profile-config.yaml
scripts/
  validate_profile.py
evals/
  evals.json
  synthetic-agent-skill/     # public controlled regression artifacts
examples/
tests/
README.md
CHANGELOG.md
LICENSE
```

为了避免为极短指导机械拆文件，实施时允许把较短模块合并到一个明确命名的模块文件；但 `module-registry.md` 必须保持每个 ID 到其指导位置的一对一映射。`SKILL.md` 只作协调器：目的/边界、执行流水线、路由、配置、证据规则、访谈与复核闸门、输出契约和按需加载指令。细节不回填到它。

## 11. 逐文件迁移计划

| 当前文件 | 分类 | v2 角色与变更理由 | 依赖 |
|---|---|---|---|
| `SKILL.md` | REFACTOR | 精简为 orchestrator；加入 intent/config、模块/深度选择、事实模型、四项重建、按需引用与输出闸门。 | registry、depth、interview、rendering、type refs |
| `references/evidence-policy.md` | REFACTOR | 保留六状态和缺口转换；补充 fact-model 必填证据、指标/归属/冲突规则。 | `SKILL.md`、validator |
| `references/profile-schema.md` | REPLACE | 用 module-aware rendering policy/schema 取代 v1 叙事优先 schema。 | registry、template |
| `references/interview-protocol.md` | REFACTOR | 模块 + 用途 + 缺口驱动；加入六信号和 review 输入。 | registry、depth、type refs |
| `references/architecture-analysis.md` | REFACTOR | 收敛为 `technical-architecture` 与 AI/类型路由共享的结构调查准则。 | modules、project-types |
| `references/extraction-patterns.md` | REPLACE | 拆为 project-type 路由与模块来源指导，避免单一泛化清单。 | registry、project-types |
| `templates/PROJECT_PROFILE.md` | REPLACE | 反映概览、选择模块、事实包、coverage、unknown/N/A/conflicts、完整 ledger、review；无固定空段。 | rendering policy、fact model |
| `examples/example-skill-project-profile.md` | REFACTOR | 英文示例展示配置选择、模块化正文、事实包与完整审计边界。 | template、evidence policy |
| `examples/example-skill-project-profile.zh-CN.md` | REFACTOR | 与英文示例语义等价但中文原生行文；验证本地化。 | template、evidence policy |
| `tests/README.md` | REPLACE | 从最小文档清单升级为测试计划、fixture matrix、静态和定性检查说明。 | scripts、evals |
| `README.md` | REFACTOR | 更新定位、选择配置、预设、深度语义、交付物和 eval 边界。 | 完成后的 Skill/示例 |
| `CHANGELOG.md` | RETAIN | 记录批准后 v2 变更；不在 Phase 1 添加实现发布条目。 | 实施完成 |
| `LICENSE` | RETAIN | 许可证不变。 | 无 |
| `docs/development/MASTER_PLAN.md` | RETAIN | 最高优先级设计规格，不由实现改写。 | 无 |
| `evals/GOLDEN_EVAL_SPEC.md` | RETAIN | 质量与回归规格，不由实现稀释。 | evals |
| `docs/development/V2_DESIGN.md` | ADD | Phase 1 的批准对象与实施蓝图。 | 用户批准 |
| `references/depth-policy.md` | ADD | 规范调查深度、记录和验证语义。 | SKILL、validator、eval |
| `references/module-registry.md` | ADD | 模块 ID、适用性、默认/预设映射和指导索引。 | SKILL、module refs |
| `references/interview-policy.md` | ADD | 若迁移时将其从旧文件改名；承载 v2 访谈契约。 | SKILL、registry |
| `references/rendering-policy.md` | ADD | 事实模型到可读档案/附录的投影规则。 | template、SKILL |
| `references/modules/*` | ADD | 每模块调查与访谈细则。 | registry、depth |
| `references/project-types/*` | ADD | 类型路由、证据优先级和常见问题。 | registry |
| `templates/profile-config.yaml` | ADD | 用户可复制的配置示例及注释。 | registry、presets |
| `scripts/validate_profile.py` | ADD | 结构/状态/ledger/指标/配置静态检查；不替代事实评审。 | template、policy |
| `evals/evals.json` | ADD | 六场景及断言的机器可读索引。 | fixtures、validator |
| `evals/synthetic-agent-skill/*` | ADD | 合成黄金输入、两份产出、矩阵、差异与未解事实。 | 公开合成 fixture |
| `docs/development/DECISIONS.md` | ADD（批准后） | 仅记录批准架构决策、替代方案和偏离原因。 | 用户批准 |

## 12. 实施顺序与验收闸门

批准后的 Phase 2 应按以下可回滚的小批次执行：

1. 创建 `docs/development/DECISIONS.md`，固定获批设计和任何批准后的偏离；建立 registry、depth、rendering 与 interview policy。
2. 重构 `SKILL.md` 为引用这些政策的协调器；迁移证据政策，保留六状态与现有安全规则。
3. 添加项目类型和模块指导，以及配置模板；更新 profile 模板与双语示例。
4. 添加 validator、eval manifest 和测试说明；建立三个 fixture × 两预设的评估流程。
5. 使用受控合成输入执行黄金评估，生成 baseline diff；逐项解决高价值回归。
6. 更新 README/CHANGELOG；运行静态检查与完整 eval matrix，并进行人工质量审阅。

通过条件：所有 Master Plan Definition of Done 项均满足；无高价值支持事实丢失；实质不支持声明为零；Resume/Technical 与三档深度有可审计的调查差异；下游可从 `PROJECT_PROFILE.md` 开始工作，而非重新逆向原仓库。

## 13. 风险与待批准设计决策

| 项目 | 风险/未决点 | 本设计的建议 | 需要的批准 |
|---|---|---|---|
| 敏感事实持久化 | 独立 fact file 可能把用户资料扩散到仓库 | 默认仅在 Agent 工作内存维护模型，并将受控 ledger 写入正式档案；eval 才允许简化 JSON。 | 确认 |
| 配置体验 | 每次强制选择 15 项模块会提高门槛 | 默认 `balanced`，允许自然语言与 YAML 覆盖；只有歧义时提问。 | 确认 |
| 模块文件粒度 | 15 个文件可能产生导航负担 | 先以注册表索引；短指导可合理合并，但不可丢失独立 ID 语义。 | 确认 |
| `profile-schema.md` 迁移 | 替换旧 schema 可能损失可读叙事约束 | 以 rendering policy 保留自然语言、选择性章节与附录契约。 | 确认 |
| 黄金量化指标 | 真实使用或效率指标不应进入公开回归 | 合成 fixture 不含真实量化结果；任何未支持指标保留为 UNKNOWN。 | 确认 |
| 归属结论 | Git/仓库位置不足以区分个人、协作和 AI 辅助工作 | 使用单独 ownership 字段和专门访谈；默认不归属。 | 确认 |
| 静态 validator 误判 | 关键词检查不能验证语义真实性 | validator 只做结构提醒；黄金 diff 和人工审查拥有最终否决权。 | 确认 |
| `docs/development/DECISIONS.md` 时间点 | Master Plan 要求维护决策日志，但当前用户限制 Phase 1 只产出设计文档 | 依当时明确指令，Phase 1 不新增决策日志；批准后立即创建并记录获批项。 | 确认 |

## 14. 批准后首个执行检查表

- [ ] 确认第 13 节的默认事实模型持久化策略与配置体验。
- [ ] 将批准的设计记录到 `docs/development/DECISIONS.md`。
- [ ] 保留而非弱化 `evidence-policy.md` 的六状态和缺口转换。
- [ ] 先建立模块/深度/访谈政策，再改写 orchestrator。
- [ ] 在实现中为每个新增模块写出深度差异的来源、事实和问题行为。
- [ ] 不将合成 Golden 断言表述为真实项目证据或量化结果。
- [ ] 完整执行 3 fixture × 2 preset matrix，并把 v2 与旧基线按事实而非措辞比较。
