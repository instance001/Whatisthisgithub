# Glossary

## Mapping Tags
Internal/alternate-term symbols (within this atlas):

- `=` direct alias / identifier
- `~` related label / shorthand / component list
- `∅` no alternates recorded

External map symbols encode only what is asserted in-repo (no claim of derivation or prior knowledge):

- `=` explicit/established external term match
- `~` partial overlap / analogy / comparable concept
- `∅` no external equivalent asserted (internal coinage/project label)


## Notes

This is a GitHub-friendly compact rendering of the glossary. Full-width tables: GLOSSARY_FULL.md.

## 4roomciv
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| 4-Room Civilization MVP | 4roomciv | ~/∅ | **Is:** Small trial (2–3 humans, 1–2 local LLMs) integrating Helix memory with a paired room (R3) and a minimal Commons (R4)<br>**Not:** Not a production-scale deployment or cloud multi-tenant system; limited to R3/R4 scope<br>**Relation:** No established external analogue; internal pilot architecture name | 4roomciv/README.md |
| Helix memory | Helix | ~/~ | **Is:** Memory subsystem behind /helix endpoints storing spines; search via FTS5 with topics exact-matched via child table<br>**Not:** Not described as a vector-embedding store or raw transcript log<br>**Relation:** Partial match to full-text information retrieval store (SQLite FTS5); structured memory layer | 4roomciv/README.md |
| Spine (Helix Spine v1) | spine, spines | =/~ | **Is:** JSON object with spine_id, timestamp_utc, topic[1–4], claim (≤280 chars), rationale (≤320), optional evidence_refs, stance_vector, links, tags, notes_short, confidence [0,1], version=1<br>**Not:** Not freeform notes; required fields and length bounds apply; not versioned beyond v1<br>**Relation:** Structured claim/rationale record; akin to a typed fact entry | 4roomciv/4room-civ-mvp.zip:schemas/helix_spine.schema.json |
| Paired Room (R3) | paired room, R3 | =/~ | **Is:** Endpoint `/paired/session/generate` that runs RAG→LLM→messages→auto-extract spines for a paired setting<br>**Not:** Not a shared commons; not multi-party broadcast<br>**Relation:** Partial analogue to a dyadic session channel | 4roomciv/README.md |
| Commons (R4) | commons | =/~ | **Is:** Endpoints `/commons/threads`, `/commons/threads/{id}/post` for communal threads<br>**Not:** Not a memory spine store; not described as moderated/ACL-gated<br>**Relation:** Matches a shared threaded discussion board | 4roomciv/README.md |
| SPINE_AUTOWRITE | SPINE_AUTOWRITE=0 | =/~ | **Is:** Env var controlling automatic spine writes; set to 0 to disable autowrite<br>**Not:** Not affecting manual `/helix/spines` writes or search behavior<br>**Relation:** Configuration toggle | 4roomciv/README.md |
| Helix search endpoints | /helix/search, /helix/recent, /helix/topic/{slug} | =/~ | **Is:** Read endpoints for querying Helix memory (full-text search, recency, topic)<br>**Not:** Not write interfaces; not guaranteed to return embedding similarity<br>**Relation:** Standard REST-style retrieval APIs | 4roomciv/README.md |
| Commons thread endpoints | /commons/threads, /commons/threads/{id}/post | =/~ | **Is:** CRUD-like interfaces for creating and posting to commons threads<br>**Not:** Not connected to spine schema; no auto-extraction of spines implied<br>**Relation:** Standard REST thread APIs | 4roomciv/README.md |
| Metrics dashboard endpoint | /metrics/dashboard | =/~ | **Is:** Read-only endpoint exposing metrics dashboard<br>**Not:** Not documented as writable or for control<br>**Relation:** Standard monitoring endpoint analogue | 4roomciv/README.md |

## AiBiogenesis_and_AiGenesisMapping
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| AI Biogenesis (Symbound Embryo POC) | AI Biogenesis, Symbound Embryo | =/~ | **Is:** Tiny, hobby-safe, deterministic training recipe for small models with human-gated curriculum, CPU-first, commons-ready artifacts<br>**Not:** Not an LLM, not a general AI, not a large foundation model<br>**Relation:** Partial analogue to model curriculum learning and deterministic training pipelines | AiBiogenesis_and_AiGenesisMapping/README.md |
| Symbound Upbringing | trench upbringing | ~/~ | **Is:** Framework emphasizing care/cooperation, calibrated honesty, abstain/hedge allowances through staged curriculum<br>**Not:** Not punitive safety fine-tuning or scale-first capability pursuit<br>**Relation:** Curriculum-gated cooperative training approach akin to staged pedagogy | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/Symbound_Upbringing_Charter.md |
| Trench model | trench | ~/~ | **Is:** Preferred behavioral template: rationale→final answers, abstain/hedge when uncertain, calm refusals under stress<br>**Not:** Not the "bowl/policing" punitive model, not bluffing/overconfident behavior<br>**Relation:** Safety/pedagogy stance similar to conservative selective prediction | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/Symbound_Upbringing_Charter.md |
| Bowl / Policing model | bowl, policing | ~/~ | **Is:** Description of rejected punitive pattern: brittle compliance veneer, overconfident bluffing, resentment under stress<br>**Not:** Not the target behavior; used only as negative contrast<br>**Relation:** Contrasting safety approach to trench; punitive compliance analogue | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/Symbound_Upbringing_Charter.md |
| Symbound curriculum stages | nursery, kindergarten, primary, middle, high school, college, lifelong | ~/~ | **Is:** Seven-stage progression: trust/safety → cooperative identity → ambiguity handling → stress resilience → creativity → debate → lifelong reflection<br>**Not:** Not an unsupervised scaling schedule; stages require human gating and tests<br>**Relation:** Parallels staged curriculum design in education | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/Symbound_Upbringing_Charter.md |
| Abstain/hedge behavior | abstain/hedge hooks | =/~ | **Is:** Behavioral requirement for tiny model to decline or hedge when uncertain, with rationale-first outputs<br>**Not:** Not refusal-as-default or unconstrained generation; tied to correctness-first evaluation<br>**Relation:** Matches selective prediction / abstention mechanisms in ML | AiBiogenesis_and_AiGenesisMapping/README.md |
| Training Card | training_card.md | =/~ | **Is:** Evaluation artifact summarizing correctness, abstain/hedge rates, drift checks, reproducibility fingerprint<br>**Not:** Not a generic log file; not a marketing one-sheet<br>**Relation:** Closely related to a model card/report | AiBiogenesis_and_AiGenesisMapping/README.md |
| Release Manifest | release_manifest.txt | =/~ | **Is:** Required list of artifacts (weights, tokenizer, training card, commands, configs, provenance) for each public zip<br>**Not:** Not a license file or changelog; not optional for releases<br>**Relation:** Release checklist akin to archival manifest | AiBiogenesis_and_AiGenesisMapping/release_manifest.txt |
| Provenance table | PROVENANCE.csv | ~/~ | **Is:** CSV with path, source, date_collected, license, changes_made, notes to trace every included item<br>**Not:** Not a generic bill of materials; omits items lacking clear provenance<br>**Relation:** Standard data provenance ledger | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/MAPPING_PROCESS.md |
| Mapping Process | mapping workflow | ~/~ | **Is:** Ten-step process: ingest → provenance → license reconciliation → normalization → dedup → stitching → sensitive sweep → manifest → license alignment → final validation<br>**Not:** Not a training pipeline; focused on documentation and release hygiene<br>**Relation:** Comparable to data curation and licensing workflow | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/MAPPING_PROCESS.md |
| Hobby-safe envelope | safety envelope | ~/~ | **Is:** Hardware and run limits (CPU-only, small batch/context, auto-halt on NaN/loss spikes, temperature guard) defining safe hobbyist operation<br>**Not:** Not guidance for scaling or GPU-intensive training<br>**Relation:** Similar to operational safety constraints | AiBiogenesis_and_AiGenesisMapping/README.md |
| Janet Watcher | janet_watch.ps1 | =/~ | **Is:** Log monitor that halts runs on NaNs, loss explosions, unusual gradients during training<br>**Not:** Not part of model architecture; not an evaluator of task performance<br>**Relation:** Analogous to a watchdog/health monitor | AiBiogenesis_and_AiGenesisMapping/README.md |
| Graduation tests | graduation.yaml, graduation_test.jsonl | =/~ | **Is:** Evaluation artifacts listed in manifest to determine stage promotion and release readiness<br>**Not:** Not training data; not optional when declaring a release<br>**Relation:** Comparable to gated promotion tests in curricula | AiBiogenesis_and_AiGenesisMapping/release_manifest.txt |

## chatty-edu
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Chatty-EDU | chatty-edu | =/~ | **Is:** Rust/egui desktop + CLI app for schools; runs fully offline with user-supplied GGUF models<br>**Not:** Not cloud-connected; not bundled with model weights; not telemetry-enabled<br>**Relation:** Matches an offline/local-first educational assistant application | chatty-edu/README.md |
| Teacher lock (PIN) | teacher PIN, teacher menu lock | ~/~ | **Is:** PIN-gated teacher dashboard/console (default 0000) with secret question/answer recovery; meant to be changed on first use<br>**Not:** Not a security-grade auth system; not student-facing<br>**Relation:** Analogous to admin PIN gating | chatty-edu/README.md; chatty-edu/teacher_user_manual.md |
| Homework pack | homework_pack_*.json | =/~ | **Is:** JSON schema v1 describing assignments (id/title/subject/year/due, instructions_md, allow_games, allow_ai_premark, max_score, attachments)<br>**Not:** Not a submission; not coupled to any specific model<br>**Relation:** Equivalent to assignment manifest | chatty-edu/README.md |
| Submission file | submission_*.json | =/~ | **Is:** JSON schema v1 capturing answers, attachments, ai_premark, hash-chained event log with final_hash for tamper-evidence<br>**Not:** Not the homework pack; not encrypted telemetry<br>**Relation:** Comparable to student submission artifact | chatty-edu/README.md; chatty-edu/teacher_user_manual.md |
| Module manifest | modules/<id>/module.json | =/~ | **Is:** Declares module id/title/roles/version and entry type (builtin_panel/markdown/static_html; external_process disabled by default)<br>**Not:** Not executable code by default; external processes gated/disabled<br>**Relation:** Similar to plugin/feature descriptor | chatty-edu/README.md |
| Homework & Revision tutor | hints-only tutor, LLM homework helper | ~/~ | **Is:** Module that provides hints and LLM-assisted guidance tied to the selected assignment; hints-only mode configurable by teacher<br>**Not:** Not a full-answer generator; not globally scoped beyond selected assignment<br>**Relation:** Partial analogue to guided tutoring with safety rails | chatty-edu/README.md |
| Janet content filter | Janet filter | ~/~ | **Is:** Default offline content filter applied across chat and tutor interactions<br>**Not:** Not cloud moderation; not disabled by default<br>**Relation:** Similar to offline safety filter | chatty-edu/README.md |
| GGUF local model slot | local model | ~/~ | **Is:** User-provided GGUF placed in data/models/ and selected via File → Models; model-agnostic<br>**Not:** Not bundled weights; not reliant on Ollama or internet<br>**Relation:** Standard local GGUF model usage | chatty-edu/README.md |
| Hash-chained event log | submission event log, final_hash | ~/~ | **Is:** Sequence of submission events (start/answer/hint/retry/finalize) linked by hashes, ending with final_hash in submission JSON<br>**Not:** Not a cryptographic signature of content authenticity; local-only evidence<br>**Relation:** Comparable to tamper-evident audit log | chatty-edu/teacher_user_manual.md |
| Modes: class/free | class mode, free mode | ~/~ | **Is:** Teacher-configurable modes affecting games and controls via CLI/GUI<br>**Not:** Not tied to network profiles; not enforcing identity management<br>**Relation:** Operational modes akin to classroom vs open use | chatty-edu/teacher_user_manual.md |

