# Legal and Attribution Findings

This is operational guidance, not legal advice. Any new non-permissive licensing term requires confirmation from every relevant rights holder and qualified legal review.

## Legally required for copied AGPL-covered expression

- AGPLv3 requires preservation of appropriate copyright and licence notices when conveying verbatim copies; modified source also needs prominent modification/date notices and the applicable licence/section-7 notices. See [AGPLv3](https://www.gnu.org/licenses/agpl-3.0.html) §§4–5.
- Where a covered work has interactive interfaces that already display Appropriate Legal Notices, modified works must display them. The duty is not a blanket requirement to add a UI notice to an interface that did not have one. [AGPLv3 §5](https://www.gnu.org/licenses/agpl-3.0.html).
- Copying selected source files can still copy protected expression. Preserve applicable notices and comply with the licence for the resulting covered work; determine scope and combination questions case by case.

## Permitted additional terms — only with authority

AGPLv3 §7 permits, for material the relevant copyright holders authorize, specified reasonable legal-notice/author-attribution preservation (7(b)), reasonable origin/misrepresentation terms (7(c)), and trademark/publicity limitations (7(d)–(e)). Any other non-permissive term is a further restriction and may be removable. Terms must be scoped to the material and identified in relevant source files or by a notice directing to them. No FMI-wide binding additional term is adopted by this retrofit.

## Recommended attribution — voluntary

- Cite a repository, versioned release, specification, or associated paper through its `CITATION.cff`/provenance record.
- Acknowledge genuine methodological influence in papers, talks, and documentation.
- Use truthful wording that does not imply FMI endorsement; logo/name use is voluntary unless separate approved trademark rules apply.

## Not enforceable through the software licence

AGPLv3 cannot turn an independently implemented abstract method into covered software, and it cannot require academic citations for use of a program or its output. The FSF says a research-citation requirement exceeds §7(b) and is a further restriction: [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html#RequireCitation). Australian Government guidance likewise states that copyright protects original expression, not ideas or information: [Attorney-General’s Department](https://www.ag.gov.au/rights-and-protections/copyright/copyright-basics).

## Source and identifier practice

Use SPDX identifiers only where the file’s actual licence supports them; SPDX recommends explicit GNU identifiers such as `AGPL-3.0-or-later`, and says not to remove existing copyright notices: [SPDX guidance](https://spdx.dev/learn/handling-license-info/). GitHub recognizes root `CITATION.cff` files: [GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files?apiVersion=2022-11-28).
