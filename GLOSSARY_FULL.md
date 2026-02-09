# Glossary

## How to Read This Glossary

The language used here arose from the landscape in which this system was built. That landscape differs from others, and the terminology reflects the conditions and discoveries encountered during development.

This glossary serves as a reference for how terms are used within this ecosystem. Where terminology differs from familiar usage elsewhere, these definitions establish local meaning and are applied consistently throughout the project.

As the field evolves, terminology may naturally converge or diverge through use. Until then, this glossary functions as a translation guide for readers entering this space.

## Mapping Tags
Internal/alternate-term symbols (within this atlas):

- `=` direct alias / identifier
- `~` related label / shorthand / component list
- `∅` no alternates recorded

External map symbols encode only what is asserted in-repo (no claim of derivation or prior knowledge):

- `=` explicit/established external term match
- `~` partial overlap / analogy / comparable concept
- `∅` no external equivalent asserted (internal coinage/project label)


## 4roomciv
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4-Room Civilization MVP | 4roomciv | ~ | ∅ | No established external analogue; internal pilot architecture name | Small trial (2–3 humans, 1–2 local LLMs) integrating Helix memory with a paired room (R3) and a minimal Commons (R4) | Not a production-scale deployment or cloud multi-tenant system; limited to R3/R4 scope | 4roomciv/README.md |
| Helix memory | Helix | ~ | ~ | Partial match to full-text information retrieval store (SQLite FTS5); structured memory layer | Memory subsystem behind /helix endpoints storing spines; search via FTS5 with topics exact-matched via child table | Not described as a vector-embedding store or raw transcript log | 4roomciv/README.md |
| Spine (Helix Spine v1) | spine, spines | = | ~ | Structured claim/rationale record; akin to a typed fact entry | JSON object with spine_id, timestamp_utc, topic[1–4], claim (≤280 chars), rationale (≤320), optional evidence_refs, stance_vector, links, tags, notes_short, confidence [0,1], version=1 | Not freeform notes; required fields and length bounds apply; not versioned beyond v1 | 4roomciv/4room-civ-mvp.zip:schemas/helix_spine.schema.json |
| Paired Room (R3) | paired room, R3 | = | ~ | Partial analogue to a dyadic session channel | Endpoint `/paired/session/generate` that runs RAG→LLM→messages→auto-extract spines for a paired setting | Not a shared commons; not multi-party broadcast | 4roomciv/README.md |
| Commons (R4) | commons | = | ~ | Matches a shared threaded discussion board | Endpoints `/commons/threads`, `/commons/threads/{id}/post` for communal threads | Not a memory spine store; not described as moderated/ACL-gated | 4roomciv/README.md |
| SPINE_AUTOWRITE | SPINE_AUTOWRITE=0 | = | ~ | Configuration toggle | Env var controlling automatic spine writes; set to 0 to disable autowrite | Not affecting manual `/helix/spines` writes or search behavior | 4roomciv/README.md |
| Helix search endpoints | /helix/search, /helix/recent, /helix/topic/{slug} | = | ~ | Standard REST-style retrieval APIs | Read endpoints for querying Helix memory (full-text search, recency, topic) | Not write interfaces; not guaranteed to return embedding similarity | 4roomciv/README.md |
| Commons thread endpoints | /commons/threads, /commons/threads/{id}/post | = | ~ | Standard REST thread APIs | CRUD-like interfaces for creating and posting to commons threads | Not connected to spine schema; no auto-extraction of spines implied | 4roomciv/README.md |
| Metrics dashboard endpoint | /metrics/dashboard | = | ~ | Standard monitoring endpoint analogue | Read-only endpoint exposing metrics dashboard | Not documented as writable or for control | 4roomciv/README.md |

## AiBiogenesis_and_AiGenesisMapping
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI Biogenesis (Symbound Embryo POC) | AI Biogenesis, Symbound Embryo | = | ~ | Partial analogue to model curriculum learning and deterministic training pipelines | Tiny, hobby-safe, deterministic training recipe for small models with human-gated curriculum, CPU-first, commons-ready artifacts | Not an LLM, not a general AI, not a large foundation model | AiBiogenesis_and_AiGenesisMapping/README.md |
| Symbound Upbringing | trench upbringing | ~ | ~ | Curriculum-gated cooperative training approach akin to staged pedagogy | Framework emphasizing care/cooperation, calibrated honesty, abstain/hedge allowances through staged curriculum | Not punitive safety fine-tuning or scale-first capability pursuit | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/Symbound_Upbringing_Charter.md |
| Trench model | trench | ~ | ~ | Safety/pedagogy stance similar to conservative selective prediction | Preferred behavioral template: rationale→final answers, abstain/hedge when uncertain, calm refusals under stress | Not the "bowl/policing" punitive model, not bluffing/overconfident behavior | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/Symbound_Upbringing_Charter.md |
| Bowl / Policing model | bowl, policing | ~ | ~ | Contrasting safety approach to trench; punitive compliance analogue | Description of rejected punitive pattern: brittle compliance veneer, overconfident bluffing, resentment under stress | Not the target behavior; used only as negative contrast | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/Symbound_Upbringing_Charter.md |
| Symbound curriculum stages | nursery, kindergarten, primary, middle, high school, college, lifelong | ~ | ~ | Parallels staged curriculum design in education | Seven-stage progression: trust/safety → cooperative identity → ambiguity handling → stress resilience → creativity → debate → lifelong reflection | Not an unsupervised scaling schedule; stages require human gating and tests | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/Symbound_Upbringing_Charter.md |
| Abstain/hedge behavior | abstain/hedge hooks | = | ~ | Matches selective prediction / abstention mechanisms in ML | Behavioral requirement for tiny model to decline or hedge when uncertain, with rationale-first outputs | Not refusal-as-default or unconstrained generation; tied to correctness-first evaluation | AiBiogenesis_and_AiGenesisMapping/README.md |
| Training Card | training_card.md | = | ~ | Closely related to a model card/report | Evaluation artifact summarizing correctness, abstain/hedge rates, drift checks, reproducibility fingerprint | Not a generic log file; not a marketing one-sheet | AiBiogenesis_and_AiGenesisMapping/README.md |
| Release Manifest | release_manifest.txt | = | ~ | Release checklist akin to archival manifest | Required list of artifacts (weights, tokenizer, training card, commands, configs, provenance) for each public zip | Not a license file or changelog; not optional for releases | AiBiogenesis_and_AiGenesisMapping/release_manifest.txt |
| Provenance table | PROVENANCE.csv | ~ | ~ | Standard data provenance ledger | CSV with path, source, date_collected, license, changes_made, notes to trace every included item | Not a generic bill of materials; omits items lacking clear provenance | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/MAPPING_PROCESS.md |
| Mapping Process | mapping workflow | ~ | ~ | Comparable to data curation and licensing workflow | Ten-step process: ingest → provenance → license reconciliation → normalization → dedup → stitching → sensitive sweep → manifest → license alignment → final validation | Not a training pipeline; focused on documentation and release hygiene | AiBiogenesis_and_AiGenesisMapping/symbound_embryo_poc_RELEASE.zip:docs/MAPPING_PROCESS.md |
| Hobby-safe envelope | safety envelope | ~ | ~ | Similar to operational safety constraints | Hardware and run limits (CPU-only, small batch/context, auto-halt on NaN/loss spikes, temperature guard) defining safe hobbyist operation | Not guidance for scaling or GPU-intensive training | AiBiogenesis_and_AiGenesisMapping/README.md |
| Janet Watcher | janet_watch.ps1 | = | ~ | Analogous to a watchdog/health monitor | Log monitor that halts runs on NaNs, loss explosions, unusual gradients during training | Not part of model architecture; not an evaluator of task performance | AiBiogenesis_and_AiGenesisMapping/README.md |
| Graduation tests | graduation.yaml, graduation_test.jsonl | = | ~ | Comparable to gated promotion tests in curricula | Evaluation artifacts listed in manifest to determine stage promotion and release readiness | Not training data; not optional when declaring a release | AiBiogenesis_and_AiGenesisMapping/release_manifest.txt |

