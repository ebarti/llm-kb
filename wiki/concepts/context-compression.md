---
title: "Context Compression"
type: concept
sources: ["[[sources/context-compression-techniques]]", "[[sources/logrocket-llm-context-problem]]", "[[sources/redis-rag-vs-long-context]]"]
related: ["[[concepts/context-windows]]", "[[concepts/context-engineering]]", "[[concepts/hierarchical-memory]]", "[[concepts/lost-in-the-middle]]"]
last_compiled: 2026-04-05
summary: "Techniques for reducing token count while preserving information: hard prompts (LLMLingua, 20x), soft prompts (480x), structured pruning (Provence, 95%), and hierarchical summarization."
---

## Overview

Context compression encompasses all techniques that reduce the number of tokens in an LLM's context while preserving the information needed for accurate responses. This is critical because larger contexts are slower (O(n^2) attention), more expensive (per-token pricing), and less accurate (the [[concepts/lost-in-the-middle]] problem).

Effective compression can reduce tokens by **50-80%** using combined techniques, with specialized tools achieving up to **95%** compression while maintaining response quality.

## Technique Spectrum

### Hard Prompt Methods (Model-Agnostic)

These work at the token level on the text prompt itself:

| Method | Approach | Compression | Training Required |
|--------|----------|------------|-------------------|
| **SelectiveContext** | Filters low-information tokens by self-information scores | ~5-10x | No |
| **LLMLingua** | Small LM ranks and preserves key tokens | Up to **20x** | No (uses existing small model) |
| **LongLLMLingua** | Document-level compression with question-aware filtering | ~10-20x | No |
| **RL-based methods** | Reinforcement learning for optimal token selection | ~10-20x | Yes |

### Soft Prompt Methods (Model-Specific)

Encode prompts into continuous embeddings or key-value pairs:
- Compression ratios up to **480x**
- Requires training per model
- Not transferable between model families
- Best for stable, repeated prompt components

### Structured Pruning

Treats context as a structured object with priority levels:

```
always_keep:    system instructions, user goal
high_priority:  current query context, key constraints
medium:         recent conversation, relevant docs
low_priority:   old messages, tangential information
prune:          superseded results, redundant content
```

**Provence** achieves up to **95% compression** using this approach, automatically removing low-relevance content while preserving essential information.

### Hierarchical Summarization

Pyramid-structured summarization:
1. Divide input into chunks
2. Summarize each chunk (Level 1)
3. Summarize the summaries (Level 2)
4. Repeat to desired granularity

Risk: cumulative errors propagate upward. Each summarization level may lose nuance, and early mistakes amplify through layers.

### Knowledge Graph Extraction

Extract entities and relationships into a structured graph, then provide the LLM with the graph representation rather than raw text. LangChain's `ConversationKGMemory` achieves **40-60% reduction** with structured relationship preservation.

## Adaptive Compression for Long Sessions

For long-running interactions, adaptive compression scales savings with conversation length:

| Messages | Token Reduction |
|----------|----------------|
| 10 | 1% |
| 25 | 50% |
| 50 | 69% (8,560 tokens saved) |
| 100 | 83% |

This is particularly relevant for agent-based systems that maintain long conversation threads.

## Connection to Wiki Systems

For [[concepts/llm-knowledge-base]] systems, the compilation pipeline is itself a compression system:

| Wiki Layer | Compression Function |
|-----------|---------------------|
| Raw sources | Uncompressed ground truth |
| Source summaries | ~80-90% compression of raw content |
| Concept articles | Cross-source synthesis (higher compression) |
| Summaries.md | One-line per article (~99% compression) |
| Master index | Structural skeleton only |

This hierarchical compression mirrors the hierarchical summarization technique, with each wiki layer providing a different compression level for different query needs.

## Sources

- [[sources/context-compression-techniques]] — comprehensive survey of compression methods
- [[sources/logrocket-llm-context-problem]] — context pruning and summarization in practice
- [[sources/redis-rag-vs-long-context]] — compression as part of smart layering

## Related Concepts

- [[concepts/context-windows]] — the constraint compression addresses
- [[concepts/context-engineering]] — compression is a key context engineering technique
- [[concepts/hierarchical-memory]] — hierarchical summarization maps to memory tiers
- [[concepts/lost-in-the-middle]] — compression reduces the vulnerable middle zone
- [[concepts/wiki-compilation]] — wiki compilation is a domain-specific compression pipeline
