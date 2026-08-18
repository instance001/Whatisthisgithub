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

## Glossary Status Rule

Glossary entries should help readers translate between historical FMI wording and current technical language.

When updating terminology, make the status clear:

- foundational terms remain current and should be defined strongly
- ordinary mechanisms should use ordinary technical terms
- product labels may remain when they help users, but should map to the technical equivalent
- legacy names should be marked as provenance, compatibility, or source wording rather than presented as equally current

Do not delete historical names needed to understand older repositories. Do stop using those names as the preferred term for current architecture when a smaller technical term is clearer.

Modernization must not accidentally narrow ontology. Do not replace cognition-neutral or cognition-broad wording merely because it could be read anthropomorphically; first check whether the local source intends human-only endpoints, artificial endpoints, hybrid systems, or a broader substrate-agnostic category.

`Hybrid cognition` is not globally deprecated. It remains valid for modern Symbound work where the intended meaning is a broader human-AI hybrid cognitive engine or mixed human/AI cognition system. Repo-local replacements, such as `audited human-LLM collaboration` in `collapse-of-the-semantic-middle`, should be used only when the source is explicitly bounded to observable human-LLM communication evidence rather than broader cognition claims.

## Update Order

When refreshing public-facing metadata:

1. Update the source repo README or user manual.
2. Update repo-local glossary entries if the repo has one.
3. Update `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`.
4. Update `Whatisthisgithub/EASY_START.md` if the repo changes navigation status.
5. Update `repo_metadata_overrides.json` only if the generated index needs wording GitHub metadata does not yet provide.
6. Regenerate `Whatisthisgithub/README.md` with `python scripts/generate_index.py`.
7. Update `instance001.github.io` if the public website or app-support surface also needs the change.
