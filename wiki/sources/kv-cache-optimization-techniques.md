---
title: "Source: Techniques for KV Cache Optimization"
type: source-summary
source: "[[raw/kv-cache-optimization-techniques]]"
related: ["[[concepts/kv-cache]]", "[[concepts/grouped-query-attention]]", "[[concepts/sliding-window-attention]]", "[[concepts/paged-attention]]", "[[concepts/llm-inference-optimization]]", "[[entities/vllm]]"]
last_compiled: 2026-04-05
summary: "Deep technical review of KV cache optimization: GQA (8x reduction), Sliding Window Attention (2x reduction), PagedAttention (waste from 60-80% to 4%), MQA, distributed caching for million-token contexts, and per-token memory calculations."
---

## Key Points
- KV cache for Llama-2-13B at full context + batch 8 requires ~25GB GPU memory
- Grouped-Query Attention: 8x cache reduction (Llama-2-70B: 64 query heads, 8 KV heads)
- Sliding Window Attention: halves cache size while supporting 2x context length
- PagedAttention: reduces memory waste from 60-80% to 4% via virtual memory concepts
- Combined GQA+SWA: 16x reduction (1MB → 32KB per token for Mistral-7B)
- Distributed KV cache enables million-token contexts across multiple GPUs

## Detailed Summary

Omri Mallis's technical article provides a layered view of [[concepts/kv-cache|KV cache]] optimization, the memory bottleneck that determines how many concurrent requests and how long a context an LLM can serve.

Grouped-Query Attention (GQA) reduces cache by sharing KV heads across query heads — Llama-2-70B uses 64 query heads but only 8 KV heads, achieving 8x reduction. Sliding Window Attention (SWA, used in Mistral-7B) limits attention to the most recent W tokens, halving cache while compensating through layered architecture. [[entities/vllm|vLLM's]] PagedAttention eliminates memory fragmentation by using virtual-to-physical address mapping, reducing waste from 60-80% to under 4%.

For massive contexts (GPT-4's 128K, Gemini 1.5's 1M tokens), distributed KV cache assigns attention head subsets to different GPUs, scaling horizontally.

## Related Concepts
- [[concepts/kv-cache]] — the central topic
- [[concepts/llm-inference-optimization]] — KV cache as part of the optimization stack
- [[concepts/continuous-batching]] — PagedAttention enables efficient continuous batching
