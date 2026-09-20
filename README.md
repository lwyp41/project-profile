# project-profile

> Turn an old project into a clear, honest project story.

`project-profile` is an Agent Skill for reconstructing a completed project from the materials that still exist: source code, documents, prompts, notebooks, examples, generated artifacts, and Git history. It produces a reviewable `PROJECT_PROFILE.md` for portfolios, handoffs, project retrospectives, and AI product documentation.

[![Agent Skill](https://img.shields.io/badge/format-SKILL.md-6f42c1)](https://github.com/lwyp41/project-profile/blob/main/SKILL.md)
[![Latest release](https://img.shields.io/github/v/release/lwyp41/project-profile?display_name=tag)](https://github.com/lwyp41/project-profile/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## English

### The problem

You finish a project, then months later need to explain it:

- What problem did it solve?
- Who was it for?
- What did you actually build?
- Why was it designed this way?
- What evidence supports the results?
- What do you no longer remember?

The answers are usually spread across a repository and a few memories. `project-profile` helps an agent investigate those materials and turn them into one coherent project profile.

### Use it when

Use this Skill when you have a completed or abandoned project and want to:

- turn a codebase into a portfolio case study;
- reconstruct a project before a job interview or review;
- hand a project to another person or Agent;
- document an AI agent, prompt system, Skill, library, data project, or research project;
- make sense of a small, partial, or poorly documented repository.

It can work with more than traditional software repositories. The project may be a folder of prompts, an Agent Skill, a notebook, a research bundle, a documentation site, or a sparse artifact.

### Try it

Install the Skill, point your agent at a project, and say:

```text
Use project-profile to reconstruct this completed project.
Inspect the files and Git history first. Then ask me only the questions
that cannot be answered reliably from the evidence. Produce a PROJECT_PROFILE.md.
```

Or, if you want a portfolio-oriented result:

```text
Use project-profile to turn this project into an evidence-backed portfolio profile.
Emphasize the problem, my contribution, important design decisions, trade-offs,
results, limitations, and career-relevant signals. Do not invent metrics.
```

### What you get

The main output is `PROJECT_PROFILE.md`, covering the parts that apply to the project:

- background and motivation;
- goals, users, and usage scenarios;
- capabilities and technical or research approach;
- architecture, data flow, modules, or operating model;
- key challenges, decisions, and trade-offs;
- metrics and outcomes when they are actually supported;
- limitations, risks, and future work;
- evidence coverage and a claim-level evidence ledger;
- career-relevant signals.

For AI and agent projects, it can also document the AI capability, the reason to use AI, model or LLM choices, prompts, tools, retrieval, human review, evaluation, reliability, cost, and risks—when those details are relevant and supported by evidence.

For a Skill or documentation project, it focuses on what the Skill is for, when it should trigger, how its workflow works, what decisions it makes, what references and examples it uses, what output it should produce, and how it can fail.

### What it will not do

It will not make up:

- performance numbers or business impact;
- user counts, adoption, or revenue;
- a decision rationale you never documented;
- alternatives you never considered;
- success claims that the available evidence cannot support.

If an important answer cannot be recovered, the profile says so. If a section does not apply, it marks it as not applicable. Before the final profile is generated, you get a review step to correct the draft and confirm unresolved claims.

### Supported project shapes

The Skill adapts to the material it finds. Examples include:

```text
software repository     AI agent or prompt system
Agent Skill             library or package
data project            research project
documentation project   lightweight or sparse artifact
```

The output is not a score for the project. It is a transparent reconstruction of what can and cannot be established.

### Install

Clone this repository:

```bash
git clone https://github.com/lwyp41/project-profile.git
```

Copy the `project-profile` folder into the skills directory used by your agent. For Codex, the typical global location is:

```text
~/.codex/skills/project-profile
```

For other agents, use their equivalent `skills/` directory. The Skill follows the portable `SKILL.md` format and does not require a runtime dependency.

### How it works

The Skill follows a simple sequence:

```text
inspect → classify → map evidence → identify gaps
→ ask focused questions → draft → validate → review → generate
```

Every important claim is labelled as one of:

- `VERIFIED`: directly supported by a project artifact or user statement;
- `INFERRED`: a reasoned interpretation, clearly labelled as such;
- `CLARIFICATION_REQUIRED`: important and worth asking the user;
- `UNKNOWN`: relevant but not recoverable;
- `NOT_APPLICABLE`: not relevant to this project;
- `CONFLICTING`: credible sources disagree.

This is the evidence-first part of the Skill: not a special feature that makes it different from all other Skills, but the rule that keeps a project profile from becoming polished fiction.

### Project structure

```text
project-profile/
├─ SKILL.md
├─ references/
│  ├─ profile-schema.md
│  ├─ evidence-policy.md
│  ├─ interview-protocol.md
│  ├─ architecture-analysis.md
│  └─ extraction-patterns.md
├─ templates/PROJECT_PROFILE.md
├─ examples/
├─ tests/
├─ CHANGELOG.md
└─ LICENSE
```

### Contributing

Issues and pull requests are welcome. Useful contributions include anonymized fixtures, clearer project-type guidance, compatibility notes for other agents, and evaluation cases that catch unsupported claims.

Please do not submit secrets or private project data. If a change affects the profile output, update the schema, template, example, and changelog together.

### License

MIT. See [LICENSE](LICENSE).

---

## 中文

### 它解决什么问题

一个项目做完几个月以后，你可能需要重新回答：

- 它解决了什么问题？
- 给谁使用？
- 我到底做了什么？
- 为什么这样设计？
- 哪些结果有证据支持？
- 哪些内容我已经记不清了？

这些答案通常散落在代码、文档、Prompt、Notebook、示例、生成物、Git 历史和个人记忆中。`project-profile` 帮助 Agent 调查这些材料，整理出一份完整、可复核的项目档案。

### 什么时候使用

当你有一个已经完成、暂停或废弃的项目，并且希望：

- 把代码仓库整理成作品集案例；
- 在面试或项目复盘前恢复项目上下文；
- 把项目交接给其他人或其他 Agent；
- 记录 AI Agent、Prompt System、Skill、Library、Data 或 Research 项目；
- 看懂一个小型、残缺或文档很少的项目。

它不只适用于传统软件仓库。项目也可以是一组 Prompt、一个 Agent Skill、一个 Notebook、一个研究资料包、一个文档站点，或者只有少量文件的项目产物。

### 试试看

安装 Skill 后，把 Agent 指向你的项目，然后说：

```text
请使用 project-profile 还原这个已经完成的项目。
先检查文件和 Git 历史，只询问那些无法从现有证据可靠回答的问题，
最后生成 PROJECT_PROFILE.md。
```

如果你想生成偏作品集的版本，可以说：

```text
请使用 project-profile 把这个项目整理成一份有证据支持的作品集档案。
重点说明项目问题、我的贡献、关键设计决策、取舍、结果、限制和职业相关信号。
不要编造 metrics。
```

### 你会得到什么

主要输出是 `PROJECT_PROFILE.md`，会根据项目实际情况覆盖：

- 项目背景和动机；
- 目标、用户和使用场景；
- 核心能力以及技术或研究方法；
- 系统架构、数据流、模块或运行方式；
- 关键难点、设计决策和 Trade-offs；
- 有真实证据支持的指标和成果；
- 限制、风险和未来工作；
- Evidence Coverage 和逐条证据记录；
- Career-Relevant Signals。

对于 AI 和 Agent 项目，如果材料中有相关信息，它还可以整理 AI 能力、为什么使用 AI、模型或 LLM 选择、Prompt、工具、检索、人机协作、评估、可靠性、成本和风险。

对于 Skill 或 Documentation 项目，它重点说明这个 Skill 是做什么的、什么时候触发、如何工作、如何做决策、使用哪些参考资料和示例、应该输出什么，以及可能如何失败。

### 它不会做什么

它不会编造：

- 性能数字或商业影响；
- 用户数量、采用情况或收入；
- 你没有记录过的决策理由；
- 你没有真正考虑过的替代方案；
- 证据不足的成功结论。

如果重要信息无法恢复，档案会明确写成 Unknown。如果某个部分确实不适用于这个项目，会标记为 N/A。最终生成前还会有一次 Review，让你修改草稿并确认未解决的结论。

### 支持的项目形态

```text
软件仓库                AI Agent 或 Prompt System
Agent Skill             Library 或 Package
Data Project            Research Project
Documentation Project  轻量仓库或 Sparse Artifact
```

它输出的不是项目质量评分，而是对“哪些内容可以确定、哪些内容不能确定”的透明还原。

### 安装

克隆仓库：

```bash
git clone https://github.com/lwyp41/project-profile.git
```

把 `project-profile` 文件夹复制到你的 Agent 使用的 skills 目录。Codex 的典型全局路径是：

```text
~/.codex/skills/project-profile
```

其他 Agent 使用它们对应的 `skills/` 目录即可。这个 Skill 遵循通用的 `SKILL.md` 格式，不需要额外运行时依赖。

### 它如何工作

```text
检查材料 → 判断项目类型 → 建立证据图 → 找出缺口
→ 提出少量问题 → 起草 → 验证 → Review → 生成
```

每个重要结论会标记为：

- `VERIFIED`：有项目材料或用户明确回答直接支持；
- `INFERRED`：基于观察结果的推断，并会明确标注；
- `CLARIFICATION_REQUIRED`：重要且值得向用户确认；
- `UNKNOWN`：相关，但现有材料无法恢复；
- `NOT_APPLICABLE`：与当前项目无关；
- `CONFLICTING`：可信来源之间存在冲突。

这里的 evidence-first（证据优先）不是宣称这个 Skill 拥有其他 Skill 没有的神奇能力，而是一条防止项目档案变成“写得很像真的故事”的工作规则。

### 项目结构

```text
project-profile/
├─ SKILL.md
├─ references/
│  ├─ profile-schema.md
│  ├─ evidence-policy.md
│  ├─ interview-protocol.md
│  ├─ architecture-analysis.md
│  └─ extraction-patterns.md
├─ templates/PROJECT_PROFILE.md
├─ examples/
├─ tests/
├─ CHANGELOG.md
└─ LICENSE
```

### 参与贡献

欢迎提交 Issue 和 Pull Request。适合的贡献包括脱敏后的项目样例、新项目类型的说明、其他 Agent 的兼容性说明，以及能发现无依据结论的评估案例。

请不要提交密钥或私人项目数据。如果修改影响了输出格式，请同步更新 schema、template、example 和 changelog。

### 许可证

MIT，详见 [LICENSE](LICENSE)。
