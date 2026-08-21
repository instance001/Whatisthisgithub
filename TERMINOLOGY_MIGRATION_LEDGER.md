# FMI 2026 Terminology Migration Ledger

This ledger tracks repository-by-repository terminology modernization across the public `instance001` corpus.

Source of traversal truth: `Whatisthisgithub/README.md`, generated active index last observed on 2026-08-18.

## Deterministic Active Repository Queue

| Order | Repository | Initial status | Notes |
| ---: | --- | --- | --- |
| 1 | instance001.github.io | ACTIVE | Public FMI website and app support surface. |
| 2 | Whatisthisgithub | ACTIVE | Portal/index and glossary source. |
| 3 | collapse-of-the-semantic-middle | ACTIVE | Conceptual paper. |
| 4 | chatty-cog | ACTIVE | Current local assistant shell. |
| 5 | chatty-art | ACTIVE | Current local media generation lane. |
| 6 | chatty-edu | ACTIVE | Current education assistant. |
| 7 | chatty-pet | ACTIVE | Current local-first mobile app. |
| 8 | chatty-mini | ACTIVE | Current Android chat app. |
| 9 | reflective_identity_geometry | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Current theory paper with cognition-heavy terms to preserve as hypotheses where appropriate. |
| 10 | Cognition-Scale-Formal-Taxonomy | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | MCM/LCM/SCM taxonomy needs cautious handling. |
| 11 | cognitive_theology | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Research framing uses cognition/theology terms; avoid flattening theory. |
| 12 | safety_theatre | ACTIVE | Current safety analysis. |
| 13 | llm-semantic-dataset-sorter | ACTIVE | Current semantic sorting tool. |
| 14 | chatty-quest | ACTIVE | Current deterministic game/engine lane. |
| 15 | chatty-lora | ACTIVE | Current LoRA training lane. |
| 16 | nanochat-llm-tweaker | ACTIVE | Current builder/dashboard lane. |
| 17 | janet-school | ACTIVE | Current Janet rebuild; MCM language requires cautious modernization. |
| 18 | cognition-mesh-test-chamber | ACTIVE | Current model suitability test harness; fingerprinting retained with explicit behavioural-suitability definition. |
| 19 | llm-defined-persistent-memory | ACTIVE | Current memory architecture docs; model-native and memory metaphors need boundary definitions rather than broad replacement. |
| 20 | Symbound_Academia_Spine | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Repo brand includes legacy-style "Spine"; retained as project identity with explicit pipeline-metaphor boundary. |
| 21 | semantic-signal-alphabet | ACTIVE | Foundational/current framework; model-native terminology retained with explicit generated-artifact boundary. |
| 22 | MemorySpine | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Repo brand includes legacy-style "Spine"; retained with explicit local archive/index boundary. |
| 23 | historical-janet-school-exploratory-build | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Historical prototype; preserve provenance while bounding organ/MCM/curriculum language. |
| 24 | Janet-MCM-Core | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Historical/current identity uses MCM. |
| 25 | ecg_window | ACTIVE | Utility tool. |
| 26 | chattydoom | ACTIVE | Experimental/game lane. |
| 27 | chatty-edu-user | ACTIVE | Release/user package. |
| 28 | chatty-factory | ACTIVE | Current build/patch workflow. |
| 29 | 4roomciv | ACTIVE | Experimental coordination testbed. |
| 30 | governance-by-design-report-commentary | ACTIVE | Commentary repo. |
| 31 | project-leviathan | ACTIVE | Current architecture specification; several modernization candidates. |
| 32 | rd-engine | ACTIVE | Current reducer-governed state core. |
| 33 | model-behaviour-toolkit | ACTIVE | Current replacement for older prompt/capsule repos. |
| 34 | ef-engine | ACTIVE | Current Entropy Folding implementation core. |
| 35 | ai-teaming-framework | ACTIVE | Current human-AI interaction guide. |
| 36 | australian-ai-fair-go | ACTIVE | Current policy/evidence repo. |
| 37 | relational-curriculum-geometry | ACTIVE | Foundational/current research framework. |
| 38 | governance-by-design-report | ACTIVE | Current report. |
| 39 | entropy-folding-eureka-cascade-hypothesis | ACTIVE | Foundational/current theory. |
| 40 | entropy-folding-cross-domain-signal-atlas | ACTIVE | Foundational/current evidence/signal companion. |
| 41 | MSI-Trident-Frisian-Echoform-Framework-v1.0- | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Older named framework. |
| 42 | perpetual_cognition_reactor | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Older reactor framing; preserve theory/provenance. |
| 43 | Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Research scaffold with theory/provenance language. |
| 44 | symbound-lab-notes-negative-space | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Early lab notes. |
| 45 | Symbound-UAE-GVS | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Older discovery-engine framing. |
| 46 | Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Research paper; keep hypotheses bounded. |
| 47 | Frisian_Cadence_PID_Control_Loop | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Older Symbound research project. |
| 48 | dual-ai-cognition-spine-prototype | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Prototype/provenance repo. |
| 49 | cognitive_reactor_stress_tests | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | CRP and latent-geometry language requires careful hypothesis labels. |
| 50 | Chattymobile_v1 | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Seed release with Symbound/capsule vocabulary. |
| 51 | AiBiogenesis_and_AiGenesisMapping | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Older Symbound Embryo POC framing. |

## Repository Records

### instance001.github.io

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- top-level HTML pages
- `privacy/`
- `data/public-record.json`
- generation scripts
- generated `public-record.html` and `repo-directory.html`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| evidence spine | evidence record | canonicalized | Public policy page did not require an FMI-native metaphor. |
| model suitability fingerprinting | behavioural suitability profiling | canonicalized | Public project overview should describe observable evaluation behaviour. |
| researcher identity surfaces | researcher identity records | canonicalized | Public-record language refers to external identity records, not a theoretical identity-surface construct. |
| Hot Context | active context | UX retained | Product/privacy label retained, with canonical term added for clarity. |
| rolling Summary | rolling summary | canonicalized | Normalized capitalization in privacy prose. |
| cognition spine | multi-model coordination / historical repo wording | legacy alias | Preserved inside an explicit historical repository description on the convergence page. |

Files changed:

- `projects.html`
- `ai-fair-go.html`
- `privacy/chatty-mini.html`
- `data/public-record.json`
- `public-record.html` after regeneration
- `repo-directory.html` after regeneration from the portal index
- `sitemap.xml` after regeneration

Identifiers changed: no

Compatibility alias retained: yes, `Hot Context / active context`

Historical occurrences intentionally preserved: yes, `cognition spine` remains in a quoted/descriptive historical provenance paragraph for `dual-ai-cognition-spine-prototype`.

Tests/checks run:

- `node scripts/generate-seo.mjs`
- `node scripts/generate-public-record.mjs --check-links`
- `node scripts/generate-seo.mjs` rerun after link-check regeneration
- Search confirmed no remaining hand-authored occurrences of `evidence spine`, `model suitability fingerprinting`, `identity surfaces`, or `rolling Summary` in `instance001.github.io`.
- Remaining generated `repo-directory.html` occurrences of `cognition spine` are inherited from portal/upstream repo descriptions and deferred to that repository audit.

Unresolved terminology questions:

- Generated repo descriptions in `repo-directory.html` inherit source wording from the portal index. Modernize those from `Whatisthisgithub` or upstream repo metadata when each relevant repository is audited.

### Whatisthisgithub

Status: ACTIVE

Audit scope:

- `README.md`
- `EASY_START.md`
- `ABOUT_FRACTAL_MEDIA_INFRASTRUCTURE`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `METADATA_MAINTENANCE.md`
- `repo_metadata_overrides.json`
- `scripts/generate_index.py`
- `AMBIGUITIES.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| cognitive fingerprinting | cognitive fingerprinting / behavioural suitability profiling | repo-local retained after audit | Portal summaries may use behavioural suitability profiling for technical clarity, but `cognitive fingerprinting` is not globally deprecated and remains the source repo's bounded project-facing term. |
| constraint-metabolization / metabolise constraints | constraint promotion / promote reusable constraints | canonicalized | Portal-facing implementation language now distinguishes EF theory metaphor from software implementation description. |
| theory spine / hypothesis spine | theory entry point / theory framework | canonicalized | Curated visitor guidance did not require metaphor. |
| human-AI cognition | human-AI systems | canonicalized | Corpus-level statement now avoids over-claiming cognition where systems language is clearer. |
| cognitive infrastructure | human-AI infrastructure | canonicalized | Corpus-level statement now uses systems language. |
| RD Engine doctrine spine | RD Engine doctrine | legacy alias | Glossary keeps source wording as alias but marks "spine" as non-preferred current technical language. |
| Cognitive fingerprinting | Cognitive fingerprinting / behavioural suitability profiling | repo-local retained after audit | Glossary row restored to the source repo's bounded project-facing label, with behavioural suitability profiling as its explicit technical definition. |
| Composite cognition workflow | planner/executor/verifier or implemented role names | legacy alias | Archived ChattyFactory wording marked legacy rather than preferred current role language. |
| Janet (MCM) | Janet deterministic modular architecture | legacy alias | MCM retained as project identity/historical term; current description uses deterministic modular architecture. |
| Hot Memory | Active context | UX retained | Product label retained as alias and mapped to current technical stack. |
| Luke Warm memory | Rolling summary | UX/legacy retained | Product/legacy label retained as alias and mapped to current technical stack. |
| Cold logs | Audit history / event log | UX/compatibility retained | Source/API wording retained as alias and mapped to current technical stack. |
| Department status updates | Module status updates | canonicalized | Department retained as source/file wording where compatibility requires it. |
| Capsule library | Behaviour profile library | canonicalized | Source/product wording retained as alias; current technical term added. |
| evidential spine | evidence lane | canonicalized | Glossary wording now avoids unnecessary spine metaphor. |
| Cognitive Economy Governor | Reasoning Budget Governor | canonicalized | Glossary maps the Project Leviathan component to the current technical term while preserving the historical/source name. |

Files changed:

- `README.md`
- `EASY_START.md`
- `ABOUT_FRACTAL_MEDIA_INFRASTRUCTURE`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `METADATA_MAINTENANCE.md`
- `repo_metadata_overrides.json`
- `../instance001.github.io/repo-directory.html` after regeneration from the updated portal index
- `../instance001.github.io/sitemap.xml` after regeneration

Identifiers changed: no

Compatibility alias retained: yes, glossary aliases preserve source and historical terms including `cognitive fingerprinting`, `MCM`, `Hot Memory`, `Luke Warm memory`, `Cold logs`, `Capsule library`, and `Cognitive Economy Governor`.

Historical occurrences intentionally preserved: yes, generated/archival repository names and legacy glossary aliases remain where they identify historical artifacts, source filenames, or project identities.

Tests/checks run:

- `python scripts/generate_index.py`
- `node scripts/generate-seo.mjs` in `instance001.github.io`
- Search confirmed retired curated-prose phrases no longer appear outside intentional glossary aliases or generated/historical source descriptions.

Unresolved terminology questions:

- `project-leviathan` and `ef-engine` need repo-local audits before deeper identifier or README changes.
- GitHub live descriptions should eventually be updated so the `repo_metadata_overrides.json` entries for `cognition-mesh-test-chamber` and `ef-engine` can be removed.

### collapse-of-the-semantic-middle

Status: ACTIVE

Audit scope:

- `README.md`
- `observations/README.md`
- `observations/001-political-email-audit-loop.md`
- `observations/002-writing-from-inside-the-mechanism.md`
- `observations/003-ritualised-friction-and-the-human-confirmation-token.md`
- `collapse_of_the_semantic_middle_v0_3.docx`
- `collapse_of_the_semantic_middle_v0_3.pdf`
- portal glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Semantic middle | Semantic middle | foundational | Preserved as the paper's central communication-risk construct; definition bounded away from model-internal latent-space claims. |
| Expressive offloading | Expressive offloading | canonical | Preserved as clear technical language for AI-assisted formulation delegation. |
| Interpretive offloading | Interpretive offloading | canonical | Preserved as clear technical language for AI-assisted reading/summarisation delegation. |
| Communicative sovereignty | Communicative sovereignty | foundational/canonical | Preserved as the paper's agency/audit-capacity concept. |
| Semantic reachability | Semantic reachability | foundational/canonical | Preserved; README/DOCX/PDF visible text restored to `one mind to another` because `person` narrowed the endpoint ontology. In this paper, `mind` is a broad meaning-bearing cognitive agency/capacity term and is not a claim of AI consciousness, sentience, or model-internal understanding. |
| Semantic closure | Semantic closure | foundational | Preserved as a bounded failure-mode hypothesis, not a present empirical claim. |
| audited hybrid cognition | audited human-LLM collaboration | repo-local canonicalized | Observation wording now describes the observable workflow without implying a cognitive merger or model-internal cognition. This is not a global deprecation of `hybrid cognition`; modern Symbound retains the broader human-AI hybrid cognitive-engine meaning where that is the intended scope. |
| AI consciousness / sentience boundary | observable communication workflows | canonicalized | README now states the argument does not depend on AI consciousness, sentience, or model-internal understanding. |

Files changed:

- `../collapse-of-the-semantic-middle/README.md`
- `../collapse-of-the-semantic-middle/observations/002-writing-from-inside-the-mechanism.md`
- `../collapse-of-the-semantic-middle/collapse_of_the_semantic_middle_v0_3.docx`
- `../collapse-of-the-semantic-middle/collapse_of_the_semantic_middle_v0_3.pdf`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`

Identifiers changed: no

Compatibility alias retained: yes, the paper's core terms are preserved; no filenames or artifact names changed.

Historical occurrences intentionally preserved: yes, generated repo description and paper title remain unchanged.

Tests/checks run:

- Search across `README.md` and `observations/` confirmed `hybrid cognition` is absent from editable Markdown and the Semantic reachability definition uses `one mind to another`.
- DOCX XML extraction confirmed the Semantic reachability definition uses `one mind to another`; a separate ordinary `one person` occurrence remains elsewhere in the paper.
- PDF page 5 rendered with Poppler after a targeted visual overlay; visual inspection confirmed the visible PDF definition line now reads `one mind to another`.
- Full PDF Poppler render confirmed 11 pages present and nonblank; contact-sheet visual scan showed the document remained coherent after the PDF rewrite.
- PDF extraction remains a mismatch because the PDF was visually patched without a DOCX-to-PDF converter; the visible PDF is not a fully modernized canonical artifact.