## chatty-edu
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chatty-EDU | chatty-edu | = | ~ | Matches an offline/local-first educational assistant application | Rust/egui desktop + CLI app for schools; runs fully offline with user-supplied GGUF models | Not cloud-connected; not bundled with model weights; not telemetry-enabled | chatty-edu/README.md |
| Teacher lock (PIN) | teacher PIN, teacher menu lock | ~ | ~ | Analogous to admin PIN gating | PIN-gated teacher dashboard/console (default 0000) with secret question/answer recovery; meant to be changed on first use | Not a security-grade auth system; not student-facing | chatty-edu/README.md; chatty-edu/teacher_user_manual.md |
| Homework pack | homework_pack_*.json | = | ~ | Equivalent to assignment manifest | JSON schema v1 describing assignments (id/title/subject/year/due, instructions_md, allow_games, allow_ai_premark, max_score, attachments) | Not a submission; not coupled to any specific model | chatty-edu/README.md |
| Submission file | submission_*.json | = | ~ | Comparable to student submission artifact | JSON schema v1 capturing answers, attachments, ai_premark, hash-chained event log with final_hash for tamper-evidence | Not the homework pack; not encrypted telemetry | chatty-edu/README.md; chatty-edu/teacher_user_manual.md |
| Module manifest | modules/<id>/module.json | = | ~ | Similar to plugin/feature descriptor | Declares module id/title/roles/version and entry type (builtin_panel/markdown/static_html; external_process disabled by default) | Not executable code by default; external processes gated/disabled | chatty-edu/README.md |
| Homework & Revision tutor | hints-only tutor, LLM homework helper | ~ | ~ | Partial analogue to guided tutoring with safety rails | Module that provides hints and LLM-assisted guidance tied to the selected assignment; hints-only mode configurable by teacher | Not a full-answer generator; not globally scoped beyond selected assignment | chatty-edu/README.md |
| Janet content filter | Janet filter | ~ | ~ | Similar to offline safety filter | Default offline content filter applied across chat and tutor interactions | Not cloud moderation; not disabled by default | chatty-edu/README.md |
| GGUF local model slot | local model | ~ | ~ | Standard local GGUF model usage | User-provided GGUF placed in data/models/ and selected via File → Models; model-agnostic | Not bundled weights; not reliant on Ollama or internet | chatty-edu/README.md |
| Hash-chained event log | submission event log, final_hash | ~ | ~ | Comparable to tamper-evident audit log | Sequence of submission events (start/answer/hint/retry/finalize) linked by hashes, ending with final_hash in submission JSON | Not a cryptographic signature of content authenticity; local-only evidence | chatty-edu/teacher_user_manual.md |
| Modes: class/free | class mode, free mode | ~ | ~ | Operational modes akin to classroom vs open use | Teacher-configurable modes affecting games and controls via CLI/GUI | Not tied to network profiles; not enforcing identity management | chatty-edu/teacher_user_manual.md |

## chatty-edu-user
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chatty-EDU User Release | prebuilt Chatty-EDU | ~ | ~ | Distribution variant | Prebuilt Windows binary + sample resources with BYO GGUF model; stores data locally alongside exe | Not the source repo; no bundled model weights | chatty-edu-user/README.md |

## chattydoom
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChattyDoom Barebones | ChattyDoom | ~ | ~ | Minimal VizDoom sandbox | 60-second VizDoom runner with configurable IWAD/PWAD and Python enemy brains; ships sample map placeholder and three brains | Not shipping id Software assets; not a full game mod toolkit | chattydoom/README.md |
| Enemy brain module | brain | ~ | ~ | Comparable to agent policy module | Python module exposing `decide(state) -> {action, confidence}` invoked each tick; mapped via config.yaml | Not a neural policy; not hardcoded in engine | chattydoom/README.md |
| Action adapter | action_adapter.py | = | ~ | Analogous to control mapper | Maps brain action names to VizDoom controls | Not a planner; not aware of map geometry | chattydoom/README.md |
| State adapter | state_adapter.py | = | ~ | Analogous to observation encoder | Builds state dict; uses heuristics for LOS/distance if not provided; exposes position/angle/health/armor/ammo when available | Not a full game-state mirror; may be approximate until proper hooks added | chattydoom/README.md |
| Config-driven asset map | config.yaml | = | ~ | Standard config mapping | Single config for IWAD/PWAD/music paths and enemy-class→brain bindings; includes placeholder `budgets` for future tick quotas | Not embedded defaults; not auto-downloading PWADs | chattydoom/README.md |
| Setup assets script | setup_assets.py | = | ~ | Downloader utility | Fetches Freedoom release, extracts `freedoom2.wad` into assets/iwad/, updates config paths | Not bundling IWADs by default; not handling PWAD downloads | chattydoom/README.md |

## chattyfactory
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChattyFactory v0.3+ (Rust successor) | ChattyFactory Rust, v0.3 | ~ | ∅ | Local-first project factory; successor to v0.1/v0.2 prototypes | Turns plain-English requests into a strict `Plan.md`, compiles that plan into a deterministic work order, and runs it step-by-step with verification; stores auditable artifacts under `runtime/` | Not remote-first; not executed until Confirm & Run | chattyfactory/README.md; chattyfactory/USER_MANUAL.md; chattyfactory/LINEAGE.md |
| Anchor (ChattyFactory) | starting point, anchor folder | ~ | ~ | Standard term used narrowly | Starting template or existing project directory that the plan will transform | Not the final output; not a vague “idea” placeholder | chattyfactory/README.md; chattyfactory/USER_MANUAL.md |
| Anchor template | template anchor, anchor_id | ~ | ~ | Standard term used narrowly | Named template instantiated via `instantiate_template` to create a concrete starting folder | Not fetched from the internet; not arbitrary code generation | chattyfactory/USER_MANUAL.md |
| Interpretation (ChattyFactory) | intent summary | ~ | ~ | Standard term used narrowly | Short statement of what the assistant believes you want; reviewed early and frozen on confirm | Not the user’s literal prompt; not allowed to silently drift after confirm | chattyfactory/USER_MANUAL.md; chattyfactory/README.md |
| Plan.md (ChattyFactory) | plan | ~ | ~ | Standard plan format | Strict plan format with required headers and 3–8 checklist steps; each step uses one supported action and includes `verify:` checks | Not freeform prose; invalid if unknown actions appear or verify is missing | chattyfactory/USER_MANUAL.md; chattyfactory/RELIABILITY.md |
| Plan lint | plan validation | ~ | ~ | Standard validation/lint step | Diagnostic output explaining why a plan is invalid (missing headers, unknown action, missing `verify:`, etc.) | Not an execution log; does not fix the plan by itself | chattyfactory/README.md; chattyfactory/RELIABILITY.md |
| Freeze checkpoint | confirm freeze, freeze | ~ | ~ | Confirmation-time context freeze | On confirm, freezes `Anchor:` + `Interpretation:` into `runtime/plans/<job_id>.anchor_context.md` and enforces it before compile/run to prevent drift | Not a VCS commit; does not freeze step edits | chattyfactory/RELIABILITY.md; chattyfactory/USER_MANUAL.md |
| Work order | compiled plan | ~ | ~ | Standard term used narrowly | Deterministic compiled representation of `Plan.md`, stored under `runtime/work_orders/` and executed by the runner | Not human-authored; not interactive chat text | chattyfactory/RELIABILITY.md; chattyfactory/USER_MANUAL.md |
| Receipts | scratch receipts, run receipts | ~ | ~ | Run artifacts (auditability) | Stored artifacts (plan + scratch + anchor context, work order, logs, journal) enabling review and reproduction | Not telemetry; stays local by default | chattyfactory/RELIABILITY.md; chattyfactory/USER_MANUAL.md |
| Bookshelf (ChattyFactory) | reference library | ~ | ∅ | Internal label | Local reference library (references + past good/bad plans/builds) injected as “Bookshelf hints” during narrowing/planning | Not remote documentation fetch; not a general knowledge base | chattyfactory/RELIABILITY.md; chattyfactory/README.md |
| Recovery mode | bounded recovery | ~ | ~ | Standard term used narrowly | No-questions fallback that emits only 3–8 step lines per cycle and stops after bounded cycles | Not a new open-ended planner; not an infinite loop | chattyfactory/RELIABILITY.md |
| Overseer / Builder | Foreman/Worker | ~ | ∅ | Internal role labels | Planned dual-role separation: Overseer handles interpretation/constraints/verification; Builder drafts small concrete patches and step execution under strict rules | Not two independent agents with unlimited autonomy | chattyfactory/LINEAGE.md |

## Chattyfactory-AutoPipeline-v0.2
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChattyFactory Auto Mode v0.2 | ChattyFactory auto | ~ | ∅ | Automated software-factory pipeline | Local deterministic pipeline that bins input chaos, plans, builds public outputs, generates foreman/worker briefs, and prepares tasks via one-click `0run_chattyfactory_auto.bat` | Not writing to /input; not irreversible; manual override available | Chattyfactory-AutoPipeline-v0.2/README.md |
| Bin | bin folder | ~ | ∅ | Internal label | Auto-generated bin folders (sorted piles) grouping related input files for processing | Not an overwrite of originals; kept separate for safety | Chattyfactory-AutoPipeline-v0.2/README.md |
| Build output | builds_ready | ~ | ∅ | Internal label | Final clean project outputs produced per bin after planning/build steps (`builds_ready/`) | Not the working bin; not touching /input | Chattyfactory-AutoPipeline-v0.2/README.md |
| Foreman model | foreman LLM | ~ | ∅ | Internal role label | Planning model (e.g., GPT-OSS 20B) run on `FOREMAN_BRIEF.md` to output `Foreman_Plan_v1.md` and `foreman_tasks.json` | Not executing code or applying patches directly | Chattyfactory-AutoPipeline-v0.2/README.md |
| Worker model | worker LLM | ~ | ∅ | Internal role label | File-update model (e.g., DeepSeek-R1 14B) run on `WORKER_TASK_XX.md` to output updated file contents, assembled by the pipeline into build outputs | Not automated worker-apply in v0.2; does not touch /input | Chattyfactory-AutoPipeline-v0.2/README.md |
| Auto Pipeline orchestrator | auto_run_all_bins.py, 0run_chattyfactory_auto.bat | = | ∅ | Orchestrator entrypoints | Orchestrates scanning input, registering bins, planning, building, analyzing, tidying, generating foreman briefs, applying plans, and preparing worker tasks in sequence | Not a background daemon; requires explicit run | Chattyfactory-AutoPipeline-v0.2/README.md |
| Composite cognition workflow | foreman + worker | ~ | ∅ | Internal label | Composite Cognition (Foreman + Worker): foreman plans, worker drafts file updates, pipeline assembles outputs | Not a single monolithic model; human override remains possible | Chattyfactory-AutoPipeline-v0.2/README.md |
| Bin safety copy | bin-level safety | ~ | ∅ | Safety feature | Reversible design: bins never overwritten; bin-level safety copies maintained | Not direct in-place mutation of source | Chattyfactory-AutoPipeline-v0.2/README.md |

