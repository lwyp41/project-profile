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
