---
title: "Mixed-Precision Training"
type: concept
sources: ["[[sources/rohan-paul-stabilizing-llm-training]]"]
related: ["[[concepts/training-stability]]", "[[concepts/distributed-training]]", "[[concepts/llm-pretraining]]"]
last_compiled: 2026-04-05
summary: "Using lower-precision formats (FP16, BFloat16) during training to reduce memory and increase throughput. BFloat16 is now industry standard — its 8 exponent bits match FP32's dynamic range, virtually eliminating the overflow issues that plague FP16."
---

## Overview

Mixed-precision training uses lower-precision floating-point formats for most computations while maintaining higher precision for critical operations (like loss computation and gradient accumulation). This halves memory usage and doubles throughput on GPUs with tensor cores, but introduces numerical stability risks.

## Precision Formats

| Format | Bits | Exponent Bits | Mantissa Bits | Dynamic Range | Use Case |
|--------|------|--------------|--------------|---------------|----------|
| FP32 | 32 | 8 | 23 | ~3.4x10^38 | Master weights, loss, accumulation |
| FP16 | 16 | 5 | 10 | ~6.5x10^4 | Legacy mixed precision |
| BFloat16 | 16 | 8 | 7 | ~3.4x10^38 | Modern standard for training |
| FP8 | 8 | 4-5 | 2-3 | Limited | Emerging for inference, some training |

## BFloat16 vs FP16

**FP16** has only 5 exponent bits, creating a ceiling at ~6.5x10^4. Gradients, activations, or weights exceeding this value overflow to infinity, generating NaNs that propagate through the network. This requires **dynamic loss scaling**: multiplying the loss by a large factor before backward pass, then dividing gradients afterward.

**BFloat16** has 8 exponent bits (matching FP32), giving it the same dynamic range (~3.4x10^38). This virtually eliminates overflow concerns, making loss scaling unnecessary in most cases. The trade-off is lower precision (7 mantissa bits vs FP16's 10), but in practice this rarely affects training quality.

**BFloat16 is now the industry standard** for LLM training, especially on TPUs where it has native hardware support. All modern NVIDIA GPUs (A100, H100, H200, B200) also support BFloat16.

## Practical Implementation

- **PyTorch AMP**: `torch.cuda.amp` with `GradScaler` for FP16; BFloat16 often needs no scaler
- **Master weights in FP32**: Keep a full-precision copy of parameters for optimizer updates
- **Accumulate in FP32**: Sum gradients and loss in FP32 even when computing in BF16
- **LayerNorm in FP32**: Critical normalization layers should use full precision

## Sources

- [[sources/rohan-paul-stabilizing-llm-training]] — FP16 vs BFloat16 analysis, framework implementations

## Related Concepts

- [[concepts/training-stability]] — mixed precision is a key stability factor
- [[concepts/distributed-training]] — precision affects communication volume
- [[concepts/training-infrastructure]] — GPU hardware determines available formats