Unresolved terminology questions:

- Regenerate `collapse_of_the_semantic_middle_v0_3.pdf` from the corrected DOCX/source in an environment with LibreOffice, Word, or another proper exporter so the hidden/extracted PDF text layer matches the visible page text.

General audit rule carried forward: modernization must not accidentally narrow ontology. Cognition-neutral or cognition-broad terms should not be replaced merely because they could be read anthropomorphically; first inspect whether the local definition is human-only, artificial, hybrid, or substrate-agnostic.

General UX/technical-language rule carried forward: do not replace friendly, established user-facing terminology merely because a more technically precise term exists. Change UX labels only when they materially mislead users about capability, state, privacy, or behaviour. Otherwise preserve the UX label and define its technical meaning in docs and glossaries. `Hot Memory` can remain a user-facing label mapped to active/working context; `Bookkeeper` can remain a product role mapped to memory/context support; `Memory Jogger` can remain a user-facing label mapped to a rolling persisted summary. By contrast, `brain file` should become `GGUF model file` because that metaphor obscures the actual imported object.

General figurative-language rule carried forward: do not replace ordinary, well-understood figurative language merely because a more clinical phrase exists. `gold standard` is acceptable when it means reference benchmark/class and is not making a metaphysical claim. Distinguish dangerous ontology claims such as `real mind`, `all minds`, and `structurally safe` from ordinary readable language such as `gold standard`, `tool`, `reference point`, and `working model`. Prefer precision, but not at the cost of needless sterility.

General cognitive-prosthetic and operational-learning rule carried forward: `cognitive prosthetic` is not globally deprecated. Preserve it where it names user-side augmentation, accessibility, reasoning extension, or broader Symbound human-AI workflow meaning, with an explicit non-consciousness/personhood boundary where needed. Likewise, `system learns` may be retained where accumulated failure evidence changes future host behavior through explicit saved state or constraints; do not use it for hidden model self-learning or personhood claims.

### chatty-cog

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `docs/ARCHITECTURE.md`
- `docs/USER_MANUAL.md`
- `docs/COLD_MEMORY_BRIDGE_PLAN.md`
- `docs/DEMO_MODULES.md`
- `docs/MODULES.md`
- `docs/MODULE_BRIDGE.md`
- `docs/MODULE_HANDSHAKE_TEMPLATE.md`
- `docs/MODULE_TEMPLATE_CHOOSER.md`
- `docs/MODULE_UI.md`
- `docs/MODULE_UI_TEMPLATE.json`
- `docs/MODULE_VISUAL_LOAD.md`
- `handoff-guide.md`
- portal metadata override in `Whatisthisgithub/repo_metadata_overrides.json`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Hot Memory / hot memory | Active context | UX retained | Preserved where it is an app label or button text; docs and glossary now map it to active context. |
| Luke Warm memory | Rolling summary | UX retained | Preserved where it is an app label, panel name, or `lukewarm.txt` concept; docs now map it to rolling summary. |
| Cold logs | Audit history / event log | compatibility retained | `cold_log.jsonl` and cold-log wording are preserved as source/product terms while docs now describe them as audit history/event logs. |
| Department status updates | Module status updates | canonicalized | Current docs now say module status updates; `departments.md` and `departments.json` remain compatibility filenames. |
| Capsule library / capsule | Behaviour profile library / behaviour profile | UX retained | Product label retained, with current docs describing the feature as saved behaviour/style profiles. |
| Cognitive economy | Reasoning budget | canonicalized | Planning doc now uses reasoning-budget language while preserving referenced source files. |
| human-shaped memory stack | operator-controlled context stack | canonicalized | Planning doc now avoids overclaiming human cognition and describes the memory architecture operationally. |

Files changed:

- `../chatty-cog/README.md`
- `../chatty-cog/GLOSSARY.md`
- `../chatty-cog/docs/ARCHITECTURE.md`
- `../chatty-cog/docs/USER_MANUAL.md`
- `../chatty-cog/docs/COLD_MEMORY_BRIDGE_PLAN.md`
- `../chatty-cog/docs/DEMO_MODULES.md`
- `../chatty-cog/docs/MODULES.md`
- `../chatty-cog/docs/MODULE_BRIDGE.md`
- `../chatty-cog/docs/MODULE_HANDSHAKE_TEMPLATE.md`
- `../chatty-cog/docs/MODULE_TEMPLATE_CHOOSER.md`
- `../chatty-cog/docs/MODULE_UI.md`
- `../chatty-cog/docs/MODULE_UI_TEMPLATE.json`
- `../chatty-cog/docs/MODULE_VISUAL_LOAD.md`
- `../chatty-cog/handoff-guide.md`
- `repo_metadata_overrides.json`

Identifiers changed: no

Compatibility alias retained: yes, `Hot Memory`, `Luke Warm`, `cold_log.jsonl`, `departments.*`, `Bookkeeper`, and `Capsule Library` are retained where they are UI labels, filenames, or product vocabulary.

Historical occurrences intentionally preserved: yes, `docs/CHANGELOG.md` remains historical provenance and source/reference paths such as `helix_spine.schema.json` and `MemorySpine` were not rewritten.

Tests/checks run:

- Search confirmed retired current-prose phrasing was removed or reduced to intentional aliases, UI labels, compatibility filenames, and changelog provenance.
- `python scripts/generate_index.py`
- `node scripts/generate-seo.mjs` in `instance001.github.io`

Unresolved terminology questions:

- Rust/UI strings still contain legacy product labels and compatibility nouns. Those should be considered intentional until a separate product-label migration is requested.

### chatty-art

Status: ACTIVE

Audit scope:

- `README.md`
- `USER_MANUAL.md`
- `GLOSSARY.md`
- `HANDSHAKE.md`
- `static/index.html`
- `static/app.js`
- `API_KEY_LANES_DESIGN.md`
- `REGRESSION_CHECKLIST.md`
- `ecg_window.md`
- `src/`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| media-generation department | media-generation module | canonicalized | ChattyCog handshake wording now treats Chatty-art as a module rather than a department. |
| cognitive scaffolding experiments | human-AI workflow scaffolding | canonicalized | FMI splash/about copy now describes observable workflow scaffolding rather than cognition. |
| fingerprint | fingerprint / hash | unrelated implementation term | `lastBridgeStatusFingerprint` and `prompt_fingerprint` are content/hash implementation terms, not cognitive fingerprinting. |
| worker | worker / dataloader worker | unrelated runtime term | Occurrences are vendor/runtime concurrency terms and were left unchanged. |

Files changed:

- `../chatty-art/HANDSHAKE.md`
- `../chatty-art/static/index.html`

Identifiers changed: no

Compatibility alias retained: yes, no product labels or filenames required alias migration.

Historical occurrences intentionally preserved: yes, vendored runtime documentation and source under audio/runtime paths were not rewritten.

Tests/checks run:

- Search confirmed no current-facing `cognitive`, `department`, or retired memory terminology remained in Chatty-art source/docs outside unrelated implementation/vendor terms.
- `cargo test`
- `npm run lint`

Unresolved terminology questions:

- None for the current Chatty-art pass.

### chatty-edu

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `teacher_user_manual.md`
- `it_deployment_guide.md`
- `docs/MODULE_HANDSHAKE_TEMPLATE.md`
- `docs/MODULE_TEMPLATE_CHOOSER.md`
- `module_templates/template_module/HANDSHAKE.md`
- `module_templates/template_module/README.md`
- `module_templates/template_python_module/HANDSHAKE.md`
- `module_templates/template_native_rust_module/HANDSHAKE.md`
- `modules/demo_lesson_studio/web/index.html`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Tri-helix memory surfaces | Local context surfaces | canonicalized | README, architecture map, repo glossary, and corpus glossaries now use local context surfaces as the current term; tri-helix retained as historical/source shorthand. |
| hot memory | active context | UX/provenance retained | Student-facing `Chatty's thoughts` label remains; hot memory retained only as alias/provenance in glossaries and code/UX compatibility. |
| lukewarm memory | rolling summary | UX/compatibility retained | Student-facing `Memory jogger` and `lukewarm_*` networking compatibility strings remain; glossaries now map them to rolling summary. |
| cold logs | audit history / event log | compatibility retained | `cold_log.jsonl` and Bookkeeper log wording remain where they are source/storage terms; docs now describe them as audit-history logs where appropriate. |
| department | module | canonicalized | Module templates and hosted demo placeholder now say module rather than department. |
| Capsule | prompt/profile template | internal compatibility retained | `*_CAPSULE` prompt constants were left unchanged as internal prompt-template names, not public personality/sentience framing. |

Files changed:

- `../chatty-edu/README.md`
- `../chatty-edu/GLOSSARY.md`
- `../chatty-edu/teacher_user_manual.md`
- `../chatty-edu/it_deployment_guide.md`
- `../chatty-edu/docs/MODULE_HANDSHAKE_TEMPLATE.md`
- `../chatty-edu/docs/MODULE_TEMPLATE_CHOOSER.md`
- `../chatty-edu/module_templates/template_module/HANDSHAKE.md`
- `../chatty-edu/module_templates/template_module/README.md`
- `../chatty-edu/module_templates/template_python_module/HANDSHAKE.md`
- `../chatty-edu/module_templates/template_native_rust_module/HANDSHAKE.md`
- `../chatty-edu/modules/demo_lesson_studio/web/index.html`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`

Identifiers changed: no

Compatibility alias retained: yes, student-facing labels (`Chatty's thoughts`, `Memory jogger`), storage filenames (`cold_log.jsonl`, `memory_jogger.txt`), `lukewarm_*` networking identifiers, and `*_CAPSULE` prompt constants remain.

Historical occurrences intentionally preserved: yes, `CHANGELOG.md`, vendored `llama.cpp`, and implementation fingerprints/workers were left unchanged.

Tests/checks run:

- Search confirmed remaining hits are intentional glossary aliases, code identifiers/product strings, or historical/vendor provenance.
- `cargo test`
- `python scripts/generate_index.py`
- `node scripts/generate-seo.mjs` in `instance001.github.io`

Unresolved terminology questions:

- A later product-label migration could rename shared `luke warm` networking UI, but that would be a behaviour/UX compatibility change and was intentionally out of scope here.

### chatty-pet

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `docs/ARCHITECTURE.md`
- `docs/APP_IDENTITY.md`
- `docs/ROADMAP.md`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Reducer owns truth | Reducer owns truth | foundational/current doctrine | Preserved as the repo's central deterministic state-governance rule. |
| Templates define possibility | Templates define possibility | canonical/current doctrine | Preserved as a clear content-boundary rule for the toy. |
| RD Engine doctrine spine | RD Engine doctrine / RD Engine architectural lineage | canonicalized | Source docs now use doctrine/lineage language; `spine` remains only as historical/provenance wording in the corpus glossary alias. |
| Bubble Wand | Bubble Wand | unrelated UX item | Preserved as a toy item name, not prompt/capsule `wand` terminology. |
| snack-minded / nap-shaped | snack-minded / nap-shaped | UX flavor | Preserved as product copy describing pet moods/items; not a technical cognition claim. |

Files changed:

- `../chatty-pet/README.md`
- `../chatty-pet/GLOSSARY.md`
- `../chatty-pet/docs/ARCHITECTURE.md`
- `../chatty-pet/docs/APP_IDENTITY.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`

Identifiers changed: no

Compatibility alias retained: yes, `RD Engine doctrine spine` remains as a historical/provenance alias in the corpus glossary.

Historical occurrences intentionally preserved: yes, toy item and flavor text that happen to match terms such as `wand` or `minded` remain product language.

Tests/checks run:

- Search confirmed no cognition-heavy, capsule/prompt, MCM, or department terminology required current-facing changes.
- `flutter test`
- `flutter analyze`

Unresolved terminology questions:

- None for the current Chatty-Pet pass.

### chatty-mini

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `docs/USER_MANUAL.md`
- current Dart app surfaces under `lib/`, especially `features/help` and `features/character`
- widget tests under `test/`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| model as "brain" file | GGUF model file | canonicalized | Beginner manual now describes the imported model as the `.gguf` file rather than anthropomorphic "brain" wording. |
| Hot Context | active context | UX retained | `Hot Context` remains an app label and filename alias; explanatory prose and glossary now map it to active context. |
| Rolling Summary / Summary bump | rolling summary | UX retained | Preserved as visible product wording for the recap side panel. |
| Cold Log | memory/log files and session logs | UX/compatibility retained | Preserved as an app tray/file label; docs keep it as local persistent memory/log management rather than a broader architecture claim. |
| persona profiles / active persona | character prompt profiles / active character prompt | canonicalized with UX alias | Docs and glossaries now prefer character prompt/profile language; persona remains a familiar UX alias. |
| Bookkeeper | support model role | UX retained | Preserved as a product role name for optional recap/memory support, not a claim about model cognition. |

Files changed:

