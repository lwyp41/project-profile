# Project Profile v2 — MASTER PLAN

> Status: Design specification for agent/Codex execution
> Repository: `https://github.com/lwyp41/project-profile`
> Priority: This document is the primary source of truth for the v2 redesign.
> If this document conflicts with earlier chat discussion, exploratory ideas, or the current implementation, follow this document unless the user gives a newer explicit instruction.

---

## 1. Mission

Redesign `project-profile` from an **evidence-first project narrative generator** into a **configurable project fact reconstruction system**.

The Skill's primary responsibility is:

> Reconstruct a completed project's facts, design, decisions, evolution, contribution, validation, outcomes, constraints, and evidence boundaries from repositories, documents, prompts, artifacts, history, and user testimony, then render those facts into a canonical project profile that downstream Skills can reuse without re-investigating the project.

The highest-priority downstream consumer is a **Resume Skill**.

Other downstream consumers may include:

- Portfolio / Case Study Skill
- Interview Preparation Skill
- Technical Summary Skill
- Project Retrospective Skill
- Reporting / Presentation Skill

The Project Profile Skill itself must **not** become a resume-writing or marketing-writing Skill.

---

# 2. Product Boundary

## 2.1 What the Skill should do

The Skill should:

- discover and inventory available project evidence;
- classify the project type;
- select relevant analysis modules;
- allow the user to choose module-level investigation depth;
- reconstruct facts from artifacts before asking the user;
- reconstruct project evolution over time;
- reconstruct key decisions and trade-offs;
- reconstruct ownership and personal contribution;
- reconstruct actual usage, scale, impact, and measurable outcomes where evidence exists;
- identify material gaps;
- ask targeted questions only when project artifacts cannot reliably answer them;
- preserve evidence provenance and uncertainty;
- create a canonical fact model before writing narrative prose;
- render a `PROJECT_PROFILE.md`;
- provide downstream reusable fact units;
- retain an auditable evidence appendix.

## 2.2 What the Skill should not do

The Skill should not:

- write resume bullets as its primary deliverable;
- turn facts into promotional achievement statements;
- embellish ownership;
- fabricate metrics, rationale, alternatives, impact, user counts, scale, or business outcomes;
- produce a final portfolio case study;
- produce a final presentation;
- optimize final DOCX visual styling as a core responsibility;
- interpret "deep" as merely "write more words";
- force irrelevant modules into every project.

Example:

Acceptable Project Profile fact:

> 用户确认该工作流实际使用约 3–4 个月，处理至少约 150 份简历；单份定制由人工约 2 小时缩短至约 15 分钟。

Not acceptable as Project Profile output:

> 主导构建 AI 简历运营平台，实现效率提升 8 倍。

The latter belongs to a downstream Resume Skill.

---

# 3. Current v1 Capabilities to Preserve

The redesign must preserve the strongest parts of v1 unless there is a clear reason to replace them.

Keep the six evidence states:

- `VERIFIED`
- `INFERRED`
- `CLARIFICATION_REQUIRED`
- `UNKNOWN`
- `NOT_APPLICABLE`
- `CONFLICTING`

Preserve these principles:

- claim-level provenance;
- source locators;
- separation of repository evidence and user testimony;
- explicit handling of conflicting evidence;
- explicit handling of negative evidence;
- distinction between `UNKNOWN` and `NOT_APPLICABLE`;
- metrics must be sourced or explicitly user-stated;
- unresolved claims must remain visibly unresolved;
- user review before final generation;
- Markdown remains the source of truth;
- downstream fact pack remains evidence-oriented rather than resume-oriented.

Do not weaken evidence policy to make the document richer.

The v2 goal is:

> richer fact reconstruction **and** strong evidence discipline.

---

# 4. Why v1 Needs Redesign

The current design over-optimizes for:

- caution;
- auditability;
- compact narrative;
- adaptive omission of sections.

