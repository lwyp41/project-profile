# v2 Validation

Run `python scripts/validate_profile.py <rendered-profile.md>` for static output checks. It checks placeholders, evidence/review markers, status presence, and a claim-ledger header; it cannot prove a claim is true.

The regression matrix is `synthetic-agent-skill`, `software`, and `sparse` × `resume` and `technical`. Every run needs source-aware coverage, unsupported-claim review, preset differentiation, and depth differentiation based on inspected sources, recovered facts, and questions—not word count. The controlled synthetic fixture additionally needs a fact-level baseline diff with no high-value supported `LOST` item.