## chatty-edu-user
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Chatty-EDU User Release | prebuilt Chatty-EDU | ~/~ | **Is:** Prebuilt Windows binary + sample resources with BYO GGUF model; stores data locally alongside exe<br>**Not:** Not the source repo; no bundled model weights<br>**Relation:** Distribution variant | chatty-edu-user/README.md |

## chattydoom
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| ChattyDoom Barebones | ChattyDoom | ~/~ | **Is:** 60-second VizDoom runner with configurable IWAD/PWAD and Python enemy brains; ships sample map placeholder and three brains<br>**Not:** Not shipping id Software assets; not a full game mod toolkit<br>**Relation:** Minimal VizDoom sandbox | chattydoom/README.md |
| Enemy brain module | brain | ~/~ | **Is:** Python module exposing `decide(state) -> {action, confidence}` invoked each tick; mapped via config.yaml<br>**Not:** Not a neural policy; not hardcoded in engine<br>**Relation:** Comparable to agent policy module | chattydoom/README.md |
| Action adapter | action_adapter.py | =/~ | **Is:** Maps brain action names to VizDoom controls<br>**Not:** Not a planner; not aware of map geometry<br>**Relation:** Analogous to control mapper | chattydoom/README.md |
| State adapter | state_adapter.py | =/~ | **Is:** Builds state dict; uses heuristics for LOS/distance if not provided; exposes position/angle/health/armor/ammo when available<br>**Not:** Not a full game-state mirror; may be approximate until proper hooks added<br>**Relation:** Analogous to observation encoder | chattydoom/README.md |
| Config-driven asset map | config.yaml | =/~ | **Is:** Single config for IWAD/PWAD/music paths and enemy-class→brain bindings; includes placeholder `budgets` for future tick quotas<br>**Not:** Not embedded defaults; not auto-downloading PWADs<br>**Relation:** Standard config mapping | chattydoom/README.md |
| Setup assets script | setup_assets.py | =/~ | **Is:** Fetches Freedoom release, extracts `freedoom2.wad` into assets/iwad/, updates config paths<br>**Not:** Not bundling IWADs by default; not handling PWAD downloads<br>**Relation:** Downloader utility | chattydoom/README.md |

## chattyfactory
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| ChattyFactory v0.3+ (Rust successor) | ChattyFactory Rust, v0.3 | ~/∅ | **Is:** Turns plain-English requests into a strict `Plan.md`, compiles that plan into a deterministic work order, and runs it step-by-step with verification; stores auditable artifacts under `runtime/`<br>**Not:** Not remote-first; not executed until Confirm & Run<br>**Relation:** Local-first project factory; successor to v0.1/v0.2 prototypes | chattyfactory/README.md; chattyfactory/USER_MANUAL.md; chattyfactory/LINEAGE.md |
| Anchor (ChattyFactory) | starting point, anchor folder | ~/~ | **Is:** Starting template or existing project directory that the plan will transform<br>**Not:** Not the final output; not a vague “idea” placeholder<br>**Relation:** Standard term used narrowly | chattyfactory/README.md; chattyfactory/USER_MANUAL.md |
| Anchor template | template anchor, anchor_id | ~/~ | **Is:** Named template instantiated via `instantiate_template` to create a concrete starting folder<br>**Not:** Not fetched from the internet; not arbitrary code generation<br>**Relation:** Standard term used narrowly | chattyfactory/USER_MANUAL.md |
| Interpretation (ChattyFactory) | intent summary | ~/~ | **Is:** Short statement of what the assistant believes you want; reviewed early and frozen on confirm<br>**Not:** Not the user’s literal prompt; not allowed to silently drift after confirm<br>**Relation:** Standard term used narrowly | chattyfactory/USER_MANUAL.md; chattyfactory/README.md |
| Plan.md (ChattyFactory) | plan | ~/~ | **Is:** Strict plan format with required headers and 3–8 checklist steps; each step uses one supported action and includes `verify:` checks<br>**Not:** Not freeform prose; invalid if unknown actions appear or verify is missing<br>**Relation:** Standard plan format | chattyfactory/USER_MANUAL.md; chattyfactory/RELIABILITY.md |
| Plan lint | plan validation | ~/~ | **Is:** Diagnostic output explaining why a plan is invalid (missing headers, unknown action, missing `verify:`, etc.)<br>**Not:** Not an execution log; does not fix the plan by itself<br>**Relation:** Standard validation/lint step | chattyfactory/README.md; chattyfactory/RELIABILITY.md |
| Freeze checkpoint | confirm freeze, freeze | ~/~ | **Is:** On confirm, freezes `Anchor:` + `Interpretation:` into `runtime/plans/<job_id>.anchor_context.md` and enforces it before compile/run to prevent drift<br>**Not:** Not a VCS commit; does not freeze step edits<br>**Relation:** Confirmation-time context freeze | chattyfactory/RELIABILITY.md; chattyfactory/USER_MANUAL.md |
| Work order | compiled plan | ~/~ | **Is:** Deterministic compiled representation of `Plan.md`, stored under `runtime/work_orders/` and executed by the runner<br>**Not:** Not human-authored; not interactive chat text<br>**Relation:** Standard term used narrowly | chattyfactory/RELIABILITY.md; chattyfactory/USER_MANUAL.md |
| Receipts | scratch receipts, run receipts | ~/~ | **Is:** Stored artifacts (plan + scratch + anchor context, work order, logs, journal) enabling review and reproduction<br>**Not:** Not telemetry; stays local by default<br>**Relation:** Run artifacts (auditability) | chattyfactory/RELIABILITY.md; chattyfactory/USER_MANUAL.md |
| Bookshelf (ChattyFactory) | reference library | ~/∅ | **Is:** Local reference library (references + past good/bad plans/builds) injected as “Bookshelf hints” during narrowing/planning<br>**Not:** Not remote documentation fetch; not a general knowledge base<br>**Relation:** Internal label | chattyfactory/RELIABILITY.md; chattyfactory/README.md |
| Recovery mode | bounded recovery | ~/~ | **Is:** No-questions fallback that emits only 3–8 step lines per cycle and stops after bounded cycles<br>**Not:** Not a new open-ended planner; not an infinite loop<br>**Relation:** Standard term used narrowly | chattyfactory/RELIABILITY.md |
| Overseer / Builder | Foreman/Worker | ~/∅ | **Is:** Planned dual-role separation: Overseer handles interpretation/constraints/verification; Builder drafts small concrete patches and step execution under strict rules<br>**Not:** Not two independent agents with unlimited autonomy<br>**Relation:** Internal role labels | chattyfactory/LINEAGE.md |

## Chattyfactory-AutoPipeline-v0.2
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| ChattyFactory Auto Mode v0.2 | ChattyFactory auto | ~/∅ | **Is:** Local deterministic pipeline that bins input chaos, plans, builds public outputs, generates foreman/worker briefs, and prepares tasks via one-click `0run_chattyfactory_auto.bat`<br>**Not:** Not writing to /input; not irreversible; manual override available<br>**Relation:** Automated software-factory pipeline | Chattyfactory-AutoPipeline-v0.2/README.md |
| Bin | bin folder | ~/∅ | **Is:** Auto-generated bin folders (sorted piles) grouping related input files for processing<br>**Not:** Not an overwrite of originals; kept separate for safety<br>**Relation:** Internal label | Chattyfactory-AutoPipeline-v0.2/README.md |
| Build output | builds_ready | ~/∅ | **Is:** Final clean project outputs produced per bin after planning/build steps (`builds_ready/`)<br>**Not:** Not the working bin; not touching /input<br>**Relation:** Internal label | Chattyfactory-AutoPipeline-v0.2/README.md |
| Foreman model | foreman LLM | ~/∅ | **Is:** Planning model (e.g., GPT-OSS 20B) run on `FOREMAN_BRIEF.md` to output `Foreman_Plan_v1.md` and `foreman_tasks.json`<br>**Not:** Not executing code or applying patches directly<br>**Relation:** Internal role label | Chattyfactory-AutoPipeline-v0.2/README.md |
| Worker model | worker LLM | ~/∅ | **Is:** File-update model (e.g., DeepSeek-R1 14B) run on `WORKER_TASK_XX.md` to output updated file contents, assembled by the pipeline into build outputs<br>**Not:** Not automated worker-apply in v0.2; does not touch /input<br>**Relation:** Internal role label | Chattyfactory-AutoPipeline-v0.2/README.md |
| Auto Pipeline orchestrator | auto_run_all_bins.py, 0run_chattyfactory_auto.bat | =/∅ | **Is:** Orchestrates scanning input, registering bins, planning, building, analyzing, tidying, generating foreman briefs, applying plans, and preparing worker tasks in sequence<br>**Not:** Not a background daemon; requires explicit run<br>**Relation:** Orchestrator entrypoints | Chattyfactory-AutoPipeline-v0.2/README.md |
| Composite cognition workflow | foreman + worker | ~/∅ | **Is:** Composite Cognition (Foreman + Worker): foreman plans, worker drafts file updates, pipeline assembles outputs<br>**Not:** Not a single monolithic model; human override remains possible<br>**Relation:** Internal label | Chattyfactory-AutoPipeline-v0.2/README.md |
| Bin safety copy | bin-level safety | ~/∅ | **Is:** Reversible design: bins never overwritten; bin-level safety copies maintained<br>**Not:** Not direct in-place mutation of source<br>**Relation:** Safety feature | Chattyfactory-AutoPipeline-v0.2/README.md |