This makes it good at avoiding unsupported claims, but not good enough at fully reconstructing project knowledge.

Major current limitations:

1. The current narrative schema encourages compression too early.
2. Evidence governance is stronger than information coverage.
3. Interviewing is primarily gap-driven, not career-signal-driven.
4. The downstream fact pack is too flat to serve as the primary knowledge structure.
5. The Skill can produce a "correct but thin" document.
6. Current tests validate workflow rules more than output quality.
7. Project evolution, decisions, ownership, actual usage, and outcomes are not investigated deeply enough by default.
8. Resume downstream use is not treated as a first-class data-reconstruction requirement.

---

# 5. Core v2 Architecture

Replace the current mental model:

```text
Evidence-first Project Narrative
```

with:

```text
Configurable Project Fact Reconstruction System
```

The fundamental design rule is:

> Reconstruct facts first. Render prose second.

Separate the Skill into two conceptual layers.

## Layer A — Project Knowledge Reconstruction

Purpose:

- investigate;
- recover facts;
- preserve detail;
- resolve or expose gaps;
- build a reusable project knowledge base.

## Layer B — Canonical Profile Rendering

Purpose:

- select enabled modules;
- respect chosen depth;
- render readable project documentation;
- expose reusable fact units;
- attach evidence appendix.

Narrative prose must never become the only place where facts exist.

---

# 6. Required v2 Workflow

Implement the following conceptual pipeline:

```text
Understand User Intent
↓
Discover Sources
↓
Classify Project Type
↓
Select Modules + Depth
↓
Build Module Coverage Map
↓
Extract Artifact Evidence
↓
Reconstruct Timeline
↓
Reconstruct Decisions
↓
Reconstruct Ownership / Contribution
↓
Reconstruct Outcomes / Scale
↓
Detect Knowledge Gaps
↓
Module-specific Progressive Interview
↓
Build Canonical Fact Model
↓
Validate Evidence
↓
User Review Gate
↓
Render PROJECT_PROFILE.md
```

Important behavior:

- artifacts are investigated before user questions;
- user questions are driven by material missing knowledge;
- module-level reconstruction occurs before final prose synthesis;
- facts should survive even if later output is concise;
- a user may explicitly request unresolved fields to remain unresolved.

---

# 7. Module Registry

Replace a single fixed narrative schema with a configurable module registry.

Minimum recommended modules:

| Module ID | Purpose |
|---|---|
| `project-overview` | What the project is, lifecycle state, main artifact/capability |
| `background-problem` | Why the project existed and what problem triggered it |
| `users-stakeholders` | Intended users, actual users, stakeholders, affected parties |
| `goals-success` | Intended goals and success conditions |
| `requirements-constraints` | Functional, non-functional, operational, privacy, compatibility, cost, time, policy constraints |
| `product-workflow` | Product logic, user flow, operating workflow, task routing |
| `technical-architecture` | System structure, modules, runtime, integrations, scripts, APIs |
| `ai-agent-design` | LLM/Agent/Prompt/RAG/context/HITL/tooling/evaluation logic |
| `information-data` | Data, source-of-truth, information organization, provenance boundaries |
| `decisions-tradeoffs` | Key choices, alternatives, rationale, rejected approaches, consequences |
| `ownership-contribution` | What the owner personally built, decided, investigated, coordinated, or validated |
| `validation-qa` | Tests, evals, manual validation, regression checks, QA processes |
| `outcomes-metrics` | Usage, scale, efficiency, quality, business or operational outcomes |
| `evolution-history` | Initial state, major phases, redesigns, migrations, current state |
| `risks-limitations` | Failure modes, unresolved issues, known limitations, evidence boundaries |

Rules:

- modules are selectable;
- modules may be disabled;
- not every module appears in every final profile;
- project type influences recommended modules;
- user intent influences recommended module depth;
- module guidance belongs in `references/modules/`, not all inside `SKILL.md`.

---

# 8. Project Type as Router, Not Output Template

