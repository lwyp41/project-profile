# Controlled observable-depth evaluation

`controlled-depth-eval.json` is a deterministic **contract fixture** for architecture, workflow, decisions, and evolution. The test compares its recovered semantic coverage with the semantic tags extracted from the corresponding Markdown artifact in `renders/`; it never compares word count. It does not execute the Skill workflow or a model, so it cannot by itself prove live agent behavior.

Each artifact is a deliberately compact rendered profile fragment. Its `[category]` tags make the evidence-backed semantic content machine-checkable without treating length or generic detail words as a proxy for depth. Brief, Standard, and Deep use the same fixture and must have strictly monotonic coverage; the multi-module record verifies Review dispositions and final destinations. See [branch-loaded-manual-acceptance.md](branch-loaded-manual-acceptance.md) for the complementary branch-loaded manual acceptance record.
