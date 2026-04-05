---
title: "Lost in the Middle"
type: concept
sources: ["[[sources/lost-in-the-middle-paper]]", "[[sources/redis-rag-vs-long-context]]", "[[sources/logrocket-llm-context-problem]]"]
related: ["[[concepts/context-windows]]", "[[concepts/needle-in-a-haystack]]", "[[concepts/context-engineering]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "LLMs exhibit a U-shaped performance curve — best at beginning/end of context, >30% degradation in the middle — caused by attention accumulation patterns in transformers."
---

## Overview

"Lost in the Middle" refers to a well-documented failure mode of transformer-based language models: they struggle to effectively use information positioned in the middle of their context windows. First characterized by Liu et al. (Stanford/UC Berkeley, TACL 2023), the phenomenon manifests as a **U-shaped performance curve** where models perform best on information at the beginning (primacy bias) and end (recency bias), with significant degradation — **more than 30%** — for middle-positioned content.

This is one of the most important practical constraints for any system that manages large contexts, including [[concepts/llm-knowledge-base]] systems, RAG pipelines, and agentic workflows.

## The U-Shaped Curve

Performance varies dramatically by information position:

```
High  |  *                                    *
      |   *                                  *
      |    **                              **
      |      ***                        ***
      |         ****              *****
Low   |             ****************
      +-------------------------------------->
      Beginning        Middle            End
                  Position in Context
```

- **Beginning** (primacy bias): Strong performance. Information here is visible to all subsequent tokens.
- **End** (recency bias): Strong performance. Most recently processed, freshest in the model's "working memory."
- **Middle**: Weakest performance. Tokens have limited visibility and accumulate less attention weight.

## Why It Happens

### Attention Accumulation
In transformer self-attention, each token can attend to all preceding tokens. Token #1 is visible to every subsequent token in the sequence, accumulating attention weight across the entire sequence. Token #500 in the middle is only visible from token #501 onward, receiving systematically less total attention. This creates an inherent positional bias.

### Task Framing vs. Fact Retrieval
Research suggests models use context primarily for task identification rather than fact extraction. Information at the beginning and end serves as strong "task framing" signals, while middle content is treated more as noise.

## Magnitude of Impact

- **>30% performance degradation** when relevant information moves from start/end to middle ([[sources/lost-in-the-middle-paper]])
- **10-20+ percentage point** accuracy drops in production RAG systems ([[sources/redis-rag-vs-long-context]])
- GPT-3.5-Turbo shows **>20% degradation** in worst cases
- The effect persists even in models specifically designed for long-context processing

## Practical Mitigations

### Strategic Document Ordering
Place the most relevant documents at the beginning and end of the context. Many RAG systems now use reranking models to optimize document position.

### Multi-scale Positional Encoding (Ms-PoE)
A plug-and-play approach that enhances middle-context capacity without fine-tuning the base model.

### Context Compression
Reduce total context length so that the "middle" zone is smaller. [[concepts/context-compression]] techniques can reduce tokens by 50-80%.

### Context Quarantine
[[sources/logrocket-llm-context-problem]]'s approach: split large contexts across isolated subagents so no single agent has a large middle zone.

### Structured Context
Tag context elements with priority and function, placing high-priority items at attention-favored positions.

## Implications for Wiki Systems

For [[concepts/llm-knowledge-base]] systems, "Lost in the Middle" validates the summaries-based navigation approach:

1. **Don't dump everything into context** — loading all articles creates a large middle zone where information will be missed
2. **Load selectively** — summaries file + targeted article loading keeps context compact and information near the beginning/end
3. **Structure matters** — system instructions at the beginning (always attended to), query-relevant content at the end, metadata in between

## Sources

- [[sources/lost-in-the-middle-paper]] — the foundational paper characterizing the phenomenon
- [[sources/redis-rag-vs-long-context]] — production impact: 10-20+ point accuracy drops
- [[sources/logrocket-llm-context-problem]] — context engineering mitigations

## Related Concepts

- [[concepts/context-windows]] — the constraint within which the problem manifests
- [[concepts/needle-in-a-haystack]] — tests retrieval at specific positions (related but tests optimistic cases)
- [[concepts/context-engineering]] — the discipline of designing around positional bias
- [[concepts/context-compression]] — reduces context size to minimize the middle zone
- [[concepts/rag-vs-index-based-retrieval]] — RAG avoids the problem by loading less context
