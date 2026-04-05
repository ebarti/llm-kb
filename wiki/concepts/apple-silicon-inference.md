---
title: "Apple Silicon Inference"
type: concept
sources: ["[[sources/mlx-vs-llamacpp-apple-silicon]]", "[[sources/apple-silicon-llm-inference-study]]"]
related: ["[[concepts/local-llm-inference]]", "[[entities/mlx]]", "[[entities/llama-cpp]]", "[[entities/ollama]]", "[[concepts/quantization]]"]
last_compiled: 2026-04-05
summary: "Apple Silicon's unified memory architecture makes Macs uniquely suited for local LLM inference; MLX leads throughput (<14B models), llama.cpp handles larger models via CPU+GPU splitting."
---

## Overview

Apple Silicon (M1, M2, M3, M4, M5) has a unique advantage for [[concepts/local-llm-inference]]: unified memory architecture (UMA). Unlike discrete GPU systems where data must be copied between CPU RAM and GPU VRAM, Apple's UMA shares a single memory pool between CPU and GPU, eliminating transfer overhead. This makes Macs surprisingly capable LLM hosts, especially for models that fit entirely in the available unified memory.

## Key Ideas

### Unified Memory Advantage

Traditional GPU inference requires:
1. Load model weights into GPU VRAM
2. Copy input data from CPU RAM to GPU VRAM
3. Run inference on GPU
4. Copy results back to CPU RAM

Apple Silicon eliminates steps 2 and 4 via zero-copy shared memory. [[entities/mlx]] fully exploits this with lazy evaluation and operation fusion.

### Runtime Comparison on Apple Silicon

ArXiv study (November 2025) on Mac Studio M2 Ultra (192GB):

| Runtime | Throughput | TTFT | Best For |
|---------|-----------|------|----------|
| [[entities/mlx]] | ~230 tok/s (highest) | Good | Small-medium models, Python workflows |
| MLC-LLM | Good | Lowest | Low-latency applications |
| [[entities/llama-cpp]] | ~180 tok/s | Good | Large models, cross-platform |
| [[entities/ollama]] | Lower | Higher | Developer ergonomics |
| PyTorch MPS | Limited | Limited | Research experimentation |

### MLX vs llama.cpp by Model Size

| Model Size | Winner | Why |
|-----------|--------|-----|
| <14B | MLX (+21-87%) | Zero-copy memory, operation fusion |
| 14-27B | Roughly equal | Both hit memory bandwidth ceiling |
| 27B+ | llama.cpp | CPU+GPU layer splitting enables larger models |
| 70B on 64GB | llama.cpp only | MLX cannot exceed GPU memory |

### Hardware Generation Matters

- **M1/M2**: llama.cpp recommended (MLX has bf16 software emulation penalty during prefill)
- **M3+**: MLX delivers superior throughput (native bf16 support)
- **M5**: Apple demonstrated up to 4x speedup vs M4 for MLX workloads using Neural Accelerators

### Ollama + MLX Integration

In March 2026, [[entities/ollama]] announced MLX integration for Apple Silicon, delivering 57% faster prefill and 93% faster decode performance. This combines Ollama's developer ergonomics with MLX's raw performance.

### Practical Recommendations for Mac Users

| Mac Configuration | Recommended Model Size | Example Models |
|------------------|----------------------|----------------|
| 8GB M1/M2 | 3-4B (Q4) | Phi-4-mini, Qwen 3 4B |
| 16GB M1/M2/M3 | 7-8B (Q4) | Llama 3.1 8B, Mistral 7B |
| 32GB M3/M4 | 14B (Q4) | Phi-4, DeepSeek Coder |
| 64GB M3/M4 Pro/Max | 32B (Q4) | Qwen 2.5 Coder 32B |
| 96-192GB M2/M4 Ultra | 70B+ (Q4) | Llama 3.1 70B, full MoE models |

### Limitations

All Apple Silicon frameworks trail NVIDIA GPU-based systems (e.g., [[entities/vllm]] on A100/H100) in absolute performance. The gap is significant for multi-user or high-throughput production scenarios. Apple Silicon inference is best suited for personal use, development, and small-team deployments.

## Sources
- [[sources/mlx-vs-llamacpp-apple-silicon]] — detailed benchmarks and recommendations
- [[sources/apple-silicon-llm-inference-study]] — academic five-framework comparison

## Related Concepts
- [[concepts/local-llm-inference]] — Apple Silicon as one inference platform
- [[entities/mlx]] — Apple's purpose-built framework
- [[entities/llama-cpp]] — cross-platform alternative on Apple Silicon
- [[concepts/quantization]] — essential for fitting models in unified memory
- [[concepts/local-knowledge-base]] — running KB systems on a Mac
