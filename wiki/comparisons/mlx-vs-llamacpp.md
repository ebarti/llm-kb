---
title: "MLX vs llama.cpp"
type: comparison
subjects: ["[[entities/mlx]]", "[[entities/llama-cpp]]"]
sources: ["[[sources/mlx-vs-llamacpp-apple-silicon]]", "[[sources/apple-silicon-llm-inference-study]]"]
last_compiled: 2026-04-05
summary: "MLX wins throughput on <14B models (+21-87%) on Apple Silicon; llama.cpp wins for large models (CPU+GPU split), cross-platform, and fine-grained quantization."
---

## Overview

[[entities/mlx]] and [[entities/llama-cpp]] are the two primary runtimes for [[concepts/apple-silicon-inference]]. They make fundamentally different architectural choices that favor different use cases.

## Comparison Table

| Dimension | MLX | llama.cpp |
|-----------|-----|-----------|
| **Small model throughput (<14B)** | +21-87% faster | Baseline |
| **Large model throughput (27B+)** | Equal (bandwidth-limited) | Equal |
| **70B on 64GB Mac** | Not possible | Supported (CPU+GPU split) |
| **Long context (8K+)** | Slower prefill | Faster (FlashAttention) |
| **Quantization range** | 4-bit, 8-bit | 1.5-bit to 8-bit |
| **Cross-platform** | Apple Silicon only | All platforms |
| **Language** | Python-first | C/C++ (with bindings) |
| **Fine-tuning** | LoRA, QLoRA on-device | Not supported |
| **Swift/iOS** | Native bindings | Via C API |
| **M1/M2 chips** | bf16 emulation penalty | No penalty |
| **M3+ chips** | Native bf16, best performance | Good performance |
| **Model format** | Safetensors-based | GGUF (universal) |
| **Setup** | `pip install mlx-lm` | Compile or use binaries |
| **Production server** | Basic | `llama-server` (OpenAI API) |

## Benchmark Data (Apple Silicon)

| Model | MLX tok/s | llama.cpp tok/s | Winner |
|-------|-----------|-----------------|--------|
| Qwen 0.6B (Q4) | 525.5 | 281.5 | MLX (+87%) |
| Llama 3.2 1B (Q4) | 461.9 | 331.3 | MLX (+39%) |
| Qwen 8B (Q4) | 93.3 | 76.9 | MLX (+21%) |
| 27B+ models | ~equal | ~equal | Tie |

Both hit memory bandwidth ceiling (~400 GB/s on M2 Ultra) at larger model sizes.

## When to Use Each

### Choose MLX When
- Running models under 14B parameters
- Using M3 or newer Apple Silicon
- Python-first development
- Need on-device fine-tuning (LoRA/QLoRA)
- Building Swift/iOS applications
- Maximum throughput per watt desired

### Choose llama.cpp When
- Need cross-platform compatibility
- Running 70B+ models via CPU+GPU layer splitting
- Long-context workloads (8K+ tokens)
- Need fine-grained quantization control (sub-4-bit)
- Production HTTP server deployment
- Using M1/M2 hardware

### For This KB on Mac
- **8-16GB Mac**: llama.cpp (more flexible with limited memory)
- **32GB M3/M4 Mac**: MLX (faster for 8-14B models)
- **64GB+ Mac with 32B+ model**: llama.cpp (CPU+GPU split may be needed)

## Sources
- [[sources/mlx-vs-llamacpp-apple-silicon]] — detailed benchmarks
- [[sources/apple-silicon-llm-inference-study]] — academic five-framework study