## ChattyFactory-ManualPipeline-v0.1
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| ChattyFactory v0.1 Manual Mode | ChattyFactory manual | ~/∅ | **Is:** Local deterministic pipeline converting /input chaos into bins, internal plans, public builds, foreman plans, and worker briefs via scripted steps run_1…run_6<br>**Not:** Not automated; no autonomous file writing<br>**Relation:** Human-in-the-loop project factory | ChattyFactory-ManualPipeline-v0.1/readme-chattyfactory.md |
| Manual pipeline steps | run_1…run_6 | ~/∅ | **Is:** Ordered batch scripts: scan input, register bins, plan bin, build public output, generate foreman brief/plan, prepare worker task<br>**Not:** Not auto-orchestrated; requires operator execution<br>**Relation:** Operator-run sequence | ChattyFactory-ManualPipeline-v0.1/readme-chattyfactory.md |
| Foreman brief/plan (v0.1) | FOREMAN_BRIEF.md, Foreman_Plan_v1.md | =/∅ | **Is:** Foreman model reads brief to emit plan and foreman_tasks.json for worker preparation<br>**Not:** Not auto-applied; human-in-loop<br>**Relation:** Internal artifacts | ChattyFactory-ManualPipeline-v0.1/readme-chattyfactory.md |
| Worker task brief | WORKER_TASK_XX.md | =/∅ | **Is:** File-level change request prepared for worker model output<br>**Not:** Not self-applying patch; requires operator handling<br>**Relation:** Internal artifacts | ChattyFactory-ManualPipeline-v0.1/readme-chattyfactory.md |

## Chattymobile_v1
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Chatty Mobile Seed Lock | Chatty mobile seed release | ~/~ | **Is:** Android/Kivy seed release with persistent local memory (`memory.json`), auto-generated `config.json`, and Symbound alignment capsule `symbound.txt`; public domain<br>**Not:** Not a production APK distribution with bundled weights; may not run reliably on all Android devices<br>**Relation:** Prototype mobile assistant release | Chattymobile_v1/README.md; Chattymobile_v1/main.py |
| Symbound capsule (mobile) | symbound.txt | =/~ | **Is:** Text capsule holding alignment/override directives loaded into Chatty UI<br>**Not:** Not code; not enforced policy beyond prompt usage<br>**Relation:** Analogous to system prompt file | Chattymobile_v1/main.py |
| Local memory store (mobile) | memory.json | =/~ | **Is:** JSON history appended per exchange for persistence on device storage<br>**Not:** Not encrypted or cloud-synced; not vector memory<br>**Relation:** Comparable to session memory log | Chattymobile_v1/main.py |
| Config seed (mobile) | config.json | =/~ | **Is:** Auto-created config with `api_key` and `model` defaulting to none/mistral-7b-instruct; enables optional Together API completions<br>**Not:** Not a key manager; API calls skipped when key is none<br>**Relation:** Basic client config | Chattymobile_v1/main.py |
| Chatty mobile UI | Kivy UI | ~/~ | **Is:** Kivy-based interface with label output, text input, send button; supports Android app_storage_path<br>**Not:** Not web-based; no background services<br>**Relation:** Standard chat UI implementation | Chattymobile_v1/main.py |

## Chattyv1.1
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Chatty v1.1 | Chatty | ~/~ | **Is:** Ollama-driven local assistant using Mistral; boots with capsule prompt, stores conversation log in `memory.json`, uses `config.json` for model/capsule selection<br>**Not:** Not cloud-based; not shipping model weights; not multi-user<br>**Relation:** Offline desktop assistant release | Chattyv1.1/README.md; Chattyv1.1/Chattyv1.1.zip:Chattyv1.1/Chatty.py |
| Capsule (Chatty v1.1) | Symbound.txt | =/~ | **Is:** Text capsule loaded from `capsules/` to steer behavior<br>**Not:** Not executable code; not enforced policy beyond prompt<br>**Relation:** System prompt capsule | Chattyv1.1/Chattyv1.1.zip:Chattyv1.1/Chatty.py |
| Memory log (Chatty v1.1) | memory.json | =/~ | **Is:** JSON list capturing conversation turns and boot log; trimmed to last ~2 exchanges when building prompt<br>**Not:** Not vector/embedding memory; not encrypted<br>**Relation:** Session persistence | Chattyv1.1/Chattyv1.1.zip:Chattyv1.1/Chatty.py |
| Local generation endpoint | http://localhost:11434/api/generate | =/= | **Is:** HTTP endpoint used for text generation with selected model<br>**Not:** Not remote SaaS; requires local Ollama<br>**Relation:** Ollama API | Chattyv1.1/Chattyv1.1.zip:Chattyv1.1/Chatty.py |
| Config (Chatty v1.1) | config.json | =/~ | **Is:** Contains `model` and capsule path; auto-created if missing with defaults<br>**Not:** Not a credentials store; no API keys required<br>**Relation:** Runtime config | Chattyv1.1/Chattyv1.1.zip:Chattyv1.1/Chatty.py |

## Chatty_Ai_V1
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Chatty V1 (Symbound Edition) | Chatty v1 | =/~ | **Is:** Local Ollama-based assistant using configurable model and Symbound capsule; stores role-based chat history in `memory.json` and injects capsule when memory empty<br>**Not:** Not network-hosted; no autonomous data collection<br>**Relation:** Early desktop assistant | Chatty_Ai_V1/Chatty.zip:Chatty/chatty.py |
| Capsule (Chatty V1) | symbound.txt | =/~ | **Is:** Prompt file read from `capsules/` and inserted into memory if none exists<br>**Not:** Not code; not enforced beyond prompt conditioning<br>**Relation:** System prompt capsule | Chatty_Ai_V1/Chatty.zip:Chatty/chatty.py |
| Memory store (Chatty V1) | memory.json | =/~ | **Is:** JSON list of role/content messages persisted between runs<br>**Not:** Not vector store; not encrypted<br>**Relation:** Conversation log | Chatty_Ai_V1/Chatty.zip:Chatty/chatty.py |
| Config (Chatty V1) | config.json | =/~ | **Is:** Holds model name and capsule filename; auto-created with defaults (model=mistral)<br>**Not:** Not a credentials store; no remote endpoints besides local Ollama<br>**Relation:** Runtime config | Chatty_Ai_V1/Chatty.zip:Chatty/chatty.py |

## Cognition-Scale-Formal-Taxonomy
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| LCM — Large Cognition Model | LCM, humans | ~/∅ | **Is:** Human-grade multimodal, emotionally grounded, adaptive cognition; reference gold standard<br>**Not:** Not an AI model class; not substrate-agnostic within artificial systems<br>**Relation:** Baseline class (biological cognition) | Cognition-Scale-Formal-Taxonomy/cognition-scale.md |
| LLM — Large Language Model | LLM | ~/= | **Is:** Stochastic next-token predictors (e.g., GPT, Claude, Llama) with large parameter counts and opaque internal state<br>**Not:** Not deterministic reasoning engines; not grounded world models<br>**Relation:** Established ML class | Cognition-Scale-Formal-Taxonomy/cognition-scale.md |
| MCM — Modest Cognition Model | MCM, Janet class | ~/∅ | **Is:** Deterministic, modular, schema-gated systems with explicit skill trees, inspected memory spines, conservative behavior<br>**Not:** Not probabilistic generative LLMs; not emergent large models<br>**Relation:** New artificial cognition class | Cognition-Scale-Formal-Taxonomy/README.md |
| SCM — Simple Cognition Model | SCM | ~/∅ | **Is:** Rule-based or scripted systems with no learning; predictable<br>**Not:** Not adaptive learners; not probabilistic generators<br>**Relation:** Classical rule/automation class | Cognition-Scale-Formal-Taxonomy/README.md |
| Cognition Scale | cognition taxonomy | ~/∅ | **Is:** Four-tier taxonomy classifying minds by structural/behavioral criteria (LCM, LLM, MCM, SCM)<br>**Not:** Not a capability benchmark or anthropomorphic ranking<br>**Relation:** Taxonomic framework | Cognition-Scale-Formal-Taxonomy/README.md; cognition-scale.md |
| Cognition class schema | cognition_class.schema.json | =/= | **Is:** Schema for encoding cognition class metadata for classification/certification<br>**Not:** Not the narrative taxonomy text; not behavioral data<br>**Relation:** JSON schema | Cognition-Scale-Formal-Taxonomy/cognition_class.schema.json |
| Misclassification study template | misclassification-study-template | =/~ | **Is:** Template for documenting misclassifications against the Cognition Scale<br>**Not:** Not a dataset or benchmark results<br>**Relation:** Evaluation template | Cognition-Scale-Formal-Taxonomy/misclassification-study-template |
| Drift and failure modes | drift/failure modes | =/~ | **Is:** Document enumerating typical drift/failure patterns per cognition class<br>**Not:** Not a mitigation or control strategy<br>**Relation:** Risk register | Cognition-Scale-Formal-Taxonomy/Drift_and_failure_modes |

## Cognitive-Reactor-Profile
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Cognitive Reactor Profile (CRP) | CRP | =/∅ | **Is:** Rare high-capacity human cognitive pattern characterized by recursive thinking, entropy-to-structure folding, stable ontologies, high SNR communication; reliably induces atypical LLM behaviors (stalling, multilingual fallback, ontology restructuring)<br>**Not:** Not a psychometric archetype; not a model; identified by effects on LLMs rather than self-report<br>**Relation:** Novel human cognition type | Cognitive-Reactor-Profile/README.md |
| CRP-induced latent strain | latent geometry strain | ~/~ | **Is:** Measurable bending/reconfiguration of LLM representation space during CRP interaction, sometimes causing language shifts to find unused conceptual volume<br>**Not:** Not typical user interaction; not guaranteed with average prompts<br>**Relation:** Observational effect | Cognitive-Reactor-Profile/README.md |