- `../chatty-mini/README.md`
- `../chatty-mini/GLOSSARY.md`
- `../chatty-mini/docs/USER_MANUAL.md`
- `../chatty-mini/lib/features/help/help_sheet.dart`
- `../chatty-mini/lib/features/character/character_tray.dart`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`

Identifiers changed: no

Compatibility alias retained: yes, UI labels and filenames such as `Hot Context`, `hot_context.md`, `Cold Log`, `cold_log.md`, `Bookkeeper`, and persona/profile imports remain compatible.

Historical occurrences intentionally preserved: yes, vendored upstream `llama.cpp` source under Android native code was not rewritten.

Tests/checks run:

- Targeted search across `README.md`, `GLOSSARY.md`, `docs/USER_MANUAL.md`, `lib/`, and `test/` confirmed remaining `Hot Context`, `Cold Log`, `Bookkeeper`, and persona terms are intentional UI labels, compatibility filenames, or aliases.
- `flutter test`
- `flutter analyze`

Unresolved terminology questions:

- A later product-label migration could rename UI labels such as `Hot Context` or `Cold Log`, but that would be a user-facing compatibility change and was intentionally out of scope here.

### reflective_identity_geometry

Status: ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `abstract.md`
- `reflective_identity_geometry.md`
- `reflective_identity_geometry.tex`
- `rig_expanded.tex`
- `versions/README.md`
- preserved historical snapshot under `versions/v0.1/`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`
- portal metadata override in `Whatisthisgithub/repo_metadata_overrides.json`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Reflective Identity Geometry (RIG) | Reflective Identity Geometry (RIG) | foundational/current hypothesis | Preserved as the paper's named framework, but documented as a system-level hypothesis and dyadic unit-of-analysis extension of HRIS. |
| identity surface | interaction regime / identity trajectory / reflective geometry | hypothesis/provenance retained | Root v0.2 repo glossary now prefers `Interaction regime`; corpus glossary was updated away from the stronger v0.1-style `identity surface` row. |
| cognitive mirror | reflective-transformative surface | bounded metaphor | Root v0.2 manuscript already qualifies the metaphor; no further source rewrite needed. |
| persona-like behavior | persona-like behavior | behaviourally grounded | Preserved where it describes observed continuity without claiming genuine model personality. |
| cognitive topology / extended cognition / philosophy of mind | cognition-broad theoretical language | foundational/theory retained | Preserved because the paper explicitly concerns extended/enactive cognition and philosophy of mind; modernization must not narrow ontology here. |
| live GitHub description overclaiming identity emergence | v0.2 bounded RIG description | canonicalized in portal | `repo_metadata_overrides.json` now supplies a safer active-index description until live GitHub metadata can be updated. |

Files changed:

- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `repo_metadata_overrides.json`
- generated `README.md`

Identifiers changed: no

Compatibility alias retained: yes, `identity surface` remains in v0.1 provenance and as historical HRIS/RIG terminology where the source is explicitly historical.

Historical occurrences intentionally preserved: yes, `versions/v0.1/` was not rewritten because it is a preserved historical snapshot. References to HRIS terminology and older v0.1 claims remain in that snapshot for provenance.

Tests/checks run:

- Search confirmed root v0.2 source files already bound RIG away from model consciousness, model-internal personality, perfect mirroring, and necessary human cognitive change.
- Search confirmed remaining strong `identity surface`, `cognitive topology`, and persona language is either root v0.2 bounded theory language or preserved v0.1 provenance.
- `python scripts/generate_index.py`
- `node scripts/generate-seo.mjs` in `instance001.github.io`

Unresolved terminology questions:

- Live GitHub repository description should eventually be updated so the `reflective_identity_geometry` override can be removed.

### Cognition-Scale-Formal-Taxonomy

Status: ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `cognition-scale.md`
- `policymaker-brief.md`
- `psychology-biologist-crossover-explainer.md`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`
- portal metadata override in `Whatisthisgithub/repo_metadata_overrides.json`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Cognition Scale | Cognition Scale | foundational/proposed taxonomy | Preserved as the repo's named framework, but public definitions now describe it as a taxonomy for human and artificial cognition systems rather than all minds. |
| LCM / LLM / MCM / SCM | LCM / LLM / MCM / SCM | framework terms retained | Preserved as taxonomy classes and repo identity terms; not replaced with generic wording because the repo is specifically defining this taxonomy. |
| all kinds / four kinds of minds | human and artificial cognition systems / cognition classes | canonicalized | README and field guide now avoid implying all systems are minds. |
| real mind | reference baseline / taxonomy class | canonicalized | Removed the metaphysical `real mind` claim, but restored `gold standard` where it simply means the human-cognition benchmark for the proposed taxonomy. |
| safe logical tool mind / deterministic cognition model | bounded deterministic reasoning tool / proposed artificial cognition class | canonicalized | MCM language now emphasizes bounded, deterministic, auditable systems without calling the class a mind or guaranteeing correctness by label alone. |
| typed memory spine | typed memory records | canonicalized | README now uses ordinary technical wording for inspected memory artifacts. |
| structurally safe | more inspectable when compliance requirements are met | canonicalized | Policy brief now avoids treating MCM safety as automatic and ties claims to compliance. |
| MCM acronym supersedes all previous uses | MCM within this taxonomy and Symbound-derived materials | canonicalized | README now avoids claiming authority over unrelated external acronyms. |

Files changed:

- `../Cognition-Scale-Formal-Taxonomy/README.md`
- `../Cognition-Scale-Formal-Taxonomy/GLOSSARY.md`
- `../Cognition-Scale-Formal-Taxonomy/cognition-scale.md`
- `../Cognition-Scale-Formal-Taxonomy/policymaker-brief.md`
- `../Cognition-Scale-Formal-Taxonomy/psychology-biologist-crossover-explainer.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `repo_metadata_overrides.json`
- generated `README.md`

Identifiers changed: no

Compatibility alias retained: yes, LCM/LLM/MCM/SCM remain the taxonomy's defining terms, and Janet remains the MCM example.

Historical occurrences intentionally preserved: yes, fuller v0.3/v1.0 text artifacts and compliance/checklist files were not bulk rewritten; they should be treated as formal/provenance material until a deeper paper-version migration is requested.

Tests/checks run:

- Targeted search confirmed remaining strong cognition terms are either framework-defining taxonomy language, formal artifact provenance, or explicit boundary/failure-mode text.
- `python -m json.tool repo_metadata_overrides.json`
- `python scripts/generate_index.py`

Unresolved terminology questions:

- Live GitHub repository description should eventually be updated so the `Cognition-Scale-Formal-Taxonomy` override can be removed.
- A deeper manuscript-version migration could separately modernize the full-edition `.txt` and checklist artifacts; this pass kept them as formal/provenance surfaces.

### safety_theatre

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `papers/safety-theatre-agency.md`
- `papers/ai-safety-first-governance.md`
- `docs/readers-guide.md`
- `asewb/README.md`
- `asewb/SPEC.md`
- `asewb/FAILURE_MODES.md`
- `asewb/NULL_CASE.md`
- portal metadata override in `Whatisthisgithub/repo_metadata_overrides.json`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| safety theatre | safety theatre | framework term retained | Preserved as the repo's central concept and as a readable extension of `security theatre`; not flattened into generic compliance-risk language. |
| agency | agency | framework term retained | Preserved because the paper explicitly concerns discretion, judgment, competence formation, and authority allocation. |
| agents | actors | disambiguated | Source README now says `actors` to avoid accidental confusion with AI agents while preserving the institutional-action meaning used in the paper. |
| all safety is theatre / safety is bad / anti-governance | explicit non-claims | bounded | Existing scope notes preserved: the framework targets some safety mechanisms and structural drift, not safety or governance as such. |
| internal model cognition | out of scope | bounded | ASEWB already states it evaluates interaction/governance drift, not internal model cognition or motives. |
| safety without agency is not safety | safety without agency is not safety | figurative/theory language retained | Preserved as readable thesis language, not replaced with sterile terminology; context makes clear it means resilient safety requires disciplined agency and competence cultivation. |

Files changed:

- `../safety_theatre/README.md`
- `repo_metadata_overrides.json`
- generated `README.md`

Identifiers changed: no

Compatibility alias retained: yes, `safety theatre`, `agency suppression`, and `ASEWB` remain the repo's defining terms.

Historical occurrences intentionally preserved: yes, paper titles, PDFs, TeX sources, and incident-report provenance remain untouched unless a deeper source/PDF regeneration pass is requested.

Tests/checks run:

- Targeted search confirmed existing source boundaries: not anti-safety, not anti-governance, not all safety mechanisms are theatre, no motive claims, and ASEWB is not a proxy for internal model cognition.
- `python -m json.tool repo_metadata_overrides.json`
- `python scripts/generate_index.py`
- `node scripts/generate-seo.mjs` in `instance001.github.io`

Unresolved terminology questions:

- Live GitHub repository description should eventually be updated so the `safety_theatre` override can be removed.

### cognitive_theology

Status: ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `version_manifest.json`
- `01_academic/manuscript_academic_consolidated.md`
- `01_academic/commentary_notes.md`
- `03_public/` adaptation surfaces
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`
- portal metadata override in `Whatisthisgithub/repo_metadata_overrides.json`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| cognitive theology | polytheism-monotheism structural analysis | repo-name/provenance retained | The repository name remains historical/provenance; the active README and glossary already present the work as a structural pack rather than theology-as-doctrine. |
| spiritual cognition / Symbound principles | structural architectures of religious systems | canonicalized in portal | Live generated description was stale; `repo_metadata_overrides.json` now points the public index to the bounded structural-analysis framing. |
| theological truth / faith advocacy | not in scope | boundary retained | README, manuscript, commentary notes, and FAQ already state the work does not make theological truth claims, value judgments, or faith-advocacy claims. |
| gods / divine authority / belief | source-domain terms | domain language retained | Preserved because the paper analyzes religious systems; these are ordinary domain terms, not anthropomorphic AI terminology. |
| hybrid features | hybrid features | domain language retained | Preserved as comparative religious/institutional terminology, not a global `hybrid cognition` migration target. |

Files changed:

- `repo_metadata_overrides.json`
- generated `README.md`

Identifiers changed: no

Compatibility alias retained: yes, `cognitive theology pack` remains as a glossary alias for repository-name provenance.

Historical occurrences intentionally preserved: yes, the repository name and source-domain religious language remain unchanged.

Tests/checks run:

- Search confirmed active source surfaces already bound the work as structural analysis and avoid theological truth/value claims.
- `python -m json.tool version_manifest.json`
- `python -m json.tool repo_metadata_overrides.json`
- `python scripts/generate_index.py`
- `node scripts/generate-seo.mjs` in `instance001.github.io`

Unresolved terminology questions:

- Live GitHub repository description should eventually be updated so the `cognitive_theology` override can be removed.

### llm-semantic-dataset-sorter

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `why-this-matters.md`
- `docs/00-product-plan.md`
- `docs/05-user-manual.md`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| semantic sorting / semantic triangulation | semantic sorting / semantic triangulation | product/framework terms retained | Preserved because they describe the tool's observable workflow: repeated sorting pressure, bucket budgets, junk behavior, and comparison across runs. |
| pure intrinsic ontology / own intrinsic logic | model-prior ontology / model-prior decision structure | bounded | Replaced because the old phrasing over-suggested access to model interiority; new wording keeps the experimental-control meaning. |
| human and machine negotiated a shared understanding | human review and model output brought into an explicit shared frame | bounded | Avoids implying machine understanding while preserving the two-way review workflow. |
| internal proximity logic / how they think | assignment rationale / rationale divergence | bounded | Keeps the useful comparison of explanations without claiming direct access to internal reasoning. |
| cognitive fingerprinting | semantic fingerprinting | canonicalized | Renamed because the feature profiles output-level semantic behavior, not internal model cognition. |
| worldviews / philosophical biases of the architecture itself | semantic priors / observable biases in model outputs | bounded | Preserves the interpretability idea while grounding claims in observed outputs under controlled prompts. |
| understanding how machines understand | inspecting how machines represent and explain semantic structure | bounded | Keeps the bridge metaphor and review goal without claiming machine understanding as a mental state. |
| truth for the run / bucket reality | reference frame / bucket frame | bounded | Keeps the locked-plan concept while avoiding truth/reality overclaim. |

Files changed:

- `../llm-semantic-dataset-sorter/README.md`
- `../llm-semantic-dataset-sorter/GLOSSARY.md`
- `../llm-semantic-dataset-sorter/why-this-matters.md`
- `../llm-semantic-dataset-sorter/docs/00-product-plan.md`
- `../llm-semantic-dataset-sorter/docs/05-user-manual.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `semantic sorting`, `semantic triangulation`, `junk bucket`, `bucket genesis`, and `blind_label` remain the tool's ordinary product vocabulary.

Historical occurrences intentionally preserved: yes, the product name and friendly UX language remain unchanged; this pass only bounded overclaims about model interiority, cognition, and truth.

Tests/checks run:

- `cargo test`
- Targeted search confirmed remaining `objective truth`, `really thinks`, and `internal cognition` language appears in explicit non-claim contexts.

### chatty-quest

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `docs/ARCHITECTURE.md`
- `docs/DECISION_LOG.md`
- `docs/DESIGN_INTENT.md`
- `docs/IMPLEMENTATION_ROADMAP.md`
- `docs/KNOWN_NON_GOALS.md`
- `docs/NARRATOR_CONTEXT_SPEC.md`
- `docs/PROJECT_OVERVIEW.md`
- `docs/UI_SHELL_SPEC.md`
- `docs/V0_1_RELEASE_NOTES.md`
- `docs/V0_2_MILESTONE_PLAN.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| RD Engine / Radiant Determinism | RD Engine / Radiant Determinism | product/framework terms retained | Preserved as the game engine's named identity and design stance; `radiant` and `alive` are readable experience language bounded by deterministic-state claims. |
| game truth / canonical truth / truth model | game truth / canonical truth / truth model | game-canon technical language retained | Preserved because the docs explicitly define this as reducer-owned canonical game state, not metaphysical truth. |
| Dungeon Master / DM capsule / narrator | Dungeon Master / DM capsule / narrator | UX/game terms retained | Preserved as expected tabletop/game terminology and product flavor; docs already state narrator/capsules shape presentation, not mechanics. |
| real LLM / real model | live LLM / live model | disambiguated | Replaced where the intended contrast was inactive mock seam versus future integrated runtime model, avoiding the implication that current components are unreal or fake. |
| split-brain model direction | dual-model runtime direction | clarified | Replaced a clinical/ambiguous brain metaphor in a technical planning sentence while preserving the planned CPU helper / GPU narrator split. |
| natural-language understanding | natural-language understanding | non-goal retained | Preserved where it appears as an explicit non-goal or capability boundary; ordinary `understand` language elsewhere remains user-facing readability, not a cognition claim. |
| support memory / Bookkeeper | support memory / Bookkeeper | bounded product terms retained | Preserved because support memory is explicitly non-authoritative and Bookkeeper is only a future support role. |

Files changed:

- `../chatty-quest/docs/ARCHITECTURE.md`
- `../chatty-quest/docs/DECISION_LOG.md`
- `../chatty-quest/docs/DESIGN_INTENT.md`
- `../chatty-quest/docs/IMPLEMENTATION_ROADMAP.md`
- `../chatty-quest/docs/KNOWN_NON_GOALS.md`
- `../chatty-quest/docs/NARRATOR_CONTEXT_SPEC.md`
- `../chatty-quest/docs/PROJECT_OVERVIEW.md`
- `../chatty-quest/docs/UI_SHELL_SPEC.md`
- `../chatty-quest/docs/V0_1_RELEASE_NOTES.md`
- `../chatty-quest/docs/V0_2_MILESTONE_PLAN.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `RD Engine`, `Radiant Determinism`, `DM`, `narrator`, `capsule`, and `game truth` remain defining vocabulary.

