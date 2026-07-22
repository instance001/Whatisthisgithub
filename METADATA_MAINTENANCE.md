# Metadata Maintenance

This repo has several public orientation surfaces:

- `README.md` for the generated public repo index and current fast lanes
- `EASY_START.md` for human entry routes
- `GLOSSARY.md` and `GLOSSARY_FULL.md` for terminology
- GitHub repository descriptions, which are imported into the generated index
- the public site in `instance001.github.io`

## Generated Index Descriptions

`scripts/generate_index.py` normally uses each repository's GitHub description.

When a live GitHub description cannot be updated at the same time as the docs, use `repo_metadata_overrides.json` for active repos only. This keeps the generated index aligned with current signage without hand-editing the generated block in `README.md`.

Keep overrides narrow:

- use them for active repo descriptions that are stale or misleading
- do not add archived repos unless the archive door-sign itself is actively wrong
- remove an override after the live GitHub repo description matches it

## Tone Rule

For current tool repos, use this stance:

> local first, cloud optional: cloud when you need it, local when you don't.

That means local/offline paths should be real, usable, and inspectable. It does not mean rejecting hosted tools or cloud providers when a user deliberately chooses them.

## Update Order

When refreshing public-facing metadata:

1. Update the source repo README or user manual.
2. Update repo-local glossary entries if the repo has one.
3. Update `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`.
4. Update `Whatisthisgithub/EASY_START.md` if the repo changes navigation status.
5. Update `repo_metadata_overrides.json` only if the generated index needs wording GitHub metadata does not yet provide.
6. Regenerate `Whatisthisgithub/README.md` with `python scripts/generate_index.py`.
7. Update `instance001.github.io` if the public website or app-support surface also needs the change.
