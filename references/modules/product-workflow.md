# Product and Workflow

## Goal

Map inputs, transformations, routing, human gates, handoffs, outputs, refusal/degradation paths, and supported rationale for material separation.

## Applicability and depth

Enable for products, services, agents, prompts, operations, and tools with meaningful flow. N/A requires no meaningful process.

- **Brief:** inspect workflow diagram, README, and entry instructions.
- **Standard:** inspect templates, examples, tests, UI/process artifacts, and failure handling; trace a happy path and guarded path.
- **Deep:** trace each public entry, state handoff, approval, source boundary, and degradation branch; compare declared and implemented behavior.

## Facts, interview, and rendering

Record actor, input, transformation, gate, output, failure path, source, rationale, and ownership. Ask which step prevents the highest-cost failure and what happens when tools, evidence, or approval are unavailable. Do not call a file list a workflow or assert quality improvement without observation; render gates explicitly.
