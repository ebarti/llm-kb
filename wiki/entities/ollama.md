---
title: "Ollama"
type: entity
entity_type: tool
sources: ["[[sources/ollama-complete-guide]]", "[[sources/ollama-vs-vllm-benchmarks]]", "[[sources/local-llm-hosting-tools-comparison]]", "[[sources/freecodecamp-local-rag-ollama]]"]
related: ["[[concepts/local-llm-inference]]", "[[entities/llama-cpp]]", "[[entities/vllm]]", "[[concepts/local-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "Most popular local LLM tool (150K+ GitHub stars) — abstracts llama.cpp into Docker-like experience with Modelfiles, OpenAI-compatible API, and cross-platform GPU support."
---

## Overview

Ollama is an open-source inference framework that simplifies running LLMs locally. With 150K+ GitHub stars and 500+ contributors, it is the most popular tool for [[concepts/local-llm-inference]]. Ollama operates as an abstraction layer above [[entities/llama-cpp]] and GGML, eliminating the complexity of manual compilation and configuration.

## Key Features

- **Modelfiles**: Docker-like blueprints for model configuration (system prompts, parameters, behavior)
- **OpenAI-compatible API**: /v1/completions, /v1/chat/completions, /v1/embeddings — drop-in replacement for cloud APIs
- **Cross-platform**: NVIDIA CUDA, Apple Silicon Metal, AMD ROCm, CPU fallback
- **One-line install**: `curl -fsSL https://ollama.com/install.sh | sh` or `brew install ollama`
- **Model library**: `ollama pull llama3.2`, `ollama pull qwen3:4b`, etc.
- **Docker support**: CPU-only and GPU-accelerated containers
- **MLX integration** (March 2026): 57% faster prefill, 93% faster decode on Apple Silicon

## Architecture

1. User provides GGUF model checkpoint
2. Ollama launches HTTP server + llama.cpp inference engine
3. GGML unpacks GGUF and constructs computation graph
4. Prompts route through llama.cpp server
5. Tokens stream back to caller

## Performance Characteristics

- Optimized for single-user, interactive use
- Default: 4 parallel requests (tunable to 32)
- On A100: ~41 TPS vs [[entities/vllm]]'s 793 TPS for concurrent workloads
- Best for: local development, prototyping, personal applications

## Ollama Cloud

Datacenter-grade hardware for models too large for local machines, maintaining API compatibility with local deployments.

## Mentioned In
- [[sources/ollama-complete-guide]] — complete architecture and setup guide
- [[sources/ollama-vs-vllm-benchmarks]] — performance comparison with vLLM
- [[sources/local-llm-hosting-tools-comparison]] — positioned as developer tool
- [[sources/freecodecamp-local-rag-ollama]] — used in local RAG tutorial