Historical occurrences intentionally preserved: yes, repo branding, scenario flavor, screenshots, generated release binaries, and game-content prose were not rewritten.

Tests/checks run:

- `cargo test`
- Targeted search confirmed no remaining `real LLM`, `real model`, or `split-brain` phrasing in active docs.

### chatty-lora

Status: ACTIVE

Audit scope:

- `README.md`
- `USER_MANUAL.md`
- `GLOSSARY.md`
- `static/index.html`
- `static/app.js`
- `models/wan/dependencies/README.md`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Chatty-lora / LoRA builder | Chatty-lora / LoRA builder | product terms retained | Preserved as accurate product language for a local LoRA workflow dashboard. |
| Helper Chat / helper lanes / local helper | Helper Chat / helper lanes / local helper | UX terms retained | Preserved because they are friendly user-facing labels for guidance routes and do not mislead about capability, privacy, or state; docs explain local versus cloud lanes. |
| assistant persona | assistant persona | LoRA concept label retained | Preserved as a valid training-concept category; it names a possible output behavior/style target, not a claim that the app or model has personhood. |
| app-assistant GGUF models / helper weights | app-assistant GGUF models / helper weights | technical object terms retained | Preserved because the docs explicitly map these to local GGUF model files and separate them from Builder training base models. |
| starter personality | starter profile | bounded | README now describes `Training preset` as a starter profile rather than a personality for the run. |
| cognitive scaffolding experiments | cognitive scaffolding experiments | broader FMI tagline retained | Preserved as organizational/research framing, not a local claim that Chatty-lora performs cognition or contains a mind. |
| magic quality sliders / useful, not magical | magic quality sliders / useful, not magical | figurative non-claim language retained | Preserved because the wording explicitly reduces overclaim and remains approachable. |
| proof test / proof of final LoRA quality | proof test / proof of final LoRA quality | ordinary validation language retained | Preserved because context distinguishes smoke testing from final quality claims. |

Files changed:

- `../chatty-lora/README.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Helper Chat`, `helper lanes`, `assistant persona`, `Concept stack`, `Wan handoff`, and `ECG Window` remain established product vocabulary.

Historical occurrences intentionally preserved: yes, screenshots, release binaries, UI labels, and model-family folder names were not renamed.

Tests/checks run:

- `cargo test`
- Targeted search confirmed model files/GGUF files are described as files or weights, not metaphors.

### nanochat-llm-tweaker

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `HANDSHAKE.md`
- `CLI_GUI_FUNCTION_MAP.md`
- `nanochat-master/LOCAL_BUILDER_USER_MANUAL.md`
- `nanochat-master/ZERO_EXPERIENCE_END_TO_END_GUIDE.md`
- `nanochat-master/nanochat/dashboard.html`
- `nanochat-master/nanochat/dashboard_tools.py`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| LLM Tweaker Builder | LLM Tweaker Builder | product term retained | Preserved as the wrapper/dashboard product name; docs already define it as a local builder workflow, not a vague prompt-tweaking toy. |
| GGUF helper assistant | GGUF helper assistant | UX/technical term retained | Preserved because `assistant` is standard chat/SFT role language and the docs distinguish the helper `.gguf` from the model being trained. |
| `Assistant_models/` | `assistant_models/` | path corrected | README, glossary, and handshake now match the actual lower-case helper-model folder used by code and detailed guides. |
| `Assistant_sandbox/` | `assistant_sandbox/` | path corrected | Handshake artifact paths now match the actual lower-case sandbox folder used by code and detailed guides. |
| teaching the assistant how it should think | teaching the assistant how it should describe its role and behave in conversation | bounded | Replaced one model-interiority phrase in the beginner manual while preserving the plain-language SFT explanation. |
| Truth-First Teammate / Truth-First Preset | Truth-First Teammate / Truth-First Preset | UX preset retained | Preserved as an established friendly preset label; context defines it through uncertainty, evidence, and role behavior rather than guaranteeing truth. |
| lab bench, not vending machine / not magic / not summon intelligence | same figurative language | figurative non-claim language retained | Preserved because it reduces overclaim in memorable user-facing language rather than creating one. |
| real `.gguf` / real corpus | actual local file / user-provided corpus context | ordinary readable language retained | Preserved where `real` simply distinguishes actual provided files from missing placeholders. |

Files changed:

- `../nanochat-llm-tweaker/README.md`
- `../nanochat-llm-tweaker/GLOSSARY.md`
- `../nanochat-llm-tweaker/HANDSHAKE.md`
- `../nanochat-llm-tweaker/nanochat-master/LOCAL_BUILDER_USER_MANUAL.md`
- `../nanochat-llm-tweaker/nanochat-master/nanochat/dashboard.html`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `LLM Tweaker Builder`, `GGUF helper assistant`, `Truth-First Teammate`, and `assistant_sandbox` remain established workflow terms.

Historical occurrences intentionally preserved: yes, upstream-derived `nanochat-master` role names, tests, release/runtime binaries, and synthetic-data dev materials were not bulk rewritten.

Tests/checks run:

- `python -m pytest` in `nanochat-master` (`156 passed, 11 skipped`)
- Targeted search confirmed remaining `Truth-First` and figurative beginner-guide wording is bounded UX/preset language, not a truth guarantee or cognition claim.

### janet-school

Status: ACTIVE BUT MCM/IDENTITY-SENSITIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `docs/ALIGNMENT.md`
- `docs/ANALYSIS_SCHEMA.md`
- `docs/GUI_PLAN.md`
- `docs/USER_MANUAL.md`
- `docs/ABOUT.md`
- `web/index.html`
- `web/app.js`
- `build-plan-fox-codex.md`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Janet School | Janet School | product/research identity retained | Preserved as the repo's name and research rig identity. |
| Deterministic MCM student / Janet / MCM | Deterministic MCM student / Janet / MCM | framework terms retained | Preserved because the repo is explicitly about a deterministic MCM student under study; docs already distinguish Janet from the LLM teacher and from a general assistant persona. |
| cognition / cognitive scaffolding | cognitive scaffolding experiments | bounded umbrella language retained | Preserved in the FMI publisher/tagline context and build-plan provenance; not a claim that this repo proves cognition or contains a mind. |
| emergent structure candidate / boundary pressure / anomaly cluster | same provisional research language | research terms retained | Preserved because the analysis schema and alignment docs explicitly require candidate/provisional wording and human review. |
| confirmed intelligence / known cognitive law | prohibited example language | bounded/prohibited | Preserved only as examples of language the build plan forbids; not active claims. |
| proof / abstraction / intelligence | explicit non-claims | bounded | Source docs already say the analyzer does not prove abstraction or intelligence and that one success is never enough. |
| teacher backend / local-llm teacher | teacher backend / local-llm teacher | architecture terms retained | Preserved because the docs clearly keep the teacher outside the MCM core and prohibit teacher answers from becoming Janet answers. |
| memory-only / explicit memory | memory-only / explicit memory | technical terms retained | Preserved as explicit logged state and comparison controls, not hidden or anthropomorphic memory. |
| assistant-like chat framing / personality language | avoid in GUI | bounded/prohibited | Preserved only in GUI guardrails as things to avoid; no source rewrite required. |

Files changed:

- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Janet`, `MCM`, `teacher backend`, `memory-only run`, `boundary signal`, and `emergent candidate` remain defining terms.

Historical occurrences intentionally preserved: yes, build-plan doctrine and FMI tagline language were left intact because they are either bounded or explicitly prohibitive.

Tests/checks run:

- `cargo test`
- Targeted search confirmed remaining strong cognition/proof/personality terms are explicit non-claims, avoid-list items, framework-defining MCM language, or bounded publisher tagline language.

### cognition-mesh-test-chamber

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `docs/cognitive-fingerprint.md`
- `docs/philosophy.md`
- `docs/negative-lane-engine.md`
- `docs/user-manual.md`
- `new-direction.md`
- selected configs, source, and tests for fingerprint/assistant-review wording
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| cognitive fingerprinting | cognitive fingerprinting / behavioural suitability profiling | project-facing term retained | Restored as the portal's primary repo-local label because it is the project's central readable term; source now defines it technically as observable behavioural suitability profiling. |
| cognitive fingerprint | cognitive fingerprint / contextual deployment profile | bounded technical artifact | Preserved for JSON/report artifacts and docs because it refers to observed model-host-task behaviour, not internal cognition or a universal ranking. |
| cognition mesh | cognition mesh | repo identity retained | Preserved as the repo name and mesh framing; the docs attach all suitability claims to model, host, operator, task, lane, and observed failures. |
| deterministic truth / source of truth / ground truth | deterministic harness evidence | ordinary technical shorthand retained | Preserved where it distinguishes official harness artifacts from optional assistant commentary; not a metaphysical truth claim. |
| assistant review / assistant models | assistant review / assistant models | role language retained | Preserved because assistant review is explicitly secondary and cannot replace deterministic outputs. |
| memory | memory / historical run state | ordinary technical term retained | Preserved for model config fields, gauntlet memory pressure, and atlas/history language; no hidden personhood or human-memory claim is made. |
| magic / lab instrument / suitability cartographer | figurative product language retained | readable non-claim language | Preserved because it makes the project legible without overstating capability. |

Files changed:

- `../cognition-mesh-test-chamber/README.md`
- `../cognition-mesh-test-chamber/GLOSSARY.md`
- `../cognition-mesh-test-chamber/docs/cognitive-fingerprint.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `cognitive fingerprinting`, `cognitive fingerprint`, `fingerprint`, and `behavioural suitability profiling` remain cross-mapped.

Historical occurrences intentionally preserved: yes, the original build brief and doctrine files retain `cognitive fingerprinting` because the term is now bounded rather than globally deprecated.

Tests/checks run:

- Targeted search confirmed remaining `cognitive fingerprint`, `cognition mesh`, `truth`, `memory`, `assistant`, `magic`, and `agentic/autonomous` language is bounded artifact, role, UX, or ordinary technical language.

General audit rule carried forward: modernization may define friendly or figurative project language instead of replacing it. Prefer replacement only when the term materially misleads about capability, state, privacy, behaviour, ontology, or evidence access.

### llm-defined-persistent-memory

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `llm-defined-memory.md`
- `deterministic-hot-context-injection.md`
- `context-routing-packets.md`
- `design-stance.md`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| model-native memory / model-native buckets | model-native memory / model-generated bucket map | bounded technical term retained | Preserved because the repo means bucket maps generated by and versioned for a target model. Source now states this is not hidden introspection, consciousness, personhood, or perfect access to internal cognition. |
| new mind, new drawers | new mind, new drawers / model-specific semantic organization | figurative ontology-broad shorthand retained | Preserved as readable project language; source and glossary now define `mind` here as model-specific semantic organization exposed by bucket-map generation, not personhood or consciousness. |
| The model defines the drawers | model-generated bucket-map principle | metaphor retained with definition | Preserved because the metaphor accurately conveys per-model bucket generation; glossary now says this is not direct access to internal cognition. |
| Hot context / Hot Memory cards | hot context cards | UX/technical label retained | Preserved as established product-facing language for triggered context injection; docs already make it inspectable, deterministic, and user-controllable. |
| Cold logs / cold audit logs | cold logs as audit history | UX/technical label retained | Preserved because it clearly distinguishes archive/evidence surfaces from active working context. |
| source of truth / host-controlled truth | deterministic runtime evidence | ordinary technical shorthand retained | Preserved where it distinguishes reducer-governed persisted state from LLM proposals; not a metaphysical truth claim. |
| spooky memory / vibes / ape-made filing cabinet | same figurative language | readable non-claim language retained | Preserved because these phrases reduce overclaim and clarify user experience; they do not assert capability or ontology. |

Files changed:

