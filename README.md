# project-profile

> Turn a completed project into an evidence-backed `PROJECT_PROFILE.md` that explains what it was, why it existed, how it worked, what is known about its results, and what remains uncertain.

[![Agent Skill](https://img.shields.io/badge/format-SKILL.md-6f42c1)](https://github.com/lwyp41/project-profile/blob/main/SKILL.md)
[![Version](https://img.shields.io/github/v/release/lwyp41/project-profile?display_name=tag)](https://github.com/lwyp41/project-profile/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## English

### Why this exists

Important project knowledge is often scattered across code, prompts, notebooks, documents, commit history, generated artifacts, and memory. `project-profile` helps an AI agent reconstruct that knowledge into a coherent, reviewable profile without turning guesses into facts.

It is especially useful for:

- portfolio and career documentation;
- AI PM, AI Operations, and AI Strategy work;
- handing completed projects to a new team or agent;
- recovering context from lightweight or incomplete repositories;
- documenting skills, prompt systems, agents, libraries, research, and data projects.

### What makes it different

`project-profile` is evidence-first. It investigates available artifacts before asking questions, records provenance for material claims, separates verified facts from bounded inferences, and keeps unresolved knowledge visible.

The workflow is:

```text
Discover → Classify → Select Analysis Mode → Map Evidence
→ Extract Knowledge → Detect Gaps → Interview → Synthesize
→ Validate → User Review Gate → Generate
```

It explicitly distinguishes:

- `VERIFIED` — directly supported by evidence;
- `INFERRED` — a bounded interpretation of observed evidence;
- `CLARIFICATION_REQUIRED` — important and answerable by the user;
- `UNKNOWN` — relevant but not recoverable;
- `NOT_APPLICABLE` — genuinely irrelevant to the project;
- `CONFLICTING` — credible sources disagree.

### Supported project types

The skill adapts its analysis to the project instead of forcing every project into a traditional software template:

- software repositories and libraries;
- AI agents and prompt systems;
- `AGENT_SKILL` projects;
- data and research projects;
- documentation projects;
- lightweight repositories and sparse artifacts.

For AI-related projects it can cover Why AI, AI capability, AI versus traditional approaches, model/LLM strategy, prompt/agent/RAG design, human-in-the-loop controls, evaluation, reliability, cost, risk, and product value when evidence exists.

For skills and documentation it focuses on Purpose, Trigger Conditions, Workflow, Instructions, Decision Logic, References, Examples, Expected Outputs, and Failure Modes.

### Output

The canonical output is:

```text
PROJECT_PROFILE.md
```

It can include:

- project background and motivation;
- goals, users, and usage scenarios;
- capabilities and technical stack;
- architecture, data flow, modules, and interfaces;
- technical or methodological challenges;
- design decisions and trade-offs;
- metrics and outcomes, only when supported;
- limitations, risks, and future work;
- objective Evidence Coverage;
- a claim-level evidence ledger;
- Career-Relevant Signals.

Markdown is the source of truth. A DOCX may be generated as an optional presentation derivative.

### Quick start

Clone the repository:

```bash
git clone https://github.com/lwyp41/project-profile.git
```

Install the `project-profile` directory into the skills directory used by your agent. For Codex, the typical global location is:

```text
~/.codex/skills/project-profile
```

Then ask your agent something like:

```text
Use the project-profile skill to reverse-engineer this completed project.
Inspect the available artifacts first, build an evidence map, ask only
high-value clarification questions, and produce PROJECT_PROFILE.md.
```

The format is intentionally portable. Any agent that supports the `SKILL.md` convention can use the same skill directory, although installation paths and invocation syntax vary by agent.

### Evidence discipline

The skill does not invent metrics, business impact, user counts, decision rationale, alternatives, adoption, or outcomes. It records sources as `repository`, `documentation`, `git_history`, `user`, `inference`, or `external_reference` and makes conflicts visible.

The final generation step includes a Project Profile Review Gate so the user can confirm, correct, or explicitly mark claims as `UNKNOWN` or `NOT_APPLICABLE`.

### Repository map

```text
project-profile/
├─ SKILL.md                         # agent instructions
├─ references/                      # schema, evidence, interview, and extraction guidance
├─ templates/PROJECT_PROFILE.md     # canonical output template
├─ examples/                        # illustrative example
├─ tests/                           # release validation contract
├─ CHANGELOG.md
└─ LICENSE
```

### Contributing

Issues and pull requests are welcome. Good contributions include:

- anonymized project fixtures;
- clearer extraction patterns for new project types;
- improved evidence and uncertainty handling;
- evaluation cases that catch unsupported claims;
- compatibility notes for additional SKILL.md-aware agents.

Please keep examples free of secrets and private project data. Changes that alter the output contract should update the schema, template, example, and changelog together.

### License

MIT. See [LICENSE](LICENSE).

---

## 中文

### 这个 Skill 解决什么问题

重要的项目知识通常散落在代码、Prompt、Notebook、文档、提交历史、生成物和个人记忆中。`project-profile` 帮助 Agent 把这些信息还原成一份结构化、可审阅的项目档案，同时避免把猜测写成事实。

它尤其适合：

- 整理作品集和职业经历；
- AI PM、AI Operations、AI Strategy 项目复盘；
- 将已完成项目交接给新团队或新 Agent；
- 从轻量仓库或不完整仓库中恢复项目上下文；
- 记录 Skill、Prompt System、AI Agent、Library、Research 和 Data 项目。

### 核心特点

这是一个 evidence-first（证据优先）的 Skill。它会先调查已有材料，再提出问题；为重要结论保留来源；区分已验证事实与有边界的推断；并明确保留无法恢复的信息。

工作流为：

```text
Discover → Classify → Select Analysis Mode → Map Evidence
→ Extract Knowledge → Detect Gaps → Interview → Synthesize
→ Validate → User Review Gate → Generate
```

它明确区分：

- `VERIFIED`：有直接证据支持；
- `INFERRED`：基于观察证据的有边界推断；
- `CLARIFICATION_REQUIRED`：重要且可以向用户确认；
- `UNKNOWN`：相关，但现有材料无法恢复；
- `NOT_APPLICABLE`：这个概念确实不适用于当前项目；
- `CONFLICTING`：可信来源之间存在冲突。

### 支持的项目类型

它不会强迫所有项目套用传统软件项目模板，而是根据项目类型调整分析方式：

- 软件仓库和 Library；
- AI Agent 和 Prompt System；
- `AGENT_SKILL` 项目；
- Data Project 和 Research Project；
- Documentation Project；
- 轻量仓库和 Sparse Artifact。

对于 AI 项目，在证据允许的情况下，它可以分析 Why AI、AI capability、AI 与传统方案的差异、模型/LLM 策略、Prompt/Agent/RAG 设计、人机协作、评估、可靠性、成本、风险和产品价值。

对于 Skill 和 Documentation 项目，它重点分析 Purpose、Trigger Conditions、Workflow、Instructions、Decision Logic、References、Examples、Expected Outputs 和 Failure Modes。

### 输出内容

标准输出是：

```text
PROJECT_PROFILE.md
```

内容可以包括：

- 项目背景和动机；
- 产品目标、用户和使用场景；
- 核心能力和技术栈；
- 系统架构、数据流、模块和接口；
- 技术或方法难点；
- 关键设计决策和 Trade-offs；
- 有证据支持的指标和项目成果；
- 限制、风险和未来工作；
- 客观的 Evidence Coverage；
- 逐条 Claim-level Evidence Ledger；
- Career-Relevant Signals。

Markdown 是唯一的 source of truth。可以额外生成 DOCX，但 DOCX 只是展示层衍生物。

### 快速开始

克隆仓库：

```bash
git clone https://github.com/lwyp41/project-profile.git
```

将 `project-profile` 目录安装到你的 Agent 使用的技能目录中。Codex 的典型全局路径是：

```text
~/.codex/skills/project-profile
```

然后向 Agent 提出类似请求：

```text
请使用 project-profile Skill 逆向分析这个已经完成的项目。
先调查现有材料，建立 evidence map，只提出高价值澄清问题，
最后生成 PROJECT_PROFILE.md。
```

这个格式有意保持跨 Agent 可移植。只要 Agent 支持 `SKILL.md` 约定，就可以使用同一个 Skill 目录；具体安装路径和调用语法可能不同。

### 证据纪律

这个 Skill 不会编造 metrics、business impact、user counts、decision rationale、alternatives、adoption 或 outcomes。它会区分 `repository`、`documentation`、`git_history`、`user`、`inference` 和 `external_reference` 等来源，并把冲突显式保留下来。

最终生成前会经过 Project Profile Review Gate，用户可以确认、修改，或明确把结论标记为 `UNKNOWN` 或 `NOT_APPLICABLE`。

### 目录结构

```text
project-profile/
├─ SKILL.md                         # Agent 指令
├─ references/                      # Schema、证据、访谈和提取规则
├─ templates/PROJECT_PROFILE.md     # 标准输出模板
├─ examples/                        # 示例
├─ tests/                           # 发布验证约定
├─ CHANGELOG.md
└─ LICENSE
```

### 参与贡献

欢迎提交 Issue 和 Pull Request。适合的贡献包括：

- 脱敏后的项目样例；
- 新项目类型的提取模式；
- 更清晰的证据和不确定性处理；
- 能发现无依据结论的评估案例；
- 其他支持 `SKILL.md` 的 Agent 兼容性说明。

请不要提交密钥或私人项目数据。如果修改了输出契约，请同时更新 schema、template、example 和 changelog。

### 许可证

MIT，详见 [LICENSE](LICENSE)。
