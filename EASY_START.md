# Easy Start Guide

This file is the practical route-map for new visitors.

The full repo index is broad and fast-moving. This guide is here to answer a simpler question:

**"Given what I care about, where should I actually start?"**

## First Three Stops

If you are completely new here, start in this order:

1. `README.md`
2. `GLOSSARY.md`
3. `EASY_START.md`

If you prefer the practical route first, you can also do:

1. `EASY_START.md`
2. `README.md`
3. `GLOSSARY.md`

If the terminology still feels dense after that:

- `GLOSSARY_FULL.md` = wider tables / fuller format
- `AMBIGUITIES.md` = terms that are still not fully pinned down

## Quick Read of the Landscape

Very roughly, this ecosystem has five big zones:

- Local-first AI tools you can use or build on
- Model-behaviour and human-AI interaction frameworks
- Cognition / taxonomy / profiling research
- Entropy-folding theory and companion papers
- Older Symbound-era toolkits and archived historical material

If you only want the current, most active entry points, stay mostly in the first two zones.

## Best Entry Points

| If you are here for... | Start with | Then look at | Why this is the right first stop |
| --- | --- | --- | --- |
| The overall corpus at a glance | `README.md` in `Whatisthisgithub` | `EASY_START.md`, `ABOUT_FRACTAL_MEDIA_INFRASTRUCTURE` | Best high-level orientation before choosing a lane. |
| Everyday local AI desktop assistant | `chatty-cog` | `chatty-edu`, `chatty-art`, `chatty-factory` | `chatty-cog` is the current general local assistant shell and the clearest "daily-use" surface. |
| Education-focused offline assistant | `chatty-edu` | `chatty-edu-user`, `chatty-cog` | `chatty-edu` is the source repo; `chatty-edu-user` is the easier prebuilt user release. |
| Click-and-run Windows release | `chatty-edu-user` | `chatty-edu` | Best first stop if you want something runnable without first building from source. |
| Local image / GIF / video / audio generation | `chatty-art` | `chatty-lora`, `ecg_window` | `chatty-art` is the current media-generation front door. |
| Local-first mobile pet / care toy | `chatty-pet` | `rd-engine`, `chatty-quest` | Best first stop if you want a small local-first consumer app showing the newer reducer-governed UI/game-loop doctrine in a lighter mobile form. |
| Local LoRA training / dataset curation | `chatty-lora` | `chatty-art` | Start here if the goal is training, dataset cleanup, or Wan/Musubi plan prep. |
| Local LLM build suite: tweaking, quantizing, training | `nanochat-llm-tweaker` | `chatty-lora`, `chatty-cog` | Best first stop if you want a guided local suite for corpus prep, tokenizer work, base-model training, quantization, checkpoint testing, and related builder workflows. |
| Plain-language software generation / patching | `chatty-factory` | `chatty-cog`, archived `chattyfactory` | Current project-factory surface; use this, not the older similarly named archive, for present-day direction. |
| How to work better with AI in general | `ai-teaming-framework` | `model-behaviour-toolkit` | `ai-teaming-framework` is the clearest beginner-to-advanced interaction guide. |
| Provider-neutral prompting / drift recovery / better sessions | `model-behaviour-toolkit` | `ai-teaming-framework`, `chatty-cog` | Best modernized prompt-and-behaviour toolkit in the corpus. |
| Honest tiny activity monitor for local jobs | `ecg_window` | `chatty-art`, `chatty-lora`, `chatty-cog` | Small, self-contained, practical utility repo. |
| Lightweight offline export utility | `MemorySpine` |  | Narrow, useful, and easy to understand quickly. |
| Game / modding / deterministic adventure engine | `chatty-quest` | `rd-engine`, `chatty-art` | `chatty-quest` is the current game-facing front door; `rd-engine` is the smaller reusable state core underneath that lane. |
| Small experimental sandbox | `chattydoom` | `chatty-quest` | Good if you want something hackable and less theory-heavy. |
| Reducer-governed state core / reusable substrate | `rd-engine` | `llm-defined-persistent-memory`, `semantic-signal-alphabet`, `chatty-quest` | Best first stop if you want the smallest reusable core behind the newer memory and deterministic engine line. |
| Local semantic dataset sorting / bucket workbench | `llm-semantic-dataset-sorter` | `semantic-signal-alphabet`, `rd-engine`, `llm-defined-persistent-memory` | Best first stop if you want an operator-facing tool for fixed-budget semantic partitioning, junk handling, and dataset structure review. |
| Model suitability testing / cognitive fingerprinting | `cognition-mesh-test-chamber` | `llm-semantic-dataset-sorter`, `rd-engine` | Best first stop if you want contained local evaluation that maps model-host-task meshes into failure logs, negative lanes, and suitability profiles rather than leaderboard scores. |
| Model-native persistent memory design | `llm-defined-persistent-memory` | `rd-engine`, `semantic-signal-alphabet`, `chatty-quest` | Best starting point for the newer compact-memory / reducer-governed continuity line. |
| Semantic compression / bucketed meaning systems | `semantic-signal-alphabet` | `rd-engine`, `llm-defined-persistent-memory` | Start here if the bucket-map idea is what brought you in. |
| Human-AI cognition taxonomy / "what kind of system is this?" | `Cognition-Scale-Formal-Taxonomy` | `Janet-MCM-Core` | Taxonomy first, implementation exemplar second. |
| Deterministic cognition / MCM implementation | `Janet-MCM-Core` | `historical-janet-school-exploratory-build` | `Janet-MCM-Core` is the cleaner conceptual anchor; the school build is historical exploratory machinery. |
| Current Janet-school cognition / training-ground implementation lane | `janet-school` | `Janet-MCM-Core`, `historical-janet-school-exploratory-build` | Start here if you want the newer school-facing Janet implementation surface, with the core and historical exploratory repo as context. |
| Curriculum-shape research for smaller LLMs | `relational-curriculum-geometry` | `janet-school`, `cognition-mesh-test-chamber` | Best first stop if you want the early hypothesis lane testing whether ordering, grouping, boundary cases, and relational placement in training data change how small models learn and transfer. |
| Human-side profiling / strain effects on LLMs | `Cognitive-Reactor-Profile` | `cognitive_reactor_stress_tests` | Profile defines the construct; stress tests probe it. |
| Foundational entropy-folding theory | `entropy-folding-eureka-cascade-hypothesis` | `entropy-folding-cross-domain-signal-atlas`, `entropy-folding-foundational-frameworks` | Best current hypothesis-first entry point for this theory cluster. |
| Evidence / provenance / signal mapping for that theory | `entropy-folding-cross-domain-signal-atlas` | `entropy-folding-eureka-cascade-hypothesis` | Use this if you want the signal map rather than the hypothesis spine first. |
| Upstream conceptual foundations | `entropy-folding-foundational-frameworks` | `Entropy-Folding-Vector-Theory`, `entropy-folding-as-directed-thermodynamics-for-cognition-finished` | Best for readers who want the deeper conceptual scaffold underneath the newer theory repos. |
| Macro / companion theory papers | `Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass` | `Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles`, `perpetual_cognition_reactor` | Companion preprint lane rather than first-principles foundations. |
| AI governance / preference-handling audit work | `governance-by-design-report-commentary` | `governance-by-design-report`, `safety_theatre` | Read the commentary first; it frames the litmus test and the main audit. |
| Safety / agency / governance critique | `safety_theatre` | `governance-by-design-report` | Best for readers interested in the safety-governance critique independent of the saved-memory audit. |
| Older Symbound-era restoration / induction / wand material | `model-behaviour-toolkit` | archived repos lower in `README.md` | Start with the modernized toolkit first; only drop into the archives if you specifically want lineage/history. |

