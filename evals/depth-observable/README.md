# Controlled observable-depth evaluation

`controlled-depth-eval.json` freezes one evidence fixture for architecture, workflow, decisions, and evolution. The test compares its recovered semantic coverage with the semantic tags extracted from the corresponding Markdown artifact in `renders/`; it never compares word count.

Each artifact is a deliberately compact rendered profile fragment. Its `[category]` tags make the evidence-backed semantic content machine-checkable without treating length or generic detail words as a proxy for depth. Brief, Standard, and Deep use the same fixture and must have strictly monotonic coverage; the multi-module record verifies Review dispositions and final destinations.
