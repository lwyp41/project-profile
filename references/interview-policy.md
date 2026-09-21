# Interview Policy v2

Investigate first, then rank material missing facts by decision value, recoverability, answerability, and conflict/safety importance. Ask 3–5 natural-language questions per round and explain why each matters. Record answers in the canonical fact model and apply the status transition in `evidence-policy.md`.

## Mandatory gap scan

After investigation and before review, inspect every enabled module for material gaps. A gap is interview-eligible when all three conditions hold:

1. the missing fact could materially change project interpretation, ownership, decision rationale, evolution, outcome, risk, or downstream reuse;
2. the repository and other available artifacts do not resolve it reliably;
3. the user could reasonably know or remember the answer.

When an interview-eligible gap exists, mark it `CLARIFICATION_REQUIRED` and ask it before the fact can become `UNKNOWN`.

If no interview is needed, do not silently skip the state. Record a concise reason such as: "No material user-answerable gaps remained after repository and history inspection." This reason must be surfaced at the review gate.

For every enabled module, use its guidance to form questions. Decision mining follows `constraint → alternatives → chosen approach → rationale → consequence`; a visible choice without a supported rationale is `CLARIFICATION_REQUIRED`, not a made-up explanation. Evolution reconstruction attempts `initial state → first implementation → discovered limitation → redesign/migration → current state`.

For `purpose: resume`, before the review gate explicitly assess these six signals: Ownership, Scale, Complexity, Decision, Impact, and Iteration. Search artifacts first; then ask about each material, user-answerable gap. Do not mark such a gap `UNKNOWN` before the interview opportunity.

## Review gate

The review gate is a user-visible stop, not an internal mental step. Show:

- selected profile mode;
- effective module/depth configuration;
- material facts and evidence states;
- fact pack;
- unresolved facts;
- proposed Unknown/N/A decisions;
- conflicts;
- interview outcome, including an explicit skip reason when no interview occurred;
- for `resume`, the six-signal check.

Final rendering waits for user approval or correction. The only exception is when the user explicitly requested an unattended/no-review run before reaching the review state.