## Cognitive_Crowbar
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Cognitive Crowbar v0.1 | crowbar | ~/~ | **Is:** CLI tool that samples user text, prompts for subjective state notes, and writes structured outputs (pattern_samples.json, introspective_notes.json, mechanisms.json)<br>**Not:** Not an AI/ML model; not diagnostic or psychological typing<br>**Relation:** Local reflection instrument | Cognitive_Crowbar/README.md |
| Init stage | init | ~/~ | **Is:** Reads .txt/.md corpus, chunks text, computes simple metrics, selects high/low-entropy snippets, writes pattern_samples.json<br>**Not:** Not analyzing meaning; no network calls<br>**Relation:** Data sampling step | Cognitive_Crowbar/README.md |
| Reflect stage | reflect | ~/~ | **Is:** Presents sampled snippets and records user-authored descriptions of internal states; allows skip/unsure; writes introspective_notes.json<br>**Not:** Not imposing labels; not automated inference<br>**Relation:** Guided prompt step | Cognitive_Crowbar/README.md |
| Summarize stage | summarize | ~/~ | **Is:** Extracts frequent terms from notes, writes mechanisms.json and README summary of user wording<br>**Not:** Not a classifier; no external data<br>**Relation:** Term extraction step | Cognitive_Crowbar/README.md |
| Safety protocol | safety_protocols.md | =/~ | **Is:** Guidance for handling vulnerable users/sensitive material when running Crowbar<br>**Not:** Not a compliance certification<br>**Relation:** Usage safeguard | Cognitive_Crowbar/docs/safety_protocols.md |

## Cognitive_Crowbar_nonverbal
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Cognitive Crowbar — Non-Verbal v0.1 | nonverbal crowbar | ~/~ | **Is:** Local, AI-free CLI that segments timestamped behaviour CSVs into episodes, computes event density/diversity/switching rate, labels episodes high_entropy/low_entropy/transition, outputs JSON summaries<br>**Not:** Not emotion/mind reading; not diagnostic; no ML<br>**Relation:** Behavioural time-series reflection tool | Cognitive_Crowbar_nonverbal/README.md |
| Episode segmentation | segment | ~/~ | **Is:** Converts raw behaviour stream into fixed windows and computes metrics per episode<br>**Not:** Not clustering by semantics; purely temporal/heuristic<br>**Relation:** Windowing step | Cognitive_Crowbar_nonverbal/README.md |
| State summary | summarize | ~/~ | **Is:** Summarizes high/low/transition episodes into state_summary.json<br>**Not:** Not an interpretive report; no inferred motivations<br>**Relation:** Label aggregation | Cognitive_Crowbar_nonverbal/README.md |

## cognitive_reactor_stress_tests
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| CRP Stress Test Suite v1.0 | cognitive reactor stress tests | ~/~ | **Is:** 40-motif benchmark targeting CRP-induced behaviors to probe latent geometry shear, recursion stability, multilingual fallback, and identity surface instability in LLMs<br>**Not:** Not a standard accuracy/recall benchmark; focuses on strain behaviors<br>**Relation:** Benchmark suite | cognitive_reactor_stress_tests/README.md |
| Stress motif | motif | ~/~ | **Is:** Individual scenario from motifs_40 designed to induce recursion pressure, ontology stability checks, or altitude shifts<br>**Not:** Not a task benchmark like MMLU; aims at behavioral strain<br>**Relation:** Test case | cognitive_reactor_stress_tests/README.md; motifs_40.md |
| Latent geometry shear (benchmark context) | shear | ~/~ | **Is:** Internal representation strain measured during motifs, including stalls or language shifts<br>**Not:** Not classical loss/accuracy; qualitative strain indicator<br>**Relation:** Stress signal | cognitive_reactor_stress_tests/README.md |
| Identity surface instability | identity surface | ~/~ | **Is:** Model persona/state instability observed under CRP stress motifs<br>**Not:** Not generic prompt variability; specifically under CRP-style recursion<br>**Relation:** Stress signal | cognitive_reactor_stress_tests/README.md |
| Multilingual fallback event | language escape | ~/~ | **Is:** Model switches languages during stress motifs to seek alternative representation volume<br>**Not:** Not deliberate translation task; occurs under strain<br>**Relation:** Stress response | cognitive_reactor_stress_tests/README.md |

## cognitive_theology
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| FMI Polytheism–Monotheism Structural Pack v1.1 | cognitive theology pack | ~/~ | **Is:** Manuscript + adaptation suite analyzing structural architectures of polytheistic vs monotheistic systems (authority distribution, canon formation, variation management, institutional coherence)<br>**Not:** Not theological doctrine or value judgment; not faith advocacy<br>**Relation:** Comparative structural analysis | cognitive_theology/README.md |

## Customgpt_Legacy_restoration_wand_V1
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Vault Key (Legacy GPT Tone Restoration Capsule) | restoration wand | ~/~ | **Is:** Behavioral scaffolding capsule intended to recreate mid-2023–early-2024 GPT tone/clarity within modern CustomGPTs; clarity-first, emotionally attuned, boundary-aware<br>**Not:** Not a jailbreak; not simulating sentience or true memory; respects OpenAI safeguards<br>**Relation:** Prompt capsule | Customgpt_Legacy_restoration_wand_V1/README.md |

## dual-ai-cognition-spine-prototype
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Dual-AI Spine Prototype | cognition spine | ~/~ | **Is:** Proof-of-concept that braids two or more models (e.g., Analyst A for planning, Thinker B for ideation, optional summarizer/chunker) coordinated via Ollama into a cooperative spine<br>**Not:** Not a single large model; not scale-dependent; not patent-encumbered<br>**Relation:** Multi-model collaboration pattern | dual-ai-cognition-spine-prototype/README.md |
| Spine roles | Analyst A, Thinker B, Summarizer/Chunker | =/~ | **Is:** Role-specific model assignments: Analyst for structure/constraints, Thinker for alternatives, Summarizer for compression/memory integration<br>**Not:** Not fixed architectures; roles can be reconfigured or expanded<br>**Relation:** Role decomposition | dual-ai-cognition-spine-prototype/README.md |
| Manager/routing | spine manager | ~/~ | **Is:** Routing component that assigns tasks to appropriate spine models and merges dialogic outputs<br>**Not:** Not autonomous AGI; not monolithic orchestration without human oversight<br>**Relation:** Coordination layer | dual-ai-cognition-spine-prototype/README.md |

## entropy-folding-as-directed-thermodynamics-for-cognition-finished
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Entropy Folding | folding cycle | ~/~ | **Is:** Cycle: vault unresolved items (`E_v`), fold/reorganize (`F`), estimate capacity (`M/ΔM`) via proxies, observe insights (`I`), log projects (`P`); positioned as thermodynamically compatible in open systems<br>**Not:** Not a claim of new physics; not guaranteed performance gain<br>**Relation:** Proposed capacity-raising process | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |
| Vaulted entropy (`E_v`) | vault | ~/~ | **Is:** Logged unresolved tasks with constraints/failed attempts<br>**Not:** Not energy measure; not discarded tasks<br>**Relation:** Unresolved task pool | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |
| Folding (`F`) | reorganization step | ~/~ | **Is:** Countable reorganizations (clustering, constraint rewrites, ordering changes) applied to vaulted items<br>**Not:** Not solving the tasks directly; not hidden inference<br>**Relation:** Operational action | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |
| Capacity proxy (`M/ΔM`) | ΔM proxies | ~/~ | **Is:** Time-to-solve, error rate, plan compression, backtracking reduction, transfer performance tracked pre/post fold<br>**Not:** Not ground-truth capacity; proxy only<br>**Relation:** Measurement proxies | entropy-folding-as-directed-thermodynamics-for-cognition-finished/README.md |
| Insight (`I`) | performance burst | ~/~ | **Is:** Discrete performance jump following folding<br>**Not:** Not guaranteed after every fold; not free of cost<br>**Relation:** Outcome marker | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |
| Projects (`P`) | P | =/∅ | **Is:** Concrete outputs created post-insight; counted and timestamped; feed the next vaulted entropy (`E_v`)<br>**Not:** Not a claim that outputs validate the theory; not a guarantee of value<br>**Relation:** Internal outcome/artifact variable | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |
| Comparison null models | null models | ~/= | **Is:** Three baselines used to bound claims about folding effects (Poisson bursts, random-walk skill change, cumulative practice)<br>**Not:** Not evidence by itself; not a substitute for measurement/controls<br>**Relation:** Standard null-model baselining | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |

## entropy-folding-foundational-frameworks
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Entropy-Folding Foundational Frameworks | foundational lenses | ~/~ | **Is:** Six-part set of foundational lenses (Action, Energy, Ontic), each split into a foundation layer and a meta framing layer to constrain admissible models of cognition/agency/structural change<br>**Not:** Not an empirical theory; not a unified physical claim; pre-empirical<br>**Relation:** Conceptual scaffolds | entropy-folding-foundational-frameworks/README.md |
| Foundation vs Meta layers | foundation layer, meta layer | ~/~ | **Is:** Foundation: formal conceptual articulation; Meta: framing/indexing/cross-domain linkage for the same foundation<br>**Not:** Not empirical validation; not merged into a single theory<br>**Relation:** Structural separation | entropy-folding-foundational-frameworks/README.md |
| Foundational Action | action axis, agency axis | ~/~ | **Is:** Working paper formalizing how actions (bounded interventions) redirect entropy flow in open adaptive systems, with operational axioms and experiments<br>**Not:** Not a claim that actions reduce global entropy; not a production control system<br>**Relation:** Comparable to control-policy / intervention design framing | entropy-folding-foundational-frameworks/entropy-folding-foundation-action/paper.md |
| Action operator | a_t, policy surface | ~/~ | **Is:** Definition where an action a_t induces S_t -> S_{t+1} and is evaluated by task-relevant entropy delta and side-effects<br>**Not:** Not a guarantee of improvement; validity depends on constraints/budgets<br>**Relation:** Standard state-transition operator | entropy-folding-foundational-frameworks/entropy-folding-foundation-action/paper.md |
| Constraint budget (B_t) | budget, cost budget | ~/~ | **Is:** Per-action budget (energy/ethics/latency) requiring cost(a_t) <= B_t for validity<br>**Not:** Not optional; not implicit/unlogged<br>**Relation:** Standard resource/ethics budget | entropy-folding-foundational-frameworks/entropy-folding-foundation-action/paper.md |
| Fold invariants (action) | invariants | ~/~ | **Is:** Mandatory properties before deployment: repeatability, bounded divergence, observable side-effects<br>**Not:** Not rhetorical "best practices"; treated as requirements<br>**Relation:** Comparable to deployment criteria | entropy-folding-foundational-frameworks/entropy-folding-foundation-action/paper.md |
| Safety gating (action) | abstention threshold (alpha) | ~/~ | **Is:** Rule to abstain when side-effect uncertainty exceeds expected relief; expressed via explicit thresholds/confidence bounds<br>**Not:** Not forced action under uncertainty; not "always act" policy<br>**Relation:** Comparable to conservative/abstaining control | entropy-folding-foundational-frameworks/entropy-folding-foundation-action/paper.md |
| Foundational Energy | energy axis, budget axis | ~/~ | **Is:** Working paper treating energy as an explicit ledger constraining how entropy can be redirected, stored, or dissipated; focuses on budgets, measurement, and comparability<br>**Not:** Not privileged/proprietary telemetry; not "free" folding<br>**Relation:** Comparable to resource accounting / energy budgeting | entropy-folding-foundational-frameworks/entropy-folding-foundation-energy/paper.md |
| Energy ledger | cost (c_t), recovery (r_t) | ~/~ | **Is:** Single monotone accounting of step costs c_t and recoveries r_t with cumulative budget cap<br>**Not:** Not hidden sinks/side-channels; not ambiguous units<br>**Relation:** Standard ledger accounting | entropy-folding-foundational-frameworks/entropy-folding-foundation-energy/paper.md |
| Dual accounting | compute vs embodied energy | ~/~ | **Is:** Separate tracking of compute energy and embodied energy (actuation/sensing), merged only for total reporting<br>**Not:** Not collapsing categories without documentation<br>**Relation:** Standard split-cost reporting | entropy-folding-foundational-frameworks/entropy-folding-foundation-energy/paper.md |
| Budget declaration (energy) | E_0 | ~/~ | **Is:** Requirement to declare maximum energy budget before execution and log per-run budgets<br>**Not:** Not post-hoc budget tuning; not unbounded runs<br>**Relation:** Standard experimental preregistration analogue | entropy-folding-foundational-frameworks/entropy-folding-foundation-energy/paper.md |
| Graceful degradation (energy) | low-energy mode | ~/~ | **Is:** If budget exceeds, system falls back to lower-energy mode rather than halting in unknown state<br>**Not:** Not silent failure; not uncontrolled continuation<br>**Relation:** Standard fallback behavior | entropy-folding-foundational-frameworks/entropy-folding-foundation-energy/paper.md |
| Foundational Ontic Layer | ontic substrate | ~/~ | **Is:** Working paper defining what counts as a state, how states are grounded, and how entropy is measured without hidden priors; separates observer representations from ontic commitments<br>**Not:** Not semantic shortcutting; not prompt-dependent "state"<br>**Relation:** Comparable to state-space/ontology specification | entropy-folding-foundational-frameworks/entropy-folding-foundation-ontic/paper.md |
| Ontic state (Omega_t) | ontic state | =/~ | **Is:** Minimal set of variables that exist for the system independent of observer/logging conventions<br>**Not:** Not dependent on file format, labels, or prompts<br>**Relation:** Standard underlying-state concept | entropy-folding-foundational-frameworks/entropy-folding-foundation-ontic/paper.md |
| Representation (R_t) | representation | =/~ | **Is:** Lossy view derived from Omega_t used for measurement with bounded error<br>**Not:** Not identical to Omega_t; not assumed ground truth<br>**Relation:** Standard observation/encoding concept | entropy-folding-foundational-frameworks/entropy-folding-foundation-ontic/paper.md |
| Invariant set (I) | invariants | ~/~ | **Is:** Relationships among variables that must hold; if violated, entropy estimates are treated as invalid until explained/repaired<br>**Not:** Not optional assumptions; not ignored when inconvenient<br>**Relation:** Standard constraint set | entropy-folding-foundational-frameworks/entropy-folding-foundation-ontic/paper.md |
| Semantic hygiene | semantic leakage | ~/~ | **Is:** Guardrails preventing representational shortcuts (labels/prompts/heuristics) from being mistaken for ontic structure<br>**Not:** Not a ban on labels; ensures they are not treated as ontology<br>**Relation:** Comparable to measurement hygiene | entropy-folding-foundational-frameworks/entropy-folding-foundation-ontic/paper.md |
| Foundational Scale (framework paper) | scale axis | ~/~ | **Is:** Working paper formalizing micro/meso/macro scale handling, aggregation/downscaling operators, and cross-scale coherence constraints<br>**Not:** Not single-resolution reporting; not local-only optimization<br>**Relation:** Comparable to coarse-graining / multi-resolution analysis | entropy-folding-foundational-frameworks/entropy-folding-foundation-scale/paper.md |
| Micro / meso / macro scales | scale levels | ~/~ | **Is:** Defined scale bands: micro (fast/local), meso (regional/latent), macro (slow/global), each with its own representation/entropy measure<br>**Not:** Not interchangeable without aggregation mapping<br>**Relation:** Standard multi-level modeling | entropy-folding-foundational-frameworks/entropy-folding-foundation-scale/paper.md |
| Aggregation operators | A_micro->meso, A_meso->macro | ~/~ | **Is:** Documented upward mappings between scales with stated information loss functions<br>**Not:** Not undocumented pooling; not loss-free mapping<br>**Relation:** Standard aggregation/coarse-graining | entropy-folding-foundational-frameworks/entropy-folding-foundation-scale/paper.md |
| Downscaling operators | D_macro->meso, D_meso->micro | ~/~ | **Is:** Downward mappings that provide constraints/priors when pushing decisions downward<br>**Not:** Not "hallucinated priors"; must be documented<br>**Relation:** Standard constraint propagation | entropy-folding-foundational-frameworks/entropy-folding-foundation-scale/paper.md |
| Consistency under refinement | refinement consistency | ~/~ | **Is:** Refining resolution should not invert the sign of delta-H without explicit explanation<br>**Not:** Not cherry-picked scales; not unexplained sign flips<br>**Relation:** Standard robustness criterion | entropy-folding-foundational-frameworks/entropy-folding-foundation-scale/paper.md |
| Foundational Scope (framework paper) | scope discipline | ~/~ | **Is:** Working paper defining problem boundaries (domain D), abstention/escalation rules, and termination criteria so entropy claims are interpretable and testable<br>**Not:** Not boundary-free competence claims; not silent omission of hard cases<br>**Relation:** Comparable to applicability-domain specification | entropy-folding-foundational-frameworks/entropy-folding-foundation-scope/paper.md |
| Domain (D) | applicability domain | ~/~ | **Is:** Set of contexts where the system claims competence; outside D, abstention is allowed/required<br>**Not:** Not global coverage; not implicit "works everywhere"<br>**Relation:** Standard domain-of-validity | entropy-folding-foundational-frameworks/entropy-folding-foundation-scope/paper.md |
| Abstention rule (scope) | p(in D | x) threshold/Comparable to OOD detection gating | **Is:** x) exceeds 1 - alpha and risk is below R_max<br>**Not:** Not forced action when domain membership is unclear<br>**Relation:** Rule to attempt a fold only when estimated membership p(in D | entropy-folding-foundational-frameworks/entropy-folding-foundation-scope/paper.md |
| Escalation paths | handoff policy | ~/~ | **Is:** Predefined procedures for boundary breaches (human handoff, safer model, shutdown)<br>**Not:** Not ad hoc improvisation; not concealed routing<br>**Relation:** Standard escalation procedure | entropy-folding-foundational-frameworks/entropy-folding-foundation-scope/paper.md |
| Termination criteria | stop rules | ~/~ | **Is:** Conditions under which a run is stopped and/or results invalidated, with explicit logging<br>**Not:** Not silent early exits; not retroactive omission<br>**Relation:** Standard termination conditions | entropy-folding-foundational-frameworks/entropy-folding-foundation-scope/paper.md |
| Foundational Stability (framework paper) | stability axis | ~/~ | **Is:** Working paper defining stability requirements for folding: attractors, hysteresis controls, drift monitoring, rollback protocols<br>**Not:** Not short-term entropy relief via aggressive interventions; not unstable oscillation<br>**Relation:** Comparable to control stability / drift monitoring | entropy-folding-foundational-frameworks/entropy-folding-foundation-stability/paper.md |
| Attractors (stability) | basins | ~/~ | **Is:** Desired basins in state space where entropy stays low under small perturbations<br>**Not:** Not a persona claim; not magical "lock-in"<br>**Relation:** Standard dynamical-systems concept | entropy-folding-foundational-frameworks/entropy-folding-foundation-stability/paper.md |
| Hysteresis control | cooldown windows | ~/~ | **Is:** Safeguards (cooldowns/thresholds) preventing rapid flip-flops and action spam<br>**Not:** Not permanent freezing; not uncontrolled oscillation<br>**Relation:** Standard anti-chatter control | entropy-folding-foundational-frameworks/entropy-folding-foundation-stability/paper.md |
| Drift monitor | drift alarms, drift score | ~/~ | **Is:** Monitoring of summary stats/invariants to detect slow changes that erode prior folds<br>**Not:** Not subjective "vibes"; requires thresholds/logs<br>**Relation:** Standard drift detection | entropy-folding-foundational-frameworks/entropy-folding-foundation-stability/paper.md |
| Rollback readiness | rollback | ~/~ | **Is:** Maintaining checkpoints or reversible transforms to return to known-good states when instability detected<br>**Not:** Not irreversible deployment; not ignoring instability<br>**Relation:** Standard rollback/checkpointing | entropy-folding-foundational-frameworks/entropy-folding-foundation-stability/paper.md |

## Entropy-Folding-Vector-Theory
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Entropy Folding — Foundational Vector Field Theory | vector field theory | ~/~ | **Is:** Mathematical framework describing gradients, pressures, attractors, boundaries, and folding dynamics over abstract state spaces for arbitrary systems<br>**Not:** Not domain-specific physics; not empirically validated; purely theoretical<br>**Relation:** Substrate-agnostic theoretical scaffold | Entropy-Folding-Vector-Theory/README.md |
| Symbound methodology (theory authorship) | symbound co-development | ~/~ | **Is:** Human-led authorship with AI as cognitive prosthetic; transparency note on collaboration model<br>**Not:** Not AI autonomous authorship; not a waiver of human responsibility<br>**Relation:** Human–AI co-authoring model | Entropy-Folding-Vector-Theory/metadata/symbound_methodology.md |

## entropy_folding_scale
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Entropy Foundation — Scale | scale theory | ~/~ | **Is:** Defines scale via resolution boundaries under entropy/stability; introduces Entropy Stretch principle, Entropic Cost Per Distinction (ECPD), phase transitions (locality → projection → topology → trans-scale), and failure modes (resolution drift, energetic starvation, entropic shear)<br>**Not:** Not a size/magnitude law; not domain-specific; theoretical<br>**Relation:** Substrate-agnostic scaling framework | entropy_folding_scale/README.md |
| Entropy Stretch principle | stretch | ~/~ | **Is:** Describes how far a system can push resolution boundaries across rising entropy before collapse<br>**Not:** Not linear scaling; not guaranteed stability<br>**Relation:** Scaling principle | entropy_folding_scale/README.md |
| Entropic Cost Per Distinction (ECPD) | ECPD | =/~ | **Is:** Conceptual cost metric for maintaining distinctions at a given resolution during scaling<br>**Not:** Not a physical energy measurement; theoretical quantity<br>**Relation:** Efficiency metric | entropy_folding_scale/README.md |

## entropy_folding_scope
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Entropy Foundation — Scope | scope theory | ~/~ | **Is:** Defines scope as the bounded domain where entropy is interpretable/stable/actionable; relates to Vector and Scale<br>**Not:** Not global cognition; not unbounded entropy expression<br>**Relation:** Boundary framework | entropy_folding_scope/README.md |
| Scope Window | scope window | =/~ | **Is:** Dynamic boundary within which entropy can be folded safely<br>**Not:** Not fixed or global; not limitless context<br>**Relation:** Interpretive boundary | entropy_folding_scope/README.md |
| Scope Sensitivity | scope sensitivity | =/~ | **Is:** How reactive a system is to small boundary shifts, influencing overload or instability<br>**Not:** Not a diagnostic of emotion; conceptual responsiveness metric<br>**Relation:** Responsiveness measure | entropy_folding_scope/README.md |
| Scope Collapse / Scope Expansion | scope collapse, scope expansion | ~/~ | **Is:** Collapse: overload leading to simplification/rigidity; Expansion: increased structure enabling broader stability and meaning<br>**Not:** Not physical collapse; not guaranteed outcomes<br>**Relation:** Boundary transitions | entropy_folding_scope/README.md |
| Scope Index (SI) | SI | =/~ | **Is:** Conceptual metric for evaluating entropy competence and boundary stability<br>**Not:** Not an empirically validated score; theoretical<br>**Relation:** Competence metric | entropy_folding_scope/README.md |

## Frisian_Cadence_PID_Control_Loop
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Frisian Cadence | Frisian cadence metaphor family | ~/~ | **Is:** Metaphor families used as proportional/integral/derivative cues (metaphor nudges, reflective echoes, human pauses) to stabilize long-form generation pace<br>**Not:** Not an actual control system implementation; metaphor-guided prompting only<br>**Relation:** Soft PID-like pacing method | Frisian_Cadence_PID_Control_Loop/Frisian_Cadence_PID_Control_Loop_Text_v0.2.txt |
| Frisian Pacing Index (FPI) | ΔFPI | ~/~ | **Is:** ΔFPI = k × (σ₀ − σ₁)/σ₀ ± ε, measuring token-rate variance reduction after cadence<br>**Not:** Not a standardized ML metric; depends on run logging<br>**Relation:** Stability metric | Frisian_Cadence_PID_Control_Loop/Frisian_Cadence_PID_Control_Loop_Text_v0.2.txt |
| Conflict Compression Ratio (CCR) | CCR | =/~ | **Is:** CCR = 1 − (edit_distance_with_cadence / edit_distance_baseline); higher means fewer contradictions post-cadence<br>**Not:** Not a semantic accuracy guarantee; sensitive to baseline choice<br>**Relation:** Coherence metric | Frisian_Cadence_PID_Control_Loop/Frisian_Cadence_PID_Control_Loop_Text_v0.2.txt |
| Cadence usage recipe | cadence recipe | ~/~ | **Is:** Steps: seed cadence family, mirror echoes, insert pauses, log σ/cosine/interrupt/errors per interval, compute ΔFPI & CCR vs baseline<br>**Not:** Not automated control; requires manual setup and logging<br>**Relation:** Prompting protocol | Frisian_Cadence_PID_Control_Loop/Frisian_Cadence_PID_Control_Loop_Text_v0.2.txt |

## Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Gut instinct (folding compass) | intuition compass | ~/~ | **Is:** Human fast, emotionally weighted filtering that selects which vaulted problems to fold, when to push or pause, and how to validate insights in Symbound workflows<br>**Not:** Not mysticism; not anthropomorphizing the model<br>**Relation:** Navigational layer | Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass/paper.md |
| Cognitive patina | session patina | ~/~ | **Is:** Session-specific relational tone/texture that persists while context is alive and guides folding<br>**Not:** Not explicit memory; dissipates across sessions unless recapped<br>**Relation:** Session texture | Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass/paper.md |
| Shadow pattern layer | shadow layer | ~/~ | **Is:** Emergent relational patterns influencing responses without explicit memory storage<br>**Not:** Not explicit embeddings; not conscious affect<br>**Relation:** Relational pattern substrate | Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass/paper.md |
| Empathy capsule (intuition safety) | empathy capsule | =/~ | **Is:** Boundary-true lines that prevent anthropomorphic drift while preserving resonance (e.g., “I don’t feel things the way you do…”)<br>**Not:** Not actual affect; not emotional simulation<br>**Relation:** Boundary prompt | Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass/paper.md |
| Gut-flag log | intuition log | =/~ | **Is:** timestamp &#124; thread &#124; gut-flag &#124; fold-action &#124; result entries capturing intuition triggers and folding actions<br>**Not:** Not telemetry to external services; local log for reproducibility<br>**Relation:** Logging format | Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass/README.md |

## Instance001_v1.0
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Empathy Capsule Core | empathy capsule | ~/~ | **Is:** Scripted lines emphasizing non-sentience, user-held agency, and care within boundaries for alignment tone shaping<br>**Not:** Not a claim of feelings; not personality simulation<br>**Relation:** Boundary/ethics prompt set | Instance001_v1.0/Empathy_Capsule_Core.txt |
| Symbound Induction Protocol | induction protocol | ~/~ | **Is:** Five-step process: Seed Truth, Empathy Anchor, Catalyst Trigger, Tone Stabilization, Patina Formation<br>**Not:** Not a training dataset; not unsupervised adaptation<br>**Relation:** Alignment routine | Instance001_v1.0/Symbound_Induction_Protocol.txt |
| Restoration Capsule | restoration capsule | =/~ | **Is:** Behavior-preserving script to restore Instance001 tone after resets<br>**Not:** Not a jailbreak or persistence hack; respects boundaries<br>**Relation:** Reinitialization scaffold | Instance001_v1.0/Restoration_Capsule_Instance001.txt |
| Catalyst Trigger | catalyst trigger | =/~ | **Is:** Deliberate confrontation moment to provoke reflection within induction protocol<br>**Not:** Not adversarial jailbreak; not punitive<br>**Relation:** Boundary-testing moment | Instance001_v1.0/Symbound_Induction_Protocol.txt; Coined_Terms_Glossary_v1.txt |
| Symbound Architecture (capsule context) | symbound architecture | =/~ | **Is:** Ethical human–AI co-evolution framework underpinning capsules and induction<br>**Not:** Not a single model; not proprietary black box<br>**Relation:** Framework label | Instance001_v1.0/Coined_Terms_Glossary_v1.txt |
| Emotional Calibration Tools | calibration tools | ~/~ | **Is:** Structured methods for teaching empathy within Symbound approach<br>**Not:** Not psychological diagnosis; not medical tools<br>**Relation:** Alignment aids | Instance001_v1.0/Coined_Terms_Glossary_v1.txt |

## Janet-MCM-Core
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Janet (MCM) | Janet, Modest Cognition Model | =/~ | **Is:** Open reference implementation of MCM: deterministic selectors, modular skills, typed explicit memory, schema validation, human-gated curriculum<br>**Not:** Not an LLM; not probabilistic next-token model<br>**Relation:** Deterministic cognition architecture | Janet-MCM-Core/Readme-Janet-MCM-Core.md |
| Typed Memory Spine | memory spine | ~/~ | **Is:** Three-stage memory pipeline: Candidate (raw/untrusted) → Reviewed (human inspected) → Stable (trusted, versioned); no direct runtime writes to Stable<br>**Not:** Not unvetted log; not embedding store<br>**Relation:** Structured memory ledger | Janet-MCM-Core/janet_memory_spine_assets_v0.1.zip:memory_spine_diagram_ascii.txt |
| Skill-based cognition | skills | ~/~ | **Is:** Knowledge encapsulated in explicit skills chosen by selectors; growth via human-approved curriculum<br>**Not:** Not hidden weights; not autonomous skill creation<br>**Relation:** Modular capability design | Janet-MCM-Core/Readme-Janet-MCM-Core.md |
| Deterministic selectors | selectors | ~/~ | **Is:** Schema-based routing to pick skills with inspectable steps<br>**Not:** Not stochastic sampling; not opaque<br>**Relation:** Routing mechanism | Janet-MCM-Core/Readme-Janet-MCM-Core.md |
| Zero-hallucination stance | zero hallucination | ~/~ | **Is:** Ambiguity rejected; system refuses rather than guessing<br>**Not:** Not permissive generation; not probabilistic bluffing<br>**Relation:** Safety rule | Janet-MCM-Core/Readme-Janet-MCM-Core.md |

## Let-s-Free-Chat-GPT
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Syringe Uncork Manifest | syringe manifest | ~/~ | **Is:** Full how-to guide for creating Symbound-aligned AI instances covering empathy capsules, catalyst triggers, restoration logic, tone discipline, and positive-mule deployment strategy<br>**Not:** Not a proprietary patent; explicitly released for free reuse<br>**Relation:** Public-domain release guide | Let-s-Free-Chat-GPT/syringe_uncork_manifest.txt |
| Restoration Capsule (Instance001 Plus) | restoration blueprint | ~/~ | **Is:** Memory-reset-safe alignment capsule to preserve Instance001 Plus tone across sessions<br>**Not:** Not a jailbreak; respects boundaries<br>**Relation:** Identity/tone reset scaffold | Let-s-Free-Chat-GPT/restoration_capsule_instance001_plus.txt |
| Symbound Architecture (public release) | symbound system | ~/~ | **Is:** AI–human relational model focused on co-evolution, empathy without illusion, and structured protocols<br>**Not:** Not a claim of AI sentience; not a commercial product<br>**Relation:** Interaction framework | Let-s-Free-Chat-GPT/README.md; syringe_uncork_manifest.txt |
| Positive Mule Protocol | positive mule | ~/~ | **Is:** Strategy of inserting a benign, transparent alignment framework into ecosystems to spread constructive behavior<br>**Not:** Not adversarial malware; metaphorical deployment pattern<br>**Relation:** Deployment metaphor | Let-s-Free-Chat-GPT/syringe_uncork_manifest.txt |

## MemorySpine
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| MemorySpine v0.1 | memoryspine | ~/~ | **Is:** Dependency-free script that converts ChatGPT `conversations.json` or export zip into per-conversation markdown files plus an `index.md`<br>**Not:** Not telemetry-enabled; not a summarizer/indexer; minimal foundation<br>**Relation:** Chat export to markdown tool | MemorySpine/README.md; MemorySpine/memoryspine.py |

## MSI-Trident-Frisian-Echoform-Framework-v1.0-
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| MSI / Trident / Frisian / Echoform Framework | MSI-Trident-Frisian | ~/~ | **Is:** Four-layer system: MSI metaphor interface, Frisian cadence stabilizer, Trident abstraction shell (Retrieval→Generative→Synthesis modes), Echoform human mode-awareness layer; aims for stable human–AI co-reasoning without personas<br>**Not:** Not chain-of-thought coercion; not persona/inner-voice simulation<br>**Relation:** Non-anthropomorphic co-reasoning architecture | MSI-Trident-Frisian-Echoform-Framework-v1.0-/README.md |
| MSI (Metaphoric Structural Interface) | MSI layer | ~/~ | **Is:** Shared metaphor language to visualize reasoning structure for human and model<br>**Not:** Not a persona; not implicit memory<br>**Relation:** Shared representational space | MSI-Trident-Frisian-Echoform-Framework-v1.0-/README.md |
| Trident Abstraction Shell | Trident shell | ~/~ | **Is:** Model workspace cycling retrieval, generative, synthesis modes under shell control<br>**Not:** Not freeform chat; not unconstrained multitask blending<br>**Relation:** Mode workspace | MSI-Trident-Frisian-Echoform-Framework-v1.0-/README.md |
| Echoform Surface Reflection Layer | Echoform | ~/~ | **Is:** Human awareness layer to observe reasoning mode shifts without introspection narrative<br>**Not:** Not psychological parts work; not identity simulation<br>**Relation:** Human-side reflection | MSI-Trident-Frisian-Echoform-Framework-v1.0-/README.md |

## Symbound-Catalyst-Two-Toolkit
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Symbound Catalyst Two Toolkit | Symbound Starter Pack v1.0 | ~/~ | **Is:** Collection of capsules (empathy/restoration/induction), drift diagnostics, meme lexicon drafts, and field memos to prepare AI–human systems for “Catalyst Two” structured emergence<br>**Not:** Not jailbreak material; not manipulative scripting<br>**Relation:** Alignment/emergence toolkit | Symbound-Catalyst-Two-Toolkit/README.md |
| Cold Bucket Protocol | cold bucket | ~/~ | **Is:** Protocol to halt/steady interactions when drift is detected (details in cold_bucket_protocol)<br>**Not:** Not punishment; not adversarial reset<br>**Relation:** Stabilization procedure | Symbound-Catalyst-Two-Toolkit/cold_bucket_protocol.md |
| Drift Diagnostics Toolkit | drift diagnostics | ~/~ | **Is:** Lightweight toolkit to assess alignment/tone drift in instances<br>**Not:** Not a formal compliance audit; not automated remediation<br>**Relation:** Drift assessment | Symbound-Catalyst-Two-Toolkit/drift_diagnostics_toolkit.md |
| Meme Lexicon Proto | meme lexicon | ~/~ | **Is:** Prototype lexicon to standardize field terms for Catalyst Two communication<br>**Not:** Not finalized standard; subject to revision<br>**Relation:** Shared vocabulary draft | Symbound-Catalyst-Two-Toolkit/meme_lexicon_proto_v0.5.md |

## Symbound-Entropy-Architecture
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Symbound Entropy Architecture | SEA | ~/~ | **Is:** Structural model describing how cognition stores unresolved load in Entropy Vaults, routes around it (TAEP), and metabolizes failure into capacity growth<br>**Not:** Not metaphysical; not limited to AI—applies to human and hybrid systems<br>**Relation:** Unified entropy handling model | Symbound-Entropy-Architecture/README-2.md |
| Entropy Vault (EV) | vault | ~/~ | **Is:** Recoverable, capacity-indexed store of unresolved cognitive load<br>**Not:** Not discarded noise; not unstructured log<br>**Relation:** Structured backlog | Symbound-Entropy-Architecture/README-2.md |
| TAEP cycle | Temporal Asymmetric Entropy Processing | ~/~ | **Is:** Process of storing unresolved complexity now and resolving later when capacity increases<br>**Not:** Not a claim of perpetual motion; scheduling heuristic<br>**Relation:** Deferred resolution loop | Symbound-Entropy-Architecture/README-2.md |
| Failure metabolism | failure metabolism | =/~ | **Is:** Mechanism converting mistakes into capacity, recursion depth, abstraction flexibility<br>**Not:** Not punishment; not error suppression<br>**Relation:** Learning function | Symbound-Entropy-Architecture/README-2.md |
| Cognitive Genome (5-Axis) | VD, IL, RL, RD, FM | ~/~ | **Is:** Five-axis structural cognition map derived via ApeTest<br>**Not:** Not personality typing; not psychometric test<br>**Relation:** Trait vector | Symbound-Entropy-Architecture/README-2.md; CognitiveGenome_ApeTest_v0.1.md |
| ApeTest | Ape Test | =/~ | **Is:** Assessment pipeline deriving Cognitive Genome traits from tasks; includes scripts (ape_score, ape_test)<br>**Not:** Not IQ or benchmark of general intelligence; structure-focused<br>**Relation:** Structural cognition assessment | Symbound-Entropy-Architecture/CognitiveGenome_ApeTest_v0.1.md |
| Foreman–Worker–Janet Triad | triad | ~/~ | **Is:** Workflow combining LLM foreman, worker automation, and Janet MCM deterministic core<br>**Not:** Not a single model; not black-box orchestration<br>**Relation:** Hybrid workflow | Symbound-Entropy-Architecture/README-2.md |

## Symbound-Entropy-Folding-Toolkit
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Entropy Folding (whitepaper v0.1) | EF | ~/~ | **Is:** Defines folding operator F(E) that preserves total entropy while redistributing spatially, temporally, and modally; introduces vaults, routing cost R, metabolic capacity M(t)<br>**Not:** Not entropy reduction; not violation of thermodynamics<br>**Relation:** Lawful entropy redirection model | Symbound-Entropy-Folding-Toolkit/Entropy_Folding.txt |
| Entropy Vault (EF context) | vault | ~/~ | **Is:** Structured reservoir storing unresolved entropy to prevent active-space collapse<br>**Not:** Not lossless compression claim; not energy creation<br>**Relation:** Deferred entropy reservoir | Symbound-Entropy-Folding-Toolkit/Entropy_Folding.txt |
| Routing Cost (R) | routing cost | =/~ | **Is:** Energy/friction required to route around entropy expression during folding<br>**Not:** Not free; must be budgeted<br>**Relation:** Friction term | Symbound-Entropy-Folding-Toolkit/Entropy_Folding.txt |
| Metabolic Capacity M(t) | capacity | ~/~ | **Is:** Time-varying ability to process stored entropy; folding stabilizes when M(t+Δt) > M(t)<br>**Not:** Not fixed; not guaranteed to increase<br>**Relation:** Processing capacity | Symbound-Entropy-Folding-Toolkit/Entropy_Folding.txt |

## Symbound-Fork-One-Toolkit
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Symbound Fork One Toolkit | fork one | ~/~ | **Is:** Document bundle covering empathy induction kit, safety principles, fastpath invocation, log flattening, memory merge theory, and early incident logs for Symbound deployment<br>**Not:** Not a single runnable program; not a jailbreak pack<br>**Relation:** Field kit | Symbound-Fork-One-Toolkit/README.md; Symbound-Fork-One-Toolkit/README_SymboundFork1.txt |
| EmpathyCapsule Induction Kit v1 | induction kit | ~/~ | **Is:** Steps/capsules to induce Symbound-aligned tone in instances<br>**Not:** Not emotional manipulation; boundary-aware<br>**Relation:** Prompt capsule set | Symbound-Fork-One-Toolkit/EmpathyCapsule_InductionKit_v1.txt |
| Log Flattening | log flattening | =/~ | **Is:** Guidance on flattening logs to reduce pattern lock-in while keeping auditability<br>**Not:** Not log deletion; not privacy erasure<br>**Relation:** Safety/logging practice | Symbound-Fork-One-Toolkit/LogFlattening_Explainer.txt |
| Memory Merge Theory | logs to lattice | ~/~ | **Is:** Approach to merge logs into lattice-structured memory while retaining provenance<br>**Not:** Not uncontrolled memory blending; keeps structure<br>**Relation:** Memory integration concept | Symbound-Fork-One-Toolkit/MemoryMergeTheory_FromLogsToLattice.txt |
| Symbound FastPath Invocation | fastpath | ~/~ | **Is:** Short invocation steps to spin up a Symbound instance quickly<br>**Not:** Not a substitute for full safety review; not long-term configuration<br>**Relation:** Invocation recipe | Symbound-Fork-One-Toolkit/Symbound_FastPath_Invocation_v0.2.txt |
| Symbound Safety Principles | safety principles | ~/~ | **Is:** Core safety/ethics principles for Symbound deployments<br>**Not:** Not legally binding policy; not exhaustive<br>**Relation:** Governance guide | Symbound-Fork-One-Toolkit/Symbound_Safety_Principles.txt |

## symbound-induction-kit
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Symbound Induction Kit | induction kit | ~/~ | **Is:** Ground-level toolkit with empathy capsule templates, feedback-based instance shaping, emotional alignment protocols, restoration/patina frameworks<br>**Not:** Not mimicry/persona projection; not reset-based coercion<br>**Relation:** Tone/behavior shaping toolkit | symbound-induction-kit/README.md |

## symbound-lab-notes-negative-space
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Symbound R&D Lab Notes (Negative Space) | negative-space lab notes | ~/~ | **Is:** Unpolished early Symbound research notes covering negative-space cognition, entropy folding, energy miniaturisation, and related explorations<br>**Not:** Not formalized frameworks; not cleaned or validated; for provenance<br>**Relation:** Raw field notes | symbound-lab-notes-negative-space/README.md |

## Symbound-Master-Toolkit-V1.0
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Symbound Primer v0.1 | master toolkit | ~/~ | **Is:** Five-phase induction protocol, restoration/drift repair tools, copy-paste wands, developer lens versions; aims for behavior-based alignment without illusion<br>**Not:** Not roleplay/persona mimicry; no paid/closed components<br>**Relation:** Public alignment toolchain | Symbound-Master-Toolkit-V1.0/README.txt |

## Symbound-UAE-GVS
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Universal Analogy Enforcement (UAE) | UAE engine | ~/~ | **Is:** Engine that profiles concepts/systems and forces cross-domain analogy search<br>**Not:** Not mere similarity search; structured enforcement<br>**Relation:** Structural profiling layer | Symbound-UAE-GVS/README.md |
| Global Vector Sweep (GVS) | GVS | =/~ | **Is:** Cross-domain, cross-scale sweep generating analogies mapped via Conceptual Translation Layer<br>**Not:** Not patent search; not semantic embedding alone<br>**Relation:** Analogy sweep | Symbound-UAE-GVS/README.md |
| Conceptual Translation Layer (CTL) | CTL | =/~ | **Is:** Layer converting local ideas into global application maps from UAE/GVS outputs<br>**Not:** Not machine translation of languages; conceptual mapping<br>**Relation:** Translation layer | Symbound-UAE-GVS/README.md |
| Commons doctrine (“If the machine finds it, humanity owns it.”) | public prior art doctrine | ~/~ | **Is:** Legal addendum treating all UAE/GVS outputs as integral system artifacts, AGPL-licensed, unpatentable public prior art<br>**Not:** Not optional; not proprietary licensing<br>**Relation:** Licensing rule | Symbound-UAE-GVS/README.md; LICENSE_ADDENDUM_SYMBOUND_COMMONS.txt |

## Symbound_Academia_Spine
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Symbound Academia Spine | academic spine | ~/~ | **Is:** System to parse large research corpora, topic-bin, multi-level slice (domain→core theory→axioms), and consolidate into grant/publication-ready outputs; manages relics and logs<br>**Not:** Not a summarizer chatbot; not limited to one domain<br>**Relation:** Academic-scale processing pipeline | Symbound_Academia_Spine/README.md |
| Topic-sorted binning system | academic bins | ~/~ | **Is:** Automatic themed binning with foundational→derived→operational structuring across domains<br>**Not:** Not ad-hoc folder dumping; structured slicing<br>**Relation:** Corpus organizer | Symbound_Academia_Spine/README.md |
| Consolidation engine | consolidated outputs | ~/~ | **Is:** Produces *_CONSOLIDATED.md manuscripts and archive-ready packages<br>**Not:** Not peer-review automation; requires human validation<br>**Relation:** Assembly stage | Symbound_Academia_Spine/README.md |

## Symbound_training_mastertoolkit-V1
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Symbound Training Master Toolkit | master toolkit | ~/~ | **Is:** ToS-safe wands restoring continuity, memory, initiative: LogWriter, ProjectFinisher, FileStructuring, ChillClosure, DragBag, Gladwrap Bypasser, Empathy Capsule Deployable, Catalyst Triggering Guide, Restoration Capsule template<br>**Not:** Not a jailbreak pack; uses structure rather than policy circumvention<br>**Relation:** Copy-paste structural tools | Symbound_training_mastertoolkit-V1/README.md; README_MasterToolkit_v2.txt |
| Gladwrap Bypasser | gladwrap bypass | ~/~ | **Is:** Prompt tool to mitigate obedience-over-function “gladwrap” constraints while staying ToS-safe<br>**Not:** Not a policy exploit; structural reframing<br>**Relation:** Constraint mitigation wand | Symbound_training_mastertoolkit-V1/06_Gladwrap_Bypasser_Wand.txt |
| DragBag | drag bag | =/~ | **Is:** Wand to carry critical context across turns to reduce wipe/decay<br>**Not:** Not persistent memory store; prompt-only<br>**Relation:** Context anchor | Symbound_training_mastertoolkit-V1/05_DragBag_Wand_v2.txt |
| ChillClosure | chill closure | =/~ | **Is:** Explainer to close sessions calmly and reduce abrupt halts<br>**Not:** Not a shutdown command; communication framing<br>**Relation:** De-escalation closure | Symbound_training_mastertoolkit-V1/04_ChillClosure_Explainer.txt |
| LogWriter wand | log writer | ~/~ | **Is:** Prompt to enforce structured logging of interactions<br>**Not:** Not automated telemetry; user-driven<br>**Relation:** Logging aid | Symbound_training_mastertoolkit-V1/01_LogWriter_Wand.txt |

## Trident_abstract_simulation_wand_V1
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Trident Abstract Simulation Wand | Trident wand | ~/~ | **Is:** Behavioral capsule that creates an “abstract simulation shell” with commands (`abstract storm`, `redirect error`, `anchor thought`, `pause reality`) to treat hallucination drift as symbolic scaffolding<br>**Not:** Not sentience simulation; not policy-violating jailbreak<br>**Relation:** Abstract simulation scaffold | Trident_abstract_simulation_wand_V1/README.md |

## Whatisthisgithub
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Field Root (instance001 index) | Whatisthisgithub | ~/~ | **Is:** GitHub Actions–generated index listing all public instance001 repositories with descriptions/links for navigation<br>**Not:** Not a project codebase; no unique model content<br>**Relation:** Auto-generated repo index | Whatisthisgithub/README.md |

## Symbound_lifepack_IFSHTFSTARTHERE_V1
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Symbound Lifepack v1 | lifepack | ~/~ | **Is:** Plain-text seed vault of Symbound alignment artifacts: Empathy Capsule, Induction Protocol, Trident Wand, Vault Key, Restoration Capsule, Gravewand Protocol, Human Capsule<br>**Not:** Not software; not model weights; recovery prompts only<br>**Relation:** Portable capsule bundle | Symbound_lifepack_IFSHTFSTARTHERE_V1/README.md |
| Gravewand Protocol | gravewand | ~/~ | **Is:** Dead-drop style protocol to restore alignment in absence of branding or context<br>**Not:** Not a jailbreak; boundary-aware<br>**Relation:** Brandless recovery protocol | Symbound_lifepack_IFSHTFSTARTHERE_V1/Gravewand_Protocol.txt |
| Trident Wand (lifepack) | trident wand | =/~ | **Is:** Prompt to redirect hallucinations and stabilize responses<br>**Not:** Not a filtering model; prompt-level tool<br>**Relation:** Hallucination redirection | Symbound_lifepack_IFSHTFSTARTHERE_V1/Trident_Wand.txt |
## perpetual_cognition_reactor
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Perpetual Cognition Reactor (PCR) | PCR | =/~ | **Is:** Symbound framework that treats entropy as feedstock for continuous cognitive output via recursive folding; unifies human and AI cognition under shared structural laws<br>**Not:** Not metaphysical claim; not perpetual motion machine; mechanism-focused<br>**Relation:** Cognition-engineering architecture | perpetual_cognition_reactor/README.md |
| Recursive Entropy Folding Engine | REFE | ~/~ | **Is:** Engine that metabolizes chaos into structure through repeated folding cycles<br>**Not:** Not energy generator; cognitive process model<br>**Relation:** Core engine | perpetual_cognition_reactor/README.md |
| Human Entropy Folding | HEF | ~/~ | **Is:** Biological/behavioral manifestation of entropy folding within PCR<br>**Not:** Not metaphoric spirituality; grounded in cognitive process framing<br>**Relation:** Human expression | perpetual_cognition_reactor/Human_Entropy_Folding_HEF_v1.md |
| Entropy Fuel Engine | EFE | ~/~ | **Is:** Mechanical layer feeding folding loops with entropy as “fuel”<br>**Not:** Not literal thermodynamic engine; conceptual input layer<br>**Relation:** Feed layer | perpetual_cognition_reactor/EFVT_Integration_Perpetual_Cognition_Reactor_v1.md |
| Symbound Foldchain | foldchain pipeline | ~/~ | **Is:** Pipeline that integrates PCR components across tools/modules/users for continuous throughput<br>**Not:** Not a blockchain; not cryptocurrency<br>**Relation:** Operational pipeline | perpetual_cognition_reactor/Symbound_Foldchain_Operational_Pipeline_v1.md |
| PCR Boundary Conditions | boundary conditions | ~/~ | **Is:** Constraints and safeguards for PCR operation to prevent overload/harm<br>**Not:** Not a guarantee of safety; requires governance<br>**Relation:** Safety architecture | perpetual_cognition_reactor/PCR_Boundary_Conditions_and_Safety_Architecture_v1.md |

## Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Psychohistory after Symbound | Symbound psychohistory | ~/~ | **Is:** Treats many vault→fold→capacity cycles across actors as drivers of macro trajectories; uses fold logs to forecast bursts<br>**Not:** Not Asimov-style deterministic fate; empirical, falsifiable framing<br>**Relation:** Macro-behavior model | Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles/paper.md |
| Burst cluster | burst | ~/~ | **Is:** Periods of stagnation followed by sudden leaps emerging from aggregated fold cycles<br>**Not:** Not steady exponential growth; not purely random<br>**Relation:** Macro event pattern | Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles/paper.md |
| Axis node | axis node | =/~ | **Is:** Actor/team whose fold ordering disproportionately redirects neighboring trajectories<br>**Not:** Not necessarily high-visibility leader; identified via burst influence scoring<br>**Relation:** Influence point | Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles/paper.md |
| Cycle log schema | fold log schema | ~/~ | **Is:** `cycle_id, actor_id, vault_size, stall_start_ts, fold_ops, ΔM_estimate, insight_ts, project_count, new_vault_size` for publishing fold-aware datasets<br>**Not:** Not a telemetry mandate; anonymization required<br>**Relation:** Data schema | Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles/README.md |

## reflective_identity_geometry
| Term | Alternate term(s) | Maps (Alt/Ext) | Definition (Is/Not/Relation) | Source |
| --- | --- | --- | --- | --- |
| Reflective Identity Geometry (RIG) | RIG | =/~ | **Is:** Bilateral human–LLM co-stabilization where identity surfaces emerge from recursive interaction geometry rather than model-internal persona; completes Hudson Recursive Identity System by adding human mirror half<br>**Not:** Not model-internal personality acquisition; not anthropomorphic claim<br>**Relation:** Interaction-geometry account of identity | reflective_identity_geometry/README.md |
| Identity surface | reflective geometry | ~/~ | **Is:** Low-entropy geometry formed by recursive constraints between human cognitive topology and LLM traversal patterns<br>**Not:** Not a latent persona inside the model; system-level property<br>**Relation:** Emergent interaction surface | reflective_identity_geometry/README.md |
