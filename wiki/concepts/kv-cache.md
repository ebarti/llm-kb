---
title: "KV Cache"
type: concept
sources: ["[[sources/kv-cache-optimization-techniques]]", "[[sources/bentoml-batching-strategies]]", "[[sources/premai-inference-servers-compared]]"]
related: ["[[concepts/transformer-architecture]]", "[[concepts/self-attention]]", "[[concepts/grouped-query-attention]]", "[[concepts/sliding-window-attention]]", "[[concepts/paged-attention]]", "[[concepts/speculative-decoding]]", "[[concepts/llm-inference-optimization]]", "[[concepts/continuous-batching]]", "[[concepts/prompt-caching]]", "[[entities/vllm]]", "[[entities/sglang]]"]
last_compiled: 2026-04-05
summary: "The key-value cache stores pre-computed attention vectors to avoid recalculation during autoregressive decoding; its management (PagedAttention, GQA, SWA) is the central bottleneck of LLM inference."
---

## Overview

The KV (Key-Value) cache is the memory structure that stores pre-computed attention key and value vectors during LLM inference. Without it, every new token generation would require recalculating attention over the entire sequence — making compute scale quadratically. With KV caching, computation scales linearly, but at the cost of significant GPU memory consumption.

For Llama-2-13B at full context (4096 tokens) with batch size 8, the KV cache requires approximately 25GB of GPU memory — nearly matching the model's parameter storage needs. This makes KV cache management the central bottleneck determining throughput, maximum context length, and concurrent request capacity.

## How It Works

During the prefill phase, the model computes key and value vectors for all input tokens and stores them in the cache. During the decode phase, each new token generation only computes its own K/V vectors and attends to the full cached history. The cache grows linearly with sequence length:

**Cache size** = 2 (K+V) x 2 (bytes for FP16) x head_dim x n_heads x n_layers x sequence_length x batch_size

Per-token memory requirements:
- Llama-2-7B: 512KB/token
- Llama-2-13B: 800KB/token
- Gemma-2B: 144KB/token

## Key Optimization Techniques

### Grouped-Query Attention (GQA)
Reduces KV heads while maintaining full query heads. Multiple query heads share individual KV pairs:
- Llama-2-70B: 64 query heads → 8 KV heads = **8x reduction**
- Mistral-7B: 4x reduction
- Gemma-2B: 144KB → 18KB per token = **8x reduction**

GQA is a generalization of Multi-Query Attention (MQA), which uses a single K head and single V head shared across all query heads.

### Sliding Window Attention (SWA)
Limits attention to the most recent W tokens. Older vectors are evicted as decoding progresses. Mistral-7B uses W=4096 to support 8192-token context at half the full cache size. The model compensates through layered architecture: information about older tokens is stored in upper-layer KV vectors.

### PagedAttention
Pioneered by [[entities/vllm|vLLM]], this borrows virtual memory concepts from operating systems:
- Allocates GPU memory in non-contiguous blocks rather than one contiguous region
- Maintains virtual-to-physical address mapping tables
- Reduces memory waste from **60-80% to under 4%**
- Enables prompt sharing: requests with identical prefixes share cached KV vectors
- Equivalent to doubling or quadrupling GPU investment without hardware cost

### RadixAttention
[[entities/sglang|SGLang's]] innovation: automatically discovers KV cache reuse opportunities via a radix tree structure. Achieves 85-95% cache hit rates on few-shot learning and 75-90% on multi-turn chat.

### Distributed KV Cache
For massive contexts (GPT-4's 128K tokens, Gemini 1.5's 1M tokens), the cache exceeds single-GPU memory. Distribution assigns attention head subsets to different GPUs, scaling horizontally.

## Combined Impact

Stacking optimizations yields dramatic reductions:
- **Mistral-7B with GQA + SWA**: 512KB → 32KB per token (**16x reduction**)
- **vLLM PagedAttention**: 2-4x throughput improvement from memory efficiency alone
- **SGLang RadixAttention**: additional 29% throughput over vLLM via automatic cache reuse

## Relevance to Provider-Side Prompt Caching

[[concepts/prompt-caching|Prompt caching]] (the API-level feature from Anthropic/OpenAI) is built on top of KV cache infrastructure. When Anthropic caches a prompt prefix, they are storing the KV cache state computed during prefill, so subsequent requests skip the prefill computation for the cached portion.

## Sources
- [[sources/kv-cache-optimization-techniques]] — GQA, SWA, PagedAttention, distributed cache deep-dive
- [[sources/premai-inference-servers-compared]] — PagedAttention vs RadixAttention in framework benchmarks
- [[sources/bentoml-batching-strategies]] — KV caching as enabler of continuous batching

## Related Concepts
- [[concepts/llm-inference-optimization]] — KV cache is the central bottleneck
- [[concepts/continuous-batching]] — PagedAttention enables efficient batch management
- [[concepts/prompt-caching]] — API-level abstraction over KV cache reuse
- [[concepts/edge-inference]] — KV cache compression critical for mobile deployment
