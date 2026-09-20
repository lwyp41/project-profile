# Progressive Interview Protocol

Interview only after discovery and evidence mapping. The agent owns the investigation burden; the user should answer only questions that artifacts and history cannot reliably answer.

## Selection rule

Rank candidate questions by:

1. whether the answer changes a material profile claim;
2. whether the answer cannot be recovered from available evidence;
3. whether the question is easy for the user to answer accurately;
4. whether it resolves a conflict or safety-sensitive ambiguity.

Ask a small batch, normally 3–5 questions. Avoid asking several variants of the same question. Show the reason for each question in plain language.

## Adaptive prompts

- Software/library: intended users, production status, key trade-off, operational constraints, measured quality.
- AI/agent/prompt: why AI, human review boundary, model choice, evaluation method, failure tolerance, cost or privacy constraints.
- Skill/documentation: intended trigger, expected output, decision boundaries, known failure modes, examples that represent success.
- Data/research: question, provenance, inclusion/exclusion, method, confidence, limitations, intended decision.
- Sparse/artifact: what the artifact was for, who used it, lifecycle status, missing surrounding materials.

## Accepted answers

Interpret “no” as a negative fact, “I don’t know” as `UNKNOWN`, “not applicable” as `NOT_APPLICABLE`, and “I don’t remember” as `UNKNOWN` unless corroborating evidence exists. “Maybe” or “I think” is normally `INFERRED` or `CLARIFICATION_REQUIRED`, not verified.

## Stop rule

Stop interviewing when the remaining questions are low-value, the user declines, or the remaining gaps can be represented transparently as unknown, N/A, or conflicting. Summarize what changed after each round.
