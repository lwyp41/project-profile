# Contributing to project-profile

This repository has two roles: it is the source repository and it can be copied directly into an Agent's Skills directory. Repository-maintenance instructions must therefore stay out of auto-loaded runtime instruction files such as `AGENTS.md` or `CLAUDE.md`.

## Repository boundaries

| Area | Role | Review focus |
|---|---|---|
| `SKILL.md`, `references/`, `templates/`, `scripts/` | Installed Skill behavior | Triggering, evidence discipline, workflow, output contract, portability |
| `examples/`, `tests/`, `evals/` | Quality and regression assets | Supported facts, failure cases, preset/depth differentiation |
| `docs/development/` and `evals/GOLDEN_EVAL_SPEC.md` | Design and evaluation sources | Requirement traceability and intentional deviations |
| `.github/`, `CONTRIBUTING.md` | Repository maintenance | Review, CI, and publication workflow |

Current user instructions take priority. Otherwise use this design-source order: `docs/development/MASTER_PLAN.md` → `evals/GOLDEN_EVAL_SPEC.md` → approved `docs/development/V2_DESIGN.md` → `docs/development/DECISIONS.md` → current implementation.

## Development workflow

1. Inspect `git status` and the applicable design/evaluation sources. Preserve unrelated or pre-existing work.
2. Define one reviewable change with explicit acceptance criteria. Behavior, evidence policy, templates, presets, and evaluation changes require a design/decision reference; minor wording fixes do not need a new design document.
3. Start new work from `origin/main` on a local `codex/<topic>` branch. If the worktree already contains uncommitted work, do not switch or recreate branches until its ownership and destination are clear.
4. Implement the smallest coherent change. Keep runtime instructions concise and put conditional detail behind references.
5. Run the relevant narrow checks, then the full local gate below.
6. Present the diff and verification results for human/web review. Review approval and publication authorization are separate decisions.
7. Only after explicit authorization, commit and push the feature branch. Open a PR against `main`; do not push implementation commits directly to `main`.
8. Merge only after CI and human review pass. Tag/release only when the user explicitly approves a release.

Recommended branch creation from this repository's current local setup (`master` tracks `origin/main`):

```powershell
git fetch origin
git switch -c codex/<topic> origin/main
```

Do not run these commands when uncommitted work would be displaced. Never use force push, history rewriting, or destructive cleanup as part of the normal workflow.

## Local verification gate

Run for behavior, reference, template, validator, or example changes:

```powershell
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_profile.py examples/example-skill-project-profile.md
python scripts/validate_profile.py examples/example-skill-project-profile.zh-CN.md
python scripts/validate_profile.py --config templates/profile-config.yaml
git diff --check
```

Also perform an evidence-aware review. Static validation cannot prove factual correctness, natural writing quality, baseline coverage, or meaningful preset/depth differentiation.

## Change coupling

- Runtime behavior change: update `SKILL.md` or its active reference, relevant example/test, and `CHANGELOG.md`.
- Output-contract change: update rendering policy, template, both localized examples, validator/tests, and changelog.
- Module, depth, or preset change: update registry/policy, config template, relevant eval assertion, and changelog.
- Evidence-state or interview change: update evidence/interview policy, regression coverage, and changelog.
- Approved architecture deviation: record it in `docs/development/DECISIONS.md` with rationale and rejected alternative.

Do not claim a controlled Golden evaluation passed until its frozen synthetic inputs, Resume and Technical profiles, coverage matrix, and fact-level baseline diff exist.

## Web review handoff

Ask the local agent for a review package like this:

```text
Read CONTRIBUTING.md and the applicable design sources.
Implement <one scoped change> locally and run the required checks.
Report changed files, commands/results, evidence or regression impact, and unresolved risks.
Do not commit, push, open a PR, merge, or release until I explicitly approve that action.
```

The implementation handoff must state: completion status, changed files and purpose, verification commands/results, known limitations, and current publication state.
