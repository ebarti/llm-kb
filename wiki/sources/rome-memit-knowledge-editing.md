---
title: "Source: ROME and MEMIT — Locating and Editing Factual Associations in LLMs"
type: source-summary
source: "[[raw/rome-memit-knowledge-editing]]"
related: ["[[concepts/knowledge-editing]]", "[[concepts/catastrophic-forgetting]]", "[[entities/rome-memit]]"]
last_compiled: 2026-04-05
summary: "ROME uses causal tracing to locate facts in MLP layers, then makes rank-one edits to change individual factual associations; MEMIT scales this to thousands of simultaneous edits."
reading_time: "2 min"
---

## Key Points

- Causal tracing reveals factual knowledge concentrates in MLP modules at middle transformer layers
- Facts are stored during processing of the last token of the subject entity
- ROME treats MLPs as key-value stores and makes rank-one weight modifications
- ROME edits generalize across paraphrases and novel contexts (not just surface pattern matching)
- MEMIT extends to thousands of simultaneous edits by modifying MLP weights across critical layers
- Sequential ROME edits cause gradual forgetting, eventually leading to catastrophic forgetting
- 2025 follow-ups: MAKE (associated knowledge transfer), NAMET (noise injection), EasyEdit2 framework
- CounterFact dataset: thousands of counterfactual statements for evaluating editing quality

## Detailed Summary

ROME represents a groundbreaking approach to understanding how factual knowledge is stored in transformer weights. Through causal tracing — running corrupted inputs and selectively restoring individual hidden states — the researchers localized factual retrieval to specific MLP modules at middle layers. This insight enables targeted editing: treating the MLP as a key-value store, ROME makes a single rank-one matrix modification to insert, update, or replace a factual association.

The critical distinction is between specificity (editing "Eiffel Tower is in Paris" to "Rome" shouldn't change beliefs about other landmarks) and generalization (the model should correctly answer "what city do I fly to to see the Eiffel Tower?" after the edit). ROME achieves both, while attention-layer editing fails to generalize.

MEMIT scales this to batch editing of thousands of facts. However, sequential editing remains problematic — accumulated edits gradually degrade model quality, revealing fundamental tensions between targeted knowledge modification and model stability.

## Related Concepts

- [[concepts/knowledge-editing]] — the core methodology
- [[concepts/catastrophic-forgetting]] — sequential edits induce forgetting
- [[concepts/fine-tuning]] — knowledge editing as alternative to full fine-tuning for fact updates
- [[concepts/hallucination-contamination]] — editing can both fix and introduce factual errors
