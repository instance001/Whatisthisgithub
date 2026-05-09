# Easy Start Guide

This file is a navigation aid for new arrivals (we know, it is a lot to take in at a glance).
It offers "surfaces to latch to" depending on what you are trying to do rather than attempting to untangle areas of YOUR specific interests amidst the hard to navigate ecosystem currently being formed here. Think of it as an optional door greeter pointing you to the aisle that might suit your needs.

## Where to start (Recommended)

If terminology is unfamiliar, start with the atlas:

- Glossary (terms + mapping symbols): `GLOSSARY.md`
- Ambiguities (needs disambiguation): `AMBIGUITIES.md`

## Entry Points by Intent

| If you are here for... | Start with | Then look at | Notes |
| --- | --- | --- | --- |
| Current everyday local AI assistant stack | `chatty-cog` | `chatty-edu`, `chatty-edu-user` | `chatty-cog` is the current general local assistant shell; `chatty-edu` is the education-focused branch; `chatty-edu-user` is the ready-to-run user release. |
| Local project factory / build pipeline | `chattyfactory` | `chatty-cog` | `chattyfactory` is the current project-factory surface. The older `Chattyfactory-AutoPipeline-v0.2` and `ChattyFactory-ManualPipeline-v0.1` repos are now historical snapshots, not the main starting point. |
| Prompting / model behaviour / drift recovery | `model-behaviour-toolkit` | `chatty-cog` | Start here for modern provider-neutral prompting, session restoration, and behaviour scaffolds. Use `chatty-cog` if you want to apply those ideas inside a local desktop assistant shell. |
| Local image / GIF / video / audio generation | `chatty-art` | `chatty-lora` | `chatty-art` is the current media-generation front door. `chatty-lora` is the sister repo for training and dataset preparation, not the first stop for pure generation. |
| Local LoRA training / dataset curation | `chatty-lora` | `chatty-art` | Start here if you want to build datasets, prepare training plans, or run the current Wan/Musubi LoRA workflow. `chatty-art` is the companion generation surface for using models, not training them. |
| Tools you can run right now without building from source | `chatty-edu-user` | `chatty-art`, `chatty-cog` | `chatty-edu-user` is the clearest ready-to-run Windows release. `chatty-art` and `chatty-cog` are more source-oriented at present. |
| Offline parsing / data export | `MemorySpine` |  | Small surface area; useful utility entry point. |
| Honest local activity monitor | `ecg_window` | `chatty-art`, `chatty-lora`, `chatty-cog` | `ecg_window` is the standalone tiny monitor. The other repos show how it can be embedded into larger local tools. |
| Sandbox / applied experiment | `chattydoom` |  | Minimal, hackable playground. |
| Foundations / theory | `entropy-folding-foundational-frameworks` | `Entropy-Folding-Vector-Theory`, `entropy-folding-as-directed-thermodynamics-for-cognition-finished` | Use the foundational repo as the canonical anchor when drafts exist. |
| Human-side companion preprints | `Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass` | `Psychohistory-after-Symbound-Macro-Trajectories-from-Entropy-Folding-Cycles` | These are written as companions; they do not substitute for the foundations. |
| Measurement / profiling | `Cognitive-Reactor-Profile` | `cognitive_reactor_stress_tests`, `perpetual_cognition_reactor` | "Profile" defines the construct; "stress tests" operationalize probes. |
| Taxonomy / classification | `Cognition-Scale-Formal-Taxonomy` | `Janet-MCM-Core` | Taxonomy defines categories; Janet is an implemented "MCM" exemplar. |
| Older Symbound interaction / restoration archives | `model-behaviour-toolkit` | archived repos listed lower in `README.md` | If you arrived looking for older prompt wands, restoration kits, or interaction toolkits, start with the modernized toolkit first. Most of the older prompt-oriented repos are now better treated as archival/historical context. |

## Notes on Drafts vs Canonical

Some repositories are marked as superseded drafts in their READMEs.
When a repo says "canonical versions are maintained at X", treat X as the reference surface.
