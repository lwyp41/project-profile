# Example: Project Profile for an Agent Skill

This example demonstrates format and evidence discipline. It is illustrative, not evidence about any real project.

## Project identity

- Name: `incident-triage`
- Type: `AGENT_SKILL`
- Status: `VERIFIED` — the artifact contains a complete Skill package.
- Primary sources: `repository` (the Skill files), `documentation` (included examples).

## Purpose

`VERIFIED`: The skill guides an agent through classifying incoming incident reports, checking reproduction details, and preparing a structured triage brief. Evidence: `SKILL.md`, “Purpose” and workflow sections.

`UNKNOWN`: Whether teams adopted the skill or reduced triage time. No metric or user statement was available.

## Trigger conditions

`VERIFIED`: It applies to incoming bug reports and feature requests that need classification and verification. Evidence: frontmatter description and trigger section.

`NOT_APPLICABLE`: A runtime API latency target is not applicable to the skill artifact itself.

## Workflow and decision logic

`VERIFIED`: The workflow collects the report, checks scope and reproducibility, classifies the request, and produces an agent-ready brief. Evidence: ordered workflow headings.

`INFERRED`: The ordered checks are intended to reduce premature implementation because the workflow requires verification before preparation. Rationale: sequence in `SKILL.md`; no measured effect is claimed.

## References, examples, and expected outputs

`VERIFIED`: References define the required report fields and examples show the expected brief shape. Evidence: `references/` and `examples/`.

## Failure modes and risks

`VERIFIED`: The skill warns against accepting unverified reproduction claims and against treating out-of-scope requests as implementation work. Evidence: constraints and stop conditions.

`UNKNOWN`: Real-world failure rate, false-positive rate, and business impact.

## Evidence Coverage

| Category | Count | Notes |
|---|---:|---|
| Verified | 6 | Purpose, triggers, workflow, references, examples, constraints |
| Inferred | 1 | Bounded interpretation of workflow ordering |
| Clarification required | 0 | No blocking clarification identified |
| Unknown | 3 | Adoption, time reduction, failure rates |
| Not applicable | 1 | Runtime latency target |
| Conflicting | 0 | No conflicting sources found |

## Review gate

The user confirmed the artifact description and explicitly accepted adoption and impact as `UNKNOWN`. The final Markdown remains the source of truth.
