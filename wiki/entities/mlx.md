---
title: "MLX"
type: entity
entity_type: tool
sources: ["[[sources/mlx-vs-llamacpp-apple-silicon]]", "[[sources/apple-silicon-llm-inference-study]]"]
related: ["[[concepts/apple-silicon-inference]]", "[[concepts/local-llm-inference]]", "[[entities/llama-cpp]]", "[[entities/ollama]]"]
last_compiled: 2026-04-05
summary: "Apple's open-source ML framework for Apple Silicon — exploits unified memory for zero-copy inference; leads throughput on <14B models; supports on-device LoRA fine-tuning."
---

## Overview

MLX is an open-source array framework created by Apple, specifically optimized for Apple Silicon. It exploits the unified memory architecture (UMA) of M-series chips to achieve zero-copy data sharing between CPU and GPU, eliminating transfer overhead that limits other frameworks. MLX is the throughput leader for [[concepts/apple-silicon-inference]] on small-to-medium models.

## Key Features

- **Zero-copy unified memory**: No CPU-GPU data transfers
- **Lazy evaluation**: Builds compute graphs before execution for operation fusion
- **Pure Python interface**: `pip install mlx-lm`, no compilation needed
- **On-device fine-tuning**: LoRA and QLoRA support
- **Swift bindings**: Native iOS/macOS app integration
- **Quantization**: 4-bit and 8-bit integer with configurable group sizes
- **Model hub**: `mlx-community` on Hugging Face

## Performance

| Model | MLX tok/s | llama.cpp tok/s | MLX Advantage |
|-------|-----------|-----------------|---------------|
| Qwen 0.6B (Q4) | 525.5 | 281.5 | +87% |
| Qwen 8B (Q4) | 93.3 | 76.9 | +21% |
| Llama 3.2 1B (Q4) | 461.9 | 331.3 | +39% |

ArXiv study: ~230 tok/s sustained (highest of all Apple Silicon runtimes), surpassing [[entities/llama-cpp]] by 20-30%.

## Limitations

- Cannot handle models exceeding available GPU memory (no CPU+GPU splitting)
- 4-bit and 8-bit quantization only (vs llama.cpp's 1.5-8 bit range)
- bf16 emulation penalty on M1/M2 chips (native on M3+)
- Slower prefill than llama.cpp at long contexts (8K+ tokens)

## Ollama Integration (March 2026)

[[entities/ollama]] announced MLX as its Apple Silicon backend, delivering:
- 57% faster prefill
- 93% faster decode
- Combines Ollama's ergonomics with MLX's raw performance

## When to Use MLX

- Models under 14B parameters on M3+ hardware
- Python-first development workflows
- On-device fine-tuning (LoRA/QLoRA)
- Swift/iOS integration
- Maximum throughput per watt on Apple Silicon

## Mentioned In
- [[sources/mlx-vs-llamacpp-apple-silicon]] — detailed benchmark comparison
- [[sources/apple-silicon-llm-inference-study]] — academic evaluation