Project type should determine:

- which module guidance is relevant;
- which evidence sources are high-signal;
- which interview questions are likely important.

Project type should **not** determine a rigid document template.

Minimum supported project-type routing should preserve existing types where useful:

- `SOFTWARE`
- `AI_AGENT`
- `AGENT_SKILL`
- `PROMPT_SYSTEM`
- `LIBRARY`
- `DATA_PROJECT`
- `RESEARCH_PROJECT`
- `DOCUMENTATION_PROJECT`
- `SPARSE_ARTIFACT`

Add or merge types only when justified.

Example:

`AGENT_SKILL` should emphasize:

- product-workflow;
- ai-agent-design;
- information-data;
- decisions-tradeoffs;
- validation-qa;
- evolution-history;
- ownership-contribution.

A `SOFTWARE` project should emphasize:

- requirements-constraints;
- technical-architecture;
- runtime/integration;
- validation-qa;
- deployment or operational boundaries if applicable.

---

# 9. Depth System

Support at least:

- `off`
- `brief`
- `standard`
- `deep`

Depth must control **investigation behavior**, not only output length.

## 9.1 `off`

- Do not investigate this module except where facts are required to interpret another enabled module.
- Do not render it in the main profile.

## 9.2 `brief`

Goal:

- recover only the highest-value facts.

Typical behavior:

- inspect obvious high-signal sources;
- extract 2–4 key facts;
- do not perform broad historical archaeology unless required to resolve a material conflict;
- ask user questions only if the missing information is essential.

## 9.3 `standard`

Goal:

- recover enough information to explain the module accurately and usefully.

Typical behavior:

- inspect primary relevant artifacts;
- recover mechanism, major decision, result, and limitation where applicable;
- inspect related docs/tests/examples;
- perform focused interview if material facts remain missing.

## 9.4 `deep`

Goal:

- reconstruct the module as fully as practical.

Typical behavior:

- inspect repository implementation;
- references;
- examples;
- tests;
- generated outputs;
- git history;
- older variants;
- commits or changelog where useful;
- conflicting sources;
- deleted/replaced approaches when recoverable.

Attempt to reconstruct:

- evolution;
- alternatives;
- rationale;
- ownership;
- usage;
- scale;
- metrics;
- failure modes.

If evidence is unavailable but the user can likely resolve it, use `CLARIFICATION_REQUIRED` and ask.

---

# 10. Module-Level Depth Configuration

Support configuration like:

