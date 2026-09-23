# Observable depth and low-friction Custom configuration contract

## Problem summary

Real usage after v0.3.1 exposed two distinct behavioral defects.

### Defect A — Custom configuration is discoverable but still high-friction

The current Custom onboarding correctly exposes all four investigation depths and all 15 canonical modules, but the interaction still presents internal canonical IDs such as `technical-architecture` and `decisions-tradeoffs` as the primary selection surface.

For a Chinese-language user, this makes configuration unnecessarily expensive to type and easy to get wrong. The user should not need to copy long English IDs just to express preferences.

### Defect B — Investigation depth is not sufficiently observable in the rendered result

The current depth contract is primarily an investigation contract. For example, `deep` tells the Skill to inspect implementation, history, failure paths, alternatives, conflicting sources, and other high-value evidence. However, rendering policy does not require the additional semantic coverage recovered at deeper levels to remain visible in Review or final output.

This allows a run to investigate deeply but render shallowly. In practice, `brief`, `standard`, and `deep` can collapse into similarly short summaries.

This is especially visible for modules such as:

- `technical-architecture`
- `product-workflow`
- `decisions-tradeoffs`
- `evolution-history`
- `validation-qa`
- `risks-limitations`

The user experience failure is not merely “the answer should be longer.” The real defect is that semantic coverage and module preservation are not strong enough to make the selected depth observable.

## Product intent

Depth must control both:

1. **Investigation commitment** — what sources and evidence must be inspected.
2. **Rendered substance** — what categories of recovered facts must remain visible in Review and final rendering.

Depth is still not a word-count setting. A longer paragraph is not proof of a deeper result. The distinction must be semantic.

Custom configuration should also be easy to express in the user's own language, without requiring canonical IDs.

## Required behavior

### 1. Low-friction Custom selection

When Custom is selected, the user-facing module list must expose a short local-language label and a numeric selector in addition to the canonical module ID.

For Chinese, a suitable interaction surface is:

1. 项目概览 — `project-overview`
2. 背景与问题 — `background-problem`
3. 用户与相关方 — `users-stakeholders`
4. 目标与成功标准 — `goals-success`
5. 需求与约束 — `requirements-constraints`
6. 产品与流程 — `product-workflow`
7. 技术架构 — `technical-architecture`
8. AI / Agent 设计 — `ai-agent-design`
9. 信息与数据 — `information-data`
10. 决策与取舍 — `decisions-tradeoffs`
11. 个人贡献 — `ownership-contribution`
12. 验证与 QA — `validation-qa`
13. 成果与指标 — `outcomes-metrics`
14. 项目演进 — `evolution-history`
15. 风险与限制 — `risks-limitations`

The user must be told explicitly that canonical IDs are optional for input.

Accepted compact forms must include:

```text
全部 standard；6,7,8,10,12,14 deep；11 brief
```

```text
全部 deep；个人贡献 brief
```

```text
架构、流程、Agent、决策、验证、演进 deep，其余 standard
```

Equivalent compact interaction must be localized for other request languages.

The Skill must normalize numbers, localized labels, reasonable aliases, and canonical IDs into the canonical module configuration before discovery.

### 2. Depth controls semantic render coverage

The current rule “depth is an investigation commitment, not a word-count setting” remains valid, but it is incomplete.

Each enabled module must define both:

- investigation obligations by depth;
- render obligations by depth.

The deeper level must preserve at least the semantic obligations of the shallower level where the facts exist.

#### Brief

Brief is intentionally selective.

Expected result:

- orientation and the highest-value facts only;
- enough context to understand what the module says;
- no requirement to explain every mechanism or historical transition.

Brief must not be used as an implicit fallback for a module configured as Standard or Deep.

#### Standard

Standard is the normal “complete project summary” depth.

Where applicable and evidence exists, Standard must make visible:

