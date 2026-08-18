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
| 18 | cognition-mesh-test-chamber | ACTIVE | Current model suitability test harness; fingerprinting terms likely candidates. |
| 19 | llm-defined-persistent-memory | ACTIVE | Current memory architecture docs. |
| 20 | Symbound_Academia_Spine | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Repo brand includes legacy-style "Spine"; inspect before renaming. |
| 21 | semantic-signal-alphabet | ACTIVE | Foundational/current framework. |
| 22 | MemorySpine | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Repo brand includes legacy-style "Spine"; active parser project. |
| 23 | historical-janet-school-exploratory-build | ACTIVE BUT HISTORICAL/COMPATIBILITY-SENSITIVE | Name and description mark historical prototype. |
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
| cognitive fingerprinting | behavioural suitability profiling | canonicalized | Portal guidance and generated active description now use behavioural profiling; old term retained only as glossary alias. |
| constraint-metabolization / metabolise constraints | constraint promotion / promote reusable constraints | canonicalized | Portal-facing implementation language now distinguishes EF theory metaphor from software implementation description. |
| theory spine / hypothesis spine | theory entry point / theory framework | canonicalized | Curated visitor guidance did not require metaphor. |
| human-AI cognition | human-AI systems | canonicalized | Corpus-level statement now avoids over-claiming cognition where systems language is clearer. |
| cognitive infrastructure | human-AI infrastructure | canonicalized | Corpus-level statement now uses systems language. |
| RD Engine doctrine spine | RD Engine doctrine | legacy alias | Glossary keeps source wording as alias but marks "spine" as non-preferred current technical language. |
| Cognitive fingerprinting | Behavioural suitability profiling | legacy alias | Glossary row renamed to current term and old label retained as alias/provenance. |
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

- `janet-school`, `project-leviathan`, `ef-engine`, and `cognition-mesh-test-chamber` need repo-local audits before deeper identifier or README changes.
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
| gold standard / real mind | biological reference class | canonicalized | Human cognition remains the reference class without turning the taxonomy into an anthropomorphic ranking. |
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
- `node scripts/generate-seo.mjs` in `instance001.github.io`

Unresolved terminology questions:

- Live GitHub repository description should eventually be updated so the `Cognition-Scale-Formal-Taxonomy` override can be removed.
- A deeper manuscript-version migration could separately modernize the full-edition `.txt` and checklist artifacts; this pass kept them as formal/provenance surfaces.

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
