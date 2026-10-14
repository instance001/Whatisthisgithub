#!/usr/bin/env python3
"""Build and validate FMI provenance inventory from authenticated GitHub metadata.

This tool inventories repository metadata without inferring authorship, novelty,
dependencies, or publication dates.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "provenance-registry.json"
REPORT = ROOT / "PROVENANCE_AUDIT_REPORT.md"

LINEAGE_REVIEW = {
    "chatty-cog": "Substantively reviewed: implemented hybrid host/model authority, Bookkeeper/memory governance, modules, approval-gated sandbox, and Cog-only local handoff lanes.",
    "chatty-edu": "Substantively reviewed: implemented education-specific offline/authority/learning-pack architecture; direct derivation from Chatty-Cog not established.",
    "chatty-edu-user": "Substantively reviewed: packaged distribution/history record aligned with Chatty-EDU source v0.4; not treated as separate source architecture.",
    "llm-semantic-dataset-sorter": "Substantively reviewed: implemented governed semantic-partitioning workbench; no dependency on Semantic Signal Alphabet or LLM-Defined Persistent Memory established from reviewed evidence.",
    "chatty-mini": "Central evidence review only: substantive project-file edit deferred because its local checkout contains unrelated active work.",
    "chatty-factory": "Substantively reviewed: implemented host-governed build/patch funnel with bounded attempts, verification, and receipt-driven next-attempt routing.",
    "chatty-art": "Substantively reviewed: implemented portable local media-generation application; relationship to Chatty-lora is approved copy-only bridge handoff, not shared internal state.",
    "chatty-lora": "Substantively reviewed: implemented review-first local LoRA curation/training workflow; relationship to Chatty-art is approved copy-only bridge handoff.",
    "chatty-pet": "Substantively reviewed: implemented local reducer-owned care-toy application; RD Engine dependency not established.",
    "ecg_window": "Substantively reviewed: implemented language-agnostic truthful-activity presentation pattern; ECG terminology is metaphorical.",
}


def github_repos() -> list[dict]:
    if not shutil.which("gh"):
        raise RuntimeError("GitHub CLI (gh) is required to refresh the inventory.")
    result = subprocess.run(
        ["gh", "api", "--paginate", "users/instance001/repos?per_page=100&type=owner"],
        check=True, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    return json.loads(result.stdout)


def item(repo: dict) -> dict:
    archived = bool(repo["archived"])
    return {
        "repository": repo["name"],
        "canonical_url": repo["html_url"],
        "default_branch": repo["default_branch"],
        "visibility": "private" if repo["private"] else "public",
        "archived": archived,
        "category": ["F. Historical or archived repository"] if archived else ["UNCLASSIFIED"],
        "originating_contribution": "Not asserted by the registry; consult the canonical repository and project-specific provenance record.",
        "public_attribution_identity": "Not asserted automatically.",
        "verified_repository_creation": repo["created_at"],
        "verified_last_push": repo["pushed_at"],
        "license_api": (repo.get("license") or {}).get("spdx_id", "NOASSERTION"),
        "provenance_document": "PROVENANCE.md" if not archived else None,
        "citation_metadata": "CITATION.cff" if not archived else None,
        "relationships": {"predecessors": [], "successors": [], "implementations": []},
        "lineage_review": LINEAGE_REVIEW.get(repo["name"], "Baseline inventory only."),
        "audit_state": "INDEXED_WITHOUT_HISTORICAL_ALTERATION" if archived else "BASELINE_PROVENANCE_AND_CITATION_PUBLISHED",
    }


def refresh() -> None:
    repos = sorted(github_repos(), key=lambda r: r["name"].lower())
    payload = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "source": "GitHub REST API authenticated as instance001; repository creation timestamps are not asserted publication dates.",
        "repositories": [item(repo) for repo in repos],
    }
    REGISTRY.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    active = sum(not repo["archived"] for repo in repos)
    archived = len(repos) - active
    lines = [
        "# FMI Provenance Audit Report",
        "",
        "Generated from authenticated GitHub repository metadata. This report is an inventory, not a claim of authorship, novelty, priority, or legal ownership.",
        "",
        f"- **Repositories discovered:** {len(repos)}",
        f"- **Active:** {active}",
        f"- **Archived:** {archived}",
        "- **ERROR:** none at inventory stage",
        f"- **Baseline provenance/citation treatment published:** {active} active repositories",
        "- **NOT APPLICABLE:** archived repository contents are not rewritten by this tool.",
        "",
        "## Inventory",
        "",
        "| Repository | API license | Provenance treatment |",
        "| --- | --- | --- |",
    ]
    for repo in payload["repositories"]:
        treatment = "indexed without alteration" if repo["archived"] else "project retrofit required"
        lines.append(f"| [{repo['repository']}]({repo['canonical_url']}) | {repo['license_api']} | {treatment} |")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def retrofit_local() -> None:
    """Add a deliberately conservative baseline record to active local clones.

    The GitHub description is quoted as repository-supplied context, not treated
    as proof of originality. Existing project-specific records are untouched.
    """
    workspace = ROOT.parent
    changed, skipped = [], []
    for repo in github_repos():
        target = workspace / repo["name"]
        if repo["archived"]:
            skipped.append(f"{repo['name']} (archived)")
            continue
        if not (target / ".git").exists():
            skipped.append(f"{repo['name']} (no local clone)")
            continue
        provenance = target / "PROVENANCE.md"
        citation = target / "CITATION.cff"
        description = (repo.get("description") or "No GitHub description supplied.").replace("\r", " ").replace("\n", " ")
        if not provenance.exists():
            provenance.write_text(f'''# Provenance: {repo['name']}

## Project identity

- Canonical repository: <{repo['html_url']}>
- Public originating identity: `instance001` (repository owner recorded by GitHub API; copyright ownership is not inferred).
- Verified repository creation record: {repo['created_at']}. This is not asserted to be an original publication date.

## Intellectual contribution

GitHub repository description (repository-supplied context): {description}

No independent originality, priority, validation, authorship, or implementation relationship is asserted by this baseline record.

## Prior art and influences

Not exhaustively reviewed by this baseline. Do not treat absence of a listed influence as a claim of novelty.

## Implementation relationships

None asserted automatically. Similar names, topics, or portfolio membership are not evidence of derivation.

## Attribution and citation

Preserve the repository's existing legal notices and applicable licence when copying protected expression. Use `CITATION.cff` for a voluntary repository citation. Independent implementation of an abstract method is not automatically governed by a software licence.

## Licensing

GitHub API licence field at inventory time: `{(repo.get('license') or {}).get('spdx_id', 'NOASSERTION')}`. This is a metadata observation, not a relicensing statement. See the repository's actual licence files and third-party notices.

## Evidence and limitations

Evidence: authenticated GitHub API metadata captured by the FMI provenance audit.
''', encoding="utf-8")
            changed.append(f"{repo['name']}: PROVENANCE.md")
        if not citation.exists():
            citation.write_text(f'''cff-version: 1.2.0
message: "If this repository informed your work, please cite the canonical repository."
title: "{repo['name']}"
url: "{repo['html_url']}"
repository-code: "{repo['html_url']}"
abstract: "Repository-level citation metadata; see PROVENANCE.md for evidence limits."
''', encoding="utf-8")
            changed.append(f"{repo['name']}: CITATION.cff")
    print(f"UPDATED: {len(changed)} files")
    print(f"NOT APPLICABLE / SKIPPED: {len(skipped)} repositories")
    for value in skipped:
        print(f"NOT APPLICABLE: {value}")


def validate() -> int:
    problems: list[tuple[str, str]] = []
    if not REGISTRY.exists():
        problems.append(("ERROR", "provenance-registry.json is missing"))
    else:
        try:
            data = json.loads(REGISTRY.read_text(encoding="utf-8"))
            for repo in data.get("repositories", []):
                if not repo.get("repository") or not repo.get("canonical_url"):
                    problems.append(("ERROR", "registry entry missing repository or canonical_url"))
                if not repo.get("archived") and repo.get("license_api") != "AGPL-3.0":
                    problems.append(("ERROR", f"{repo['repository']}: expected AGPL-3.0, found {repo.get('license_api', 'missing')}"))
        except json.JSONDecodeError as error:
            problems.append(("ERROR", f"invalid registry JSON: {error}"))
    for level, message in problems:
        print(f"{level}: {message}")
    return 1 if any(level == "ERROR" for level, _ in problems) else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("refresh", "validate", "retrofit-local"))
    args = parser.parse_args()
    if args.command == "refresh":
        refresh()
        return 0
    if args.command == "retrofit-local":
        retrofit_local()
        return 0
    return validate()


if __name__ == "__main__":
    sys.exit(main())