- what exists / what the module covers;
- how the core mechanism or workflow works;
- at least one major constraint, choice, result, or limitation relevant to that module;
- the evidence boundary for unresolved material facts.

A Standard module should not read like a one-line orientation.

#### Deep

Deep must be materially richer in semantic structure, not merely prose length.

Where applicable and evidence exists, Deep must actively recover and preserve visible coverage of relevant categories such as:

- architecture / workflow structure and component relationships;
- runtime, data flow, state handoffs, or control flow;
- failure and degradation paths;
- constraints and serious alternatives;
- choice, rationale, and consequence;
- historical variants and transition triggers;
- validation strategy and uncovered boundaries;
- conflicts or contradictory sources;
- unresolved material gaps requiring user clarification.

Not every module uses every category. The module-specific contract decides which categories are relevant.

A Deep module must not be rendered as a generic compact summary after deep investigation.

### 3. Module-specific render contracts must be explicit

Update the module guidance files so `Brief`, `Standard`, and `Deep` specify observable rendered substance.

Examples:

#### `technical-architecture`

- **Brief render:** system boundary, runtime/entry point, 1–2 core components.
- **Standard render:** component relationships, core runtime/data path, major interfaces/integrations, one consequential design choice or constraint, important limitation.
- **Deep render:** architecture layers/boundaries, runtime and data/control flow, failure/degradation paths, deterministic validation boundaries, consequential decisions/rationale, evolution where material, unresolved evidence limits.

#### `product-workflow`

- **Brief render:** primary input → processing → output.
- **Standard render:** actors, happy path, major gates/handoffs, output, guarded/failure path.
- **Deep render:** public entry paths, state handoffs, approval/HITL gates, source boundaries, fallback/degradation behavior, rationale for separation, material failure prevention.

#### `decisions-tradeoffs`

- **Brief render:** most consequential supported choice.
- **Standard render:** constraint → choice → consequence; include rationale only when supported.
- **Deep render:** constraint → serious alternatives → choice → rationale → consequence → later validation/revision; unresolved rationale remains clarification-required rather than invented.

#### `evolution-history`

- **Brief render:** major phases.
- **Standard render:** phase → trigger → major change → current state.
- **Deep render:** initial state → limitation → redesign/migration → consequence → current state; reconcile chronology conflicts and preserve uncertain pre-repository history.

Equivalent explicit render contracts should exist for all modules, not only these examples.

### 4. Preserve enabled module coverage

Rendering currently allows natural narrative composition, but it must not silently erase enabled modules.

For every module that is:

- enabled;
- applicable;
- and has material recovered facts,

the Review must include a visible module disposition:

```text
module → effective depth → recovered coverage → proposed render destination
```

Final rendering may merge closely related modules into one natural section, but only if the semantic coverage of each merged module remains identifiable.

A module may be omitted from final prose only when:

- `off`;
- genuinely `NOT_APPLICABLE`;
- or it has no material facts after investigation and that absence is explicitly surfaced at Review.

“Natural prose” is not a justification for dropping configured modules.

### 5. Review must expose depth execution before final Render

The existing Review hard gate should make depth execution inspectable.

For each enabled applicable module, show at least:

- effective depth;
- primary source classes inspected;
- recovered semantic coverage;
- material gaps / clarification state;
- proposed render destination.

The purpose is not to expose chain-of-thought or raw notes. It is to let the user detect failures such as:

- architecture configured Deep but only a generic overview was recovered;
- evolution configured Deep but no historical variants were investigated;
- a configured module disappeared entirely.

### 6. Balanced must remain balanced, but Standard must be substantive

Do not “fix” this by simply converting Balanced to all-Deep.

Current Balanced semantics remain appropriate in principle:

- `project-overview`: brief
- `risks-limitations`: brief
- other applicable modules: standard

The defect is that Standard can currently render too shallowly.

After this change, Balanced should produce a complete, useful project reconstruction because Standard has a meaningful semantic render contract. Technical / Resume / Custom Deep should then be observably richer in their selected modules.

