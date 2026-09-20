# Adaptive Architecture Analysis

Architecture means the structure that makes the project work. For a small skill or document, that may be the instruction graph and reference layout rather than services and databases.

## Analysis lens

Identify, only where applicable:

- boundaries and responsibilities;
- inputs, transformations, state, and outputs;
- interfaces, contracts, and handoffs;
- dependencies and external systems;
- control flow, decision points, and failure paths;
- persistence, retrieval, evaluation, and observability;
- deployment or distribution model;
- human approval or intervention points.

Represent uncertainty explicitly. A file tree can verify organization, but it cannot by itself verify runtime behavior, scale, or business purpose.

## Project-type cues

| Type | Architecture object |
|---|---|
| Software / library | modules, packages, APIs, runtime, dependencies, data flow |
| AI agent / prompt system | model calls, tools, memory/RAG, orchestration, guardrails, review loop |
| Agent skill | trigger, instructions, reference routing, decision logic, output contract |
| Data project | sources, transformations, storage, analysis, validation, consumers |
| Research project | question, evidence pipeline, method, analysis, findings, reproducibility |
| Documentation project | information hierarchy, audience paths, maintenance and feedback loop |
| Sparse artifact | observable structure, implied interface, missing context, confidence boundary |