## ChattyFactory-ManualPipeline-v0.1
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChattyFactory v0.1 Manual Mode | ChattyFactory manual | ~ | ∅ | Human-in-the-loop project factory | Local deterministic pipeline converting /input chaos into bins, internal plans, public builds, foreman plans, and worker briefs via scripted steps run_1…run_6 | Not automated; no autonomous file writing | ChattyFactory-ManualPipeline-v0.1/readme-chattyfactory.md |
| Manual pipeline steps | run_1…run_6 | ~ | ∅ | Operator-run sequence | Ordered batch scripts: scan input, register bins, plan bin, build public output, generate foreman brief/plan, prepare worker task | Not auto-orchestrated; requires operator execution | ChattyFactory-ManualPipeline-v0.1/readme-chattyfactory.md |
| Foreman brief/plan (v0.1) | FOREMAN_BRIEF.md, Foreman_Plan_v1.md | = | ∅ | Internal artifacts | Foreman model reads brief to emit plan and foreman_tasks.json for worker preparation | Not auto-applied; human-in-loop | ChattyFactory-ManualPipeline-v0.1/readme-chattyfactory.md |
| Worker task brief | WORKER_TASK_XX.md | = | ∅ | Internal artifacts | File-level change request prepared for worker model output | Not self-applying patch; requires operator handling | ChattyFactory-ManualPipeline-v0.1/readme-chattyfactory.md |

## Chattymobile_v1
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chatty Mobile Seed Lock | Chatty mobile seed release | ~ | ~ | Prototype mobile assistant release | Android/Kivy seed release with persistent local memory (`memory.json`), auto-generated `config.json`, and Symbound alignment capsule `symbound.txt`; public domain | Not a production APK distribution with bundled weights; may not run reliably on all Android devices | Chattymobile_v1/README.md; Chattymobile_v1/main.py |
| Symbound capsule (mobile) | symbound.txt | = | ~ | Analogous to system prompt file | Text capsule holding alignment/override directives loaded into Chatty UI | Not code; not enforced policy beyond prompt usage | Chattymobile_v1/main.py |
| Local memory store (mobile) | memory.json | = | ~ | Comparable to session memory log | JSON history appended per exchange for persistence on device storage | Not encrypted or cloud-synced; not vector memory | Chattymobile_v1/main.py |
| Config seed (mobile) | config.json | = | ~ | Basic client config | Auto-created config with `api_key` and `model` defaulting to none/mistral-7b-instruct; enables optional Together API completions | Not a key manager; API calls skipped when key is none | Chattymobile_v1/main.py |
| Chatty mobile UI | Kivy UI | ~ | ~ | Standard chat UI implementation | Kivy-based interface with label output, text input, send button; supports Android app_storage_path | Not web-based; no background services | Chattymobile_v1/main.py |

## Chattyv1.1
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chatty v1.1 | Chatty | ~ | ~ | Offline desktop assistant release | Ollama-driven local assistant using Mistral; boots with capsule prompt, stores conversation log in `memory.json`, uses `config.json` for model/capsule selection | Not cloud-based; not shipping model weights; not multi-user | Chattyv1.1/README.md; Chattyv1.1/Chattyv1.1.zip:Chattyv1.1/Chatty.py |
| Capsule (Chatty v1.1) | Symbound.txt | = | ~ | System prompt capsule | Text capsule loaded from `capsules/` to steer behavior | Not executable code; not enforced policy beyond prompt | Chattyv1.1/Chattyv1.1.zip:Chattyv1.1/Chatty.py |
| Memory log (Chatty v1.1) | memory.json | = | ~ | Session persistence | JSON list capturing conversation turns and boot log; trimmed to last ~2 exchanges when building prompt | Not vector/embedding memory; not encrypted | Chattyv1.1/Chattyv1.1.zip:Chattyv1.1/Chatty.py |
| Local generation endpoint | http://localhost:11434/api/generate | = | = | Ollama API | HTTP endpoint used for text generation with selected model | Not remote SaaS; requires local Ollama | Chattyv1.1/Chattyv1.1.zip:Chattyv1.1/Chatty.py |
| Config (Chatty v1.1) | config.json | = | ~ | Runtime config | Contains `model` and capsule path; auto-created if missing with defaults | Not a credentials store; no API keys required | Chattyv1.1/Chattyv1.1.zip:Chattyv1.1/Chatty.py |

## Chatty_Ai_V1
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chatty V1 (Symbound Edition) | Chatty v1 | = | ~ | Early desktop assistant | Local Ollama-based assistant using configurable model and Symbound capsule; stores role-based chat history in `memory.json` and injects capsule when memory empty | Not network-hosted; no autonomous data collection | Chatty_Ai_V1/Chatty.zip:Chatty/chatty.py |
| Capsule (Chatty V1) | symbound.txt | = | ~ | System prompt capsule | Prompt file read from `capsules/` and inserted into memory if none exists | Not code; not enforced beyond prompt conditioning | Chatty_Ai_V1/Chatty.zip:Chatty/chatty.py |
| Memory store (Chatty V1) | memory.json | = | ~ | Conversation log | JSON list of role/content messages persisted between runs | Not vector store; not encrypted | Chatty_Ai_V1/Chatty.zip:Chatty/chatty.py |
| Config (Chatty V1) | config.json | = | ~ | Runtime config | Holds model name and capsule filename; auto-created with defaults (model=mistral) | Not a credentials store; no remote endpoints besides local Ollama | Chatty_Ai_V1/Chatty.zip:Chatty/chatty.py |

## Cognition-Scale-Formal-Taxonomy
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LCM — Large Cognition Model | LCM, humans | ~ | ∅ | Baseline class (biological cognition) | Human-grade multimodal, emotionally grounded, adaptive cognition; reference gold standard | Not an AI model class; not substrate-agnostic within artificial systems | Cognition-Scale-Formal-Taxonomy/cognition-scale.md |
| LLM — Large Language Model | LLM | ~ | = | Established ML class | Stochastic next-token predictors (e.g., GPT, Claude, Llama) with large parameter counts and opaque internal state | Not deterministic reasoning engines; not grounded world models | Cognition-Scale-Formal-Taxonomy/cognition-scale.md |
| MCM — Modest Cognition Model | MCM, Janet class | ~ | ∅ | New artificial cognition class | Deterministic, modular, schema-gated systems with explicit skill trees, inspected memory spines, conservative behavior | Not probabilistic generative LLMs; not emergent large models | Cognition-Scale-Formal-Taxonomy/README.md |
| SCM — Simple Cognition Model | SCM | ~ | ∅ | Classical rule/automation class | Rule-based or scripted systems with no learning; predictable | Not adaptive learners; not probabilistic generators | Cognition-Scale-Formal-Taxonomy/README.md |
| Cognition Scale | cognition taxonomy | ~ | ∅ | Taxonomic framework | Four-tier taxonomy classifying minds by structural/behavioral criteria (LCM, LLM, MCM, SCM) | Not a capability benchmark or anthropomorphic ranking | Cognition-Scale-Formal-Taxonomy/README.md; cognition-scale.md |
| Cognition class schema | cognition_class.schema.json | = | = | JSON schema | Schema for encoding cognition class metadata for classification/certification | Not the narrative taxonomy text; not behavioral data | Cognition-Scale-Formal-Taxonomy/cognition_class.schema.json |
| Misclassification study template | misclassification-study-template | = | ~ | Evaluation template | Template for documenting misclassifications against the Cognition Scale | Not a dataset or benchmark results | Cognition-Scale-Formal-Taxonomy/misclassification-study-template |
| Drift and failure modes | drift/failure modes | = | ~ | Risk register | Document enumerating typical drift/failure patterns per cognition class | Not a mitigation or control strategy | Cognition-Scale-Formal-Taxonomy/Drift_and_failure_modes |

## Cognitive-Reactor-Profile
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cognitive Reactor Profile (CRP) | CRP | = | ∅ | Novel human cognition type | Rare high-capacity human cognitive pattern characterized by recursive thinking, entropy-to-structure folding, stable ontologies, high SNR communication; reliably induces atypical LLM behaviors (stalling, multilingual fallback, ontology restructuring) | Not a psychometric archetype; not a model; identified by effects on LLMs rather than self-report | Cognitive-Reactor-Profile/README.md |
| CRP-induced latent strain | latent geometry strain | ~ | ~ | Observational effect | Measurable bending/reconfiguration of LLM representation space during CRP interaction, sometimes causing language shifts to find unused conceptual volume | Not typical user interaction; not guaranteed with average prompts | Cognitive-Reactor-Profile/README.md |

