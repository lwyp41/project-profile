# Rendering Policy

The canonical fact model is constructed before prose. Its required fields are `id`, `module`, `claim`, `claim_type`, `status`, `source_kind`, `source_locator`, `time_context`, `ownership`, `metric`, `rationale`, `caveat`, `conflict`, and `review_state`; fields may be null only when inapplicable or explicitly unresolved. `claim_type` is one of `fact`, `design_intent`, `mechanism`, `observed_outcome`, or `measured_outcome`; it prevents downstream reuse from upgrading a safeguard into a result.

Use `fact` for historical, attribution, and directly evidenced state claims; use `design_intent` only for a stated goal or rationale; use `mechanism` for an implemented rule or control; and use `observed_outcome` only for an observed run result or user observation. For example, “the validator ran successfully” is an `observed_outcome`, while “the validator rejects overwrite” is a `mechanism`.

Use a Module Coverage Map while investigating: module, applicability, effective depth, priority/inspected sources, fact IDs, material gaps, interview candidates, and render decision. This map proves investigation behavior without exposing sensitive raw material by default.

Render `PROJECT_PROFILE.md` in the request language as: project overview; only enabled, applicable knowledge modules; neutral reusable downstream facts; and an evidence appendix with coverage, Unknown/N/A/conflicts, complete claim ledger, and review record. Persist every fact-model field in the ledger as separate columns; no rationale/caveat/conflict/review-state field may be collapsed. Empty headings are omitted. The fact pack is a selected projection, not the only fact store, and must not become resume bullets or promotional prose.

Metrics require value, unit, scope, time window, and source. Ownership must be sourced independently; repository location alone does not establish authorship. Every inference records its observation and reasoning. Conflicting facts remain visible.
