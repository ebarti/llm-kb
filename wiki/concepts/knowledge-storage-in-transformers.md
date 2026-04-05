---
title: "Knowledge Storage in Transformers"
type: concept
sources: ["[[sources/knowledge-circuits-transformers-research]]", "[[sources/retro-illustrated-retrieval-transformer]]"]
related: ["[[concepts/attention-mechanisms]]", "[[concepts/self-attention]]", "[[concepts/knowledge-editing]]", "[[concepts/memory-augmented-neural-networks]]", "[[concepts/weights-vs-context]]", "[[entities/rome-memit]]"]
tags: [knowledge-storage, MLP-memory, knowledge-circuits, transformer-interpretability]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "How transformer LLMs store and retrieve factual knowledge: MLP layers act as key-value memories storing facts in their weight matrices, while attention heads serve as routing mechanisms — together forming 'knowledge circuits' that enable surgical knowledge editing."
---

## Overview

Understanding how transformers store and retrieve information is one of the most important open questions in AI. Research has converged on a clear picture: **MLP layers store facts** and **attention heads route queries to the right facts**. This division of labor — storage in feed-forward networks, retrieval via attention — forms the basis of "knowledge circuits" that trace the complete path from input to output for specific pieces of knowledge.

This understanding has profound practical implications: it enables targeted [[concepts/knowledge-editing]] (changing individual facts without retraining), knowledge unlearning (removing specific information), and explains why model scale correlates with knowledge capacity (more MLP parameters = more storage slots).

## The Two Systems

### MLP Layers as Key-Value Memory

The Feed-Forward Network (FFN) in each transformer layer consists of two linear transformations with a nonlinearity:

FFN(x) = W_2 * ReLU(W_1 * x + b_1) + b_2

This can be interpreted as a key-value memory:
- **W_1** (first projection): Maps inputs to **keys** — the patterns that trigger specific knowledge
- **W_2** (second projection): Maps keys to **values** — the actual stored information
- **ReLU**: Acts as a sparse gating function, selecting which memory slots to activate

Each column of W_2 can be thought of as a fundamental unit of knowledge storage — a "knowledge neuron" that encodes a specific piece of information.

### Attention Heads as Routers

[[concepts/self-attention]] heads do not store factual knowledge themselves. Instead, they serve as the **information routing** system:

1. When processing a query like "The capital of France is ___", specific attention heads in middle layers identify "France" as the relevant entity
2. These heads route information about "France" to the MLP layers that store geographic facts
3. The MLP layers produce the association "France -> Paris"
4. Later attention heads and MLPs assemble the final output

Head ablation studies confirm this: disabling specific attention heads disrupts specific knowledge circuits without affecting unrelated facts.

## Knowledge Circuits

A knowledge circuit is the complete computational path through a transformer that produces a specific factual output. It typically includes:

1. **Early attention heads**: Identify relevant entities in the input
2. **Middle-layer MLPs**: Store and retrieve the relevant factual associations
3. **Late attention heads**: Aggregate and compose information from multiple facts
4. **Final MLP layers**: Map composed representations to output tokens

The Knowledge Circuits framework (NeurIPS 2024) provides tools to trace these paths by systematically ablating components and measuring the effect on specific factual outputs.

## The Modularity Discovery

Perhaps the most striking finding: **fact-storing MLPs are modular and swappable**. Researchers:

1. Constructed minimal MLPs encoding specific fact sets
2. Inserted them into transformer models, replacing original MLPs
3. Models immediately produced the new facts with no fine-tuning
4. Performance on unrelated tasks was barely affected

This demonstrates that factual knowledge storage is highly localized — not distributed across the entire network as previously assumed. It directly enables:

- **[[entities/rome-memit]]**: Rank-one edits to MLP weights change specific facts
- **MEMIT**: Scales to thousands of simultaneous fact edits
- **Knowledge unlearning**: Disrupting specific MLP value vectors removes targeted knowledge
- **Model merging**: Combining fact-storing modules from different models

## Parametric vs Non-Parametric Knowledge

A key distinction in how transformers access knowledge:

| Dimension | Parametric (MLP weights) | Non-Parametric (Context/Retrieval) |
|-----------|--------------------------|-----------------------------------|
| Storage | In model weights | In context window or external DB |
| Capacity | Fixed at training time | Dynamic, unbounded |
| Update cost | Requires training/editing | Zero (just change context) |
| Latency | Zero (forward pass) | Additional retrieval step |
| Traceability | Opaque (weights) | Transparent (can see source) |
| Reliability | Can hallucinate | Grounded in provided text |

[[entities/retro]] demonstrates that externalizing factual knowledge into retrieval reduces parameter requirements by 25x while matching performance. This supports the view that MLP layers are "wasteful" when used for pure memorization — a theme explored in [[concepts/weights-vs-context]].

## Implications for LLM Knowledge Bases

This research directly connects to the [[concepts/llm-knowledge-base]] paradigm:

1. **Why RAG works**: LLMs are better at reasoning with provided context than at recalling parametric facts
2. **Why knowledge editing is limited**: Editing individual MLP weights can have cascading effects through knowledge circuits
3. **Why scale matters for knowledge**: More MLP capacity = more facts storable, but retrieval-augmented approaches may be more efficient
4. **Why [[concepts/context-engineering]] is so effective**: Bypassing unreliable parametric recall by putting knowledge directly in context

## Open Questions

- What is the theoretical maximum number of facts an MLP of given dimensions can store?
- How do knowledge circuits change with model scale (1B vs 100B)?
- Can we pre-design MLP structures optimized for specific knowledge domains?
- Is there a practical way to "defragment" knowledge storage in MLPs?

## Sources

- [[sources/knowledge-circuits-transformers-research]] — Knowledge Circuits framework (NeurIPS 2024)
- [[sources/retro-illustrated-retrieval-transformer]] — RETRO's parametric vs retrieval knowledge split

## Related Concepts

- [[concepts/attention-mechanisms]] — the routing system for knowledge retrieval
- [[concepts/knowledge-editing]] — surgical modification enabled by understanding storage
- [[concepts/memory-augmented-neural-networks]] — historical context for external memory
- [[concepts/weights-vs-context]] — the fundamental knowledge placement question
- [[entities/rome-memit]] — practical knowledge editing using MLP modifications