```yaml
purpose: resume
default_depth: standard

modules:
  project-overview: brief
  background-problem: deep
  users-stakeholders: brief
  goals-success: standard
  requirements-constraints: standard
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

Users must be able to override presets.

---

# 11. Presets

Implement at least:

- `resume`
- `technical`
- `balanced`

Presets should configure recommended modules and investigation depth only.

They must not force downstream-style wording.

## 11.1 Resume preset

Recommended emphasis:

```yaml
background-problem: deep
product-workflow: deep
decisions-tradeoffs: deep
ownership-contribution: deep
outcomes-metrics: deep
evolution-history: deep
ai-agent-design: deep   # when applicable
technical-architecture: standard
validation-qa: standard
risks-limitations: brief
```

Resume mode must actively investigate:

- ownership;
- scale;
- complexity;
- decisions;
- impact;
- iteration.

## 11.2 Technical preset

Recommended emphasis:

```yaml
requirements-constraints: deep
technical-architecture: deep
ai-agent-design: deep
information-data: deep
decisions-tradeoffs: deep
validation-qa: deep
evolution-history: standard
ownership-contribution: standard
outcomes-metrics: standard
```

## 11.3 Balanced preset

Most applicable modules at `standard`, with obvious project-specific exceptions.

---

# 12. Three Required Reconstruction Mechanisms

## 12.1 Project Evolution Reconstruction

Explicitly reconstruct:

```text
Initial state
→ first implementation
→ discovered limitations/problems
→ major redesigns or migrations
→ current state
```

Potential evidence:

- README history;
- changelog;
- git commits;
- prior prompt versions;
- old config files;
- old directories;
- migration notes;
- user testimony.

Important:

Do not only document what exists now.

Recover how the project became what it is.

---

## 12.2 Career Evidence Reconstruction

When `purpose = resume`, explicitly assess six signals:

```text
Ownership
Scale
Complexity
Decision
Impact
Iteration
```

For each signal:

- search evidence first;
- if unresolved and user-answerable, ask;
- if unresolved after interview, preserve as `UNKNOWN`.

Examples of useful questions:

- How long was this actually used?
- Approximately how many tasks/projects/users did it handle?
- What was the previous workflow?
- What changed after adoption?
- Which parts did you personally own?
- Which parts were collaborative?
- What was the hardest decision?
- Which design was replaced or rejected?
- What failed or caused a redesign?

Do not rely on the user to volunteer this information without prompting.

---

## 12.3 Decision Mining

Attempt to reconstruct:

```text
constraint
→ alternatives
→ chosen approach
→ rationale
→ consequence
```

Important rule:

If artifacts prove the chosen approach but not the rationale, do not invent the rationale.

Use:

`CLARIFICATION_REQUIRED`

and ask the user if the rationale is material.

---

# 13. Canonical Fact Model

Before writing narrative prose, build structured fact units.

Recommended fields:

```yaml
id:
module:
claim:
status:
source_kind:
source_locator:
time_context:
ownership:
metric:
rationale:
caveat:
conflict:
```

Additional fields are allowed if useful.

Rules:

- not every field is mandatory for every fact;
- all material facts must retain evidence provenance;
- important facts should not exist only as prose;
- the canonical fact model is the internal source for final profile rendering;
- facts may be reused by future downstream Skills.

---

# 14. Interview Protocol v2

The interview system must become:

> gap-driven + module-driven + career-signal-driven

Keep these v1 strengths:

- investigate first;
- normally ask 3–5 questions at a time;
- explain why the question matters;
- accept:
  - no;
  - unknown;
  - not applicable;
  - don't remember;
- do not pressure the user to invent answers;
- update the evidence model after each interview round.

New rule for `resume` purpose:

Before final review, actively check whether these are sufficiently reconstructed:

- ownership;
- scale;
- impact;
- decisions;
- iteration;
- complexity.

Do not label them `UNKNOWN` merely because the repository lacks them if the user could realistically answer.

---

# 15. Output Contract

The final source-of-truth deliverable remains:

```text
PROJECT_PROFILE.md
```

Recommended high-level structure:

```text
Project Overview

Selected Knowledge Modules
  Background & Problem
  Users / Stakeholders
  Goals / Success
  Requirements / Constraints
  Product / Workflow
  Technical Architecture
  AI / Agent Design
  Information / Data
  Decisions / Trade-offs
  Ownership / Contribution
  Validation / QA
  Outcomes / Metrics
  Evolution / History
  Risks / Limitations

Reusable Downstream Facts

Evidence Appendix
  Evidence Coverage
  Unknown / N/A / Conflicts
  Claim Ledger
  Review Record
```

Rules:

- only enabled/applicable modules are rendered;
- headings should be localized naturally;
- empty sections should be omitted;
- the main body should remain readable;
- the evidence appendix remains structured and auditable.

Do not enforce a rigid word count.

Suggested ranges are informational only:

- brief profile: often <1500 Chinese characters / comparable English length;
- resume-oriented profile: often ~2500–5000 Chinese characters;
- technical deep profile: may exceed 5000–10000 Chinese characters.

Completeness and usefulness matter more than exact length.

---

# 16. Downstream Fact Pack

Preserve a reusable downstream fact section.

Each fact unit should include where relevant:

- Situation / problem
- Work / decision
- Artifact / mechanism
- Observed result
- Scope / ownership
- Evidence locator
- Caveat

Rules:

- these are neutral evidence units;
- they are not resume bullets;
- they should not use promotional wording;
- they should not combine unrelated facts into inflated claims.

The downstream fact pack is an interface for later Skills, not the main project knowledge structure.

---

# 17. DOCX Boundary

DOCX generation should not be a core v2 objective.

Recommended rule:

- Markdown is the canonical output.
- If DOCX support is retained, it is a derivative presentation format.
- Do not spend major redesign effort on DOCX layout in v2 unless the user explicitly requests it.
- Do not mix factual reconstruction logic with document-layout logic.

---

# 18. Proposed Repository Structure

Recommended direction:

```text
SKILL.md