## If You Want the Newer "Current" Cluster Only

If you do not want to wander through the full repo history, these are the strongest current entry points:

- `chatty-cog`
- `chatty-art`
- `chatty-lora`
- `nanochat-llm-tweaker`
- `chatty-factory`
- `chatty-quest`
- `chatty-pet`
- `rd-engine`
- `llm-semantic-dataset-sorter`
- `cognition-mesh-test-chamber`
- `ai-teaming-framework`
- `model-behaviour-toolkit`
- `llm-defined-persistent-memory`
- `semantic-signal-alphabet`
- `janet-school`
- `relational-curriculum-geometry`
- `entropy-folding-eureka-cascade-hypothesis`
- `entropy-folding-cross-domain-signal-atlas`

That subset will give you a much more accurate picture of where the ecosystem is actively heading.

## If You Only Have 15 Minutes

Pick one of these routes:

- Local tools route:
  `chatty-cog` -> `chatty-pet` -> `chatty-art` -> `nanochat-llm-tweaker`
- AI interaction route:
  `ai-teaming-framework` -> `model-behaviour-toolkit`
- Theory route:
  `entropy-folding-eureka-cascade-hypothesis` -> `entropy-folding-cross-domain-signal-atlas`
- Memory / architecture route:
  `rd-engine` -> `llm-semantic-dataset-sorter` -> `cognition-mesh-test-chamber` -> `llm-defined-persistent-memory`
