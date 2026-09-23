#!/usr/bin/env python3
"""Static contract checks for a rendered Project Profile v2 Markdown file."""
from __future__ import annotations
import argparse
import re
from pathlib import Path

STATUSES = {"VERIFIED", "INFERRED", "CLARIFICATION_REQUIRED", "UNKNOWN", "NOT_APPLICABLE", "CONFLICTING"}
DEPTHS = {"off", "brief", "standard", "deep"}
PURPOSES = {"resume", "technical", "balanced"}
MODULES = {
    "project-overview", "background-problem", "users-stakeholders", "goals-success",
    "requirements-constraints", "product-workflow", "technical-architecture", "ai-agent-design",
    "information-data", "decisions-tradeoffs", "ownership-contribution", "validation-qa",
    "outcomes-metrics", "evolution-history", "risks-limitations",
}
CLAIM_TYPES = {"fact", "design_intent", "mechanism", "observed_outcome", "measured_outcome"}
LEDGER_MARKER = "<!-- project-profile-ledger: v2 -->"
LEDGER_COLUMN_COUNT = 14
MODULE_COVERAGE_MARKER = "<!-- project-profile-module-coverage: v2 -->"
MODULE_COVERAGE_COLUMN_COUNT = 8


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.split("|")[1:-1]]


def fixture_ids(path: Path | None) -> set[str]:
    if path is None:
        return set()
    return set(re.findall(r"^\|\s*(T\d+)\s*\|", path.read_text(encoding="utf-8"), re.MULTILINE))

def validate(path: Path, testimony_fixture: Path | None = None) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = []
    if "{{" in text:
        errors.append("unresolved template placeholder found")
    missing_statuses = sorted(status for status in STATUSES if status not in text)
    if missing_statuses:
        errors.append(f"missing evidence statuses: {', '.join(missing_statuses)}")
    table_dividers = [line for line in text.splitlines() if line.startswith("|") and "---" in line]
    if len(table_dividers) < 4:
        errors.append("missing required fact-pack, coverage, or ledger tables")
    lines = text.splitlines()
    module_coverage_indexes = [index for index, line in enumerate(lines) if line.strip() == MODULE_COVERAGE_MARKER]
    if len(module_coverage_indexes) != 1:
        errors.append("missing or repeated module coverage schema marker")
    for marker_index in module_coverage_indexes:
        header_index = marker_index + 1
        while header_index < len(lines) and not lines[header_index].startswith("|"):
            header_index += 1
        if header_index >= len(lines) or len(table_cells(lines[header_index])) != MODULE_COVERAGE_COLUMN_COUNT:
            errors.append("module coverage header must contain eight localized columns")
            continue
        for row in lines[header_index + 2:]:
            if not row.startswith("|"):
                break
            cells = table_cells(row)
            if len(cells) != MODULE_COVERAGE_COLUMN_COUNT:
                errors.append("module coverage row has wrong column count")
                break
            applicability, depth, fact_ids, recovered, destination = cells[1], cells[2], cells[4], cells[5], cells[7]
            has_material_facts = fact_ids.lower() not in {"", "none", "—", "无"}
            enabled_applicable = depth.lower() != "off" and applicability.lower() not in {"not applicable", "不适用"}
            if enabled_applicable and has_material_facts and (not recovered.strip() or recovered.lower() in {"none", "—", "无"} or not destination.strip()):
                errors.append(f"module coverage row for {cells[0]} must preserve recovered coverage and render destination")
                break
    marker_indexes = [index for index, line in enumerate(lines) if line.strip() == LEDGER_MARKER]
    if len(marker_indexes) != 1:
        errors.append("missing or repeated canonical fact ledger schema marker")
    known_testimony_ids = fixture_ids(testimony_fixture)
    ledger_status_counts: dict[str, int] = {status: 0 for status in STATUSES}
    for marker_index in marker_indexes:
        header_index = marker_index + 1
        while header_index < len(lines) and not lines[header_index].startswith("|"):
            header_index += 1
        if header_index >= len(lines) or len(table_cells(lines[header_index])) != LEDGER_COLUMN_COUNT:
            errors.append("canonical fact ledger header must contain fourteen localized columns")
            continue
        for row in lines[header_index + 2:]:
            if not row.startswith("|"):
                break
            cells = table_cells(row)
            if len(cells) != LEDGER_COLUMN_COUNT:
                errors.append("canonical fact ledger row has wrong column count")
                break
            if cells[3] not in CLAIM_TYPES:
                errors.append(f"invalid claim type {cells[3]}")
                break
            if cells[4] not in STATUSES:
                errors.append(f"invalid ledger status {cells[4]}")
                break
            ledger_status_counts[cells[4]] += 1
            if known_testimony_ids and "user" in cells[5].lower() and cells[4] == "VERIFIED":
                referenced_ids = set(re.findall(r"\bT\d+\b", cells[6]))
                if not referenced_ids or not referenced_ids <= known_testimony_ids:
                    errors.append(f"verified user claim {cells[0]} must cite a known testimony fixture ID")
    coverage_counts = {
        match.group(1): int(match.group(2))
        for line in lines
        if (match := re.match(r"^\|\s*(VERIFIED|INFERRED|CLARIFICATION_REQUIRED|UNKNOWN|NOT_APPLICABLE|CONFLICTING)\s*\|\s*(\d+)\s*\|", line))
    }
    if marker_indexes and coverage_counts:
        for status, count in coverage_counts.items():
            if ledger_status_counts[status] != count:
                errors.append(f"evidence coverage count for {status} is {count}, ledger contains {ledger_status_counts[status]}")
    return errors

def validate_config(path: Path) -> list[str]:
    errors: list[str] = []
    in_modules = False
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.split("#", 1)[0].rstrip()
        if not line:
            continue
        if line == "modules:":
            in_modules = True
            continue
        match = re.match(r"^(\s*)([a-z_-]+):\s*([a-z-]+)\s*$", line)
        if not match:
            continue
        indent, key, value = match.groups()
        if not indent:
            in_modules = False
            if key == "purpose" and value not in PURPOSES:
                errors.append(f"line {number}: invalid purpose {value}")
            if key == "default_depth" and value not in DEPTHS:
                errors.append(f"line {number}: invalid default_depth {value}")
        elif in_modules:
            if key not in MODULES:
                errors.append(f"line {number}: unknown module {key}")
            if value not in DEPTHS:
                errors.append(f"line {number}: invalid depth {value}")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("profile", type=Path, nargs="?")
    parser.add_argument("--config", type=Path)
    parser.add_argument("--testimony-fixture", type=Path)
    args = parser.parse_args()
    if args.profile is None and args.config is None:
        parser.error("provide a profile and/or --config")
    errors = validate(args.profile, args.testimony_fixture) if args.profile else []
    if args.config:
        errors.extend(validate_config(args.config))
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
