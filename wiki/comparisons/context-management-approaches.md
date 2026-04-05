---
title: "Context Management Approaches Compared"
type: comparison
subjects: ["[[concepts/context-compression]]", "[[concepts/virtual-context-management]]", "[[concepts/infinite-context]]", "[[concepts/context-engineering]]"]
sources: ["[[sources/logrocket-llm-context-problem]]", "[[sources/memgpt-llm-operating-system]]", "[[sources/infinite-context-approaches]]", "[[sources/context-compression-techniques]]"]
last_compiled: 2026-04-05
summary: "Four approaches to the context limit problem compared: compression (fit more in), virtual context (page in/out), infinite context (remove limits architecturally), and context engineering (use less, smarter)."
---

## Overview

Every LLM-based system must contend with finite context windows. Four broad strategies have emerged, each addressing the problem from a different angle. In practice, production systems combine multiple approaches.

## Comparison Table

| Dimension | Context Compression | Virtual Context (MemGPT) | Infinite Context | Context Engineering |
|-----------|-------------------|------------------------|-----------------|-------------------|
| **Core idea** | Fit more in same window | Page between context and storage | Remove window limits | Use less context, more effectively |
| **Approach** | Reduce tokens | Memory hierarchy | Architecture changes | Selective, structured loading |
| **Compression** | 50-95% | N/A (paging) | N/A (unlimited) | Implicit (only load what's needed) |
| **Model changes** | None (hard prompt) to significant (soft prompt) | None | Yes (architecture) | None |
| **Complexity** | Low-Medium | Medium-High | Very High | Medium |
| **Information loss** | Some (especially at high compression) | Minimal (stored externally) | None (in theory) | Minimal (selective loading) |
| **Latency impact** | Reduces latency (fewer tokens) | Adds tool call overhead | Varies by approach | Reduces latency |
| **Cost impact** | Reduces cost | Similar (fewer tokens but more calls) | Varies | Reduces cost |
| **Maturity** | Production-ready | Production-ready (Letta) | Research/early production | Production-ready |

## When to Use Each

### Context Compression
**Best for**: Long conversations, document processing, cost-sensitive applications.
- Use LLMLingua for model-agnostic 20x compression
- Use structured pruning (Provence) for 95% compression of low-priority content
- Use hierarchical summarization for long documents

### Virtual Context Management
**Best for**: Stateful agents, multi-session conversations, persistent knowledge.
- Use [[entities/memgpt-letta]] for agents that need to remember across sessions
- Use when context must be maintained over days/weeks
- The LLM manages its own memory, reducing engineering complexity

### Infinite Context
**Best for**: Research applications, full-codebase analysis, comprehensive document processing.
- Use StreamingLLM for real-time streaming (no long-range retrieval needed)
- Use Ring Attention for distributed training/inference at scale
- Use Infini-attention for bounded-memory infinite processing
- Most approaches still research-stage for production use

### Context Engineering
**Best for**: Production applications, agentic systems, knowledge base Q&A.
- The default approach for most real-world applications
- Combines RAG, dynamic tool selection, context quarantine, and caching
- The [[concepts/llm-knowledge-base]] wiki approach is a context engineering system

## Combinations in Practice

The most effective production systems layer multiple approaches:

```
Query arrives
  → Context Engineering: determine what's needed
    → RAG/selective loading: retrieve relevant content
      → Context Compression: reduce retrieved content
        → Prompt Caching: avoid recomputing static prefix
          → LLM inference with optimized context
```

For wiki systems specifically:
1. **Context engineering**: Summaries file provides structured navigation
2. **Selective loading**: Only relevant articles loaded (implicit compression)
3. **Hierarchical compression**: Raw → source summary → concept → one-line summary
4. **Prompt caching**: System instructions and summaries cached across queries

## Sources

- [[sources/logrocket-llm-context-problem]] — context engineering techniques
- [[sources/memgpt-llm-operating-system]] — virtual context management
- [[sources/infinite-context-approaches]] — architectural approaches
- [[sources/context-compression-techniques]] — compression methods

## Related

- [[concepts/context-windows]] — the fundamental constraint all approaches address
- [[concepts/llm-knowledge-base]] — a system that combines multiple approaches
