---
title: "LLM Serving Frameworks"
type: concept
sources: ["[[sources/premai-inference-servers-compared]]", "[[sources/bentoml-batching-strategies]]"]
related: ["[[concepts/llm-inference-optimization]]", "[[concepts/continuous-batching]]", "[[concepts/kv-cache]]", "[[entities/vllm]]", "[[entities/sglang]]"]
last_compiled: 2026-04-05
summary: "Production software for serving LLM inference: vLLM (production default, broadest hardware), SGLang (throughput leader, multi-turn specialist), Triton (enterprise NVIDIA), with TGI in maintenance mode since Dec 2025."
---

## Overview

LLM serving frameworks are the infrastructure layer between trained models and production applications. They handle request scheduling, memory management ([[concepts/kv-cache|KV cache]]), [[concepts/continuous-batching|batching]], model parallelism, and API compatibility. The choice of framework directly determines throughput, latency, cost-per-token, and operational complexity.

## The 2026 Landscape

| Framework | Best For | Status | Core Innovation |
|-----------|----------|--------|-----------------|
| [[entities/vllm\|vLLM]] | High-concurrency API | Active, production standard | PagedAttention |
| [[entities/sglang\|SGLang]] | Multi-turn chat & agents | Active, rapidly growing | RadixAttention |
| Triton | Enterprise multi-model | Active, NVIDIA-focused | Multi-model pipelines |
| TGI | Legacy deployments | **Maintenance mode** (Dec 2025) | — |
| LMDeploy | Batch inference | Active | Competitive throughput |
| Ollama | Local development | Active | Simplicity |

## Benchmark Comparison (Llama 3.1 8B, H100, 1000 ShareGPT prompts)

| Framework | Throughput (tok/s) | vs Baseline |
|-----------|-------------------|-------------|
| SGLang | 16,215 | Baseline |
| LMDeploy | 16,132 | -0.5% |
| vLLM (FlashInfer) | 12,553 | -22.6% |
| vLLM (default) | ~10,000 | -38% |

## Decision Framework

- **High-Concurrency API (100+ users)**: vLLM — PagedAttention handles memory efficiently at scale with mature operational tooling
- **Conversational AI / Agents / RAG**: SGLang — automatic prefix caching provides measurable savings when requests share context
- **Batch Inference (offline)**: SGLang or LMDeploy — 29% throughput advantage on H100
- **Enterprise Multi-Model**: Triton — unified infrastructure for LLMs + embeddings + rerankers
- **Local Development**: Ollama — simplest setup, unsuitable for production

## Key Technical Differentiators

**vLLM**: Broadest hardware support (NVIDIA, AMD, Intel, TPU). 85-92% GPU utilization under high concurrency. OpenAI-compatible API out of the box. Trades raw speed for compatibility and operational maturity.

**SGLang**: RadixAttention automatically discovers KV cache reuse via radix tree. 85-95% cache hit rates on few-shot, 75-90% on multi-turn. 95-98% GPU utilization with zero-overhead CPU scheduler. Advantages disappear for single-turn independent requests.

**Triton**: General-purpose platform supporting PyTorch, TensorFlow, ONNX, TensorRT. TensorRT-LLM backend delivers lowest single-request latency on NVIDIA GPUs (14x TTFT reduction on H100/GH200). Complex setup justified only in established NVIDIA enterprise environments.

## Sources
- [[sources/premai-inference-servers-compared]] — 2026 comparison with benchmarks
- [[sources/bentoml-batching-strategies]] — framework support for continuous batching

## Related Concepts
- [[concepts/continuous-batching]] — the scheduling technique all frameworks implement
- [[concepts/kv-cache]] — PagedAttention and RadixAttention innovations
- [[concepts/llm-inference-optimization]] — frameworks as the serving layer of the optimization stack
