#!/usr/bin/env python3

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

CONTRACTS = {
    "code-review-architecture": {
        "rules": [
            "arch-transaction-side-effects",
            "arch-separation-domain-presentation",
            "arch-coupling-cohesion",
            "arch-unidirectional-data-flow",
            "arch-contract-rigor-extensibility",
        ],
        "retired": [
            "arch-separation-concerns",
            "arch-abstraction-interfaces",
            "arch-module-boundaries",
            "arch-design-patterns",
            "arch-data-flow",
            "arch-extensibility-maintainability",
            "arch-transaction-boundaries",
        ],
    },
    "code-review-error-handling": {
        "rules": [
            "err-signalling-hygiene",
            "err-outcome-batch-discipline",
            "err-timeouts-cancellation",
            "err-retry-idempotency",
            "err-cleanup-observability",
        ],
        "retired": [
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
    },
    "code-review-performance": {
        "rules": [
            "perf-database-nplusone",
            "perf-algorithmic-collections",
            "perf-memory-streaming",
            "perf-caching-invalidation",
            "perf-network-batching",
        ],
        "retired": [
            "perf-algorithmic-complexity",
            "perf-database-performance",
            "perf-network-io",
            "perf-memory-management",
            "perf-caching-strategy",
            "perf-concurrency",
            "perf-asset-optimization",
        ],
    },
    "code-review-security": {
        "rules": [
            "sec-injection-defense",
            "sec-auth-fail-closed",
            "sec-sink-appropriate-escaping",
            "sec-input-revalidation",
            "sec-secrets-configuration",
        ],
        "retired": [
            "sec-injection-vulnerabilities",
            "sec-auth-authorization",
            "sec-data-protection",
            "sec-input-validation",
            "sec-dependency-security",
            "sec-configuration-security",
        ],
    },
    "code-review-simplicity": {
        "rules": [
            "simp-premature-abstraction",
            "simp-shallow-control-flow",
            "simp-bounds-range-clarity",
            "simp-intention-revealing-naming",
            "simp-dead-code-elimination",
        ],
        "retired": [
            "simp-readability-clarity",
            "simp-cognitive-load",
            "simp-unnecessary-complexity",
            "simp-colliding-bounds",
            "simp-code-duplication",
            "simp-documentation-comments",
            "simp-naming-conventions",
            "simp-testing-debugging",
        ],
    },
    "code-review-type-safety": {
        "rules": [
            "type-strict-native-declarations",
            "type-shape-validation-boundaries",
            "type-symmetric-rigor",
            "type-nullability-truthfulness",
        ],
        "retired": [
            "type-type-coverage",
            "type-type-correctness",
            "type-asymmetric-rigor",
            "type-type-safety",
            "type-generic-discipline",
        ],
    },
}


def validate() -> list[str]:
    errors: list[str] = []

    for skill_name, contract in CONTRACTS.items():
        skill_dir = SKILLS / skill_name
        skill_path = skill_dir / "SKILL.md"
        skill = skill_path.read_text(encoding="utf-8")
        expected_rules = contract["rules"]

        for rule_id in expected_rules:
            if rule_id not in skill:
                errors.append(f"{skill_name}/SKILL.md is missing consolidated rule: {rule_id}")
            if not (skill_dir / "rules" / f"{rule_id}.md").is_file():
                errors.append(f"{skill_name} is missing rule file: rules/{rule_id}.md")

        for projection_name in ["README.md", "AGENTS.md", "metadata.json"]:
            projection = (skill_dir / projection_name).read_text(encoding="utf-8")
            for retired_id in contract["retired"]:
                if retired_id in projection:
                    errors.append(
                        f"{skill_name}/{projection_name} still contains retired rule id: {retired_id}"
                    )

        metadata = json.loads((skill_dir / "metadata.json").read_text(encoding="utf-8"))
        if metadata.get("meta", {}).get("rule_count") != len(expected_rules):
            errors.append(
                f"{skill_name}/metadata.json must report exactly {len(expected_rules)} consolidated rules"
            )
        if metadata.get("meta", {}).get("canonical_sources") != ["SKILL.md", "rules/"]:
            errors.append(
                f"{skill_name}/metadata.json must identify SKILL.md + rules/ as canonical sources"
            )

        category_ids = [category.get("id") for category in metadata.get("categories", [])]
        if category_ids != expected_rules:
            errors.append(
                f"{skill_name}/metadata.json category ids must match the canonical rule order"
            )

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Review-lens projection validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"Validated {len(CONTRACTS)} review-lens projection contracts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
