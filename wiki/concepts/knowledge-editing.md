---
title: "Knowledge Editing"
type: concept
sources: ["[[sources/rome-memit-knowledge-editing]]"]
related: ["[[concepts/fine-tuning]]", "[[concepts/catastrophic-forgetting]]", "[[concepts/hallucination-contamination]]", "[[entities/rome-memit]]"]
last_compiled: 2026-04-05
summary: "Targeted modification of specific factual associations in model weights without full retraining — via methods like ROME (single facts) and MEMIT (thousands of facts) — with inherent scalability limits."
---

## Overview

Knowledge editing is a family of techniques for modifying specific factual knowledge stored in language model weights without full retraining or [[concepts/fine-tuning]]. Rather than updating all parameters to change a single fact (expensive, risky for [[concepts/catastrophic-forgetting]]), knowledge editing makes targeted, surgical modifications to the specific parameters that encode a particular factual association.

This represents the most fine-grained end of the spectrum for putting knowledge into model weights:

**Knowledge Editing → [[concepts/parameter-efficient-fine-tuning|PEFT]] → Full Fine-Tuning → [[concepts/continued-pretraining]] → Pretraining from Scratch**

## How Facts Are Stored

Research using causal tracing (see [[entities/rome-memit]]) has revealed that factual knowledge in transformers is:
- **Stored in MLP modules** (not attention layers)
- **Located at middle transformer layers** (not early or late)
- **Activated during the last token of the subject entity** (e.g., the "Tower" token in "Eiffel Tower is in Paris")

MLPs function as key-value stores: the first linear layer maps inputs to keys, and the second linear layer maps keys to value vectors that encode factual associations.

## Methods

### ROME (Rank-One Model Editing)
- Makes a single rank-one modification to MLP weights
- Changes one factual association (e.g., "Eiffel Tower is in Paris" → "Eiffel Tower is in Rome")
- Achieves both **specificity** (doesn't affect unrelated facts) and **generalization** (works across paraphrases)

### MEMIT (Mass-Editing Memory in a Transformer)
- Extends ROME to batch-edit thousands of facts simultaneously
- Modifies MLP weights across a range of critical layers
- Maintains accuracy at scale for single-batch edits

### MAKE (Memory-Associated Knowledge Editing)
- 2025 advancement accounting for associated knowledge transfer
- Addresses the problem that changing one fact should update related inferences

### EasyEdit2 Framework
- Open-source toolkit (2025) providing unified interface for multiple editing methods
- Supports ROME, MEMIT, NAMET, and other algorithms

## Limitations

### Sequential Editing Degradation
Sequential ROME edits cause progressive degradation:
1. Gradual forgetting of previously edited facts
2. Loss of neighborhood specificity (edits bleed into related facts)
3. Eventually, abrupt catastrophic failure

This fundamentally limits knowledge editing as a strategy for continuously updating model knowledge — a critical consideration for [[concepts/llm-knowledge-base]] systems.

### Scope Limitations
- Works best for simple subject-relation-object triples
- Struggles with complex multi-hop reasoning or nuanced contextual knowledge
- Cannot easily add entirely new concepts (only modify existing associations)

## Knowledge Editing vs. Alternatives

| Dimension | Knowledge Editing | Fine-Tuning | RAG |
|-----------|------------------|-------------|-----|
| Granularity | Single facts | Task/domain level | Per-query |
| Cost per update | Very low | Medium-high | Zero (update corpus) |
| Scalability | Limited (sequential degradation) | Good | Excellent |
| Persistence | In weights | In weights | In external store |
| Traceability | None | None | Full citation |

## Connection to LLM Knowledge Bases

Knowledge editing is relevant to [[concepts/llm-knowledge-base]] as a potential mechanism for correcting factual errors in models used for wiki compilation. However, the sequential degradation problem means it cannot replace RAG or re-compilation for maintaining current knowledge. The practical recommendation: use knowledge editing for targeted corrections of persistent errors, not as a primary knowledge update mechanism.

## Sources

- [[sources/rome-memit-knowledge-editing]] — causal tracing, ROME algorithm, MEMIT scaling

## Related Concepts

- [[concepts/fine-tuning]] — broader alternative for knowledge updates
- [[concepts/catastrophic-forgetting]] — sequential edits cause analogous degradation
- [[concepts/hallucination-contamination]] — editing can fix or introduce errors
- [[entities/rome-memit]] — the systems implementing knowledge editing
