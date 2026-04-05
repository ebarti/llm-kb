---
title: "Training Stability"
type: concept
sources: ["[[sources/spike-no-more-training-stability]]", "[[sources/rohan-paul-stabilizing-llm-training]]"]
related: ["[[concepts/loss-spikes]]", "[[concepts/learning-rate-schedules]]", "[[concepts/mixed-precision-training]]", "[[concepts/llm-pretraining]]"]
last_compiled: 2026-04-05
summary: "Keeping LLM training runs from diverging over weeks/months: preventing loss spikes via gradient clipping, proper initialization, BFloat16 precision, learning rate warmup, and specialized optimizers (SPAM, LAMB)."
---

## Overview

Training stability is the challenge of keeping an LLM pretraining run — often lasting weeks or months on thousands of GPUs — from diverging, producing NaN values, or suffering catastrophic [[concepts/loss-spikes]] that destroy model quality. Given that a single frontier training run can cost $100M+, stability is not just a technical concern but an economic one: a diverged run at week 6 of 8 represents millions in wasted compute.

## Root Causes of Instability

### Gradient Explosions
The primary failure mode. Gradient norms suddenly spike to 1000x their typical magnitude, causing catastrophic parameter updates. In transformers, two specific mechanisms cause this (per [[sources/spike-no-more-training-stability]]):
1. **Shortcut explosion**: Residual connections amplify gradients through depth
2. **LayerNorm explosion**: When inputs to LayerNorm have small standard deviations, LN gradients become inversely proportional and explode

### Numerical Precision
[[concepts/mixed-precision-training]] with FP16 has a dynamic range ceiling of ~6.5x10^4. Values exceeding this overflow to infinity, propagating NaNs. BFloat16 (8 exponent bits matching FP32) virtually eliminates this issue.

### Learning Rate Sensitivity
Transformers have narrow stable learning rate ranges that shrink as model and batch sizes grow. GPT-3 (175B) used only 2.8e-5 peak learning rate — far lower than smaller models.

## Stabilization Techniques

### Gradient Clipping
Constrain gradient norms to a threshold (typically 1.0). Prevents runaway updates. The SPAM optimizer adds spike-aware clipping that selectively scales only spiked gradients.

### Learning Rate Warmup
Start with near-zero learning rate, gradually increase over 1-10% of total steps. Prevents instability before weights are properly calibrated. See [[concepts/learning-rate-schedules]].

### Sequence Length Warmup
Start training with shorter sequences, gradually increase. Reduces gradient variance in early training. Enables 8x larger batches and 4-40x higher learning rates.

### Proper Initialization
- Scaled initialization: reduce FFN output weights to prevent shortcut explosion
- Embed LN / Scaled Embed: normalize embedding vectors to prevent LN explosion
- Combined approach eliminates loss spikes and enables 2x larger learning rates

### Architecture Choices
- **Pre-LayerNorm**: More stable than Post-LayerNorm
- **DeepNorm**: Microsoft's modification enabling stable 1000-layer transformers
- **Mix-LN**: Hybrid pre/post-layernorm
- **Softmax capping**: Limit attention logit magnitudes

### Specialized Optimizers
- **SPAM**: Spike-Aware Adam with Momentum Reset — detects spikes and resets optimizer state
- **LAMB**: Layer-wise Adaptive Moments — enables batch sizes up to 32,000
- **Adafactor**: Memory-efficient, stable for 11B+ parameter models

## Practical Protocol

1. Start conservative: BFloat16, gradient clipping at 1.0, warmup 5-10% of steps
2. Monitor aggressively: loss curves, gradient norms, NaN frequency
3. Use proper initialization (scaled init + embedding normalization)
4. Progressively increase: learning rate, batch size, sequence length
5. Keep synchronous training (async introduces stale gradients)

## Sources

- [[sources/spike-no-more-training-stability]] — theoretical analysis of gradient explosion mechanisms
- [[sources/rohan-paul-stabilizing-llm-training]] — comprehensive practitioner guide

## Related Concepts

- [[concepts/loss-spikes]] — the specific failure mode
- [[concepts/learning-rate-schedules]] — warmup and decay strategies
- [[concepts/mixed-precision-training]] — FP16 vs BFloat16
- [[concepts/llm-pretraining]] — the process being stabilized
