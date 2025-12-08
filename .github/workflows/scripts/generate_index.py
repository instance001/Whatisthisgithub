import os
import sys
import datetime
import requests
from textwrap import dedent

API_URL_TEMPLATE = "https://api.github.com/users/{username}/repos"
AUTO_START = "<!-- AUTO-GENERATED-INDEX:START -->"
AUTO_END = "<!-- AUTO-GENERATED-INDEX:END -->"


def get_username() -> str:
    # Prefer the repo owner, fall back to a hardcoded default
    return os.environ.get("GITHUB_REPOSITORY_OWNER", "instance001")


def fetch_repos(username: str, token: str | None = None) -> list[dict]:
    """
    Fetch all public repos for the given user from GitHub.
    Handles pagination.
    """
    repos = []
    page = 1

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "instance001-field-indexer",
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    while True:
        params = {
            "per_page": 100,
            "page": page,
            "sort": "updated",
            "direction": "desc",
        }
        url = API_URL_TEMPLATE.format(username=username)
        resp = requests.get(url, headers=headers, params=params, timeout=30)

        if resp.status_code != 200:
            print(f"GitHub API error {resp.status_code}: {resp.text}", file=sys.stderr)
            sys.exit(1)

        chunk = resp.json()
        if not chunk:
            break

        repos.extend(chunk)
        page += 1

    return repos


def format_date(date_str: str) -> str:
    # Example GitHub format: "2025-12-08T04:36:22Z"
    try:
        dt = datetime.datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return date_str


def build_index_markdown(username: str, repos: list[dict]) -> str:
    """
    Build the markdown for the auto-generated section.
    """
    now = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"

    # Filter / sort logic – tweak as you like
    visible_repos = [
        r for r in repos
        if not r.get("private", False)
        # Optionally hide forks:
        # and not r.get("fork", False)
    ]

    # Sort by updated_at desc (API already does this, but we’ll be explicit)
    visible_repos.sort(
        key=lambda r: r.get("updated_at", "1970-01-01T00:00:00Z"),
        reverse=True,
    )

    lines = []
    lines.append(f"_Last updated: `{now}`_\n")
    lines.append("")
    lines.append(f"Total public repos indexed for **@{username}**: **{len(visible_repos)}**")
    lines.append("")
    lines.append("| Repo | Description | Language | Updated |")
    lines.append("| ---- | ----------- | -------- | ------- |")

    for repo in visible_repos:
        name = repo.get("name", "")
        html_url = repo.get("html_url", "")
        desc = repo.get("description") or ""
        lang = repo.get("language") or ""
        updated = format_date(repo.get("updated_at", ""))

        # Escape pipes in description to avoid breaking the table
        desc = desc.replace("|", "\\|")

        lines.append(
            f"| [{name}]({html_url}) | {desc} | {lang} | {updated} |"
        )

    return "\n".join(lines) + "\n"


def update_readme(readme_path: str, new_block: str) -> None:
    """
    Replace the AUTO-GENERATED-INDEX section in README.md with new_block.
    If markers are missing, append a new section at the end.
    """
    if not os.path.exists(readme_path):
        print(f"{readme_path} not found, creating a new one.", file=sys.stderr)
        content = ""
    else:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

    if AUTO_START in content and AUTO_END in content:
        before = content.split(AUTO_START)[0]
        after = content.split(AUTO_END)[1]
        replacement = (
            f"{AUTO_START}\n\n{new_block}\n{AUTO_END}"
        )
        new_content = before + replacement + after
    else:
        # If markers missing, append a new section at end
        auto_section = dedent(
            f"""
            {AUTO_START}

            {new_block}
            {AUTO_END}
            """
        ).strip()
        if content and not content.endswith("\n"):
            content += "\n"
        new_content = content + "\n\n" + auto_section + "\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    username = get_username()
    token = os.environ.get("GITHUB_TOKEN")  # optional; fine to be None

    print(f"Building index for GitHub user: {username}")

    repos = fetch_repos(username, token=token)
    markdown = build_index_markdown(username, repos)
    update_readme("README.md", markdown)

    print("Index generation complete.")


if __name__ == "__main__":
    main()
