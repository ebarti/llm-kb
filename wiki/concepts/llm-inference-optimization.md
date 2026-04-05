---
title: "LLM Inference Optimization"
type: concept
sources: ["[[sources/bentoml-speculative-decoding]]", "[[sources/bentoml-batching-strategies]]", "[[sources/kv-cache-optimization-techniques]]", "[[sources/premai-inference-servers-compared]]", "[[sources/quantization-gptq-gguf-awq]]", "[[sources/on-device-llms-2026]]"]
related: ["[[concepts/kv-cache]]", "[[concepts/speculative-decoding]]", "[[concepts/continuous-batching]]", "[[concepts/quantization]]", "[[concepts/llm-cost-optimization]]", "[[concepts/llm-serving-frameworks]]", "[[concepts/edge-inference]]"]
last_compiled: 2026-04-05
summary: "The umbrella discipline of reducing latency, cost, and resource consumption of LLM inference through KV cache management, batching, quantization, speculative decoding, and serving infrastructure."
---

## Overview

LLM inference optimization is the set of techniques that make running large language models faster, cheaper, and more resource-efficient in production. It spans the full stack from model compression ([[concepts/quantization]]) through memory management ([[concepts/kv-cache]]) to serving infrastructure ([[concepts/llm-serving-frameworks]]).

The stakes are high: proper optimization reduces energy usage by up to 73% compared to naive serving, typically translating to a 2-3x reduction in cloud costs (2025 ACL study). For the [[concepts/llm-knowledge-base|LLM knowledge base]] system, inference cost directly determines the viability of maintaining a wiki through continuous LLM compilation, Q&A, and linting operations.

## The Two Phases of Inference

LLM inference has two distinct phases with different bottlenecks:

1. **Prefill Phase**: Processes all input tokens in parallel. Compute-bound on GPU. Relatively fast.
2. **Decode Phase**: Generates output tokens one at a time, autoregressively. Memory-bandwidth-bound. This is the latency bottleneck.

Output tokens cost 3-5x more than input tokens at API providers, and each output token adds several to tens of milliseconds of latency. This asymmetry drives many optimization strategies.

## Key Optimization Layers

### Model Level
- **[[concepts/quantization]]**: Reduce precision from FP16 to INT4/INT8. AWQ/GPTQ achieve 75% model size reduction with minimal quality loss. Marlin-AWQ reaches 741 tok/s on benchmarks.
- **Attention architecture**: Grouped-Query Attention (GQA) reduces KV cache by 4-8x. Flash Attention optimizes memory access patterns for 2-4x speedups on long sequences.
- **[[concepts/speculative-decoding]]**: Draft-then-verify with a smaller model achieves 2-3x speedup with zero quality loss.

### Memory Level
- **[[concepts/kv-cache]]**: PagedAttention reduces KV cache waste from 60-80% to 4%. Sliding Window Attention halves cache for long contexts. Combined techniques yield 16x per-token memory reduction.
- **Cache offloading**: Moving KV data to CPU memory or disk when GPU is full, resuming without recomputation.

### Serving Level
- **[[concepts/continuous-batching]]**: Iteration-level scheduling achieves 23x throughput over naive serving, with 90%+ GPU utilization.
- **Tensor parallelism**: Splitting matrix multiplications across GPUs for sub-second latency on 70B+ models.
- **[[concepts/prompt-caching]]**: Reusing cached prompt prefixes across requests — 90% cost reduction on Anthropic, 50% on OpenAI.

### Application Level
- **[[concepts/model-routing]]**: Directing queries to appropriately-sized models saves 40-60%.
- **[[concepts/semantic-caching]]**: Caching responses for similar queries eliminates inference calls entirely.
- **[[concepts/token-optimization]]**: Prompt compression, output constraints, and context assembly optimization.

## Performance Benchmarks (2026)

| Technique | Throughput Improvement | Latency Reduction | Cost Savings |
|-----------|----------------------|-------------------|--------------|
| Continuous batching | 23x throughput | Modest increase | 85% per-token |
| PagedAttention | 2-4x throughput | — | Equivalent to doubling GPUs |
| Speculative decoding | — | 2-3x faster | — |
| 4-bit quantization | 3-10x faster | — | 75% memory |
| Prompt caching | — | 79% latency | 90% cost |
| Semantic caching | — | Seconds → milliseconds | 73% cost |
| Model routing | — | Variable | 40-85% cost |

## Sources
- [[sources/bentoml-speculative-decoding]] — draft-then-verify technique details
- [[sources/bentoml-batching-strategies]] — static → dynamic → continuous batching evolution
- [[sources/kv-cache-optimization-techniques]] — GQA, SWA, PagedAttention deep-dive
- [[sources/premai-inference-servers-compared]] — framework benchmarks and selection
- [[sources/quantization-gptq-gguf-awq]] — GPTQ/AWQ/GGUF comparison
- [[sources/on-device-llms-2026]] — edge optimization techniques

## Related Concepts
- [[concepts/llm-cost-optimization]] — cost-focused view of the same techniques
- [[concepts/llm-knowledge-base]] — the system these optimizations serve
- [[concepts/edge-inference]] — optimization taken to the extreme for mobile devices
