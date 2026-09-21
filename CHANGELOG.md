# Changelog

All notable changes to `project-profile` are recorded here.

## [Unreleased]

- Require an explicit `balanced`, `resume`, `technical`, or first-class `custom` profile mode before discovery; do not silently default.
- Require a material-gap scan, record an explicit no-interview reason when applicable, and hold final rendering behind the user-visible Review gate unless unattended/no-review was requested in advance.
- Refresh the bilingual README with the four-mode startup flow, Custom configuration guidance, and the Interview/Review gates.

## [0.3.0] - 2026-09-21

- Introduce Project Profile v2 as a configurable, evidence-backed project reconstruction system.
- Add `resume`, `technical`, and `balanced` presets with per-module investigation depth controls: `off`, `brief`, `standard`, and `deep`.
- Add a 15-module knowledge registry covering project context, users, requirements, workflow, architecture, AI/agent design, data, decisions, ownership, QA, outcomes, evolution, and risks.
- Reconstruct a Canonical Fact Model before prose, including claim type, evidence status, source locator, ownership, metric context, rationale, caveat, conflict, and review state.
- Add procedural module guidance for source inspection, interview triggers, false-inference prevention, and depth-specific investigation behavior.
- Add explicit Resume signal coverage for Ownership, Scale, Complexity, Decision, Impact, and Iteration.
- Require material, user-resolvable evidence gaps to pass through `CLARIFICATION_REQUIRED` before becoming `UNKNOWN`.
- Make profiles native-language by default and localize headings and interview questions instead of relying on a pivot-language draft.
- Replace the rigid all-sections output with an adaptive narrative, neutral downstream fact pack, and auditable evidence appendix.
- Add synthetic controlled Golden evaluations for Resume and Technical presets without publishing real-project fixtures or personal usage data.
- Add static validation for canonical ledgers, localized headers, evidence counts, testimony references, configuration values, and legacy-schema regressions.
- Add CI coverage for unit tests, bilingual examples, controlled synthetic profiles, and configuration validation.
- Add contributor guidance and a repository workflow for implementation, review, and regression checks.
- Keep resume bullets, promotional framing, and unsupported impact claims outside the Skill's responsibility.

## [0.1.0] - 2026-09-20

- Initial evidence-first completed-project reverse-engineering workflow.
- Added Core + Conditional profile schema.
- Added evidence policy, adaptive interview protocol, architecture analysis, and extraction patterns.
- Added `PROJECT_PROFILE.md` template and Agent Skill example.
