---
title: "Context Windows"
type: concept
sources: ["[[sources/epoch-context-window-growth]]", "[[sources/redis-rag-vs-long-context]]", "[[sources/logrocket-llm-context-problem]]", "[[sources/lost-in-the-middle-paper]]", "[[sources/magic-ltm-100m-context]]"]
related: ["[[concepts/long-context-models]]", "[[concepts/lost-in-the-middle]]", "[[concepts/context-engineering]]", "[[concepts/context-compression]]", "[[concepts/prompt-caching]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "The fixed-size token buffer an LLM can process in a single inference call; growing ~30x/year but effective utilization lags behind raw capacity."
---

## Overview

A context window is the total number of tokens a language model can process in a single inference call. It represents the model's "working memory" — everything the model can reference when generating a response, including system instructions, conversation history, retrieved documents, tool outputs, and the response itself.

Context windows are the fundamental constraint shaping how LLM-based systems are designed. Every architectural decision in [[concepts/llm-knowledge-base]] systems, [[concepts/rag-vs-index-based-retrieval]] pipelines, and [[concepts/multi-agent-systems]] is ultimately a response to the question: "How do we get the right information into a finite context window?"

## Growth Trajectory

According to [[sources/epoch-context-window-growth]], frontier LLM context windows have grown approximately **30x annually** since mid-2023 (based on analysis of 123 models):

| Era | Typical Context | Notable Models |
|-----|----------------|----------------|
| 2022 | 2K-4K tokens | GPT-3, early ChatGPT |
| 2023 | 8K-32K tokens | GPT-4 (8K/32K), Claude 2 (100K) |
| 2024 | 128K-1M tokens | GPT-4 Turbo (128K), Gemini 1.5 Pro (1M/2M), Claude 3 (200K) |
| 2025 | 200K-2M tokens | Gemini 2.5 Pro (1M), Claude Opus 4.6 (1M), Llama 4 Scout (10M) |
| 2026 | 1M-100M tokens | Magic LTM-2-Mini (100M), most frontier models at 1M |

Effective usage — the length where models reach 80% accuracy — has grown even faster: **250x in nine months**, meaning models are getting better at using what they have, not just accepting more tokens.

## Key Limitations

### Raw Size vs. Effective Use

Having a large context window does not mean the model can effectively use all of it. [[sources/logrocket-llm-context-problem]] identifies the "60% rule": Claude's output starts degrading at 20-40% of window capacity as the attention mechanism gives earlier instructions less weight.

### Position Bias (Lost in the Middle)

The [[concepts/lost-in-the-middle]] problem: models exhibit a U-shaped performance curve, performing best on information at the beginning and end of context, with >30% degradation for middle-positioned content.

### Cost and Latency

From [[sources/redis-rag-vs-long-context]]:
- Processing time scales with O(n^2) attention complexity
- 100K-token request latency: 30-60 seconds (vs ~1 second for RAG)
- At scale: $2,000+/month for 10,000 requests with 100K contexts

### Context Failure Modes

[[sources/logrocket-llm-context-problem]] identifies four failure modes:
1. **Context Poisoning**: Bad information reinforced through repeated reference
2. **Context Distraction**: Model relies on context over reasoning beyond ~100K tokens
3. **Context Confusion**: Irrelevant information influences outputs
4. **Context Clash**: Contradictory information causes 39% accuracy drops

## What Consumes Context

In production systems, context is consumed by many competing elements:
- System prompt and tool definitions (~20K tokens for a typical agent setup)
- MCP server tool schemas (permanent consumption per server)
- Conversation history (grows with each exchange)
- Retrieved documents and file contents
- The model's own response

## Implications for Wiki Systems

For [[concepts/llm-knowledge-base]] systems, context windows determine the fundamental architecture:

1. **Summaries-based navigation** is a response to context limits — the LLM reads a compact index rather than loading all articles
2. **Selective article loading** is manual RAG without vectors — load only what the query needs
3. **Wikilinks as structured navigation** let the LLM follow paths rather than loading everything
4. **The entire ingest → compile → query cycle** is a context engineering pipeline

As context windows grow toward 1M+ tokens, wiki systems at personal scale (~100 articles, ~400K words) may eventually fit entirely in context. But [[sources/logrocket-llm-context-problem]] argues this would be counterproductive: selective, high-quality context consistently outperforms large, unfocused context.

## Sources

- [[sources/epoch-context-window-growth]] — growth metrics: 30x/year capacity, 250x/9mo effective usage
- [[sources/redis-rag-vs-long-context]] — cost/latency analysis of large context windows
- [[sources/logrocket-llm-context-problem]] — four failure modes and six mitigation techniques
- [[sources/lost-in-the-middle-paper]] — U-shaped performance curve
- [[sources/magic-ltm-100m-context]] — 100M token window via novel architecture

## Related Concepts

- [[concepts/long-context-models]] — models pushing context boundaries
- [[concepts/lost-in-the-middle]] — the key utilization failure mode
- [[concepts/context-engineering]] — the discipline of managing context effectively
- [[concepts/context-compression]] — techniques for fitting more into less
- [[concepts/prompt-caching]] — making large contexts economically viable
- [[concepts/infinite-context]] — architectural approaches to unbounded context
- [[concepts/virtual-context-management]] — MemGPT's approach to transcending fixed windows
