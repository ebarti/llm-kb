---
title: "Local LLM Inference"
type: concept
sources: ["[[sources/ollama-complete-guide]]", "[[sources/ollama-vs-vllm-benchmarks]]", "[[sources/local-llm-hosting-tools-comparison]]", "[[sources/mlx-vs-llamacpp-apple-silicon]]", "[[sources/apple-silicon-llm-inference-study]]", "[[sources/freecodecamp-local-rag-ollama]]"]
related: ["[[concepts/open-source-llms]]", "[[concepts/apple-silicon-inference]]", "[[concepts/quantization]]", "[[concepts/local-knowledge-base]]", "[[entities/ollama]]", "[[entities/vllm]]", "[[entities/llama-cpp]]", "[[entities/mlx]]"]
last_compiled: 2026-04-05
summary: "Running LLM inference on local hardware without cloud APIs, using tools like Ollama, vLLM, llama.cpp, and MLX — enabling privacy, offline operation, and zero per-token cost."
---

## Overview

Local LLM inference is the practice of running large language model inference on hardware you control — a laptop, desktop, or on-premises server — rather than calling a cloud API. This eliminates per-token costs, ensures data never leaves your machine, and enables fully offline operation.

The local inference ecosystem has matured rapidly. By 2026, multiple production-grade tools exist for every combination of hardware, use case, and skill level.

## Key Ideas

### The Tool Ecosystem

The [[concepts/local-llm-inference]] landscape spans from user-friendly GUIs to production servers:

| Tool | Type | Best For | Key Feature |
|------|------|----------|-------------|
| [[entities/ollama]] | CLI/API | Developers, prototyping | Docker-like model management |
| [[entities/vllm]] | Server | Production, multi-user | PagedAttention, 793 TPS |
| [[entities/llama-cpp]] | Library | Cross-platform, large models | CPU+GPU splitting, GGUF format |
| [[entities/mlx]] | Framework | Apple Silicon, Python | Zero-copy unified memory |
| [[entities/lm-studio]] | Desktop GUI | Beginners | Visual model browser |
| Jan | Desktop | Privacy-first | 100% offline, no telemetry |
| LocalAI | Server | Multimodal | Text + image + audio |

### Performance Spectrum

Throughput varies enormously by tool and hardware:
- [[entities/vllm]] on A100: 793 tokens/second (production multi-user)
- [[entities/mlx]] on M2 Ultra: ~230 tokens/second (single-user)
- [[entities/ollama]] on A100: 41 tokens/second (single-user optimized)
- [[entities/llama-cpp]] on M2 Ultra: ~180 tokens/second (single-user)

For interactive single-user KB applications, even 30-50 tokens/second provides usable response times.

### Hardware Requirements

The hardware floor depends on model size:

| Model Size | Q4 VRAM | Example Models |
|-----------|---------|----------------|
| 1-2B | 1-2 GB | Gemma 270M, Qwen 0.6B |
| 3-4B | 2-4 GB | Phi-4-mini, Gemma 3 4B, Qwen 3 4B |
| 7-8B | 3.5-5 GB | Mistral 7B, Llama 3.1 8B |
| 13-14B | 7-10 GB | Phi-4, DeepSeek Coder V2 Lite |
| 32B | 20-24 GB | Qwen 2.5 Coder 32B |
| 70B | 35-45 GB | Llama 3.1 70B (requires CPU+GPU split on most hardware) |

Apple Silicon Macs with unified memory are particularly well-suited: an M2 Max with 32GB can run 14B models comfortably, and an M2 Ultra with 192GB can handle 70B+ models entirely in memory.

### OpenAI API Compatibility

A critical feature across [[entities/ollama]], [[entities/vllm]], [[entities/lm-studio]], and LocalAI: they all expose OpenAI-compatible API endpoints. This means applications built against the OpenAI/Claude API can switch to local inference with minimal code changes — often just changing the base URL and model name.

### Key Tradeoffs vs Cloud APIs

| Dimension | Local Inference | Cloud API |
|-----------|----------------|-----------|
| Cost per token | Zero (after hardware) | $0.60-$30/M tokens |
| Privacy | Complete | Data sent to provider |
| Offline capable | Yes | No |
| Setup complexity | Moderate to high | Minimal |
| Quality (frontier) | ~3 months behind | Cutting edge |
| Concurrent users | Limited by hardware | Elastic |
| Maintenance | Self-managed | Provider-managed |

## Relevance to This Knowledge Base

This KB system's wiki compilation, Q&A, and linting operations could run on local inference instead of the Claude API. The practical path:

1. **Development/testing**: [[entities/ollama]] with Qwen 3 8B or DeepSeek V3 distilled 32B
2. **Production single-user**: [[entities/mlx]] (on Mac) or llama.cpp with a 14-32B model
3. **Production multi-user**: [[entities/vllm]] with a 70B+ model on GPU server

The main limitation: complex multi-step reasoning (like compiling 10+ sources into a coherent concept article) may produce lower quality results with local models than with Claude or GPT-4.

## Sources
- [[sources/ollama-complete-guide]] — Ollama architecture and setup
- [[sources/ollama-vs-vllm-benchmarks]] — performance comparison
- [[sources/local-llm-hosting-tools-comparison]] — ecosystem overview
- [[sources/mlx-vs-llamacpp-apple-silicon]] — Apple Silicon runtime comparison
- [[sources/apple-silicon-llm-inference-study]] — academic benchmark study
- [[sources/freecodecamp-local-rag-ollama]] — practical RAG tutorial

## Related Concepts
- [[concepts/open-source-llms]] — the models that power local inference
- [[concepts/apple-silicon-inference]] — Mac-specific inference optimizations
- [[concepts/quantization]] — making models fit on local hardware
- [[concepts/local-knowledge-base]] — applying local inference to KB systems
- [[concepts/small-language-models]] — most accessible models for local use
- [[comparisons/ollama-vs-vllm]] — the two dominant tools compared
