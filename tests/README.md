# Validation fixtures

This directory defines the minimum regression checks for future releases. The first release intentionally uses documentation-based checks rather than scripts.

For each release, verify that:

- `SKILL.md` keeps the workflow order: Discover → Classify Project Type → Select Adaptive Analysis Mode → Build Evidence Map → Extract Verified Knowledge → Detect Knowledge Gaps → Progressive User Interview → Synthesize → Validate → User Review Gate → Generate.
- The six statuses remain present and distinct: `VERIFIED`, `INFERRED`, `CLARIFICATION_REQUIRED`, `UNKNOWN`, `NOT_APPLICABLE`, `CONFLICTING`.
- The nine supported project types remain routable.
- The template includes Evidence Coverage, Evidence ledger, Career-Relevant Signals, and Review record.
- The example demonstrates both `UNKNOWN` and `NOT_APPLICABLE`.
- No example asserts unsupported metrics, business impact, users, decision rationale, or alternatives.

Future versions may add anonymized fixture projects and automated validators. Keep fixtures free of secrets and private project data.