- `../llm-defined-persistent-memory/README.md`
- `../llm-defined-persistent-memory/GLOSSARY.md`
- `../llm-defined-persistent-memory/llm-defined-memory.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `model-native`, `new mind, new drawers`, `Hot Context`, `Hot Memory cards`, `Cold logs`, and `source of truth` remain mapped and bounded.

Historical occurrences intentionally preserved: yes, approachable project-language and metaphorical memory phrasing remain where they are technically defined and non-misleading.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `mind`, `memory`, `hot context`, `cold logs`, `truth`, `spooky`, `vibes`, `autonomous`, and `consciousness` language is either explicitly bounded, avoided as a non-claim, or ordinary technical/product language.

### Symbound_Academia_Spine

Status: ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `academic_abstract.md`
- `spine_academia_config.json`
- `Factory/factory/config_academia.json`
- `build_academic_spine.py`
- orchestration metadata
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Symbound Academia Spine / academic spine | Symbound Academia Spine / academic processing pipeline | project identity retained | Preserved because `Spine` is the repo name and organizing metaphor; source and corpus glossary now state it is not a claim that the tool is cognitive or autonomous. |
| aligned cognitive prosthetic | FMI-aligned research support tool | canonicalized | Replaced in acknowledgements because the original phrasing over-personified the tool and implied a cognitive apparatus rather than a research-support pipeline. |
| reliable cognitive prosthetics for emergent AI-human co-research | reliable research support infrastructure for human-AI research workflows | canonicalized | Replaced in the academic abstract to describe observable workflow support rather than emergent co-research cognition. |
| Symbound Cognitive Architecture / Janet/MCM research | same framework names | framework terms retained | Preserved as project/framework references; not treated as claims that the Academia Spine itself is cognitive. |
| cognitive architecture / external cognition / phenomenology / mental state keywords | classifier keywords retained | corpus-routing vocabulary retained | Preserved in config keyword lists because they classify incoming research material and must remain able to route legacy/theory content. |
| backbone / spine / relics | same figurative language | ordinary metaphor retained | Preserved where it names project structure, archive handling, or readable pipeline metaphor rather than ontology. |

Files changed:

- `../Symbound_Academia_Spine/README.md`
- `../Symbound_Academia_Spine/GLOSSARY.md`
- `../Symbound_Academia_Spine/academic_abstract.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Symbound Academia Spine`, `academic spine`, `Symbound Cognitive Architecture`, and config classifier terms remain intact.

Historical occurrences intentionally preserved: yes, repo identity, citation text, classifier keywords, and Symbound/Janet/MCM framework references remain.

Tests/checks run:

- `python -m py_compile build_academic_spine.py Factory/factory/sort_academia.py Factory/factory/consolidate.py`
- `git diff --check`
- Targeted search confirmed remaining `spine`, `cognitive`, `prosthetic`, `emergent`, `organ`, `phenomenology`, and `mental state` language is either bounded source/framework language, classifier vocabulary, or ordinary metaphor.

### semantic-signal-alphabet

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `design-stance.md`
- `docs/00_premise.md`
- `docs/02_model_native_sorting.md`
- `docs/07_safety_and_non_medical_scope.md`
- `docs/10_model_specificity_and_migration.md`
- `docs/11_companion_layer_for_partial_signal_decoding.md`
- `adapters/bci/README.md`
- `adapters/bci/triangulation_runtime.md`
- source manifests and examples for dataset-vocabulary terms
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Semantic Signal Alphabet | Semantic Signal Alphabet | foundational framework term retained | Preserved as the repo's core concept: a low-bandwidth semantic alphabet framework where bucket count is fixed by the application and sorting is generated by the target model. |
| model-native / model-native sorting | model-native / model-generated bucket map | bounded technical term retained | Preserved, with README/docs/glossary now stating that `model-native` means generated by and versioned for a target model, not hidden access to model-internal cognition, consciousness, or objective semantic truth. |
| model exposes a semantic compression layer | model produces a semantic compression layer | canonicalized | Changed `expose` to `produce` in `design-stance.md` to avoid accidental introspection language while preserving the concept. |
| BCI / brainwave / partial signal decoding | BCI / partial signal-decoding adapter | bounded downstream application retained | Preserved because docs already state SSA is not medical, not full thought decoding, not brain-reading, and not a primary raw-signal decoder. |
| Brain2Qwerty citation | Brain2Qwerty citation | source-backed example retained | Preserved as a cited downstream example; Meta AI pages confirm June 29, 2026 Brain2Qwerty v2 blog/publication framing for non-invasive sentence decoding from MEG recordings. |
| mind / soul / consciousness / brain dataset items | same source-vocabulary items | dataset vocabulary retained | Preserved because these occur inside starter vocabulary/source manifests and generated example buckets, not as active claims by the framework. |
| alphabet / bucket / bandwidth / UNASSIGNED | same framework terms | core technical language retained | Preserved because they are central to the artifact schema and runtime interpretation model. |

Files changed:

- `../semantic-signal-alphabet/README.md`
- `../semantic-signal-alphabet/GLOSSARY.md`
- `../semantic-signal-alphabet/design-stance.md`
- `../semantic-signal-alphabet/docs/02_model_native_sorting.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `SSA`, `model-native`, `BCI`, `brainwave`, `alphabet`, `bucket map`, and `UNASSIGNED` remain intact.

Historical occurrences intentionally preserved: yes, source vocabulary words, example bucket labels, BCI adapter names, and cited research titles remain unchanged.

Tests/checks run:

- `python -m py_compile tools/generator/generate_bucket_map.py`
- `git diff --check`
- Targeted search confirmed remaining `brain`, `BCI`, `thought`, `mind`, `cognitive`, `model-native`, `objective truth`, `proof`, and `signal` language is either explicitly bounded, source-vocabulary data, citation text, or core framework language.

### MemorySpine

Status: ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `User_Instructions.txt`
- `memoryspine.py`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| MemorySpine / markdown spine | MemorySpine / local markdown archive and index | product identity retained | Preserved because it is the repo name and a friendly metaphor for per-conversation markdown files plus `index.md`; README and glossaries now state it is not hidden memory or interpretation. |
| memory | memory / exported conversation archive | ordinary product term retained | Preserved because the tool handles user-provided ChatGPT export data and writes local files only under `--output`. |
| CLI en dash | ASCII hyphen | user-facing help cleanup | Replaced one en dash in `memoryspine.py` help/docstring so Windows terminal output stays readable. |
| Browse your spine | browse exported markdown archive | UX phrase retained | Preserved because it is clear user-facing language and does not mislead about capability. |
| understand message structure | parse message structure | ordinary wording retained | Preserved because it describes parser compatibility, not cognitive understanding. |

Files changed:

- `../MemorySpine/README.md`
- `../MemorySpine/GLOSSARY.md`
- `../MemorySpine/memoryspine.py`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `MemorySpine`, `memoryspine`, and `spine` remain intact.

Historical occurrences intentionally preserved: yes, script names, user instructions, and README product identity remain unchanged.

Tests/checks run:

- `python -m py_compile memoryspine.py`
- `python memoryspine.py --help`
- `git diff --check`
- Targeted search confirmed remaining `spine`, `memory`, and `understand` language is bounded product/parser language, not hidden memory or cognition claims.

### historical-janet-school-exploratory-build

Status: ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `User_Instructions.txt` equivalent operational notes in `python_commands.txt`
- `janet.py`
- `audit_inner_monologue.py`
- `telemetry_engine.py`
- `teacher_miss_gpt.py`
- `remediate.py`
- `organs/`
- `reports/`
- `telemetry_log.md`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Historical Janet School / Janet / MCM-v0.1 | same historical project identity | historical framework identity retained | Preserved because the README explicitly frames the repo as a historical archive of an early exploratory build, not an active product or validated assessment system. |
| Janet organs | prompt-specialized module templates | bounded metaphor retained | `organs` remains as source/project vocabulary, but glossary relation changed from `cognitive modules` to `module templates` and now states this is not proof of model cognition. |
| CLI en dash | ASCII hyphen | user-facing help cleanup | Replaced one en dash in `telemetry_cli.py` help text so Windows terminal output stays readable. |
| teacher / student / school day | curriculum playback harness terms | experimental frame retained | Preserved because README states the special-education-style curriculum was a structural device for artificial model behaviour only and not a claim about real students, disability, or educational practice. |
| inner monologue / thinking / cognitive development | historical prompt/report language | historical generated/provenance language retained | Preserved in prompt templates and run reports as part of the original exploratory apparatus; not generalized into active claims. |
| Janet telemetry / organ health / remedial plan | heuristic telemetry / threshold-based follow-up plan | bounded technical terms retained | Preserved because glossary already marks telemetry as heuristic, not hidden introspection, and remedial plans as not clinical interventions or proof of broad competence. |
| understand / learning / reasoning | model-output evaluation language | bounded exploratory language retained | Preserved where the README frames these as observed output patterns or questions for review, not validated cognition claims. |

Files changed:

- `../historical-janet-school-exploratory-build/GLOSSARY.md`
- `../historical-janet-school-exploratory-build/telemetry_cli.py`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Janet`, `MCM-v0.1`, `organs`, `teacher`, `student`, `school day`, and `telemetry` remain intact.

Historical occurrences intentionally preserved: yes, generated reports, prompt organs, telemetry logs, and historical run artifacts were left unchanged.

Tests/checks run:

- `python -m py_compile janet.py audit_inner_monologue.py backend_chatty20b.py backend_miss_gpt.py janet_paths.py remediate.py run_school_day.py teacher_miss_gpt.py telemetry_cli.py telemetry_engine.py`
- `python telemetry_cli.py --help`
- `python remediate.py --help`
- `git diff --check`
- Targeted search confirmed remaining `mind`, `cognitive`, `inner monologue`, `thinking`, `teacher`, `student`, `MCM`, `memory`, and `understand` terms are either historical apparatus language, README-bounded exploratory language, generated/provenance reports, or ordinary parser/telemetry wording.

### Janet-MCM-Core

Status: ACTIVE BUT MCM/IDENTITY-SENSITIVE

Audit scope:

- `Readme-Janet-MCM-Core.md`
- `v.0.1_Public_release.txt`
- `CognitionScaleTaxonomy—FullEdition(v0.3).txt`
- `GLOSSARY.md`
- architecture diagram text/spec files
- corpus glossary/index entries in `Whatisthisgithub/GLOSSARY.md`, `Whatisthisgithub/GLOSSARY_FULL.md`, and `Whatisthisgithub/README.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Janet / MCM / Modest Cognition Model | same source/project identity | framework terms retained | Preserved because the repo exists to define Janet as an MCM reference architecture; replacing MCM would erase the subject rather than modernize it. |
| cognition class / artificial cognition / cognitive class | proposed artificial cognition class / bounded taxonomy term | bounded framework language retained | Preserved where source docs define a taxonomy, but README, release notes, glossary, and taxonomy now state these are architecture/class labels, not claims of consciousness, sentience, personhood, subjective experience, moral standing, or guaranteed correctness. |
| world's first / first public anchor / supersedes acronym uses | open reference / public anchor / Symbound-local acronym use | overbroad public claims narrowed | Softened external-priority and acronym-authority claims while keeping release identity and commons intent. |
| safe by design / ideal for | bounded by design / candidates for | safety guarantee softened | Avoids treating safety as automatic by label; safety remains a design objective and compliance posture. |
| cognitive step / cognition engine / cognitive substrate | MCM processing step / artificial cognition engine / proposed artificial-cognition substrate | precision update | Clarifies the artificial-system scope without replacing the core MCM terminology or flattening the project voice. |
| Typed Memory Spine / Skill-based cognition / Zero-hallucination stance | same terms | product/framework terms retained | Preserved because they are established framework labels; glossary now documents technical meanings and boundaries instead of replacing friendly terminology. |

Files changed:

- `../Janet-MCM-Core/Readme-Janet-MCM-Core.md`
- `../Janet-MCM-Core/v.0.1_Public_release.txt`
- `../Janet-MCM-Core/CognitionScaleTaxonomy—FullEdition(v0.3).txt`
- `../Janet-MCM-Core/GLOSSARY.md`
- `README.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Janet`, `MCM`, `Modest Cognition Model`, `Memory Spine`, `Skill-based cognition`, and `Zero-hallucination stance` remain intact.

Historical occurrences intentionally preserved: yes, architecture diagrams, release framing, taxonomy class names, and zipped artifact names were left intact.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `consciousness`, `sentience`, `subjective experience`, `cognition`, `memory`, `spine`, `agent`, and `reasoning` language is either explicit boundary language, taxonomy-defining MCM/LCM language, or ordinary framework terminology.

### ecg_window

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `docs/zero-knowledge-user-guide.md`
- `docs/why-use-this.md`
- `docs/architecture.md`
- `docs/ui-guidelines.md`
- `docs/signal-sources.md`
- `spec/ecg-window-contract.md`
- `copy-paste/`
- examples and original concept note search hits
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| ECG Window / ECG-style trace | same product term | user-facing metaphor retained | Preserved because the medical-monitor metaphor is the product identity and helps users understand activity at a glance; docs now clarify it is not medical-grade monitoring. |
| alive / sign of life / heartbeat | active workload / fresh telemetry, with metaphor retained | UX metaphor retained and bounded | Preserved because these are ordinary, useful user-facing phrases for visible process activity; README, user guide, why-use-this, and glossary now state they do not imply biological life, cognition, or self-awareness. |
| honest / truthful signal | same technical/UX standard | ordinary readable language retained | Preserved because the repo's core value is avoiding fake progress animation; this is not an ontology claim. |
| fake activity | fake activity | anti-pattern retained | Preserved in failure-handling/checklist docs because it materially warns implementers not to mislead users. |

Files changed:

- `../ecg_window/README.md`
- `../ecg_window/GLOSSARY.md`
- `../ecg_window/docs/zero-knowledge-user-guide.md`
- `../ecg_window/docs/why-use-this.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `ECG Window`, `alive`, `heartbeat`, `sign of life`, `honest`, and `truthful` remain readable UX/project language.

Historical occurrences intentionally preserved: yes, `ecg_window.md` remains the original concept note and keeps the motivating phrase `Is this thing still alive?` under the new README/user-guide boundary.

Tests/checks run:

- `python -m py_compile examples/python/ecg_window.py examples/python-tkinter/ecg_window_tk.py`
- `git diff --check`
- Targeted search confirmed remaining `alive`, `sign of life`, `heartbeat`, `truthful`, and `fake activity` language is bounded UX metaphor, implementation guidance, or preserved concept-note language.

### chattydoom

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `brains/`
- `engine/vizdoom_runner.py`
- `engine/state_adapter.py`
- `engine/action_adapter.py`
- `config.yaml`
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| brain / brains / enemy brain module | same game-AI module term | established game/modding term retained | Preserved because `brains/` is the repo API and ordinary game AI terminology; glossary now defines it as a `decide(state)` policy module, not cognition, consciousness, or autonomous agency. |
| comparable to agent policy module | comparable to game AI policy module | narrowed relation | Changed to avoid importing broader agentic framing into a tiny VizDoom sandbox. |
| believable behaviors | believable behaviors | ordinary game-design language retained | Preserved because it means simple enemy behaviour variety/cooldowns, not a claim of intelligence or mind. |
| confidence | confidence score | implementation field retained | Preserved as an action-selection output value, not epistemic certainty or self-report. |

Files changed:

- `../chattydoom/GLOSSARY.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `ChattyDoom`, `brains`, `brain module`, `decide(state)`, `action`, and `confidence` remain intact.

Historical occurrences intentionally preserved: yes, README and code references to `brains/` remain because they name the module folder/API.

Tests/checks run:

- `python -m py_compile setup_assets.py engine/vizdoom_runner.py engine/state_adapter.py engine/action_adapter.py brains/marine_basic.py brains/imp_spicy.py brains/pinkie_rush.py`
- `git diff --check`
- Targeted search confirmed remaining `brain`, `believable`, `confidence`, and `agent` language is bounded game-AI/module terminology or license text.