references/
  evidence-policy.md
  depth-policy.md
  module-registry.md
  interview-policy.md

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

examples/
```

Do not mechanically create one file per concept if the guidance would be trivial.

Combine short references where that improves clarity.

---

# 19. SKILL.md Design Requirement

`SKILL.md` should become a concise orchestrator.

It should primarily contain:

- purpose;
- boundary;
- core workflow;
- project-type routing;
- module selection;
- depth selection;
- evidence rules;
- interview trigger;
- user review gate;
- output contract;
- reference loading instructions.

Detailed analysis content belongs in:

```text
references/modules/
references/project-types/
```

Do not keep expanding `SKILL.md` with all domain knowledge.

---

# 20. Evaluation Strategy

The redesign must not be considered complete merely because:

- YAML is valid;
- the Skill triggers;
- static checks pass.

The primary quality question is:

> Does v2 reconstruct a project more completely and more usefully than v1 without weakening factual discipline?

Evaluation must include:

- golden baseline comparison;
- qualitative output review;
- structured assertions;
- regression across project types and presets.

---

# 21. Required Quality Dimensions

At minimum evaluate:

- Fact coverage
- Evidence correctness
- Module completeness
- Resume downstream usability
- Technical downstream usability
- Decision reconstruction
- Ownership reconstruction
- Outcome reconstruction
- Evolution reconstruction
- Unsupported claim rate
- Unknown / N/A correctness
- Conflict preservation
- Natural writing quality
- Preset differentiation
- Depth differentiation

---

# 22. Required Fixtures

At least three fixture types:

## A. Synthetic Agent Skill

Purpose:

- controlled workflow evidence;
- synthetic evolution and decision history;
- explicit absence of real-world outcomes;
- safe public Resume/Technical regression coverage.

Test with:

- `resume`
- `technical`

## B. Software project

Purpose:

- rich technical evidence;
- architecture;
- implementation;
- tests;
- possibly sparse user/business evidence.

Test with:

- `resume`
- `technical`

## C. Sparse project

Purpose:

- few artifacts;
- critical reliance on focused user interview;
- test whether the Skill asks good questions instead of fabricating.

Test with:

- `resume`
- `technical`

Minimum initial matrix:

```text
3 fixture types × 2 presets = 6 scenarios
```

---

# 23. Key Acceptance Criteria

## 23.1 Coverage

For the controlled synthetic fixture, v2 must recover all important supported synthetic baseline facts when relevant modules are enabled.

It must not become thinner merely because the final narrative is adaptive.

## 23.2 Evidence discipline

No unsupported:

- metrics;
- ownership;
- rationale;
- alternatives;
- users;
- business impact;
- outcomes.

## 23.3 Depth behavior

`brief`, `standard`, and `deep` must create meaningfully different investigation behavior.

It is not sufficient for them to produce different word counts.

## 23.4 Preset behavior

Resume and Technical presets must produce visibly different investigative priorities.

## 23.5 Downstream independence

A downstream Resume Skill should normally be able to begin from `PROJECT_PROFILE.md` without reverse-engineering the original repository again.

## 23.6 Adaptability

Irrelevant modules should be:

- omitted;
- or explicitly marked N/A when the distinction matters.

Do not generate filler.

## 23.7 Narrative quality

The final profile should read like natural project documentation, not like an evidence ledger converted into paragraphs.

---

# 24. Execution Sequence for Codex / Another Agent

Do not rewrite everything in one pass.

## Phase 1 — Design Only

First inspect the repository and produce a design document.

Do **not** modify the existing Skill implementation yet.

Deliver:

1. Current-state diagnosis
2. v1 → v2 architecture mapping
3. Module Registry proposal
4. Depth Policy proposal
5. Preset definitions
6. Canonical Fact Model
7. Interview redesign
8. Golden eval design
9. Proposed repository structure
10. File-by-file migration plan
11. Risks and unresolved design decisions

Recommended design artifact in this repository:

```text
docs/development/V2_DESIGN.md
```

Stop and wait for user approval.

## Phase 2 — Implementation

Only after user approval:

1. refactor `SKILL.md`;
2. add/update references;
3. add module registry;
4. add depth policy;
5. add presets;
6. update profile template;
7. implement or update validation scripts;
8. add eval fixtures;
9. migrate examples;
10. run existing checks;
11. run new evals;
12. run the controlled synthetic golden scenario;
13. compare v2 output with baseline;
14. iterate until acceptance criteria are met.

---

# 25. File-by-File Migration Categories

During Phase 1, every current file should be classified as:

- `RETAIN`
- `REFACTOR`
- `REPLACE`
- `DELETE`
- `ADD`

For each file, explain:

- current role;
- v2 role;
- why the change is necessary;
- dependencies.

Do not delete working evidence-policy logic merely to simplify structure.

---

# 26. Prohibited Shortcuts

Do not:

- solve the problem by only making `SKILL.md` longer;
- solve the problem by adding fixed mandatory headings;
- merge Resume Skill responsibilities into Project Profile;
- weaken evidence requirements;
- interpret `deep` as "write more";
- invent decision rationale;
- invent business impact;
- invent personal ownership;
- force unused modules into the output;
- hide missing evidence behind polished prose;
- discard detailed facts merely because the final narrative is concise;
- make every project look like a software project;
- make every project look like an AI project.

---

# 27. Source Priority

When implementing or evaluating, use this priority order:

```text
1. Latest explicit user instruction
2. `docs/development/MASTER_PLAN.md`
3. `evals/GOLDEN_EVAL_SPEC.md`
4. Approved `docs/development/V2_DESIGN.md`
5. Golden baseline content
6. Earlier chat discussion / rationale
7. Current repository implementation
```

Earlier chat messages are context, not authoritative requirements when they conflict with this document.

---

# 28. Decision Log

Maintain a concise:

```text
docs/development/DECISIONS.md
```

during redesign.

Record only:

- approved architecture decisions;
- why they were made;
- what alternatives were rejected;
- any intentional deviation from `docs/development/MASTER_PLAN.md`.

Do not turn this into a transcript or scratchpad.

---

# 29. Definition of Done

v2 is not complete until all of the following are true:

- the v2 design is approved;
- module registry exists;
- depth semantics are explicit;
- presets are implemented;
- evidence states remain intact;
- project evolution reconstruction exists;
- decision mining exists;
- ownership and outcome reconstruction exist;
- resume-purpose interview logic exists;
- canonical fact model exists;
- final profile remains readable;
- downstream fact pack remains neutral;
- controlled synthetic golden regression is run;
- no important supported baseline facts are lost;
- at least one new useful fact category beyond the baseline is recovered;
- no unsupported factual inflation is introduced;
- regression fixtures pass;
- Resume and Technical presets demonstrably differ.

---

# 30. First Instruction to the Implementing Agent

Start by reading the current repository in full enough to understand its architecture and existing evidence model.

Then produce `docs/development/V2_DESIGN.md`.

Do not modify production Skill files before user approval.

The goal of the first phase is not code generation.

The goal is to convert this specification into an implementation-ready architecture with explicit migration decisions.
