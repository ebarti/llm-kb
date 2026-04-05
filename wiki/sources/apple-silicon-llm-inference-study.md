---
title: "Source: Production-Grade Local LLM Inference on Apple Silicon"
type: source-summary
source: "[[raw/apple-silicon-llm-inference-study]]"
related: ["[[entities/mlx]]", "[[entities/llama-cpp]]", "[[entities/ollama]]", "[[concepts/apple-silicon-inference]]"]
last_compiled: 2026-04-05
summary: "ArXiv study on M2 Ultra: MLX leads throughput (~230 tok/s), MLC-LLM leads TTFT, llama.cpp efficient for single-stream, Ollama lags but best ergonomics — all viable for production on-device inference."
---

## Key Points
- Tested on Mac Studio M2 Ultra with 192GB unified memory
- Five frameworks compared: [[entities/mlx]], MLC-LLM, [[entities/llama-cpp]], [[entities/ollama]], PyTorch MPS
- MLX: highest sustained throughput (~230 tok/s), surpasses llama.cpp by 20-30%
- MLC-LLM: consistently lower time-to-first-token for moderate prompts
- llama.cpp: highly efficient for lightweight single-stream use
- Ollama: best ergonomics but lags in throughput and TTFT
- PyTorch MPS: limited by memory constraints on large models
- All frameworks trail NVIDIA GPU-based systems (e.g., [[entities/vllm]]) in absolute performance
- All provide strong privacy guarantees: fully on-device, no telemetry

## Detailed Summary

This November 2025 ArXiv paper provides the most comprehensive benchmark of [[concepts/apple-silicon-inference]] runtimes. Testing with Qwen-2.5 models across prompt sizes from hundreds to 100,000 tokens, the study establishes MLX as the throughput leader on Apple Silicon while noting that no single framework dominates all dimensions.

The key finding for [[concepts/local-knowledge-base]] applications: Apple Silicon inference is production-grade for personal and small-team use, but cannot match dedicated NVIDIA GPU servers for multi-user or high-throughput scenarios.

## Related Concepts
- [[concepts/apple-silicon-inference]] — primary subject of the study
- [[concepts/local-llm-inference]] — Apple Silicon as a local inference platform
- [[concepts/local-knowledge-base]] — implications for running KB systems locally