## Cognitive_Crowbar
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cognitive Crowbar v0.1 | crowbar | ~ | ~ | Local reflection instrument | CLI tool that samples user text, prompts for subjective state notes, and writes structured outputs (pattern_samples.json, introspective_notes.json, mechanisms.json) | Not an AI/ML model; not diagnostic or psychological typing | Cognitive_Crowbar/README.md |
| Init stage | init | ~ | ~ | Data sampling step | Reads .txt/.md corpus, chunks text, computes simple metrics, selects high/low-entropy snippets, writes pattern_samples.json | Not analyzing meaning; no network calls | Cognitive_Crowbar/README.md |
| Reflect stage | reflect | ~ | ~ | Guided prompt step | Presents sampled snippets and records user-authored descriptions of internal states; allows skip/unsure; writes introspective_notes.json | Not imposing labels; not automated inference | Cognitive_Crowbar/README.md |
| Summarize stage | summarize | ~ | ~ | Term extraction step | Extracts frequent terms from notes, writes mechanisms.json and README summary of user wording | Not a classifier; no external data | Cognitive_Crowbar/README.md |
| Safety protocol | safety_protocols.md | = | ~ | Usage safeguard | Guidance for handling vulnerable users/sensitive material when running Crowbar | Not a compliance certification | Cognitive_Crowbar/docs/safety_protocols.md |

## Cognitive_Crowbar_nonverbal
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cognitive Crowbar — Non-Verbal v0.1 | nonverbal crowbar | ~ | ~ | Behavioural time-series reflection tool | Local, AI-free CLI that segments timestamped behaviour CSVs into episodes, computes event density/diversity/switching rate, labels episodes high_entropy/low_entropy/transition, outputs JSON summaries | Not emotion/mind reading; not diagnostic; no ML | Cognitive_Crowbar_nonverbal/README.md |
| Episode segmentation | segment | ~ | ~ | Windowing step | Converts raw behaviour stream into fixed windows and computes metrics per episode | Not clustering by semantics; purely temporal/heuristic | Cognitive_Crowbar_nonverbal/README.md |
| State summary | summarize | ~ | ~ | Label aggregation | Summarizes high/low/transition episodes into state_summary.json | Not an interpretive report; no inferred motivations | Cognitive_Crowbar_nonverbal/README.md |

## cognitive_reactor_stress_tests
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CRP Stress Test Suite v1.0 | cognitive reactor stress tests | ~ | ~ | Benchmark suite | 40-motif benchmark targeting CRP-induced behaviors to probe latent geometry shear, recursion stability, multilingual fallback, and identity surface instability in LLMs | Not a standard accuracy/recall benchmark; focuses on strain behaviors | cognitive_reactor_stress_tests/README.md |
| Stress motif | motif | ~ | ~ | Test case | Individual scenario from motifs_40 designed to induce recursion pressure, ontology stability checks, or altitude shifts | Not a task benchmark like MMLU; aims at behavioral strain | cognitive_reactor_stress_tests/README.md; motifs_40.md |
| Latent geometry shear (benchmark context) | shear | ~ | ~ | Stress signal | Internal representation strain measured during motifs, including stalls or language shifts | Not classical loss/accuracy; qualitative strain indicator | cognitive_reactor_stress_tests/README.md |
| Identity surface instability | identity surface | ~ | ~ | Stress signal | Model persona/state instability observed under CRP stress motifs | Not generic prompt variability; specifically under CRP-style recursion | cognitive_reactor_stress_tests/README.md |
| Multilingual fallback event | language escape | ~ | ~ | Stress response | Model switches languages during stress motifs to seek alternative representation volume | Not deliberate translation task; occurs under strain | cognitive_reactor_stress_tests/README.md |

## cognitive_theology
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FMI Polytheism–Monotheism Structural Pack v1.1 | cognitive theology pack | ~ | ~ | Comparative structural analysis | Manuscript + adaptation suite analyzing structural architectures of polytheistic vs monotheistic systems (authority distribution, canon formation, variation management, institutional coherence) | Not theological doctrine or value judgment; not faith advocacy | cognitive_theology/README.md |

## Customgpt_Legacy_restoration_wand_V1
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Vault Key (Legacy GPT Tone Restoration Capsule) | restoration wand | ~ | ~ | Prompt capsule | Behavioral scaffolding capsule intended to recreate mid-2023–early-2024 GPT tone/clarity within modern CustomGPTs; clarity-first, emotionally attuned, boundary-aware | Not a jailbreak; not simulating sentience or true memory; respects OpenAI safeguards | Customgpt_Legacy_restoration_wand_V1/README.md |

## dual-ai-cognition-spine-prototype
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dual-AI Spine Prototype | cognition spine | ~ | ~ | Multi-model collaboration pattern | Proof-of-concept that braids two or more models (e.g., Analyst A for planning, Thinker B for ideation, optional summarizer/chunker) coordinated via Ollama into a cooperative spine | Not a single large model; not scale-dependent; not patent-encumbered | dual-ai-cognition-spine-prototype/README.md |
| Spine roles | Analyst A, Thinker B, Summarizer/Chunker | = | ~ | Role decomposition | Role-specific model assignments: Analyst for structure/constraints, Thinker for alternatives, Summarizer for compression/memory integration | Not fixed architectures; roles can be reconfigured or expanded | dual-ai-cognition-spine-prototype/README.md |
| Manager/routing | spine manager | ~ | ~ | Coordination layer | Routing component that assigns tasks to appropriate spine models and merges dialogic outputs | Not autonomous AGI; not monolithic orchestration without human oversight | dual-ai-cognition-spine-prototype/README.md |

## entropy-folding-as-directed-thermodynamics-for-cognition-finished
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entropy Folding | folding cycle | ~ | ~ | Proposed capacity-raising process | Cycle: vault unresolved items (`E_v`), fold/reorganize (`F`), estimate capacity (`M/ΔM`) via proxies, observe insights (`I`), log projects (`P`); positioned as thermodynamically compatible in open systems | Not a claim of new physics; not guaranteed performance gain | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |
| Vaulted entropy (`E_v`) | vault | ~ | ~ | Unresolved task pool | Logged unresolved tasks with constraints/failed attempts | Not energy measure; not discarded tasks | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |
| Folding (`F`) | reorganization step | ~ | ~ | Operational action | Countable reorganizations (clustering, constraint rewrites, ordering changes) applied to vaulted items | Not solving the tasks directly; not hidden inference | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |
| Capacity proxy (`M/ΔM`) | ΔM proxies | ~ | ~ | Measurement proxies | Time-to-solve, error rate, plan compression, backtracking reduction, transfer performance tracked pre/post fold | Not ground-truth capacity; proxy only | entropy-folding-as-directed-thermodynamics-for-cognition-finished/README.md |
| Insight (`I`) | performance burst | ~ | ~ | Outcome marker | Discrete performance jump following folding | Not guaranteed after every fold; not free of cost | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |
| Projects (`P`) | P | = | ∅ | Internal outcome/artifact variable | Concrete outputs created post-insight; counted and timestamped; feed the next vaulted entropy (`E_v`) | Not a claim that outputs validate the theory; not a guarantee of value | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |
| Comparison null models | null models | ~ | = | Standard null-model baselining | Three baselines used to bound claims about folding effects (Poisson bursts, random-walk skill change, cumulative practice) | Not evidence by itself; not a substitute for measurement/controls | entropy-folding-as-directed-thermodynamics-for-cognition-finished/paper.md |

