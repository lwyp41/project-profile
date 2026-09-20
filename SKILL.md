---
name: project-profile
description: Evidence-first reverse-engineer a completed project into a validated PROJECT_PROFILE.md for AI PM, AI Operations, and AI Strategy use. Use when reconstructing project purpose, architecture, decisions, outcomes, or AI-relevant career signals from repositories, documents, skills, prompts, artifacts, or sparse evidence. Do NOT use for inventing project plans, generic portfolio copy, or unverified impact claims.
---

# Project Profile

Create a defensible profile of a completed project. Treat every claim as evidence-backed knowledge, not as marketing copy. Markdown is the source of truth; a DOCX is optional and must be derived from it.

## Operating contract

- Use the workflow: **Discover → Classify Project Type → Select Adaptive Analysis Mode → Build Evidence Map → Extract Verified Knowledge → Detect Knowledge Gaps → Progressive User Interview → Synthesize → Validate → User Review Gate → Generate**.
- Read [profile-schema.md](references/profile-schema.md) before shaping the profile, [evidence-policy.md](references/evidence-policy.md) before assigning certainty, and only the conditional references needed for the project type.
- Model each material claim with one of: `VERIFIED`, `INFERRED`, `CLARIFICATION_REQUIRED`, `UNKNOWN`, `NOT_APPLICABLE`, `CONFLICTING`.
- Distinguish `UNKNOWN` (relevant but not recoverable) from `NOT_APPLICABLE` (the concept does not apply). A missing traditional software artifact is not evidence that the project is low quality.
- Accepted user answers include “no”, “I don’t know”, “not applicable”, and “I don’t remember”; encode them explicitly rather than pressing for a speculative answer.
- Never fabricate metrics, business impact, user counts, decision rationale, alternatives, or outcomes. Preserve conflicts and provenance.

## Workflow

### 1. Discover

Inventory available files, folders, metadata, documentation, examples, generated outputs, tests, configuration, commit history, and user-provided context. Record what was inspected and what was unavailable. Prefer direct artifacts over summaries.

### 2. Classify Project Type

Select one or more applicable types: `SOFTWARE`, `AI_AGENT`, `AGENT_SKILL`, `PROMPT_SYSTEM`, `LIBRARY`, `DATA_PROJECT`, `RESEARCH_PROJECT`, `DOCUMENTATION_PROJECT`, `SPARSE_ARTIFACT`, or another justified type. Record primary and secondary types plus evidence for the classification.

### 3. Select Adaptive Analysis Mode

Choose the smallest set of analysis modes that can explain the project:

- Software/library: architecture, modules/API, runtime, tests, integration, deployment.
- AI/agent/prompt: capability, model/LLM strategy, prompt/agent/RAG design, human-in-the-loop, evaluation, reliability, cost, risks.
- Skill/documentation: purpose, trigger conditions, workflow, instructions, decision logic, references, examples, expected outputs, failure modes.
- Data/research: question, data/evidence, method, reproducibility, limitations, findings, uncertainty.
- Sparse/artifact: artifact anatomy, observable intent, usage contract, missing evidence, and interview needs.

Read [architecture-analysis.md](references/architecture-analysis.md) for system or module structure, [extraction-patterns.md](references/extraction-patterns.md) for artifact-specific extraction, and [interview-protocol.md](references/interview-protocol.md) before asking questions.

### 4. Build the Evidence Map

Create an internal table with: claim or profile field, source kind, source locator, observed fact, status, confidence rationale, conflict, and next action. Source kinds are `repository`, `documentation`, `git_history`, `user`, `inference`, and `external_reference`. Use `external_reference` only when the user permits or supplies it; it cannot silently replace project evidence.

### 5. Extract Verified Knowledge

Extract facts first, then bounded inferences. For each inference, state the observation and reasoning. Capture negative evidence and absences when they affect interpretation. Keep implementation facts separate from product or business interpretation.

### 6. Detect Knowledge Gaps

Mark every required schema field as `VERIFIED`, `INFERRED`, `CLARIFICATION_REQUIRED`, `UNKNOWN`, `NOT_APPLICABLE`, or `CONFLICTING`. Rank gaps by decision value: a gap blocks a material claim only if resolving it would change the profile’s interpretation, safety, or user-facing conclusion.

### 7. Progressive User Interview

Ask only a small batch of high-value questions per round, prioritizing gaps that cannot be reliably recovered. Adapt questions to the project type. Offer answer choices such as “no”, “unknown”, “not applicable”, and “don’t remember”. After each round, update the evidence map and stop when remaining gaps are non-blocking or the user declines to answer. Follow [interview-protocol.md](references/interview-protocol.md).

### 8. Synthesize

Draft the canonical profile from the schema. Use Core sections for every project and expand only conditional sections that apply. Put `N/A` where a concept genuinely does not apply and `Unknown` where it matters but evidence is unavailable. Include an objective Evidence Coverage section; do not collapse it into a flattering overall score.

### 9. Validate

Check that every consequential claim has a source and status, every metric is attributed or marked unknown, conflicts are visible, AI claims answer “Why AI?”, and the profile does not imply unsupported users, value, or rationale. Validate against [evidence-policy.md](references/evidence-policy.md) and the schema checklist.

### 10. User Review Gate

Before final generation, show the user the draft’s material claims, unresolved gaps, conflicts, and proposed `UNKNOWN`/`N/A` classifications. Ask the user to confirm, correct, or explicitly mark claims as unknown/not applicable. Do not generate the final profile until the user approves the gate or explicitly asks to proceed with the unresolved labels preserved.

### 11. Generate

Write `PROJECT_PROFILE.md` using [templates/PROJECT_PROFILE.md](templates/PROJECT_PROFILE.md). Preserve the evidence ledger and status labels. Optionally generate `PROJECT_PROFILE.docx` only after Markdown is approved; the DOCX is a presentation derivative, never the source of truth.

## Completion checklist

- [ ] Project type and analysis mode are justified by evidence.
- [ ] Evidence map covers every material claim and uses allowed source kinds.
- [ ] Unknown and N/A are not conflated.
- [ ] No unsupported metrics, impact, users, rationale, alternatives, or outcomes were invented.
- [ ] Conditional sections are expanded only when applicable.
- [ ] AI/agent projects address capability, AI-vs-traditional choice, model/prompt/RAG, human oversight, evaluation, reliability, cost, risks, and value when applicable.
- [ ] Evidence Coverage is objective and claim-level.
- [ ] User Review Gate was completed or the user explicitly authorized unresolved labels.
- [ ] Final Markdown is `PROJECT_PROFILE.md`; any DOCX is derived from it.
