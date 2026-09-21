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

    def test_controlled_eval_has_no_divergent_input_state(self) -> None:
        root = ROOT / "evals" / "synthetic-agent-skill"
        legacy_markers = ("INCONCLUSIVE", "not a controlled test", "clean rerun is still needed", "supplied differently across")
        for path in (root / "coverage-matrix.md", root / "baseline-diff.md", root / "unresolved-facts.md"):
            text = path.read_text(encoding="utf-8")
            with self.subTest(artifact=path.name):
                for marker in legacy_markers:
                    self.assertNotIn(marker, text)
