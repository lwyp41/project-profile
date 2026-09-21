# Golden Evaluation Specification

This public regression framework uses only synthetic fixtures. It validates the Project Profile Skill's evidence handling and output contract; it is not evidence about a real repository, person, product, customer, or outcome.

## Controlled fixture contract

- Every controlled run uses one frozen synthetic repository revision and one frozen testimony fixture.
- The Resume and Technical presets consume the same inputs but differ in source priority, module emphasis, and unanswered questions.
- A verified user-sourced ledger claim must cite a known T ID from the fixture.
- Coverage counts must equal the canonical ledger's status totals.
- Unsupported impact, adoption, time-saving, or quality claims remain `UNKNOWN`.

## Required artifacts

```text
evals/synthetic-agent-skill/
  input/testimony-fixture.md
  README.md
  coverage-matrix.md
  baseline-diff.md
  unresolved-facts.md
  resume-profile-v2.md
  technical-profile-v2.md
```

## Acceptance criteria

1. Both profiles validate against the same fixture.
2. Both contain the canonical 14-column ledger and all evidence states.
3. The profiles have distinct preset emphasis without upgrading inference or unknowns into facts.
4. The baseline diff has no high-value supported `LOST` item.
5. CI runs both controlled profiles and the unit tests.