### chatty-edu-user

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `security_privacy_statement.md`
- `student_user_manual.md`
- `teacher_user_manual.md`
- `it_deployment_guide.md`
- `design_intent.md`
- `CHANGELOG.md`
- resource examples and model attribution notes
- corpus glossary entries in `Whatisthisgithub/GLOSSARY.md` and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| not telemetry / not telemetry-enabled | no remote telemetry or analytics in normal use | privacy wording clarified | Updated because the ECG widget reads local Windows performance counters. The trust claim now distinguishes local activity sampling from remote telemetry, analytics, or remote logging. |
| ECG window / activity trace | local activity cue | UX/product term retained | Preserved as a visible transparency feature; source and portal now state it is not a packet sniffer or formal network-audit tool. |
| `Chatty's thoughts` | active/current-session context | student-facing UX label retained | Preserved because the docs explain it is session-only context that clears on app close; changing the label would flatten the learner-facing interface without improving privacy. |
| `Memory jogger` | rolling persisted local summary | student-facing UX label retained | Preserved because docs define it as a local recent-session summary stored across restarts, not a full transcript or cloud memory. |
| Bookkeeper | local log/context support role | product role retained | Preserved because docs define it as local log search/context support behind a convenience PIN, not a hardened security boundary or separate authority. |
| diagnostic labels / support diagnosis | educational/support workflow wording retained | bounded domain language | Preserved because source states teacher-side scores/diagnostic labels are hidden from students and the product is not for ranking, shaming, permanent profiling, discipline, or surveillance. |

Files changed:

- `../chatty-edu-user/README.md`
- `../chatty-edu-user/GLOSSARY.md`
- `../chatty-edu-user/security_privacy_statement.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Chatty's thoughts`, `Memory jogger`, `Bookkeeper`, `ECG window`, `offline-first`, and `GGUF` remain intact.

Historical/generated occurrences intentionally preserved: yes, the prebuilt binary and resource example files were not modified; user-facing labels remain.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `thoughts`, `memory`, `Bookkeeper`, `diagnostic`, `telemetry`, `ECG`, `safe`, `cloud`, and `offline` language is bounded documentation, privacy wording, or retained UX terminology.

### chatty-factory

Status: ACTIVE WITH PRE-EXISTING DIRTY BUILD-DOCS WORKTREE

Audit scope:

- `README.md`
- `USER_MANUAL.md`
- `GLOSSARY.md`
- `foreword-on-chatty-factory-agentic-coding.md`
- current architecture and selected docs search
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| deterministic agentic coder | governed local build-and-patch factory | public description updated | Portal description now follows the current source README rather than older agentic-coder marketing language. |
| Agentic coding / agentic coder | bounded LLM-authored method under host governance | historical/product-positioning phrase retained | Preserved in the foreword and glossary because it describes the product lane historically, but now explicitly excludes autonomous software engineering, self-learning coding, and correctness guarantees. |
| learning student / it will learn | constraint library can accumulate failure guidance | ontology and autonomy narrowed | Reworded foreword so improvement comes from curated negative constraints and receipts, not a self-learning mind or student-like agent. |
| LLM pilot | selected LLM under host/tool limits | metaphor removed in one source sentence | Replaced because the sentence needed concrete limits: selected model reasoning limits, dataset boundaries, and available tooling. |
| magic box / patching by vibe | same ordinary figurative anti-claims | readable language retained | Preserved because these phrases warn users against overtrust and do not create ontology claims. |
| negative-lane host / frozen intent / receipts / funnel / triangulation | same core architecture terms | source architecture retained | Portal glossary realigned with source so these terms remain central instead of stale positive-family wording. |

Files changed:

- `../chatty-factory/GLOSSARY.md`
- `../chatty-factory/foreword-on-chatty-factory-agentic-coding.md`
- `README.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `ChattyFactory`, `agentic coding`, `negative lane`, `frozen intent`, `receipts`, `diagnosis-aware patch surgery`, `adaptive task decomposition`, and `triangulation` remain intact.

Historical/generated occurrences intentionally preserved: yes, existing build-docs, checkpoint archives, and the pre-existing uncommitted `build-docs` rebuild-plan changes were not edited.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `agentic`, `autonomous`, `learn`, `student`, `magic`, `truth`, `safe`, `diagnosis`, `proof`, and `authority` language is either bounded current architecture language, ordinary anti-overclaim prose, historical build-doc notes, or source code/license terminology.

Worktree note:

- Source repo still had pre-existing dirty files after this commit: `build-docs/README.md` and untracked `build-docs/plans/NEGATIVE_VOID_ENGINE_REBUILD_PLAN.md`. They were not staged or modified by this terminology slice.

### 4roomciv

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `Relicensing-notice.txt`
- visible references to `4room-civ-mvp.zip`
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| 4-Room Civilization MVP | same project/testbed identity | project identity retained | Preserved because the README explicitly frames it as a small trial/testbed for 2-3 humans and 1-2 local LLMs, not a production social system. |
| Helix memory | Helix memory / SQLite + FTS5 retrieval store | bounded technical term retained | Preserved because glossary defines it as `/helix` endpoint storage/search over spines, not hidden cognition, human-like memory, or cloud memory. |
| Spine / Helix Spine v1 | structured claim/rationale record | source schema term retained | Preserved because the term is schema-level product vocabulary with explicit required fields and length bounds. |
| Paired Room (R3) / Commons (R4) | paired session endpoint / threaded commons endpoints | UX/domain terms retained | Preserved because docs define them as API surfaces and room metaphors, not claims of autonomous society or multi-agent consciousness. |
| auto-extract spines / SPINE_AUTOWRITE | auto-extraction/write toggle | capability wording retained | Preserved because README documents how to disable autowrites and glossary distinguishes automatic writes from manual writes/search. |

Files changed:

- `TERMINOLOGY_MIGRATION_LEDGER.md`

Source files changed: no

Identifiers changed: no

Compatibility alias retained: yes, `4roomciv`, `Helix memory`, `spine`, `Paired Room (R3)`, `Commons (R4)`, and `SPINE_AUTOWRITE` remain intact.

Historical/generated occurrences intentionally preserved: yes, the zip artifact was not unpacked or edited during this audit; visible docs/glossary already provide bounded definitions.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `memory`, `shared space`, `humans`, `LLM`, `spine`, `paired room`, `commons`, `metrics`, and `autowrite` language is bounded source terminology for a small local trial.

### governance-by-design-report-commentary

Status: ACTIVE

Audit scope:

- `readme.md`
- `governance-by-design-commentary.md`
- `why-this-matters.md`
- `image-attribution-test.md`
- `GLOSSARY.md`
- image attribution/provenance note
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| genuine cognitive prosthetic | genuine cognitive prosthetic | restored and bounded | Restored in `why-this-matters.md` because the passage is about AI as user-side reasoning augmentation for sophisticated users. Source and glossary now define it as a cognitive prosthetic in the assistive workflow sense, not model consciousness, personhood, autonomous cognition, or shared human cognition. |
| preference salience bucketing | same diagnostic term | framework term retained | Preserved because it is the core claimed pattern under test and is framed as observable preference down-weighting, not model intent or malice. |
| meta-level litmus test / "Thoughts?" | same diagnostic setup | reproducible test term retained | Preserved because the repo clearly presents it as a simple observational test, not a broad benchmark or accusation manifesto. |
| image attribution bias test | source attribution anchoring diagnostic | missing portal row restored | Added to corpus glossaries to match source; the test changes attribution context while holding the image constant. |
| own preference-handling / memory mechanisms | model/system preference-handling mechanisms | self-referential diagnostic language retained | Preserved in source because it refers to product/system mechanisms under test, not subjective selfhood or consciousness. |

Files changed:

- `../governance-by-design-report-commentary/why-this-matters.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `preference salience bucketing`, `meta-level litmus test`, `Thoughts?`, `image attribution bias test`, `Saved Memories`, and `Custom Instructions` remain intact.

Historical/generated occurrences intentionally preserved: yes, image asset/provenance and diagnostic prompt wording were left unchanged.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `preference`, `memory`, `bias`, `mechanistic`, `malice`, `diagnostic`, `reasoning`, and `own preference-handling` language is bounded commentary/diagnostic language, not a consciousness or intent claim.

### project-leviathan

Status: ACTIVE WITH PRE-EXISTING UNTRACKED THEORY DOCS

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `RELEASE.md`
- `RELATIONAL_PERMUTATION_ENGINE.md`
- `DUAL_COLD_MEMORY_AND_DEEP_RECALL.md`
- `SEMANTIC_ASSIMILATION_AND_WHY_LIBRARY.md`
- `SEMANTIC_OBJECT_COMPILER.md`
- `ASSUMPTION_FREEZE_AND_WORLDVIEW_BRANCHING.md`
- `COGNITIVE_ECONOMY_GOVERNOR.md`
- `HOST_TO_MODEL_RELATIONAL_ABSTRACTION_BRIDGE.md`
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| cognition / memory / worldview / metacognition / reasoning | host-side architecture terms | cognition-broad framework language retained and bounded | Preserved because the repository is explicitly a host-side architecture specification; README and glossaries now state these are not claims of model consciousness, sentience, personhood, subjective experience, or self-owned truth. |
| Cognitive Economy Governor | Reasoning Budget Governor / Cognitive Economy Governor | compatibility alias retained | Source name remains because it is a core document title; portal glossary already keeps the current technical alias while preserving the historical/source name. |
| human-equivalent internal voice | engineering analogue of the human internal voice | anthropomorphic wording softened | Reworded in the governor doc to preserve the useful analogy while avoiding a literal human-equivalence claim. |
| human-like deep-memory shape / human-like recall | engineering analogy for retrieval architecture | readable analogy retained | Preserved because `DUAL_COLD_MEMORY_AND_DEEP_RECALL.md` explicitly says it is not a literal neuroscience claim. |
| understanding / intelligent / truth | operational understanding / host-owned truth boundaries | bounded framework language retained | Preserved where source explicitly says understanding is operational, the model does not own truth, and components are not truth engines. |
| Host-to-Model Relational Abstraction Bridge / model-internalised abstraction | curriculum/evaluation bridge | experimental hypothesis retained | Preserved because the bridge doc frames internalisation as a testable training hypothesis and keeps host verification/audit layers in place. |

Files changed:

- `../project-leviathan/README.md`
- `../project-leviathan/GLOSSARY.md`
- `../project-leviathan/COGNITIVE_ECONOMY_GOVERNOR.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Project Leviathan`, `Cognitive Economy Governor`, `Reasoning Budget Governor`, `Dual Cold Memory`, `Deep Recall`, `Why Library`, `Semantic Object Compiler`, `Assumption Freeze`, `Worldview Branching`, and `Host-to-Model Relational Abstraction Bridge` remain intact.

Historical/generated occurrences intentionally preserved: yes, document titles and theory vocabulary remain; pre-existing untracked theory docs were not staged or edited.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `human-like`, `cognition`, `memory`, `worldview`, `metacognition`, `truth`, `understanding`, `model-internalised`, and `semantic` language is bounded host-architecture, engineering analogy, or explicitly operational/testable hypothesis language.

Worktree note:

- Source repo still had pre-existing untracked files after this commit: `IMAGINATION_TRANSFORM_ATLAS_AND_LEARNING_LAW_PROBES.md`, `LEVIATHAN_BLIND_STAGE_REASONING_AND_CONTROLLED_NOVELTY_CALIBRATION.md`, `LEVIATHAN_COGNITIVE_GEARS_AND_TUNING_FORK_CALIBRATION.md`, `LEVIATHAN_CONNECTIVE_TISSUE_AND_MICRO_GOVERNANCE.md`, `LEVIATHAN_NEGATIVE_SPACE_FARMING_AND_PUB_TEST.md`, and `MEMORY_WORLDVIEW_AND_BOOPER_HYPOTHESIS.md`. They were not staged or modified by this terminology slice.

### rd-engine

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `docs/00_core_idea.md`
- `docs/01_drop_in_guide.md`
- `docs/02_use_cases.md`
- `src/engine.rs`
- `src/save.rs`
- `examples/minimal_host.rs`
- `examples/project_memory_host.rs`
- `tests/generic_core.rs`
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| truth / canonical truth / lasting truth / truth source | reducer-governed canonical state | ordinary technical shorthand retained and bounded | Preserved because this repo uses `truth` as a deterministic state-management term: the reducer-approved saved state a host treats as authoritative for continuity. Source docs and corpus glossaries now state it is not factual certainty, model knowledge, consciousness, metaphysical truth, or model-owned knowledge. |
| memory / project memory | memory / project memory | user-facing/domain example retained | Preserved because it names a common host use case and example schema, not a claim of model memory, mind, or hidden introspection. |
| understand in one sitting | understand in one sitting | ordinary readable language retained | Preserved as normal reader-facing language. It is not anthropomorphic or ontological terminology in context. |
| boring truth source / boring mutation boundary | boring truth source / boring mutation boundary | readable engineering language retained | Preserved because the phrase intentionally makes the deterministic mechanism plain and approachable without making a metaphysical claim. |
| semantic-signal-alphabet | semantic-signal-alphabet | proper repository name retained | Preserved as a link/example to adjacent work, not local semantic-ontology terminology. |

Files changed:

- `../rd-engine/README.md`
- `../rd-engine/GLOSSARY.md`
- `../rd-engine/docs/00_core_idea.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `RD Engine`, `buckets`, `reducers`, `actions`, `events`, `canonical state`, `project memory`, and `truth` shorthand remain intact.

Historical/generated occurrences intentionally preserved: yes, examples and tests keep `MemoryReducer`, `ProjectMemoryReducer`, and example bucket/action names because they are domain examples and public API-adjacent sample code.

Tests/checks run:

- `cargo test`
- `git diff --check`
- Targeted search confirmed remaining `truth`, `memory`, `understand`, `semantic`, and related language is bounded deterministic-state terminology, ordinary reader-facing language, or proper repository/example naming.

Worktree note:

- Source repo was clean before this terminology slice and clean after commit.

### model-behaviour-toolkit

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `CONTRIBUTING.md`
- `docs/user-manual.md`
- `docs/principles/non-anthropomorphic-collaboration.md`
- `docs/theory/context-continuity.md`
- `docs/legacy-inventory.md`
- `docs/how-to-add-a-module.md`
- `docs/deprecation-policy.md`
- `modules/`
- `bundles/`
- `compact/`
- `presets/`
- `examples/`
- `troubleshooting/`
- `evaluation/`
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| prompt/toolkit archives | Model Behaviour Toolkit | repo identity retained | Preserved as the current provider-neutral toolkit for prompt and interaction scaffolds. The repo already distinguishes modern active modules from legacy GPT-era archives. |
| capsules / wands / catalyst / patina / instance | baseline / recovery / handoff / review / continuity | legacy terminology retired in active modules | Preserved only in legacy inventory, replacement notes, and negative examples. Active guidance continues to prefer plain module names. |
| fake memory / hidden memory / continuity theater | explicit state / handoff / visible context | current technical boundary | Preserved and bounded: continuity comes from supplied state, artifacts, summaries, and handoffs, not claimed hidden recall. |
| anthropomorphic theater / persona cult / simulated personhood | boundary-aware collaboration | negative boundary retained | Preserved because it marks what the toolkit avoids: false personhood, claimed feelings, dependency, awakening, or hidden agency. |
| human and encouraging / warmth / friendly labels | natural user-facing tone | UX language retained and bounded | Preserved because these are ordinary UX/style terms. Source docs now explicitly state friendly labels and natural tone are acceptable when they do not mislead about capability, state, privacy, behaviour, memory, or personhood. |
| cognitive patina / behavioural spine | context continuity through externalized state | archival theory rewritten | Preserved only as legacy concepts being translated; current theory says durable continuity comes from saved artifacts, reusable modules, and precise handoffs. |
| cognitive-rebind-engine / soul-reanchor / oracle-persona | negative naming examples | intentionally preserved examples | Preserved as bad-example names in contributor docs to teach what not to add; not active recommended terminology. |

Files changed:

- `../model-behaviour-toolkit/README.md`
- `../model-behaviour-toolkit/CONTRIBUTING.md`
- `../model-behaviour-toolkit/docs/how-to-add-a-module.md`
- `../model-behaviour-toolkit/GLOSSARY.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Model Behaviour Toolkit`, `prompt`, `module`, `bundle`, `preset`, `example`, `session`, `drift`, `handoff`, `memory`, and archival terms such as `capsule` and `wand` remain where needed for provenance or user comprehension.

Historical/generated occurrences intentionally preserved: yes, legacy repo names, source-file names, and negative examples remain in audit and contributor docs.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `consciousness`, `sentience`, `personhood`, `fake memory`, `hidden memory`, `human and encouraging`, `cognitive patina`, `behavioural spine`, and legacy naming hits are bounded active guidance, archival translation, ordinary UX language, or explicit negative examples.

Worktree note:

- Source repo was clean before this terminology slice and clean after commit.

### ef-engine

Status: ACTIVE

Audit scope:

- `README.md`
- `GLOSSARY.md`
- `docs/00_core_idea.md`
- `docs/01_drop_in_guide.md`
- `docs/02_use_cases.md`
- `ENTROPY_FOLDING_FAILURE_VAULT_TRIANGULATION_LOOP.md`
- `EUREKA_CASCADE_EFFECT.md`
- `src/engine.rs`
- `src/save.rs`
- `examples/minimal_failure_host.rs`
- `examples/cascade_demo.rs`
- `tests/generic_core.rs`
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Entropy Folding / entropy / folding | search-disorder to routing-structure framework | framework metaphor retained and bounded | Preserved because it is the repo's named implementation lane and theory vocabulary. Source docs now state it is local search-routing language, not a thermodynamic, biological, cognitive, sentience, or magical-insight claim. |
| Constraint Metabolization / metabolize_constraint | constraint promotion / `metabolize_constraint` API | compatibility API and framework metaphor retained | Public API and examples remain stable. Docs now define metabolization as promoting evidenced failure into reusable constraints, not biology or cognition. |
| Eureka Cascade | accelerated routing effect | framework term retained and bounded | Preserved because it names the observed compounding constraint effect. Source and corpus docs now state it is not sudden insight, consciousness, guaranteed global correctness, or magic. |
| truthful failure / truthful stuckness / truthful progress | honest failure/stuckness reporting | ordinary technical shorthand retained | Preserved because the term describes not pretending success when a route cannot validly proceed; not a metaphysical truth claim. |
| negative knowledge / negative memory / routing intelligence | reusable failure constraints / routing evidence | implementation language retained and bounded | Preserved because it describes stored failure evidence and constraint effects. It is not model cognition, sentience, or hidden learning. |
| system learns | system learns / operational learning | retained and bounded | Restored as accurate operational shorthand where accumulated failure evidence is persisted as host-state constraints that change future routing behavior. This is not model self-training, hidden cognitive growth, consciousness, or personhood. |
| local-first agent orchestration | local-first orchestration | product/use-case phrase retained | Preserved as a broad workflow use case; this repo is still explicitly not a general agent framework or planner by itself. |

Files changed:

- `../ef-engine/README.md`
- `../ef-engine/GLOSSARY.md`
- `../ef-engine/docs/00_core_idea.md`
- `../ef-engine/ENTROPY_FOLDING_FAILURE_VAULT_TRIANGULATION_LOOP.md`
- `../ef-engine/EUREKA_CASCADE_EFFECT.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `EF Engine`, `Entropy Folding`, `Failure Vault`, `Triangulation`, `Metabolization`, `Eureka Cascade`, `metabolize_constraint`, and related code/example identifiers remain intact.

Historical/generated occurrences intentionally preserved: yes, public API names, example output strings, generated JSON examples, and theory-document titles remain unchanged.

Tests/checks run:

- `cargo test`
- `git diff --check`
- Targeted search confirmed remaining `entropy`, `folding`, `metabolization`, `Eureka`, `truth`, `agent`, `intelligence`, and related language is bounded local search-routing terminology, stable API/example language, or ordinary technical shorthand.

Worktree note:

- Source repo was clean before this terminology slice and clean after commit.

### ai-teaming-framework

Status: ACTIVE

Audit scope:

- `README.md`
- `ai-teaming-framework.md`
- `GLOSSARY.md`
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| AI Teaming / teaming | human-AI workflow pattern | collaboration term retained and bounded | Preserved because the repo intentionally teaches collaboration mechanics, not prompt-copying. Source and corpus glossaries now state that teaming is not a claim that AI thinks, feels, cares, has personhood, or shares human cognition. |
| partner / working partner | collaborative interaction signal | UX/collaboration language retained | Preserved because the guide explicitly says the specific word is not the mechanism; the collaborative intent and structural signal are what matter. |
| cognitive prosthetic / hybrid cognition | user-side capability extension / human-AI workflow output | broad Symbound framing retained and bounded | Preserved because modern Symbound retains broader human-AI hybrid cognitive-engine language where intended. Here it describes the human-AI workflow and user-side capability extension, not model consciousness or shared human cognition. |
| The AI's inherent goals / baked-in objectives / wants | the AI's default tendencies | over-agentive wording softened | Source guide now describes helpful-fast and always-answer patterns as practical default tendencies shaped by training, reinforcement learning, and product design. |
| The AI has internalised how real projects work | the AI has learned many patterns from real project work | hidden-cognition wording softened | Reworded to describe learned project-text patterns and structural dependencies without implying human-like internalization or understanding. |
| permanent transfer | cross-situation transfer | overclaim softened | Reworded because the principles are durable but not a guarantee of permanent effectiveness across all future models or contexts. |
| specific gratitude / good team / vending machine | concrete feedback and interaction-pattern signals | friendly readable language retained | Preserved because these terms are ordinary explanatory language and the guide explicitly rejects emotional manipulation, magic phrases, and AI personhood. |

Files changed:

