# project-profile

Evidence-first reverse engineering of completed projects into a validated `PROJECT_PROFILE.md`.

This skill is designed for software repositories, lightweight repositories, `AGENT_SKILL`, `PROMPT_SYSTEM`, `AI_AGENT`, `LIBRARY`, `DATA_PROJECT`, `RESEARCH_PROJECT`, `DOCUMENTATION_PROJECT`, and sparse/artifact projects. It emphasizes provenance, bounded inference, explicit uncertainty, adaptive interviews, and a user review gate.

## Install

Copy the `project-profile` directory into the target agent's skills directory. For Codex, the usual location is:

```text
~/.codex/skills/project-profile
```

The skill is provider-neutral: agents that support the `SKILL.md` convention can use the same directory.

## Use

Ask the agent to use `project-profile` to reverse-engineer a completed project. The generated `PROJECT_PROFILE.md` is the canonical output. A DOCX, if requested, is only a derivative.

## Design commitments

- Discover before interviewing.
- Separate `UNKNOWN` from `NOT_APPLICABLE`.
- Never invent metrics, impact, users, rationale, alternatives, or outcomes.
- Preserve evidence source kinds: repository, documentation, git_history, user, inference, and external_reference.
- Require a Project Profile Review Gate before final generation.

## Development

Edit the files in this repository, update `CHANGELOG.md`, run the checks in `tests/`, and tag a release. Keep installed copies pinned to a release for stable use.