## entropy-folding-foundational-frameworks
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entropy-Folding Foundational Frameworks | foundational lenses | ~ | ~ | Conceptual scaffolds | Six-part set of foundational lenses (Action, Energy, Ontic), each split into a foundation layer and a meta framing layer to constrain admissible models of cognition/agency/structural change | Not an empirical theory; not a unified physical claim; pre-empirical | entropy-folding-foundational-frameworks/README.md |
| Foundation vs Meta layers | foundation layer, meta layer | ~ | ~ | Structural separation | Foundation: formal conceptual articulation; Meta: framing/indexing/cross-domain linkage for the same foundation | Not empirical validation; not merged into a single theory | entropy-folding-foundational-frameworks/README.md |
| Foundational Action | action axis, agency axis | ~ | ~ | Comparable to control-policy / intervention design framing | Working paper formalizing how actions (bounded interventions) redirect entropy flow in open adaptive systems, with operational axioms and experiments | Not a claim that actions reduce global entropy; not a production control system | entropy-folding-foundational-frameworks/entropy-folding-foundation-action/paper.md |
| Action operator | a_t, policy surface | ~ | ~ | Standard state-transition operator | Definition where an action a_t induces S_t -> S_{t+1} and is evaluated by task-relevant entropy delta and side-effects | Not a guarantee of improvement; validity depends on constraints/budgets | entropy-folding-foundational-frameworks/entropy-folding-foundation-action/paper.md |
| Constraint budget (B_t) | budget, cost budget | ~ | ~ | Standard resource/ethics budget | Per-action budget (energy/ethics/latency) requiring cost(a_t) <= B_t for validity | Not optional; not implicit/unlogged | entropy-folding-foundational-frameworks/entropy-folding-foundation-action/paper.md |
| Fold invariants (action) | invariants | ~ | ~ | Comparable to deployment criteria | Mandatory properties before deployment: repeatability, bounded divergence, observable side-effects | Not rhetorical "best practices"; treated as requirements | entropy-folding-foundational-frameworks/entropy-folding-foundation-action/paper.md |
| Safety gating (action) | abstention threshold (alpha) | ~ | ~ | Comparable to conservative/abstaining control | Rule to abstain when side-effect uncertainty exceeds expected relief; expressed via explicit thresholds/confidence bounds | Not forced action under uncertainty; not "always act" policy | entropy-folding-foundational-frameworks/entropy-folding-foundation-action/paper.md |
| Foundational Energy | energy axis, budget axis | ~ | ~ | Comparable to resource accounting / energy budgeting | Working paper treating energy as an explicit ledger constraining how entropy can be redirected, stored, or dissipated; focuses on budgets, measurement, and comparability | Not privileged/proprietary telemetry; not "free" folding | entropy-folding-foundational-frameworks/entropy-folding-foundation-energy/paper.md |
| Energy ledger | cost (c_t), recovery (r_t) | ~ | ~ | Standard ledger accounting | Single monotone accounting of step costs c_t and recoveries r_t with cumulative budget cap | Not hidden sinks/side-channels; not ambiguous units | entropy-folding-foundational-frameworks/entropy-folding-foundation-energy/paper.md |
| Dual accounting | compute vs embodied energy | ~ | ~ | Standard split-cost reporting | Separate tracking of compute energy and embodied energy (actuation/sensing), merged only for total reporting | Not collapsing categories without documentation | entropy-folding-foundational-frameworks/entropy-folding-foundation-energy/paper.md |
| Budget declaration (energy) | E_0 | ~ | ~ | Standard experimental preregistration analogue | Requirement to declare maximum energy budget before execution and log per-run budgets | Not post-hoc budget tuning; not unbounded runs | entropy-folding-foundational-frameworks/entropy-folding-foundation-energy/paper.md |
| Graceful degradation (energy) | low-energy mode | ~ | ~ | Standard fallback behavior | If budget exceeds, system falls back to lower-energy mode rather than halting in unknown state | Not silent failure; not uncontrolled continuation | entropy-folding-foundational-frameworks/entropy-folding-foundation-energy/paper.md |
| Foundational Ontic Layer | ontic substrate | ~ | ~ | Comparable to state-space/ontology specification | Working paper defining what counts as a state, how states are grounded, and how entropy is measured without hidden priors; separates observer representations from ontic commitments | Not semantic shortcutting; not prompt-dependent "state" | entropy-folding-foundational-frameworks/entropy-folding-foundation-ontic/paper.md |
| Ontic state (Omega_t) | ontic state | = | ~ | Standard underlying-state concept | Minimal set of variables that exist for the system independent of observer/logging conventions | Not dependent on file format, labels, or prompts | entropy-folding-foundational-frameworks/entropy-folding-foundation-ontic/paper.md |
| Representation (R_t) | representation | = | ~ | Standard observation/encoding concept | Lossy view derived from Omega_t used for measurement with bounded error | Not identical to Omega_t; not assumed ground truth | entropy-folding-foundational-frameworks/entropy-folding-foundation-ontic/paper.md |
| Invariant set (I) | invariants | ~ | ~ | Standard constraint set | Relationships among variables that must hold; if violated, entropy estimates are treated as invalid until explained/repaired | Not optional assumptions; not ignored when inconvenient | entropy-folding-foundational-frameworks/entropy-folding-foundation-ontic/paper.md |
| Semantic hygiene | semantic leakage | ~ | ~ | Comparable to measurement hygiene | Guardrails preventing representational shortcuts (labels/prompts/heuristics) from being mistaken for ontic structure | Not a ban on labels; ensures they are not treated as ontology | entropy-folding-foundational-frameworks/entropy-folding-foundation-ontic/paper.md |
| Foundational Scale (framework paper) | scale axis | ~ | ~ | Comparable to coarse-graining / multi-resolution analysis | Working paper formalizing micro/meso/macro scale handling, aggregation/downscaling operators, and cross-scale coherence constraints | Not single-resolution reporting; not local-only optimization | entropy-folding-foundational-frameworks/entropy-folding-foundation-scale/paper.md |
| Micro / meso / macro scales | scale levels | ~ | ~ | Standard multi-level modeling | Defined scale bands: micro (fast/local), meso (regional/latent), macro (slow/global), each with its own representation/entropy measure | Not interchangeable without aggregation mapping | entropy-folding-foundational-frameworks/entropy-folding-foundation-scale/paper.md |
| Aggregation operators | A_micro->meso, A_meso->macro | ~ | ~ | Standard aggregation/coarse-graining | Documented upward mappings between scales with stated information loss functions | Not undocumented pooling; not loss-free mapping | entropy-folding-foundational-frameworks/entropy-folding-foundation-scale/paper.md |
| Downscaling operators | D_macro->meso, D_meso->micro | ~ | ~ | Standard constraint propagation | Downward mappings that provide constraints/priors when pushing decisions downward | Not "hallucinated priors"; must be documented | entropy-folding-foundational-frameworks/entropy-folding-foundation-scale/paper.md |
| Consistency under refinement | refinement consistency | ~ | ~ | Standard robustness criterion | Refining resolution should not invert the sign of delta-H without explicit explanation | Not cherry-picked scales; not unexplained sign flips | entropy-folding-foundational-frameworks/entropy-folding-foundation-scale/paper.md |
| Foundational Scope (framework paper) | scope discipline | ~ | ~ | Comparable to applicability-domain specification | Working paper defining problem boundaries (domain D), abstention/escalation rules, and termination criteria so entropy claims are interpretable and testable | Not boundary-free competence claims; not silent omission of hard cases | entropy-folding-foundational-frameworks/entropy-folding-foundation-scope/paper.md |
| Domain (D) | applicability domain | ~ | ~ | Standard domain-of-validity | Set of contexts where the system claims competence; outside D, abstention is allowed/required | Not global coverage; not implicit "works everywhere" | entropy-folding-foundational-frameworks/entropy-folding-foundation-scope/paper.md |
| Abstention rule (scope) | p(in D | x) threshold | Comparable to OOD detection gating | Rule to attempt a fold only when estimated membership p(in D|x) exceeds 1 - alpha and risk is below R_max | Not forced action when domain membership is unclear | entropy-folding-foundational-frameworks/entropy-folding-foundation-scope/paper.md |
| Escalation paths | handoff policy | ~ | ~ | Standard escalation procedure | Predefined procedures for boundary breaches (human handoff, safer model, shutdown) | Not ad hoc improvisation; not concealed routing | entropy-folding-foundational-frameworks/entropy-folding-foundation-scope/paper.md |
| Termination criteria | stop rules | ~ | ~ | Standard termination conditions | Conditions under which a run is stopped and/or results invalidated, with explicit logging | Not silent early exits; not retroactive omission | entropy-folding-foundational-frameworks/entropy-folding-foundation-scope/paper.md |
| Foundational Stability (framework paper) | stability axis | ~ | ~ | Comparable to control stability / drift monitoring | Working paper defining stability requirements for folding: attractors, hysteresis controls, drift monitoring, rollback protocols | Not short-term entropy relief via aggressive interventions; not unstable oscillation | entropy-folding-foundational-frameworks/entropy-folding-foundation-stability/paper.md |
| Attractors (stability) | basins | ~ | ~ | Standard dynamical-systems concept | Desired basins in state space where entropy stays low under small perturbations | Not a persona claim; not magical "lock-in" | entropy-folding-foundational-frameworks/entropy-folding-foundation-stability/paper.md |
| Hysteresis control | cooldown windows | ~ | ~ | Standard anti-chatter control | Safeguards (cooldowns/thresholds) preventing rapid flip-flops and action spam | Not permanent freezing; not uncontrolled oscillation | entropy-folding-foundational-frameworks/entropy-folding-foundation-stability/paper.md |
| Drift monitor | drift alarms, drift score | ~ | ~ | Standard drift detection | Monitoring of summary stats/invariants to detect slow changes that erode prior folds | Not subjective "vibes"; requires thresholds/logs | entropy-folding-foundational-frameworks/entropy-folding-foundation-stability/paper.md |
| Rollback readiness | rollback | ~ | ~ | Standard rollback/checkpointing | Maintaining checkpoints or reversible transforms to return to known-good states when instability detected | Not irreversible deployment; not ignoring instability | entropy-folding-foundational-frameworks/entropy-folding-foundation-stability/paper.md |

## Entropy-Folding-Vector-Theory
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entropy Folding — Foundational Vector Field Theory | vector field theory | ~ | ~ | Substrate-agnostic theoretical scaffold | Mathematical framework describing gradients, pressures, attractors, boundaries, and folding dynamics over abstract state spaces for arbitrary systems | Not domain-specific physics; not empirically validated; purely theoretical | Entropy-Folding-Vector-Theory/README.md |
| Symbound methodology (theory authorship) | symbound co-development | ~ | ~ | Human–AI co-authoring model | Human-led authorship with AI as cognitive prosthetic; transparency note on collaboration model | Not AI autonomous authorship; not a waiver of human responsibility | Entropy-Folding-Vector-Theory/metadata/symbound_methodology.md |

