import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "references" / "modules"


class InstructionContractTests(unittest.TestCase):
    def test_every_module_has_procedural_contract(self) -> None:
        required = ("Goal", "Applicability", "Brief", "Standard", "Deep", "Facts", "render")
        for path in MODULES.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            with self.subTest(module=path.name):
                for marker in required:
                    self.assertIn(marker.lower(), text.lower())

    def test_canonical_fact_model_preserves_claim_type_and_fields(self) -> None:
        policy = (ROOT / "references" / "rendering-policy.md").read_text(encoding="utf-8")
        template = (ROOT / "templates" / "PROJECT_PROFILE.md").read_text(encoding="utf-8")
        for marker in ("claim_type", "rationale", "caveat", "conflict", "review_state"):
            self.assertIn(marker, policy)
        for marker in ("CLAIM_TYPE", "RATIONALE", "CAVEAT", "CONFLICT", "REVIEW_STATE"):
            self.assertIn(marker, template)

    def test_profile_mode_selection_is_mandatory_and_includes_custom(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8").lower()
        registry = (ROOT / "references" / "module-registry.md").read_text(encoding="utf-8").lower()
        self.assertIn("mandatory profile-mode selection", skill)
        self.assertIn("do not infer, auto-select, or silently default", skill)
        for mode in ("balanced", "resume", "technical", "custom"):
            self.assertIn(mode, skill)
            self.assertIn(mode, registry)

    def test_custom_onboarding_exposes_complete_choice_space_before_discovery(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8").lower()
        registry = (ROOT / "references" / "module-registry.md").read_text(encoding="utf-8").lower()
        onboarding_start = skill.index("for **custom**, complete an explicit onboarding exchange")
        onboarding_end = skill.index("## workflow", onboarding_start)
        onboarding = skill[onboarding_start:onboarding_end]
        self.assertIn("immediately after custom is selected, proactively show", onboarding)
        self.assertLess(
            onboarding.index("immediately after custom is selected"),
            onboarding.index("the custom onboarding must include this complete choice space"),
        )
        for depth in ("off", "brief", "standard", "deep"):
            self.assertIn(f"`{depth}`", onboarding)
        modules = (
            "project-overview", "background-problem", "users-stakeholders",
            "goals-success", "requirements-constraints", "product-workflow",
            "technical-architecture", "ai-agent-design", "information-data",
            "decisions-tradeoffs", "ownership-contribution", "validation-qa",
            "outcomes-metrics", "evolution-history", "risks-limitations",
        )
        for module in modules:
            with self.subTest(module=module):
                self.assertIn(f"`{module}`", onboarding)
                self.assertIn(f"`{module}`", registry)
        self.assertIn("compact example", onboarding)
        self.assertIn("natural-language", onboarding)
        self.assertIn("visible `standard` baseline", onboarding)
        self.assertIn("explicit module overrides always take precedence", onboarding)
        self.assertIn("do not begin new repository discovery until custom configuration is resolved", onboarding)

    def test_custom_configuration_gate_precedes_discovery(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        selection = skill.index("1. **Select profile mode")
        discovery = skill.index("2. **Discover")
        custom_gate = skill.index("For Custom, the onboarding/configuration exchange is part of this gate")
        self.assertLess(selection, discovery)
        self.assertLess(custom_gate, discovery)

    def test_interview_and_review_states_are_explicit_runtime_gates(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8").lower()
        policy = (ROOT / "references" / "interview-policy.md").read_text(encoding="utf-8").lower()
        self.assertIn("interview_resolved_or_justified_skip", skill)
        self.assertIn("review_approved", skill)
        self.assertIn("explicitly record why the interview is skipped", skill)
        self.assertIn("review gate is a user-visible stop", policy)
        self.assertIn("final rendering waits for user approval", policy)

    def test_controlled_eval_has_no_divergent_input_state(self) -> None:
        root = ROOT / "evals" / "synthetic-agent-skill"
        legacy_markers = ("INCONCLUSIVE", "not a controlled test", "clean rerun is still needed", "supplied differently across")
        for path in (root / "coverage-matrix.md", root / "baseline-diff.md", root / "unresolved-facts.md"):
            text = path.read_text(encoding="utf-8")
            with self.subTest(artifact=path.name):
                for marker in legacy_markers:
                    self.assertNotIn(marker, text)
