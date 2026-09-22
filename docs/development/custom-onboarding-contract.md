# Custom onboarding interaction contract

## Problem

The mandatory profile-mode gate now correctly requires the user to choose `Balanced`, `Resume`, `Technical`, or `Custom` before discovery. In real usage, however, choosing `Custom` can still produce an under-specified prompt such as "tell me which modules and depths you want" without first showing the available module set, the four depth levels, or how unspecified modules are handled.

That behavior forces the user to ask follow-up questions such as "how should I choose?" or "are these the only modules?" before they can configure the run. The configuration gate is therefore enforced, but not self-explanatory.

## Product intent

A user who selects `Custom` should be able to provide a valid configuration in the next message without needing to know Project Profile internals or ask for the option space.

This change is about onboarding and interaction clarity. It must not weaken evidence rules, Interview behavior, the Review gate, or the first-class nature of Custom.

## Required behavior

### 1. Custom must explain the choice space before asking for configuration

After the user selects `Custom`, and before repository discovery begins, the Skill must proactively show:

- the four investigation depths and a short meaning for each:
  - `off` — do not independently investigate or render the module;
  - `brief` — inspect only obvious high-signal sources;
  - `standard` — inspect primary artifacts plus relevant docs/examples/tests;
  - `deep` — also investigate history, alternatives, conflicts, outcomes, failures, and user-answerable gaps;
- all 15 canonical modules, using the canonical module ID plus a short explanation in the user's language;
- at least one compact valid configuration example.

The user must not have to ask "what modules exist?", "what do the depths mean?", or "how do I write the configuration?" before being able to answer.

### 2. Make compact configuration the default interaction

Do not require the user to configure all 15 modules one by one.

Explain that the user can provide only the exceptions they care about, for example:

```text
default depth: standard
deep: technical-architecture, decisions-tradeoffs, validation-qa
brief: outcomes-metrics
off: ownership-contribution
```

Natural-language equivalents remain valid, for example:

```text
默认 standard；架构、关键决策和验证 deep；成果 brief；不分析个人贡献。
```

### 3. Unspecified modules need a visible baseline

For `Custom`, unspecified applicable modules use a visible `standard` baseline unless the user explicitly chooses another default depth.

The Skill must state this baseline in the Custom onboarding response. It must not silently apply it.

If the user sets a different default depth, that explicit choice becomes the baseline. Explicit per-module overrides still win.

### 4. Improve the initial Custom mode description

The first four-way mode prompt should keep the mode descriptions brief, but the `Custom` line should make discoverability explicit, e.g. that Custom controls 15 modules and four depth levels and that the Skill will show the full option set after selection.

The detailed 15-module/depth explanation belongs after the user selects Custom, not in the initial four-way mode prompt.

### 5. No discovery before Custom configuration is complete

The existing hard gate remains binding:

`PROFILE_MODE_SELECTED -> DISCOVERED`

For Custom, profile-mode selection alone does not complete configuration. The Skill must finish the Custom onboarding/configuration exchange before discovery.

Previously injected context may be summarized if it already exists in the conversation, but the Skill must not initiate new repository inspection before the Custom configuration is resolved.

## Canonical module list

The onboarding response must expose all 15 canonical IDs:

1. `project-overview`
2. `background-problem`
3. `users-stakeholders`
4. `goals-success`
5. `requirements-constraints`
6. `product-workflow`
7. `technical-architecture`
8. `ai-agent-design`
9. `information-data`
10. `decisions-tradeoffs`
11. `ownership-contribution`
12. `validation-qa`
13. `outcomes-metrics`
14. `evolution-history`
15. `risks-limitations`

The one-line descriptions should come from the module registry rather than introducing a second conflicting taxonomy.

## Acceptance scenarios

### Scenario A: user selects Custom by number

Given the Skill has shown the four profile modes and the user replies:

```text
4
```

The next Skill response must, before discovery:

- identify that Custom was selected;
- explain `off / brief / standard / deep`;
- show all 15 modules;
- explain that unspecified applicable modules default visibly to `standard`;
- provide a compact configuration example;
- ask the user for their configuration.

A response that only says "tell me which modules and depths you want" fails this contract.

### Scenario B: user names Custom directly

Given the initial request explicitly says:

```text
Use project-profile in Custom mode.
```

The same Custom onboarding contract applies before discovery unless the request already contains enough valid module/depth configuration to fully resolve Custom.

### Scenario C: configuration already complete

If the user explicitly supplies a valid Custom configuration in the initial request, do not repeat the full onboarding unnecessarily. Confirm the interpreted configuration concisely and proceed to discovery.

### Scenario D: partial configuration

If the user supplies only overrides such as:

```text
deep decisions and architecture; off outcomes
```

Interpret them against the visible `standard` baseline, confirm the resulting rule, and clarify only genuine ambiguities such as unknown module names or invalid depth values.

## Tests

Add regression coverage in `tests/test_instruction_contracts.py` (or an equivalent focused contract test) so CI protects the interaction contract.

At minimum, tests should verify that the Skill instructions require:

- proactive Custom onboarding after Custom selection;
- all four depth names;
- the complete 15-module option space;
- a compact configuration example;
- a visible default-depth rule for unspecified applicable modules;
- no repository discovery before Custom configuration is resolved.

If the repository has an appropriate deterministic interaction/eval fixture, add a lightweight scenario for "select Custom -> receive complete option space" as well. Do not introduce a heavyweight agent runtime dependency solely for this test.

## Scope / non-goals

- Do not change the six evidence states or Canonical Fact Model.
- Do not weaken the material-gap Interview requirement.
- Do not weaken the user-visible Review hard gate.
- Do not generate resume bullets or promotional claims.
- Do not restructure the README bilingual layout. The intended README pattern remains: within each section, complete English content first, then complete Chinese content.
- Keep `Custom` first-class; do not implement it as Balanced plus hidden tweaks.
