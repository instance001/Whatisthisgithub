import os
import sys
import datetime
import requests
from textwrap import dedent

API_URL_TEMPLATE = "https://api.github.com/users/{username}/repos"
AUTO_START = "<!-- AUTO-GENERATED-INDEX:START -->"
AUTO_END = "<!-- AUTO-GENERATED-INDEX:END -->"


def get_username():
    # Prefer the repo owner, fall back to a hardcoded default
    env_owner = os.environ.get("GITHUB_REPOSITORY_OWNER")
    if env_owner:
        print("GITHUB_REPOSITORY_OWNER:", env_owner)
        return env_owner
    print("GITHUB_REPOSITORY_OWNER not set, falling back to 'instance001'")
    return "instance001"


def fetch_repos(username, token=None):
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
        headers["Authorization"] = "Bearer {}".format(token)

    while True:
        params = {
            "per_page": 100,
            "page": page,
            "sort": "updated",
            "direction": "desc",
        }
        url = API_URL_TEMPLATE.format(username=username)
        print("Requesting:", url, "page", page)
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        print("Status:", resp.status_code)

        if resp.status_code != 200:
            print("GitHub API error {}: {}".format(resp.status_code, resp.text), file=sys.stderr)
            sys.exit(1)

        chunk = resp.json()
        if not chunk:
            break

        print("Got {} repos on page {}".format(len(chunk), page))
        repos.extend(chunk)
        page += 1

    print("Total repos fetched:", len(repos))
    return repos


def format_date(date_str):
    try:
        dt = datetime.datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return date_str


def build_index_markdown(username, repos):
    """
    Build the markdown for the auto-generated section.
    """
    now = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"

    visible_repos = [
        r for r in repos
        if not r.get("private", False)
        # Uncomment to hide forks:
        # and not r.get("fork", False)
    ]

    visible_repos.sort(
        key=lambda r: r.get("updated_at", "1970-01-01T00:00:00Z"),
        reverse=True,
    )

    print("Visible public repos:", len(visible_repos))

    lines = []
    lines.append("_Last updated: `{}`_".format(now))
    lines.append("")
    lines.append("Total public repos indexed for **@{}**: **{}**".format(username, len(visible_repos)))
    lines.append("")
    lines.append("| Repo | Description | Language | Updated |")
    lines.append("| ---- | ----------- | -------- | ------- |")

    for repo in visible_repos:
        name = repo.get("name", "")
        html_url = repo.get("html_url", "")
        desc = repo.get("description") or ""
        lang = repo.get("language") or ""
        updated = format_date(repo.get("updated_at", ""))

        desc = desc.replace("|", "\\|")

        lines.append(
            "| [{}]({}) | {} | {} | {} |".format(name, html_url, desc, lang, updated)
        )

    return "\n".join(lines) + "\n"


def update_readme(readme_path, new_block):
    """
    Replace the AUTO-GENERATED-INDEX section in README.md with new_block.
    If markers are missing, append a new section at the end.
    """
    if not os.path.exists(readme_path):
        print("README not found at {}, creating a new one.".format(readme_path), file=sys.stderr)
        content = ""
    else:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

    if AUTO_START in content and AUTO_END in content:
        before = content.split(AUTO_START)[0]
        after = content.split(AUTO_END)[1]
        replacement = "{}\n\n{}\n{}".format(AUTO_START, new_block, AUTO_END)
        new_content = before + replacement + after
    else:
        auto_section = dedent(
            """
            {start}

            {block}
            {end}
            """
        ).format(start=AUTO_START, block=new_block, end=AUTO_END).strip()

        if content and not content.endswith("\n"):
            content += "\n"
        new_content = content + "\n\n" + auto_section + "\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("README updated.")


def main():
    username = get_username()
    token = os.environ.get("GITHUB_TOKEN")

    print("Building index for GitHub user: @{}".format(username))
    repos = fetch_repos(username, token=token)
    markdown = build_index_markdown(username, repos)
    update_readme("README.md", markdown)
    print("Index generation complete.")


if __name__ == "__main__":
    main()
