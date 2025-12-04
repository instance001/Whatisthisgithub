#!/usr/bin/env python3
import json
from pathlib import Path
from textwrap import dedent

MANIFEST_PATH = Path("repo_manifest.json")
README_PATH = Path("README.md")

START_MARKER = "<!-- REPO_INDEX_START -->"
END_MARKER = "<!-- REPO_INDEX_END -->"


def load_manifest():
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"Missing {MANIFEST_PATH}. Create repo_manifest.json first.")
    with MANIFEST_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("repo_manifest.json must contain a JSON array of repo objects.")

    # Basic sanity check
    for idx, repo in enumerate(data):
        for key in ("name", "description", "category", "license", "link"):
            if key not in repo:
                raise ValueError(f"Entry {idx} is missing field '{key}' in repo_manifest.json")

    # Optionally sort by name
    data.sort(key=lambda r: r["name"].lower())
    return data


def build_table(repos):
    header = "| Repository | Description | Category | License | Link |\n"
    sep = "|-----------|-------------|----------|---------|------|\n"

    rows = []
    for r in repos:
        name = r["name"]
        desc = r["description"]
        cat = r["category"]
        lic = r["license"]
        link = r["link"]

        # Escape pipes in description/category if any
        desc = desc.replace("|", "\\|")
        cat = cat.replace("|", "\\|")

        row = f"| {name} | {desc} | {cat} | {lic} | {link} |"
        rows.append(row)

    return header + sep + "\n".join(rows) + "\n"


def update_readme(table_md: str):
    if not README_PATH.exists():
        raise FileNotFoundError("README.md not found in current directory.")

    text = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in text or END_MARKER not in text:
        raise ValueError(
            f"README.md must contain both '{START_MARKER}' and '{END_MARKER}' markers."
        )

    before, remainder = text.split(START_MARKER, 1)
    _, after = remainder.split(END_MARKER, 1)

    new_block = dedent(
        f"""\
        {START_MARKER}

        # 📚 Complete Repository Index

        {table_md}
        {END_MARKER}
        """
    )

    updated = before.rstrip() + "\n\n" + new_block + "\n" + after.lstrip()
    README_PATH.write_text(updated, encoding="utf-8")


def main():
    repos = load_manifest()
    table_md = build_table(repos)
    update_readme(table_md)
    print("✅ README.md repo index updated from repo_manifest.json")


if __name__ == "__main__":
    main()