### 7. No invented facts to satisfy depth

A deeper render contract must never force fabricated material.

If a Deep obligation cannot be satisfied from project evidence and the missing information is material and user-answerable, it becomes `CLARIFICATION_REQUIRED`.

If it is not user-answerable or remains unresolved after interview, preserve the correct evidence state.

Never invent:

- alternatives;
- rationale;
- ownership;
- adoption;
- metrics;
- outcomes;
- failure causes;
- chronology.

Depth increases investigation and visible evidence coverage, not speculation.

## Acceptance scenarios

### Scenario A — Chinese Custom configuration without canonical IDs

Given the user selects Custom in Chinese, the next response must allow a valid answer such as:

```text
全部 standard；6,7,8,10,12,14 deep；11 brief
```

The user must not need to type `technical-architecture` or other canonical IDs.

### Scenario B — Natural-language aliases

Given:

```text
架构、流程、Agent、决策、验证、演进 deep，其他 standard，个人贡献 brief
```

the Skill must map these to the correct canonical modules without unnecessary clarification.

### Scenario C — Standard is observably more complete than Brief

For the same fixture and module, Standard must preserve the Brief core orientation and add the module's required Standard semantic categories.

A test should fail if Standard merely produces the same semantic coverage as Brief with slightly different prose.

### Scenario D — Deep is observably richer than Standard

For the same fixture and module, Deep must preserve the Standard semantic categories and add the relevant Deep categories where evidence exists.

For example, Technical Architecture Deep should surface failure/degradation or runtime/data-flow/evolution categories when the frozen fixture contains them.

### Scenario E — Enabled module cannot silently disappear

Given `technical-architecture=deep`, `product-workflow=deep`, and `evolution-history=deep` with material evidence for all three, Review and final rendering must preserve identifiable semantic coverage for all three even if sections are merged.

### Scenario F — Deep gap triggers clarification instead of invention

If a Deep decision reconstruction finds a visible choice but no supported rationale, the result must create `CLARIFICATION_REQUIRED` rather than inventing a rationale to satisfy the Deep contract.

## Test requirements

The current instruction-contract tests are not sufficient by themselves.

Add layered regression coverage:

1. **Instruction contract tests**
   - numeric/localized Custom selectors;
   - canonical IDs are optional user input;
   - depth controls both investigation and rendered substance;
   - enabled material modules cannot silently disappear;
   - Review exposes effective depth and recovered semantic coverage.

2. **Module contract tests**
   - every module file contains explicit Brief / Standard / Deep render obligations, not only investigation verbs.

3. **Controlled depth-differentiation evaluation**
   - use a frozen synthetic fixture;
   - compare the same module at Brief / Standard / Deep;
   - assert semantic coverage differences, not word count;
   - deeper coverage should be monotonic where fixture evidence exists;
   - include at least architecture, workflow, decisions, and evolution.

4. **Coverage-preservation evaluation**
   - configure multiple modules at Deep;
   - verify each enabled applicable material module has a Review disposition and a final render destination.

Do not make “more words” the passing criterion.

## Likely implementation areas

Expected files include:

- `SKILL.md`
- `references/depth-policy.md`
- `references/rendering-policy.md`
- `references/module-registry.md`
- all relevant `references/modules/*.md`
- `references/interview-policy.md` if Review disclosure needs alignment
- `tests/test_instruction_contracts.py`
- controlled synthetic eval assets/tests
- `CHANGELOG.md`

Update README only if user-facing configuration examples need alignment. Do not restructure its bilingual layout.

## Non-goals

- Do not make Deep synonymous with maximum verbosity.
- Do not require one heading per canonical module if natural grouping is clearer.
- Do not convert Balanced to all-Deep.
- Do not weaken evidence discipline.
- Do not generate resume bullets.
- Do not invent rationale, ownership, metrics, impact, or outcomes.
- Do not remove the Review hard gate.