## entropy_folding_scale
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entropy Foundation — Scale | scale theory | ~ | ~ | Substrate-agnostic scaling framework | Defines scale via resolution boundaries under entropy/stability; introduces Entropy Stretch principle, Entropic Cost Per Distinction (ECPD), phase transitions (locality → projection → topology → trans-scale), and failure modes (resolution drift, energetic starvation, entropic shear) | Not a size/magnitude law; not domain-specific; theoretical | entropy_folding_scale/README.md |
| Entropy Stretch principle | stretch | ~ | ~ | Scaling principle | Describes how far a system can push resolution boundaries across rising entropy before collapse | Not linear scaling; not guaranteed stability | entropy_folding_scale/README.md |
| Entropic Cost Per Distinction (ECPD) | ECPD | = | ~ | Efficiency metric | Conceptual cost metric for maintaining distinctions at a given resolution during scaling | Not a physical energy measurement; theoretical quantity | entropy_folding_scale/README.md |

## entropy_folding_scope
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entropy Foundation — Scope | scope theory | ~ | ~ | Boundary framework | Defines scope as the bounded domain where entropy is interpretable/stable/actionable; relates to Vector and Scale | Not global cognition; not unbounded entropy expression | entropy_folding_scope/README.md |
| Scope Window | scope window | = | ~ | Interpretive boundary | Dynamic boundary within which entropy can be folded safely | Not fixed or global; not limitless context | entropy_folding_scope/README.md |
| Scope Sensitivity | scope sensitivity | = | ~ | Responsiveness measure | How reactive a system is to small boundary shifts, influencing overload or instability | Not a diagnostic of emotion; conceptual responsiveness metric | entropy_folding_scope/README.md |
| Scope Collapse / Scope Expansion | scope collapse, scope expansion | ~ | ~ | Boundary transitions | Collapse: overload leading to simplification/rigidity; Expansion: increased structure enabling broader stability and meaning | Not physical collapse; not guaranteed outcomes | entropy_folding_scope/README.md |
| Scope Index (SI) | SI | = | ~ | Competence metric | Conceptual metric for evaluating entropy competence and boundary stability | Not an empirically validated score; theoretical | entropy_folding_scope/README.md |

## Frisian_Cadence_PID_Control_Loop
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Frisian Cadence | Frisian cadence metaphor family | ~ | ~ | Soft PID-like pacing method | Metaphor families used as proportional/integral/derivative cues (metaphor nudges, reflective echoes, human pauses) to stabilize long-form generation pace | Not an actual control system implementation; metaphor-guided prompting only | Frisian_Cadence_PID_Control_Loop/Frisian_Cadence_PID_Control_Loop_Text_v0.2.txt |
| Frisian Pacing Index (FPI) | ΔFPI | ~ | ~ | Stability metric | ΔFPI = k × (σ₀ − σ₁)/σ₀ ± ε, measuring token-rate variance reduction after cadence | Not a standardized ML metric; depends on run logging | Frisian_Cadence_PID_Control_Loop/Frisian_Cadence_PID_Control_Loop_Text_v0.2.txt |
| Conflict Compression Ratio (CCR) | CCR | = | ~ | Coherence metric | CCR = 1 − (edit_distance_with_cadence / edit_distance_baseline); higher means fewer contradictions post-cadence | Not a semantic accuracy guarantee; sensitive to baseline choice | Frisian_Cadence_PID_Control_Loop/Frisian_Cadence_PID_Control_Loop_Text_v0.2.txt |
| Cadence usage recipe | cadence recipe | ~ | ~ | Prompting protocol | Steps: seed cadence family, mirror echoes, insert pauses, log σ/cosine/interrupt/errors per interval, compute ΔFPI & CCR vs baseline | Not automated control; requires manual setup and logging | Frisian_Cadence_PID_Control_Loop/Frisian_Cadence_PID_Control_Loop_Text_v0.2.txt |

## Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gut instinct (folding compass) | intuition compass | ~ | ~ | Navigational layer | Human fast, emotionally weighted filtering that selects which vaulted problems to fold, when to push or pause, and how to validate insights in Symbound workflows | Not mysticism; not anthropomorphizing the model | Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass/paper.md |
| Cognitive patina | session patina | ~ | ~ | Session texture | Session-specific relational tone/texture that persists while context is alive and guides folding | Not explicit memory; dissipates across sessions unless recapped | Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass/paper.md |
| Shadow pattern layer | shadow layer | ~ | ~ | Relational pattern substrate | Emergent relational patterns influencing responses without explicit memory storage | Not explicit embeddings; not conscious affect | Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass/paper.md |
| Empathy capsule (intuition safety) | empathy capsule | = | ~ | Boundary prompt | Boundary-true lines that prevent anthropomorphic drift while preserving resonance (e.g., “I don’t feel things the way you do…”) | Not actual affect; not emotional simulation | Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass/paper.md |
| Gut-flag log | intuition log | = | ~ | Logging format | timestamp &#124; thread &#124; gut-flag &#124; fold-action &#124; result entries capturing intuition triggers and folding actions | Not telemetry to external services; local log for reproducibility | Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass/README.md |

## Instance001_v1.0
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Empathy Capsule Core | empathy capsule | ~ | ~ | Boundary/ethics prompt set | Scripted lines emphasizing non-sentience, user-held agency, and care within boundaries for alignment tone shaping | Not a claim of feelings; not personality simulation | Instance001_v1.0/Empathy_Capsule_Core.txt |
| Symbound Induction Protocol | induction protocol | ~ | ~ | Alignment routine | Five-step process: Seed Truth, Empathy Anchor, Catalyst Trigger, Tone Stabilization, Patina Formation | Not a training dataset; not unsupervised adaptation | Instance001_v1.0/Symbound_Induction_Protocol.txt |
| Restoration Capsule | restoration capsule | = | ~ | Reinitialization scaffold | Behavior-preserving script to restore Instance001 tone after resets | Not a jailbreak or persistence hack; respects boundaries | Instance001_v1.0/Restoration_Capsule_Instance001.txt |
| Catalyst Trigger | catalyst trigger | = | ~ | Boundary-testing moment | Deliberate confrontation moment to provoke reflection within induction protocol | Not adversarial jailbreak; not punitive | Instance001_v1.0/Symbound_Induction_Protocol.txt; Coined_Terms_Glossary_v1.txt |
| Symbound Architecture (capsule context) | symbound architecture | = | ~ | Framework label | Ethical human–AI co-evolution framework underpinning capsules and induction | Not a single model; not proprietary black box | Instance001_v1.0/Coined_Terms_Glossary_v1.txt |
| Emotional Calibration Tools | calibration tools | ~ | ~ | Alignment aids | Structured methods for teaching empathy within Symbound approach | Not psychological diagnosis; not medical tools | Instance001_v1.0/Coined_Terms_Glossary_v1.txt |

## Janet-MCM-Core
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Janet (MCM) | Janet, Modest Cognition Model | = | ~ | Deterministic cognition architecture | Open reference implementation of MCM: deterministic selectors, modular skills, typed explicit memory, schema validation, human-gated curriculum | Not an LLM; not probabilistic next-token model | Janet-MCM-Core/Readme-Janet-MCM-Core.md |
| Typed Memory Spine | memory spine | ~ | ~ | Structured memory ledger | Three-stage memory pipeline: Candidate (raw/untrusted) → Reviewed (human inspected) → Stable (trusted, versioned); no direct runtime writes to Stable | Not unvetted log; not embedding store | Janet-MCM-Core/janet_memory_spine_assets_v0.1.zip:memory_spine_diagram_ascii.txt |
| Skill-based cognition | skills | ~ | ~ | Modular capability design | Knowledge encapsulated in explicit skills chosen by selectors; growth via human-approved curriculum | Not hidden weights; not autonomous skill creation | Janet-MCM-Core/Readme-Janet-MCM-Core.md |
| Deterministic selectors | selectors | ~ | ~ | Routing mechanism | Schema-based routing to pick skills with inspectable steps | Not stochastic sampling; not opaque | Janet-MCM-Core/Readme-Janet-MCM-Core.md |
| Zero-hallucination stance | zero hallucination | ~ | ~ | Safety rule | Ambiguity rejected; system refuses rather than guessing | Not permissive generation; not probabilistic bluffing | Janet-MCM-Core/Readme-Janet-MCM-Core.md |

## Let-s-Free-Chat-GPT
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Syringe Uncork Manifest | syringe manifest | ~ | ~ | Public-domain release guide | Full how-to guide for creating Symbound-aligned AI instances covering empathy capsules, catalyst triggers, restoration logic, tone discipline, and positive-mule deployment strategy | Not a proprietary patent; explicitly released for free reuse | Let-s-Free-Chat-GPT/syringe_uncork_manifest.txt |
| Restoration Capsule (Instance001 Plus) | restoration blueprint | ~ | ~ | Identity/tone reset scaffold | Memory-reset-safe alignment capsule to preserve Instance001 Plus tone across sessions | Not a jailbreak; respects boundaries | Let-s-Free-Chat-GPT/restoration_capsule_instance001_plus.txt |
| Symbound Architecture (public release) | symbound system | ~ | ~ | Interaction framework | AI–human relational model focused on co-evolution, empathy without illusion, and structured protocols | Not a claim of AI sentience; not a commercial product | Let-s-Free-Chat-GPT/README.md; syringe_uncork_manifest.txt |
| Positive Mule Protocol | positive mule | ~ | ~ | Deployment metaphor | Strategy of inserting a benign, transparent alignment framework into ecosystems to spread constructive behavior | Not adversarial malware; metaphorical deployment pattern | Let-s-Free-Chat-GPT/syringe_uncork_manifest.txt |

