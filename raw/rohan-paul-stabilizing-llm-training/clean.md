---
title: "Stabilizing LLM Training: Techniques and Insights"
source: "https://www.rohan-paul.com/p/stabilizing-llm-training-techniques"
author: "Rohan Paul"
date_published: 2025-03-01
date_ingested: 2026-04-05
tags: [training-stability, gradient-clipping, learning-rate, mixed-precision, loss-spikes, optimizers]
type: article
status: raw
discovered_via: search
---

# Stabilizing LLM Training: Comprehensive Guide

## Core Causes of Training Instability

### Gradient Explosions and Loss Spikes
Training instability primarily stems from sudden gradient norm explosions, manifesting as sharp loss spikes. These can reach magnitudes far exceeding typical gradients. In transformer architectures, attention and feedforward components contribute disproportionately.

### Numerical Precision Challenges
Mixed-precision training (FP16/BFloat16) introduces vulnerabilities. FP16 has limited dynamic range (~6.5x10^4), causing overflow to infinity and NaNs. BFloat16 mitigates with 8 exponent bits (matching FP32) vs FP16's 5 bits.

### Learning Rate and Batch Size Effects
Stability-efficiency dilemma: increasing batch size or learning rate improves throughput but destabilizes training. Transformers exhibit narrow stable learning rate ranges that shrink as model and batch sizes grow.

## Stabilization Techniques

### Learning Rate Management
- Warmup: Starting with minimal learning rates, gradually increasing over hundreds/thousands of steps
- Lower base rates for scale: GPT-3 (175B) used only 2.8e-5 peak learning rate
- Sequence Length Warmup (SLW): Beginning with shorter sequences enables 8x larger batches and 4-40x higher learning rates
- Cosine decay and linear reduction schedules prevent late-training instabilities

### Gradient Clipping
Constraining gradient norms to fixed thresholds (typically 1.0 or 0.5) prevents runaway updates. SPAM optimizer refines with spike-aware clipping.

### Optimizer Innovation
- SPAM (Spike-Aware Adam with Momentum Reset): Detects large spikes and resets momentum estimates
- LAMB: Enables stable training with batch sizes up to 32,000 by adapting learning rates per layer
- Adafactor: Memory-efficient, reliable for 11B+ parameter models

### Initialization and Normalization
- Weight Scaling: Small initial parameter values prevent high-variance outputs
- DeepNorm: Microsoft's approach enables stable 1000-layer transformers
- Enhanced LayerNorm: Additional normalization after attention projections and FFN
- Mix-LN: Hybrid pre/post-layernorm

### Framework Implementations
- PyTorch AMP with dynamic loss scaling
- BFloat16 as industry standard for TPU-based training
- FSDP includes NaN detection for massive models

## Practical Recommendations
1. Start conservative: warmup (5-10% of total steps), gradient clipping at 1.0, BFloat16
2. Monitor aggressively: loss spikes, NaN frequency, gradient norm statistics
3. Progressively optimize: sequence length warmup, higher learning rates, larger batches
4. Architecture: Pre-LayerNorm with additional normalization
5. Distributed: synchronous training with careful all-reduce
