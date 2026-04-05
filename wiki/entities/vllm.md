---
title: "vLLM"
type: entity
entity_type: tool
sources: ["[[sources/ollama-vs-vllm-benchmarks]]", "[[sources/local-llm-hosting-tools-comparison]]", "[[sources/premai-inference-servers-compared]]", "[[sources/kv-cache-optimization-techniques]]", "[[sources/bentoml-batching-strategies]]"]
related: ["[[concepts/local-llm-inference]]", "[[entities/ollama]]", "[[concepts/llm-serving-frameworks]]", "[[concepts/kv-cache]]", "[[concepts/continuous-batching]]", "[[entities/sglang]]"]
last_compiled: 2026-04-05
summary: "Production-grade LLM inference engine using PagedAttention — achieves 793 TPS on A100 (vs Ollama's 41), best for multi-user and enterprise local deployments."
---

## Overview

vLLM is an open-source, production-grade inference engine for large language models. Its core innovation is PagedAttention, which reduces memory fragmentation by 50%+ and increases throughput 2-4x compared to naive implementations. vLLM is the standard choice for production [[concepts/local-llm-inference]] deployments where multiple concurrent users or high throughput is required.

## Key Features

- **PagedAttention**: Memory-efficient attention mechanism inspired by OS virtual memory paging
- **Continuous batching**: Dynamically batches incoming requests for maximum GPU utilization
- **OpenAI-compatible API**: Production-ready with full function calling support
- **Linear scaling**: Throughput scales almost linearly with concurrent users
- **Hardware support**: A100, H100, RTX 4090, MI300X

## Performance

Benchmarked on A100-PCIE-40GB with Llama-3.1-8B-instruct:
- Peak throughput: 793 TPS (vs [[entities/ollama]]'s 41 TPS)
- P99 latency at peak: 80ms (vs Ollama's 673ms)
- Stable under extreme concurrency

## When to Use vLLM

- Multi-user applications (team KB, shared inference server)
- Production deployments requiring SLAs
- Autonomous agent systems needing robust tool orchestration
- High-volume batch processing

## When to Use Ollama Instead

- Local development and prototyping
- Single-user applications
- When setup simplicity matters more than throughput

## 2026 Benchmark Update (H100)

Per [[sources/premai-inference-servers-compared]], on Llama 3.1 8B (H100, 1000 ShareGPT prompts):
- Default backend: ~10,000 tok/s
- FlashInfer backend: 12,553 tok/s
- GPU utilization: 85-92% under high concurrency
- Scales linearly to 100-150 concurrent requests
- Broadest hardware support: NVIDIA, AMD, Intel, TPU

Note: [[entities/sglang|SGLang]] achieves 16,215 tok/s (29% faster) on the same benchmark, but vLLM's broader hardware support and mature ecosystem make it the safer production default.

## Mentioned In
- [[sources/ollama-vs-vllm-benchmarks]] — detailed A100 benchmark comparison
- [[sources/local-llm-hosting-tools-comparison]] — positioned as production tool
- [[sources/premai-inference-servers-compared]] — 2026 H100 benchmarks vs SGLang, TGI, Triton
- [[sources/kv-cache-optimization-techniques]] — PagedAttention as KV cache innovation
- [[sources/bentoml-batching-strategies]] — continuous batching implementation
