---
title: "Production-Grade Local LLM Inference on Apple Silicon: A Comparative Study"
source: "https://arxiv.org/abs/2511.05502"
author: "ArXiv researchers"
date_published: 2025-11-08
date_ingested: 2026-04-05
tags: [apple-silicon, mlx, llama-cpp, ollama, pytorch, local-inference, benchmarks, paper]
type: paper
status: raw
discovered_via: search
---

# Production-Grade Local LLM Inference on Apple Silicon

## Study Setup
- Hardware: Mac Studio with M2 Ultra, 192GB unified memory
- Frameworks tested: MLX, MLC-LLM, llama.cpp, Ollama, PyTorch MPS
- Model: Qwen-2.5 family
- Prompt range: Hundreds to 100,000 tokens
- Metrics: TTFT, steady-state throughput, latency percentiles, long-context behavior

## Performance Rankings

### Throughput Leader: MLX
- Highest sustained generation throughput (~230 tokens/sec)
- Surpasses llama.cpp by 20-30% on Apple Silicon

### Time-to-First-Token: MLC-LLM
- Consistently lower TTFT for moderate prompt sizes
- Stronger out-of-the-box inference features

### Lightweight Single-Stream: llama.cpp
- Highly efficient for lightweight single-stream use

### Developer Experience: Ollama
- Prioritizes ergonomics but lags in throughput and TTFT

### Limitations: PyTorch MPS
- Limited by memory constraints on large models and long contexts

## Key Findings
- All frameworks offer strong privacy guarantees through fully on-device execution with no telemetry
- Viable, production-grade solutions for private, on-device LLM inference
- Still trail NVIDIA GPU-based systems such as vLLM in absolute performance
