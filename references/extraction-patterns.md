# Extraction Patterns

Use these patterns as prompts for investigation, not as claims about every project.

## Repository and software

Inspect entry points, package manifests, configuration, tests, CI, deployment files, schemas, API routes, error handling, and examples. Compare documentation claims with implementation and history.

## AGENT_SKILL

Inspect frontmatter, trigger boundaries, workflow order, decision logic, references, examples, expected outputs, safety constraints, and failure modes. Distinguish intended behavior stated in instructions from behavior demonstrated by examples or tests.

## PROMPT_SYSTEM / AI_AGENT

Inspect prompts, model configuration, tool definitions, retrieval sources, memory/state, orchestration, guardrails, evaluator prompts, human checkpoints, and cost-sensitive choices. Do not infer model quality from prompt sophistication.

## LIBRARY

Inspect public entry points, exported interfaces, version metadata, dependencies, compatibility claims, tests, examples, and release history. Separate API existence from adoption or production use.

## DATA_PROJECT

Inspect source provenance, schemas, transformations, validation, missingness, privacy controls, outputs, and reproducibility. Do not infer data quality without measurements or documented validation.

## RESEARCH_PROJECT

Inspect question, hypotheses, sources, method, analysis, uncertainty, limitations, and reproducibility artifacts. Separate findings from interpretation and interpretation from application value.

## DOCUMENTATION_PROJECT

Inspect information architecture, audience, navigation, examples, update signals, ownership, and feedback mechanisms. Do not claim readership or effectiveness without evidence.

## SPARSE_ARTIFACT

Describe only observable structure and bounded implications. Maintain an explicit missing-evidence list and use interview questions to recover context where it materially changes interpretation.
