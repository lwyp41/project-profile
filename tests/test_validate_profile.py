import tempfile
import unittest
from pathlib import Path

from scripts.validate_profile import validate, validate_config

def validate_content(content: str) -> list[str]:
    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as handle:
        handle.write(content)
        profile = Path(handle.name)
    try:
        return validate(profile)
    finally:
        profile.unlink(missing_ok=True)


LEDGER_MARKER = "<!-- project-profile-ledger: v2 -->"
LEDGER_HEADER = "| ID | Module | Claim | Claim type | Status | Source kind | Locator | Time | Ownership | Metric | Rationale | Caveat | Conflict | Review state |"
CHINESE_LEDGER_HEADER = "| ID | 模块 | 主张 | 主张类型 | 状态 | 来源类型 | 定位 | 时间 | 归属 | 指标 | 理由 | 限制 | 冲突 | 审阅状态 |"
LEDGER_DIVIDER = "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"
LEDGER_ROW = "| F01 | project-overview | Example | fact | VERIFIED | repository | README | current | — | — | — | — | 无 | controlled-reviewed |"

class ValidateProfileTests(unittest.TestCase):
    def test_accepts_minimal_contract(self) -> None:
        statuses = "\n".join(("VERIFIED", "INFERRED", "CLARIFICATION_REQUIRED", "UNKNOWN", "NOT_APPLICABLE", "CONFLICTING"))
        table = "| a | b | c |\n|---|---|---|"
        ledger = "\n".join((LEDGER_MARKER, LEDGER_HEADER, LEDGER_DIVIDER, LEDGER_ROW))
        errors = validate_content(f"# Profile\n{statuses}\n{table}\n{table}\n{table}\n{ledger}")
        self.assertEqual(errors, [])

    def test_accepts_chinese_only_ledger_header(self) -> None:
        statuses = "\n".join(("VERIFIED", "INFERRED", "CLARIFICATION_REQUIRED", "UNKNOWN", "NOT_APPLICABLE", "CONFLICTING"))
        table = "| a | b | c |\n|---|---|---|"
        ledger = "\n".join((LEDGER_MARKER, CHINESE_LEDGER_HEADER, LEDGER_DIVIDER, LEDGER_ROW))
        self.assertEqual(validate_content(f"# 档案\n{statuses}\n{table}\n{table}\n{table}\n{ledger}"), [])

    def test_rejects_legacy_ten_column_ledger(self) -> None:
        statuses = "\n".join(("VERIFIED", "INFERRED", "CLARIFICATION_REQUIRED", "UNKNOWN", "NOT_APPLICABLE", "CONFLICTING"))
        table = "| a | b | c |\n|---|---|---|"
        legacy = "\n".join((LEDGER_MARKER, "| ID | Module | Claim | Status | Source | Locator | Time | Ownership | Metric | Notes |", "|---|---|---|---|---|---|---|---|---|---|", "| F01 | x | y | VERIFIED | repository | z | now | — | — | — |"))
        errors = validate_content(f"# Profile\n{statuses}\n{table}\n{table}\n{table}\n{legacy}")
        self.assertTrue(any("canonical fact ledger" in error for error in errors))

    def test_rejects_coverage_count_mismatch(self) -> None:
        statuses = "\n".join(("VERIFIED", "INFERRED", "CLARIFICATION_REQUIRED", "UNKNOWN", "NOT_APPLICABLE", "CONFLICTING"))
        table = "| a | b | c |\n|---|---|---|"
        ledger = "\n".join((LEDGER_MARKER, LEDGER_HEADER, LEDGER_DIVIDER, LEDGER_ROW))
        profile = f"# Profile\n{statuses}\n| VERIFIED | 2 | wrong |\n{table}\n{table}\n{ledger}"
        self.assertTrue(any("evidence coverage count" in error for error in validate_content(profile)))

    def test_rejects_verified_user_claim_outside_fixture(self) -> None:
        statuses = "\n".join(("VERIFIED", "INFERRED", "CLARIFICATION_REQUIRED", "UNKNOWN", "NOT_APPLICABLE", "CONFLICTING"))
        table = "| a | b | c |\n|---|---|---|"
        user_row = LEDGER_ROW.replace("repository | README", "user | T02")
        profile_text = f"# Profile\n{statuses}\n{table}\n{table}\n{table}\n{LEDGER_MARKER}\n{LEDGER_HEADER}\n{LEDGER_DIVIDER}\n{user_row}"
        with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as profile_handle, tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as fixture_handle:
            profile_handle.write(profile_text)
            fixture_handle.write("| T01 | supported testimony |\n")
            profile = Path(profile_handle.name)
            fixture = Path(fixture_handle.name)
        try:
            errors = validate(profile, fixture)
        finally:
            profile.unlink(missing_ok=True)
            fixture.unlink(missing_ok=True)
        self.assertTrue(any("testimony fixture" in error for error in errors))

    def test_rejects_unresolved_placeholder(self) -> None:
        errors = validate_content("# {{TITLE}}")
        self.assertIn("unresolved template placeholder found", errors)

    def test_rejects_invalid_config_values(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", encoding="utf-8", delete=False) as handle:
            handle.write("purpose: brochure\ndefault_depth: verbose\nmodules:\n  unknown-module: deep\n")
            config = Path(handle.name)
        try:
            errors = validate_config(config)
        finally:
            config.unlink(missing_ok=True)
        self.assertEqual(len(errors), 3)
