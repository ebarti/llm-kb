---
title: "llama.cpp"
type: entity
entity_type: tool
sources: ["[[sources/mlx-vs-llamacpp-apple-silicon]]", "[[sources/apple-silicon-llm-inference-study]]", "[[sources/ollama-complete-guide]]"]
related: ["[[concepts/local-llm-inference]]", "[[concepts/quantization]]", "[[entities/ollama]]", "[[entities/mlx]]"]
last_compiled: 2026-04-05
summary: "C/C++ LLM inference engine — foundation for Ollama; supports GGUF format, 1.5-8 bit quantization, CPU+GPU splitting; runs on every platform from phones to servers."
---

## Overview

llama.cpp is an open-source C/C++ library for LLM inference, created by Georgi Gerganov. It is the foundational technology underlying [[entities/ollama]] and many other local inference tools. Its primary goal is to enable LLM inference with minimal setup and state-of-the-art performance across the widest range of hardware.

## Key Features

- **GGUF format**: Single-file format storing model weights and metadata, cross-platform portable
- **Extensive quantization**: 1.5-bit (IQ1_S) through 8-bit (Q8_0), plus importance-matrix guided quantization
- **CPU+GPU hybrid**: Split model layers between CPU and GPU via `-ngl` flag — enables 70B models on 64GB machines
- **Cross-platform**: Windows, Linux, macOS, Android, iOS
- **Apple Silicon optimized**: ARM NEON, Accelerate, Metal frameworks
- **x86 optimized**: AVX, AVX2, AVX512, AMX support
- **HTTP server**: `llama-server` with OpenAI-compatible API

## Architecture

llama.cpp processes models stored in GGUF format through the GGML tensor library. It constructs a computation graph and executes inference using available hardware acceleration (Metal on Mac, CUDA on NVIDIA, ROCm on AMD, or CPU).

## Performance on Apple Silicon

From benchmarks (M2 Ultra, 192GB):
- ~180 tokens/second sustained throughput
- Efficient for single-stream use
- Can run 70B models via CPU+GPU layer splitting (MLX cannot)
- llama.cpp preferred over [[entities/mlx]] for M1/M2 chips and long-context workloads

## Quantization Capabilities

| Level | Bits | Use Case |
|-------|------|----------|
| IQ1_S | ~1.5 | Extreme compression, significant quality loss |
| Q2_K | 2 | Maximum compression with usable quality |
| Q3_K_M | 3 | Good balance for very large models |
| Q4_K_M | 4 | Sweet spot for most use cases |
| Q5_K_M | 5 | Higher quality, moderate compression |
| Q6_K | 6 | Near-lossless |
| Q8_0 | 8 | Minimal quality loss |

## Mentioned In
- [[sources/mlx-vs-llamacpp-apple-silicon]] — Apple Silicon benchmark comparison
- [[sources/apple-silicon-llm-inference-study]] — academic evaluation
- [[sources/ollama-complete-guide]] — llama.cpp as Ollama's foundation