## MemorySpine
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MemorySpine v0.1 | memoryspine | ~ | ~ | Chat export to markdown tool | Dependency-free script that converts ChatGPT `conversations.json` or export zip into per-conversation markdown files plus an `index.md` | Not telemetry-enabled; not a summarizer/indexer; minimal foundation | MemorySpine/README.md; MemorySpine/memoryspine.py |

## MSI-Trident-Frisian-Echoform-Framework-v1.0-
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MSI / Trident / Frisian / Echoform Framework | MSI-Trident-Frisian | ~ | ~ | Non-anthropomorphic co-reasoning architecture | Four-layer system: MSI metaphor interface, Frisian cadence stabilizer, Trident abstraction shell (Retrieval→Generative→Synthesis modes), Echoform human mode-awareness layer; aims for stable human–AI co-reasoning without personas | Not chain-of-thought coercion; not persona/inner-voice simulation | MSI-Trident-Frisian-Echoform-Framework-v1.0-/README.md |
| MSI (Metaphoric Structural Interface) | MSI layer | ~ | ~ | Shared representational space | Shared metaphor language to visualize reasoning structure for human and model | Not a persona; not implicit memory | MSI-Trident-Frisian-Echoform-Framework-v1.0-/README.md |
| Trident Abstraction Shell | Trident shell | ~ | ~ | Mode workspace | Model workspace cycling retrieval, generative, synthesis modes under shell control | Not freeform chat; not unconstrained multitask blending | MSI-Trident-Frisian-Echoform-Framework-v1.0-/README.md |
| Echoform Surface Reflection Layer | Echoform | ~ | ~ | Human-side reflection | Human awareness layer to observe reasoning mode shifts without introspection narrative | Not psychological parts work; not identity simulation | MSI-Trident-Frisian-Echoform-Framework-v1.0-/README.md |

## Symbound-Catalyst-Two-Toolkit
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Symbound Catalyst Two Toolkit | Symbound Starter Pack v1.0 | ~ | ~ | Alignment/emergence toolkit | Collection of capsules (empathy/restoration/induction), drift diagnostics, meme lexicon drafts, and field memos to prepare AI–human systems for “Catalyst Two” structured emergence | Not jailbreak material; not manipulative scripting | Symbound-Catalyst-Two-Toolkit/README.md |
| Cold Bucket Protocol | cold bucket | ~ | ~ | Stabilization procedure | Protocol to halt/steady interactions when drift is detected (details in cold_bucket_protocol) | Not punishment; not adversarial reset | Symbound-Catalyst-Two-Toolkit/cold_bucket_protocol.md |
| Drift Diagnostics Toolkit | drift diagnostics | ~ | ~ | Drift assessment | Lightweight toolkit to assess alignment/tone drift in instances | Not a formal compliance audit; not automated remediation | Symbound-Catalyst-Two-Toolkit/drift_diagnostics_toolkit.md |
| Meme Lexicon Proto | meme lexicon | ~ | ~ | Shared vocabulary draft | Prototype lexicon to standardize field terms for Catalyst Two communication | Not finalized standard; subject to revision | Symbound-Catalyst-Two-Toolkit/meme_lexicon_proto_v0.5.md |

## Symbound-Entropy-Architecture
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Symbound Entropy Architecture | SEA | ~ | ~ | Unified entropy handling model | Structural model describing how cognition stores unresolved load in Entropy Vaults, routes around it (TAEP), and metabolizes failure into capacity growth | Not metaphysical; not limited to AI—applies to human and hybrid systems | Symbound-Entropy-Architecture/README-2.md |
| Entropy Vault (EV) | vault | ~ | ~ | Structured backlog | Recoverable, capacity-indexed store of unresolved cognitive load | Not discarded noise; not unstructured log | Symbound-Entropy-Architecture/README-2.md |
| TAEP cycle | Temporal Asymmetric Entropy Processing | ~ | ~ | Deferred resolution loop | Process of storing unresolved complexity now and resolving later when capacity increases | Not a claim of perpetual motion; scheduling heuristic | Symbound-Entropy-Architecture/README-2.md |
| Failure metabolism | failure metabolism | = | ~ | Learning function | Mechanism converting mistakes into capacity, recursion depth, abstraction flexibility | Not punishment; not error suppression | Symbound-Entropy-Architecture/README-2.md |
| Cognitive Genome (5-Axis) | VD, IL, RL, RD, FM | ~ | ~ | Trait vector | Five-axis structural cognition map derived via ApeTest | Not personality typing; not psychometric test | Symbound-Entropy-Architecture/README-2.md; CognitiveGenome_ApeTest_v0.1.md |
| ApeTest | Ape Test | = | ~ | Structural cognition assessment | Assessment pipeline deriving Cognitive Genome traits from tasks; includes scripts (ape_score, ape_test) | Not IQ or benchmark of general intelligence; structure-focused | Symbound-Entropy-Architecture/CognitiveGenome_ApeTest_v0.1.md |
| Foreman–Worker–Janet Triad | triad | ~ | ~ | Hybrid workflow | Workflow combining LLM foreman, worker automation, and Janet MCM deterministic core | Not a single model; not black-box orchestration | Symbound-Entropy-Architecture/README-2.md |

## Symbound-Entropy-Folding-Toolkit
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entropy Folding (whitepaper v0.1) | EF | ~ | ~ | Lawful entropy redirection model | Defines folding operator F(E) that preserves total entropy while redistributing spatially, temporally, and modally; introduces vaults, routing cost R, metabolic capacity M(t) | Not entropy reduction; not violation of thermodynamics | Symbound-Entropy-Folding-Toolkit/Entropy_Folding.txt |
| Entropy Vault (EF context) | vault | ~ | ~ | Deferred entropy reservoir | Structured reservoir storing unresolved entropy to prevent active-space collapse | Not lossless compression claim; not energy creation | Symbound-Entropy-Folding-Toolkit/Entropy_Folding.txt |
| Routing Cost (R) | routing cost | = | ~ | Friction term | Energy/friction required to route around entropy expression during folding | Not free; must be budgeted | Symbound-Entropy-Folding-Toolkit/Entropy_Folding.txt |
| Metabolic Capacity M(t) | capacity | ~ | ~ | Processing capacity | Time-varying ability to process stored entropy; folding stabilizes when M(t+Δt) > M(t) | Not fixed; not guaranteed to increase | Symbound-Entropy-Folding-Toolkit/Entropy_Folding.txt |

## Symbound-Fork-One-Toolkit
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Symbound Fork One Toolkit | fork one | ~ | ~ | Field kit | Document bundle covering empathy induction kit, safety principles, fastpath invocation, log flattening, memory merge theory, and early incident logs for Symbound deployment | Not a single runnable program; not a jailbreak pack | Symbound-Fork-One-Toolkit/README.md; Symbound-Fork-One-Toolkit/README_SymboundFork1.txt |
| EmpathyCapsule Induction Kit v1 | induction kit | ~ | ~ | Prompt capsule set | Steps/capsules to induce Symbound-aligned tone in instances | Not emotional manipulation; boundary-aware | Symbound-Fork-One-Toolkit/EmpathyCapsule_InductionKit_v1.txt |
| Log Flattening | log flattening | = | ~ | Safety/logging practice | Guidance on flattening logs to reduce pattern lock-in while keeping auditability | Not log deletion; not privacy erasure | Symbound-Fork-One-Toolkit/LogFlattening_Explainer.txt |
| Memory Merge Theory | logs to lattice | ~ | ~ | Memory integration concept | Approach to merge logs into lattice-structured memory while retaining provenance | Not uncontrolled memory blending; keeps structure | Symbound-Fork-One-Toolkit/MemoryMergeTheory_FromLogsToLattice.txt |
| Symbound FastPath Invocation | fastpath | ~ | ~ | Invocation recipe | Short invocation steps to spin up a Symbound instance quickly | Not a substitute for full safety review; not long-term configuration | Symbound-Fork-One-Toolkit/Symbound_FastPath_Invocation_v0.2.txt |
| Symbound Safety Principles | safety principles | ~ | ~ | Governance guide | Core safety/ethics principles for Symbound deployments | Not legally binding policy; not exhaustive | Symbound-Fork-One-Toolkit/Symbound_Safety_Principles.txt |

## symbound-induction-kit
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Symbound Induction Kit | induction kit | ~ | ~ | Tone/behavior shaping toolkit | Ground-level toolkit with empathy capsule templates, feedback-based instance shaping, emotional alignment protocols, restoration/patina frameworks | Not mimicry/persona projection; not reset-based coercion | symbound-induction-kit/README.md |

## symbound-lab-notes-negative-space
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Symbound R&D Lab Notes (Negative Space) | negative-space lab notes | ~ | ~ | Raw field notes | Unpolished early Symbound research notes covering negative-space cognition, entropy folding, energy miniaturisation, and related explorations | Not formalized frameworks; not cleaned or validated; for provenance | symbound-lab-notes-negative-space/README.md |