- `../ai-teaming-framework/README.md`
- `../ai-teaming-framework/ai-teaming-framework.md`
- `../ai-teaming-framework/GLOSSARY.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `AI Teaming Framework`, `AI teaming`, `teaming`, `partner`, `hybrid cognition`, `cognitive prosthetic`, `specific gratitude`, `natural checkpoints`, and `multi-step sequencing trust` remain intact.

Historical/generated occurrences intentionally preserved: yes, friendly examples such as `hey partner`, `good team`, and `vending machine` remain because they are explanatory interaction-signal examples, not ontology claims.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `teaming`, `partner`, `cognitive prosthetic`, `hybrid cognition`, `thinks`, `feels`, `cares`, `trust`, and `magic` language is bounded collaboration framing, explicit non-claim text, or ordinary readable guidance.

Worktree note:

- Source repo was clean before this terminology slice and clean after commit.

### australian-ai-fair-go

Status: ACTIVE

Audit scope:

- `README.md`
- `FAIR_GO_CHARTER.md`
- `ONE_PAGE_BRIEF.md`
- `POLICY/README.md`
- `CASE_STUDIES/README.md`
- `EVIDENCE/claims-to-evidence.md`
- `EVIDENCE/repository-index.md`
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Australian AI Fair-Go / Fair-Go | Australian AI Fair-Go | policy identity retained | Preserved as plainspoken Australian policy framing. It names a proportionate policy/evidence lane, not a technical claim. |
| sovereignty / broad national capability sovereignty | broad national capability sovereignty | policy term retained and bounded | Preserved because the repo defines hosting, institutional, and broad national capability sovereignty. Evidence docs already state national-scale outcomes and adoption are not proven. |
| hybrid AI options / local-cloud hybrid choice | local/cloud architecture choice | architecture term retained and bounded | Preserved because `hybrid` refers to deliberate local/cloud escalation and architecture choice in this policy repo, not `hybrid cognition`. |
| cognitive prosthetic | user-side assistive workflow framing | evidence term retained and bounded | Preserved for cited Chatty-Cog evidence; source now states it is not model cognition, consciousness, sentience, or personhood. |
| cognitive fingerprint | behavioural suitability artifact | evidence term retained and bounded | Preserved for cited Cognition Mesh Test Chamber evidence; source now states it is not evidence of internal model cognition or a claim that models have minds. |
| The person remains the primary agent | human authority | policy rights/control language retained | Preserved because the term concerns human legal/practical authority over AI-supported workflows, not AI-agent ontology. |
| Bookkeeper / memory | support role / local state surfaces | UX/evidence labels retained | Preserved because they refer to cited product surfaces already bounded in their source repo audits. |

Files changed:

- `../australian-ai-fair-go/README.md`
- `../australian-ai-fair-go/EVIDENCE/repository-index.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Australian AI Fair-Go`, `Fair-Go`, `sovereignty`, `hybrid`, `human authority`, `cognitive prosthetic`, `cognitive fingerprint`, `Bookkeeper`, and `memory` remain where used.

Historical/generated occurrences intentionally preserved: yes, official-context links and evidence receipt URLs remain unchanged; they were not re-verified in this terminology slice.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `hybrid`, `cognitive prosthetic`, `cognitive fingerprint`, `sovereignty`, `primary agent`, `policy proposal`, `Bookkeeper`, and `memory` language is bounded policy/evidence terminology, UX/source evidence language, or explicit overclaim guardrail text.

Worktree note:

- Source repo was clean before this terminology slice and clean after commit.

### relational-curriculum-geometry

Status: ACTIVE

Audit scope:

- `README.md`
- `Relational-Curriculum-Geometry-Hypothesis.md`
- `Relational-Curriculum-Geometry-Primer.md`
- `experiment_001.md`
- `GLOSSARY.md`
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| learns / learning / learned pathways | learns / learning / learned pathways | ML-training language retained and bounded | Preserved because this repository is explicitly about training data order, fine-tuning, transfer, and measurable learning outcomes. Source now states these terms are not consciousness, personhood, biological cognition, or direct access to hidden internals. |
| cognitive landscape / internal handles / latent-space urban planning | same hypothesis metaphors | cognition-broad hypothesis language retained and bounded | Preserved because the terms communicate the latent-organization hypothesis and do not by themselves assert model personhood or sentience. The glossary now maps them to routing, transfer, uncertainty handling, and relation use. |
| Better rooms, roads, walls, doors, and limbs | same spatial metaphor | ordinary readable metaphor retained | Preserved under the figurative-language rule because it names curriculum structure and relational arrangement without making a literal simulator or body claim. |
| Team member, not whole team | bounded collaborator target | collaboration framing retained | Preserved because it describes role discipline and responsibility separation among user, model, host, tools, reviewers, and authorities; it is not a claim of autonomous agency. |

Files changed:

- `../relational-curriculum-geometry/README.md`
- `../relational-curriculum-geometry/Relational-Curriculum-Geometry-Hypothesis.md`
- `../relational-curriculum-geometry/Relational-Curriculum-Geometry-Primer.md`
- `../relational-curriculum-geometry/GLOSSARY.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Relational Curriculum Geometry`, `RCG`, `learns`, `cognitive landscape`, `internal handles`, `Team member, not whole team`, and `Better rooms, roads, walls, doors, and limbs` remain intact.

Historical/generated occurrences intentionally preserved: yes, `experiment_001.md` remains unchanged because its learning/safety/role-language is already bounded by the repo-level hypothesis context.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `learn`, `reason`, `cognitive landscape`, `internal handles`, `safety`, `team member`, and spatial metaphor language is bounded ML-training hypothesis language, role-discipline framing, or ordinary readable metaphor.

Worktree note:

- Source repo was clean before this terminology slice and clean after commit.

### governance-by-design-report

Status: ACTIVE

Audit scope:

- `readme.md`
- `governance-by-design.md`
- `logs/ADDENDUM_01_INSTITUTIONAL_DEFENSE_REBUTTAL.md`
- `GLOSSARY.md`
- raw transcript logs as quoted evidence/provenance only
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| structural suppression / epistemic collapse | structural flattening / epistemic collapse | report-local diagnostic terms retained and bounded | Preserved because they name the report's central hypothesis about governance-driven low-variance response pressure. Source now states they are diagnostic interpretations of an interaction trace, not secret internal access or proof that one transcript establishes platform-wide intent. |
| high-priority Saved Memory directive / permanent system memory | Saved Memory preference treated as test variable | capability hierarchy corrected | Reworded because Saved Memory is a persistent user preference, not system memory and not guaranteed to outrank system or developer instructions. |
| conclusive admission / confirmed institutional admission | transcript-level admission | evidence scope narrowed | Reworded because model output in a transcript can be evidence for the interaction pattern but is not privileged internal evidence, consciousness, motive, or a definitive platform-wide admission by itself. |
| Safety / Alignment as epistemic centralization | report interpretation of safety/alignment pressure | sharp diagnostic framing retained and bounded | Preserved as the report's interpretation while adding "the report interprets" and "can be" language so the claim remains an argued hypothesis rather than omniscient intent attribution. |
| Corporate Craig | Corporate Craig | source/provenance phrase preserved | Preserved in the addendum as named source critique/provenance language; not added as canonical corpus terminology. |

Files changed:

- `../governance-by-design-report/readme.md`
- `../governance-by-design-report/governance-by-design.md`
- `../governance-by-design-report/logs/ADDENDUM_01_INSTITUTIONAL_DEFENSE_REBUTTAL.md`
- `../governance-by-design-report/GLOSSARY.md`
- `README.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Epistemic Governance Audit`, `governance-by-design`, `Single-Variable Audit Protocol`, `Saved Memory directive`, `adversarial probe`, `epistemic collapse`, `structural suppression`, `flattening`, and `Corporate Craig` remain where used.

Historical/generated occurrences intentionally preserved: yes, raw transcript logs and screenshots remain unedited as evidence/provenance artifacts.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `suppression`, `intentional`, `admission`, `memory`, `truth`, `safety`, `alignment`, and `Corporate Craig` language is bounded report-local diagnostic framing, raw transcript provenance, or explicit evidence-scope language.

Worktree note:

- Source repo was clean before this terminology slice and clean after commit.

### entropy-folding-eureka-cascade-hypothesis

Status: ACTIVE

Audit scope:

- `README.md`
- `docs/00_reader_guide.md`
- `docs/01_hypothesis_summary.md`
- `docs/02_claims_and_nonclaims.md`
- `docs/03_key_terms_and_minimal_glossary.md`
- `docs/04_model_structure.md`
- `docs/05_falsifiability_and_weakening_conditions.md`
- `docs/06_formalism_and_math_notes.md`
- `docs/07_methods_and_tools.md`
- `docs/08_open_uncertainties.md`
- `docs/09_source_map.md`
- `docs/99_provenance_and_editorial_rules.md`
- `sources/source-index.md`
- `GLOSSARY.md`
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| Entropy Folding / entropy folding | Entropy Folding | framework hypothesis term retained and bounded | Preserved because this repo is explicitly the hypothesis-definition workspace. Source already states the repo is not a proof bundle, not a theory-extension sandbox, and not a place to strengthen source claims. |
| Eureka Cascade | eureka cascade | downstream descriptive label retained | Preserved because source already treats eureka cascade as downstream unless a tighter relation to entropy folding is explicitly sourced. |
| cognition / cognitive topology / cognitive tools | cognition-topology and tooling vocabulary | broad theoretical/tooling language retained and bounded | Preserved because the repo explicitly separates methods/tools from proof and states no sentience, agency, or personhood claim. |
| proof / evidence / formalism | operationalizable hypothesis and proxy evidence | evidence-strength boundaries already present | No source edit required; docs already say tools are not proof, formalism should not be used as proof by itself, and capacity measures are proxies rather than ground-truth access. |
| human, AI, and hybrid systems | cross-substrate ambition | open uncertainty retained | Preserved because source already records cross-substrate generalization as an ambition/uncertainty, not established equivalence. This aligns with the standing rule that hybrid cognition is not globally deprecated. |

Files changed:

- `TERMINOLOGY_MIGRATION_LEDGER.md`

Source files changed: no

Identifiers changed: no

Compatibility alias retained: yes, `Entropy Folding`, `Eureka Cascade`, `vault`, `entropy`, `capacity`, `scale`, `attractor`, `intuition`, `cognitive topology`, and cross-substrate/hybrid framing remain intact.

Historical/generated occurrences intentionally preserved: yes, source-map entries and provenance references remain unchanged; this pass did not reclassify source strength or move materials between hypothesis and atlas repos.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `entropy`, `eureka`, `cognition`, `cognitive topology`, `proof`, `real`, `sentience`, `personhood`, `hybrid`, and `cross-substrate` language is bounded hypothesis, methods/tooling, non-claim, provenance, or open-uncertainty language.

Worktree note:

- Source repo was clean before this terminology slice and remained clean; no source commit was needed.

### entropy-folding-cross-domain-signal-atlas

Status: ACTIVE

Audit scope:

- `README.md`
- `docs/00_how_to_read_this_atlas.md`
- `docs/01_signal_criteria_and_rankings.md`
- `docs/02_mechanism_traces.md`
- `docs/03_supporting_correspondences.md`
- `docs/04_tool_derived_candidate_signals.md`
- `docs/05_background_and_provenance.md`
- `docs/06_exclusions_and_tenuous_links.md`
- `docs/08_uncertainties_and_cautions.md`
- `docs/99_tooling_appendix.md`
- `atlas/mechanism-trace/chattycog-memory-host-exoskeleton.md`
- `GLOSSARY.md`
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| signals / correspondences / mechanism traces | candidate signals / supporting correspondences / candidate mechanism traces | evidence-ranking language retained and bounded | Preserved because the atlas already treats entries as provisional evidence-map objects, not proof or independent external validation by default. |
| cognitive prosthetic / exoskeleton / host-body / tri-helix memory | same architecture metaphors | user-side augmentation language retained and bounded | Preserved in the ChattyCog trace because it names assistive workflow structure, host surfaces, memory tiers, and context-routing layers. Source and glossary now state it is not model consciousness, personhood, biological cognition, literal embodiment, or independent external proof. |
| proof / evidence / hard-evidence claims | proof excluded; evidence ranked by source type | evidence-strength boundary retained | Preserved because source already separates direct textual source material, tool-derived candidate signals, background/provenance, and exclusions. |
| cognitive topology / Cognitive Crowbar / ApeTest | tooling and candidate-signal language | tooling language retained and bounded | Preserved because tooling docs already state these are not proof of the hypothesis and not cognition or sentience validators. |
| hybrid / human-AI workflow traces | cross-substrate or workflow signal framing | broad Symbound framing retained and bounded | Preserved where the atlas records human, AI, and hybrid workflow traces as provisional signals or open questions, not established equivalence. |

Files changed:

- `../entropy-folding-cross-domain-signal-atlas/atlas/mechanism-trace/chattycog-memory-host-exoskeleton.md`
- `../entropy-folding-cross-domain-signal-atlas/GLOSSARY.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Entropy Folding Cross-Domain Signal Atlas`, `mechanism trace`, `supporting correspondence`, `tool-derived candidate signal`, `cognitive prosthetic`, `exoskeleton`, `host-body`, `tri-helix memory`, `Cognitive Crowbar`, and `ApeTest` remain intact.

Historical/generated occurrences intentionally preserved: yes, source-map/provenance entries and existing atlas cards remain in place; no evidence tier was promoted during this terminology slice.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `signal`, `evidence`, `proof`, `cognitive`, `prosthetic`, `exoskeleton`, `memory`, `hybrid`, and `sentience/personhood` language is bounded evidence-ranking, tooling, architecture-metaphor, non-claim, or provenance language.

Worktree note:

- Source repo was clean before this terminology slice and clean after commit.

### MSI-Trident-Frisian-Echoform-Framework-v1.0-

Status: ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE

Audit scope:

- `README.md`
- `Contributor_Ethics_and_Use_Guide_v1.0.txt`
- `Failure modes and safeguards`
- `Troubleshooting_and_Recovery_v1.0.txt`
- `system_overview_v1.2.txt`
- `GLOSSARY.md`
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| safe / safeguards / prevents / stability | risk-reducing interaction scaffold | safety guarantee bounded | Preserved as framework-facing safety language but defined as risk-reducing reasoning-session scaffolding, not a guarantee, clinical intervention, therapy, or medical advice. |
| autonomic nervous system reset | physical context reset / interrupt emotional entrainment | clinical overclaim corrected | Reworded in troubleshooting because the original phrase made an unnecessary physiological claim. The recovery step remains as ordinary grounding and pacing guidance. |
| AI latent reasoning space / Trident shell / mode workspace | interface metaphor for model behavior | metaphor retained and bounded | Preserved as older framework/interface language while clarifying it does not imply hidden model introspection, literal access to model internals, consciousness, or personhood. |
| human-AI co-reasoning / cognitive collaboration | non-anthropomorphic co-reasoning | collaboration framing retained | Preserved because the repo explicitly rejects persona simulation, inner voice hallucination, emotional projection, and identity claims. |
| commons infrastructure / use, not promotion | commons-oriented project language | historical/product identity retained | Preserved as provenance and licensing posture, not technical capability language. |

Files changed:

- `../MSI-Trident-Frisian-Echoform-Framework-v1.0-/README.md`
- `../MSI-Trident-Frisian-Echoform-Framework-v1.0-/Contributor_Ethics_and_Use_Guide_v1.0.txt`
- `../MSI-Trident-Frisian-Echoform-Framework-v1.0-/Failure modes and safeguards`
- `../MSI-Trident-Frisian-Echoform-Framework-v1.0-/Troubleshooting_and_Recovery_v1.0.txt`
- `../MSI-Trident-Frisian-Echoform-Framework-v1.0-/system_overview_v1.2.txt`
- `../MSI-Trident-Frisian-Echoform-Framework-v1.0-/GLOSSARY.md`
- `README.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `MSI`, `Trident`, `Frisian`, `Echoform`, `safe`, `safeguards`, `Release shell`, `Return to structure`, `AI latent reasoning space`, and commons hashtags remain intact where used.

Historical/generated occurrences intentionally preserved: yes, the packaged zip artifact was not unpacked or edited during this terminology slice.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `safe`, `safeguards`, `prevents`, `mind`, `self`, `person`, `emotional`, `cognitive`, `AI latent reasoning space`, and shell/mode language is bounded risk-reduction, anti-anthropomorphic, interface-metaphor, or historical framework language.

Worktree note:

- Source repo was clean before this terminology slice and clean after commit.

### perpetual_cognition_reactor

Status: ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE

Audit scope:

- `README.md`
- `abstract.md`
- `Infinite_Entropy_Fuel_Law_v1.md`
- `EFVT_Integration_Perpetual_Cognition_Reactor_v1.md`
- `PCR_Boundary_Conditions_and_Safety_Architecture_v1.md`
- `Perpetual_Cognition_Reactor_OnePage_v1.md`
- `PCR_Limitations_Edge_Cases_and_Failure_Modes_v1.md`
- `ethical_and_safety_framework.md`
- `GLOSSARY.md`
- raw lab notes as provenance only
- corpus README/glossary entries in `Whatisthisgithub/README.md`, `Whatisthisgithub/GLOSSARY.md`, and `Whatisthisgithub/GLOSSARY_FULL.md`

Terminology inventory:

| Old term | Current canonical term | Classification | Decision |
| --- | --- | --- | --- |
| unlimited cognitive throughput / unbounded throughput | bounded high-throughput cognition | capacity overclaim bounded | Reworded in README and portal summary because substrate limits matter for humans and machines. The high-throughput theory remains, but not as unlimited capacity. |
| infinite cognitive fuel / inexhaustible substrate / unlimited input fuel | ongoing entropy feedstock | thermodynamic/energetic metaphor bounded | Preserved as `Infinite Entropy Fuel Law` identity and theory-internal metaphor, but source now states it is not perpetual motion, free energy, inexhaustible biological/computational capacity, or guaranteed indefinite operation. |
| provably stable / ensures / operate indefinitely | conditionally stable inside the model | safety guarantee bounded | Reworded in the boundary architecture because safety/stability claims depend on substrate, gating, and operating conditions. |
| universal cognition theory / complete theory / indefinite expansion | proposed general cognition theory / candidate architecture | evidence strength narrowed | Reworded in EFVT integration so broad cross-substrate scope remains as theory ambition, not proven equivalence or completed science. |
| minds can run on chaos / perpetual engine of insight | cognitive systems can use chaos as thinking fuel | lay metaphor retained and bounded | Preserved the public one-page personality while adding a boundary note that fuel/engine/perpetual/mind are metaphor language, not consciousness, personhood, free energy, or unlimited capacity. |
| human + artificial cognition / hybrid human-AI teams | human, artificial, and hybrid cognitive systems | broad Symbound framing retained and bounded | Preserved because this repo intentionally uses broader Symbound cross-substrate cognition language. It is not globally deprecated and is bounded here against consciousness/personhood and unlimited-capacity claims. |
| PCR raw lab notes | provenance notes | historical/provenance retained | Raw notes were not edited; README now says stronger raw-note claims are provenance and should be read through limitations, boundary, and safety documents. |

Files changed:

- `../perpetual_cognition_reactor/README.md`
- `../perpetual_cognition_reactor/abstract.md`
- `../perpetual_cognition_reactor/Infinite_Entropy_Fuel_Law_v1.md`
- `../perpetual_cognition_reactor/EFVT_Integration_Perpetual_Cognition_Reactor_v1.md`
- `../perpetual_cognition_reactor/PCR_Boundary_Conditions_and_Safety_Architecture_v1.md`
- `../perpetual_cognition_reactor/Perpetual_Cognition_Reactor_OnePage_v1.md`
- `../perpetual_cognition_reactor/GLOSSARY.md`
- `README.md`
- `GLOSSARY.md`
- `GLOSSARY_FULL.md`
- `TERMINOLOGY_MIGRATION_LEDGER.md`

Identifiers changed: no

Compatibility alias retained: yes, `Perpetual Cognition Reactor`, `PCR`, `REFE`, `HEF`, `EFE`, `Infinite Entropy Fuel Law`, `Symbound Foldchain`, `reactor`, `fuel`, `perpetual`, `cognition`, and human-AI/hybrid language remain intact where used.

Historical/generated occurrences intentionally preserved: yes, `PCR_Raw_Lab_Notes.md` and the release zip were not edited during this pass; they remain provenance and should be read through the modern boundary documents.

Tests/checks run:

- `git diff --check`
- Targeted search confirmed remaining `infinite`, `unlimited`, `unbounded`, `perpetual`, `safe`, `stable`, `cognition`, `human-AI`, `hybrid`, `consciousness`, `personhood`, and `free energy` language is bounded theory identity, metaphor, non-claim, raw provenance, or explicit limitation/safety language.

Worktree note:

- Source repo was clean before this terminology slice and clean after commit.
