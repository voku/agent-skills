#!/usr/bin/env python3

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

RETIRED_RULE_IDS = {
    "code-review-architecture": [
        "arch-separation-concerns",
        "arch-abstraction-interfaces",
        "arch-module-boundaries",
        "arch-design-patterns",
        "arch-data-flow",
        "arch-extensibility-maintainability",
        "arch-transaction-boundaries",
    ],
    "code-review-error-handling": [
        "err-signalling-discipline",
        "err-outcome-messaging",
        "err-exception-hygiene",
        "err-timeout-cancellation",
        "err-retry-semantics",
        "err-partial-failure",
        "err-observability",
        "err-resource-cleanup",
        "err-defensive-overreach",
    ],
    "code-review-performance": [
        "perf-algorithmic-complexity",
        "perf-database-performance",
        "perf-network-io",
        "perf-memory-management",
        "perf-caching-strategy",
        "perf-concurrency",
        "perf-asset-optimization",
    ],
    "code-review-security": [
        "sec-injection-vulnerabilities",
        "sec-auth-authorization",
        "sec-data-protection",
        "sec-input-validation",
        "sec-dependency-security",
        "sec-configuration-security",
    ],
    "code-review-simplicity": [
        "simp-readability-clarity",
        "simp-cognitive-load",
        "simp-unnecessary-complexity",
        "simp-colliding-bounds",
        "simp-code-duplication",
        "simp-documentation-comments",
        "simp-naming-conventions",
        "simp-testing-debugging",
    ],
    "code-review-type-safety": [
        "type-type-coverage",
        "type-type-correctness",
        "type-asymmetric-rigor",
        "type-type-safety",
        "type-generic-discipline",
    ],
}

RULE_LINK_PATTERN = re.compile(r"rules/([a-z0-9-]+)\.md")


def canonical_rule_ids(skill: str) -> list[str]:
    rule_ids: list[str] = []
    for rule_id in RULE_LINK_PATTERN.findall(skill):
        if rule_id not in rule_ids:
            rule_ids.append(rule_id)
    return rule_ids


def validate() -> list[str]:
    errors: list[str] = []

    for skill_name, retired_rule_ids in RETIRED_RULE_IDS.items():
        skill_dir = SKILLS / skill_name
        skill_path = skill_dir / "SKILL.md"
        rules_dir = skill_dir / "rules"
        skill = skill_path.read_text(encoding="utf-8")

        expected_rules = canonical_rule_ids(skill)
        actual_rules = sorted(
            path.stem
            for path in rules_dir.glob("*.md")
            if not path.name.startswith("_")
        )

        if not expected_rules:
            errors.append(f"{skill_name}/SKILL.md does not reference any canonical rule files")
        if set(expected_rules) != set(actual_rules):
            errors.append(
                f"{skill_name}: SKILL.md rule references must match canonical rules/ files"
            )

        for projection_name in ["README.md", "AGENTS.md", "metadata.json"]:
            projection = (skill_dir / projection_name).read_text(encoding="utf-8")
            for retired_id in retired_rule_ids:
                if retired_id in projection:
                    errors.append(
                        f"{skill_name}/{projection_name} still contains retired rule id: {retired_id}"
                    )

        metadata = json.loads((skill_dir / "metadata.json").read_text(encoding="utf-8"))
        if metadata.get("meta", {}).get("canonical_sources") != ["SKILL.md", "rules/"]:
            errors.append(
                f"{skill_name}/metadata.json must identify SKILL.md + rules/ as canonical sources"
            )

        category_ids = [category.get("id") for category in metadata.get("categories", [])]
        if category_ids != expected_rules:
            errors.append(
                f"{skill_name}/metadata.json category ids must match the canonical SKILL.md rule order"
            )

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Review-lens projection validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"Validated {len(RETIRED_RULE_IDS)} review-lens projection contracts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