- Janet / cognition route:
  `Janet-MCM-Core` -> `janet-school`
- Curriculum research route:
  `relational-curriculum-geometry` -> `janet-school` -> `cognition-mesh-test-chamber`

## Active vs Historical

Not every repo here should be treated as an equally current starting point.

As a rule of thumb:

- Repos near the top of the auto-generated active index in `README.md` are the best first stops.
- Repos listed under "Archived Repositories" in `README.md` are historical unless a file explicitly tells you otherwise.
- If an older repo says work continues in a newer repo, trust the newer repo.

Example:

- `chatty-factory` = current
- `chattyfactory` = archived predecessor
- `ChattyFactory-ManualPipeline-v0.1` and `Chattyfactory-AutoPipeline-v0.2` = historical snapshots

## Canonical vs Draft

Some repos are older drafts whose README points to a newer canonical home.

When a repo says "canonical versions are maintained at X":

- treat `X` as the reference surface
- treat the current repo as historical context or intermediate development history

Known examples:

- `entropy_folding_scope` -> `entropy-folding-foundational-frameworks`
- `entropy_folding_scale` -> `entropy-folding-foundational-frameworks`

## A Good Default Reading Order

If you want a balanced overview without getting lost:

1. `Whatisthisgithub/README.md`
2. `Whatisthisgithub/GLOSSARY.md`
3. `ai-teaming-framework`
4. `model-behaviour-toolkit`
5. `chatty-cog`
6. `chatty-art`
7. `nanochat-llm-tweaker`
8. `chatty-factory`
9. `chatty-pet`
10. `rd-engine`
11. `llm-semantic-dataset-sorter`
12. `cognition-mesh-test-chamber`
13. `semantic-signal-alphabet`
14. `llm-defined-persistent-memory`
15. `janet-school`
16. `relational-curriculum-geometry`
17. `entropy-folding-eureka-cascade-hypothesis`

That order gets you:

- the navigation layer
- the interaction philosophy
- the practical tools
- the small reusable state core behind part of the newer stack
- the semantic sorting workbench that sits beside the newer stack
- the newer memory architecture ideas
- the current theory spine

## Final Note

This ecosystem is modular, not linear.

You do **not** need to understand every repo before using one of them.
Pick the lane closest to your actual reason for arriving, and let the rest stay peripheral until needed.

If you lose the thread, return to:

- `README.md` for the front door
- `EASY_START.md` for route selection
- `GLOSSARY.md` for local language
