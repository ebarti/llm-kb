---
title: "FlashAttention"
type: entity
entity_type: framework
url: "https://github.com/Dao-AILab/flash-attention"
related: ["[[concepts/flash-attention]]", "[[concepts/self-attention]]", "[[concepts/kv-cache]]", "[[entities/tri-dao]]"]
tags: [flash-attention, GPU-optimization, efficient-attention]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "IO-aware exact attention algorithm by Tri Dao reducing memory from O(N^2) to O(N) via tiling — now the default attention implementation in PyTorch, JAX, and all major LLM frameworks, with v3 achieving 75% H100 utilization."
---

## Overview

FlashAttention is an exact attention algorithm that restructures the computation of scaled dot-product [[concepts/self-attention]] to minimize GPU memory traffic. Created by [[entities/tri-dao]], it is the most impactful systems-level optimization for the [[concepts/transformer-architecture]].

## Key Facts

- **Type**: Software library / algorithm
- **URL**: https://github.com/Dao-AILab/flash-attention
- **Notable for**: Making exact attention compute in O(N) memory instead of O(N^2) by never materializing the full attention matrix
- **Created by**: [[entities/tri-dao]] (Princeton, then Together AI)
- **Language**: CUDA/C++ with Python bindings

## Version History

| Version | Year | Key Innovation | Performance |
|---------|------|---------------|-------------|
| v1 | 2022 | IO-aware tiling + online softmax trick | 2-4x speedup, O(N) memory |
| v2 | 2023 | Improved parallelism + head scheduling | ~70% A100 utilization |
| v3 | 2024 | Async warp specialization + FP8 incoherent processing | 75% H100 utilization, 740 TFLOPS FP16, ~1.2 PFLOPS FP8 |

## Adoption

FlashAttention is now the default attention implementation in:
- **PyTorch**: `torch.nn.functional.scaled_dot_product_attention` uses FlashAttention when available
- **JAX/XLA**: FlashAttention kernels integrated
- **Hugging Face Transformers**: Default for compatible hardware
- **vLLM, SGLang, TensorRT-LLM**: All inference frameworks use FlashAttention

## Mentioned In

- [[sources/flashattention-3-tri-dao-blog]] — detailed technical overview of v3
- [[sources/flashattention-3-paper]] — NeurIPS 2024 paper
- [[sources/attention-mechanisms-comprehensive-survey]] — FlashAttention as key efficiency approach

## External References

- [GitHub Repository](https://github.com/Dao-AILab/flash-attention)
- [FlashAttention-3 Paper](https://arxiv.org/abs/2407.08691)
- [Tri Dao's Blog](https://tridao.me/blog/2024/flash3/)