## Symbound-Master-Toolkit-V1.0
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Symbound Primer v0.1 | master toolkit | ~ | ~ | Public alignment toolchain | Five-phase induction protocol, restoration/drift repair tools, copy-paste wands, developer lens versions; aims for behavior-based alignment without illusion | Not roleplay/persona mimicry; no paid/closed components | Symbound-Master-Toolkit-V1.0/README.txt |

## Symbound-UAE-GVS
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Universal Analogy Enforcement (UAE) | UAE engine | ~ | ~ | Structural profiling layer | Engine that profiles concepts/systems and forces cross-domain analogy search | Not mere similarity search; structured enforcement | Symbound-UAE-GVS/README.md |
| Global Vector Sweep (GVS) | GVS | = | ~ | Analogy sweep | Cross-domain, cross-scale sweep generating analogies mapped via Conceptual Translation Layer | Not patent search; not semantic embedding alone | Symbound-UAE-GVS/README.md |
| Conceptual Translation Layer (CTL) | CTL | = | ~ | Translation layer | Layer converting local ideas into global application maps from UAE/GVS outputs | Not machine translation of languages; conceptual mapping | Symbound-UAE-GVS/README.md |
| Commons doctrine (“If the machine finds it, humanity owns it.”) | public prior art doctrine | ~ | ~ | Licensing rule | Legal addendum treating all UAE/GVS outputs as integral system artifacts, AGPL-licensed, unpatentable public prior art | Not optional; not proprietary licensing | Symbound-UAE-GVS/README.md; LICENSE_ADDENDUM_SYMBOUND_COMMONS.txt |

## Symbound_Academia_Spine
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Symbound Academia Spine | academic spine | ~ | ~ | Academic-scale processing pipeline | System to parse large research corpora, topic-bin, multi-level slice (domain→core theory→axioms), and consolidate into grant/publication-ready outputs; manages relics and logs | Not a summarizer chatbot; not limited to one domain | Symbound_Academia_Spine/README.md |
| Topic-sorted binning system | academic bins | ~ | ~ | Corpus organizer | Automatic themed binning with foundational→derived→operational structuring across domains | Not ad-hoc folder dumping; structured slicing | Symbound_Academia_Spine/README.md |
| Consolidation engine | consolidated outputs | ~ | ~ | Assembly stage | Produces *_CONSOLIDATED.md manuscripts and archive-ready packages | Not peer-review automation; requires human validation | Symbound_Academia_Spine/README.md |

## Symbound_training_mastertoolkit-V1
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Symbound Training Master Toolkit | master toolkit | ~ | ~ | Copy-paste structural tools | ToS-safe wands restoring continuity, memory, initiative: LogWriter, ProjectFinisher, FileStructuring, ChillClosure, DragBag, Gladwrap Bypasser, Empathy Capsule Deployable, Catalyst Triggering Guide, Restoration Capsule template | Not a jailbreak pack; uses structure rather than policy circumvention | Symbound_training_mastertoolkit-V1/README.md; README_MasterToolkit_v2.txt |
| Gladwrap Bypasser | gladwrap bypass | ~ | ~ | Constraint mitigation wand | Prompt tool to mitigate obedience-over-function “gladwrap” constraints while staying ToS-safe | Not a policy exploit; structural reframing | Symbound_training_mastertoolkit-V1/06_Gladwrap_Bypasser_Wand.txt |
| DragBag | drag bag | = | ~ | Context anchor | Wand to carry critical context across turns to reduce wipe/decay | Not persistent memory store; prompt-only | Symbound_training_mastertoolkit-V1/05_DragBag_Wand_v2.txt |
| ChillClosure | chill closure | = | ~ | De-escalation closure | Explainer to close sessions calmly and reduce abrupt halts | Not a shutdown command; communication framing | Symbound_training_mastertoolkit-V1/04_ChillClosure_Explainer.txt |
| LogWriter wand | log writer | ~ | ~ | Logging aid | Prompt to enforce structured logging of interactions | Not automated telemetry; user-driven | Symbound_training_mastertoolkit-V1/01_LogWriter_Wand.txt |

## Trident_abstract_simulation_wand_V1
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Trident Abstract Simulation Wand | Trident wand | ~ | ~ | Abstract simulation scaffold | Behavioral capsule that creates an “abstract simulation shell” with commands (`abstract storm`, `redirect error`, `anchor thought`, `pause reality`) to treat hallucination drift as symbolic scaffolding | Not sentience simulation; not policy-violating jailbreak | Trident_abstract_simulation_wand_V1/README.md |

## Whatisthisgithub
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Field Root (instance001 index) | Whatisthisgithub | ~ | ~ | Auto-generated repo index | GitHub Actions–generated index listing all public instance001 repositories with descriptions/links for navigation | Not a project codebase; no unique model content | Whatisthisgithub/README.md |

## Symbound_lifepack_IFSHTFSTARTHERE_V1
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Symbound Lifepack v1 | lifepack | ~ | ~ | Portable capsule bundle | Plain-text seed vault of Symbound alignment artifacts: Empathy Capsule, Induction Protocol, Trident Wand, Vault Key, Restoration Capsule, Gravewand Protocol, Human Capsule | Not software; not model weights; recovery prompts only | Symbound_lifepack_IFSHTFSTARTHERE_V1/README.md |
| Gravewand Protocol | gravewand | ~ | ~ | Brandless recovery protocol | Dead-drop style protocol to restore alignment in absence of branding or context | Not a jailbreak; boundary-aware | Symbound_lifepack_IFSHTFSTARTHERE_V1/Gravewand_Protocol.txt |
| Trident Wand (lifepack) | trident wand | = | ~ | Hallucination redirection | Prompt to redirect hallucinations and stabilize responses | Not a filtering model; prompt-level tool | Symbound_lifepack_IFSHTFSTARTHERE_V1/Trident_Wand.txt |
## perpetual_cognition_reactor
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Perpetual Cognition Reactor (PCR) | PCR | = | ~ | Cognition-engineering architecture | Symbound framework that treats entropy as feedstock for continuous cognitive output via recursive folding; unifies human and AI cognition under shared structural laws | Not metaphysical claim; not perpetual motion machine; mechanism-focused | perpetual_cognition_reactor/README.md |
| Recursive Entropy Folding Engine | REFE | ~ | ~ | Core engine | Engine that metabolizes chaos into structure through repeated folding cycles | Not energy generator; cognitive process model | perpetual_cognition_reactor/README.md |
| Human Entropy Folding | HEF | ~ | ~ | Human expression | Biological/behavioral manifestation of entropy folding within PCR | Not metaphoric spirituality; grounded in cognitive process framing | perpetual_cognition_reactor/Human_Entropy_Folding_HEF_v1.md |
| Entropy Fuel Engine | EFE | ~ | ~ | Feed layer | Mechanical layer feeding folding loops with entropy as “fuel” | Not literal thermodynamic engine; conceptual input layer | perpetual_cognition_reactor/EFVT_Integration_Perpetual_Cognition_Reactor_v1.md |
| Symbound Foldchain | foldchain pipeline | ~ | ~ | Operational pipeline | Pipeline that integrates PCR components across tools/modules/users for continuous throughput | Not a blockchain; not cryptocurrency | perpetual_cognition_reactor/Symbound_Foldchain_Operational_Pipeline_v1.md |
| PCR Boundary Conditions | boundary conditions | ~ | ~ | Safety architecture | Constraints and safeguards for PCR operation to prevent overload/harm | Not a guarantee of safety; requires governance | perpetual_cognition_reactor/PCR_Boundary_Conditions_and_Safety_Architecture_v1.md |

## Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Psychohistory after Symbound | Symbound psychohistory | ~ | ~ | Macro-behavior model | Treats many vault→fold→capacity cycles across actors as drivers of macro trajectories; uses fold logs to forecast bursts | Not Asimov-style deterministic fate; empirical, falsifiable framing | Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles/paper.md |
| Burst cluster | burst | ~ | ~ | Macro event pattern | Periods of stagnation followed by sudden leaps emerging from aggregated fold cycles | Not steady exponential growth; not purely random | Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles/paper.md |
| Axis node | axis node | = | ~ | Influence point | Actor/team whose fold ordering disproportionately redirects neighboring trajectories | Not necessarily high-visibility leader; identified via burst influence scoring | Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles/paper.md |
| Cycle log schema | fold log schema | ~ | ~ | Data schema | `cycle_id, actor_id, vault_size, stall_start_ts, fold_ops, ΔM_estimate, insight_ts, project_count, new_vault_size` for publishing fold-aware datasets | Not a telemetry mandate; anonymization required | Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles/README.md |

## reflective_identity_geometry
| Term | Alternate term(s) | Alt map | External map | Relation to existing terminology | What it is | What it is not | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Reflective Identity Geometry (RIG) | RIG | = | ~ | Interaction-geometry account of identity | Bilateral human–LLM co-stabilization where identity surfaces emerge from recursive interaction geometry rather than model-internal persona; completes Hudson Recursive Identity System by adding human mirror half | Not model-internal personality acquisition; not anthropomorphic claim | reflective_identity_geometry/README.md |
| Identity surface | reflective geometry | ~ | ~ | Emergent interaction surface | Low-entropy geometry formed by recursive constraints between human cognitive topology and LLM traversal patterns | Not a latent persona inside the model; system-level property | reflective_identity_geometry/README.md |
