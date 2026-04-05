---
title: "Source: Stabilizing LLM Training — Techniques and Insights"
type: source-summary
source: "[[raw/rohan-paul-stabilizing-llm-training]]"
related: ["[[concepts/training-stability]]", "[[concepts/loss-spikes]]", "[[concepts/learning-rate-schedules]]", "[[concepts/mixed-precision-training]]"]
last_compiled: 2026-04-05
summary: "Comprehensive practitioner guide to training stability: gradient clipping, learning rate warmup, BFloat16 precision, optimizer innovations (SPAM, LAMB, Adafactor), architectural choices (DeepNorm, Mix-LN), and framework-specific implementations (PyTorch AMP, FSDP)."
---

## Key Points

- BFloat16 eliminates most FP16 overflow issues (8 vs 5 exponent bits)
- GPT-3 (175B) used only 2.8e-5 peak learning rate for stability
- Sequence Length Warmup enables 8x larger batches and 4-40x higher learning rates
- SPAM optimizer: spike-aware gradient clipping with momentum reset
- LAMB enables batch sizes up to 32,000
- DeepNorm enables stable 1000-layer transformers
- Practical rule: start with warmup (5-10% of steps), gradient clipping at 1.0, BFloat16

## Detailed Summary

This article provides the most comprehensive practical guide to [[concepts/training-stability]] across the ingested sources.

**Root causes**: gradient explosions (sudden norm spikes 1000x typical), numerical precision overflow (FP16), learning rate/batch size sensitivity, and RLHF policy drift.

**[[concepts/mixed-precision-training]]**: BFloat16 is now industry standard. Its 8 exponent bits match FP32's dynamic range, virtually eliminating overflow. FP16's 5 exponent bits create a ceiling at ~6.5x10^4 that causes NaN propagation.

**[[concepts/learning-rate-schedules]]**: Warmup (5-10% of steps), cosine decay for late-stage stability, and the novel Sequence Length Warmup (SLW) that starts with short sequences and gradually increases.

**Optimizer innovations**:
- SPAM: detects gradient spikes and resets momentum, preventing spike persistence
- LAMB: per-layer adaptive learning rates for extreme batch sizes
- Adafactor: memory-efficient factored second moments for 11B+ models

**Architecture**: Pre-LayerNorm placement, DeepNorm for ultra-deep models, Mix-LN (hybrid pre/post), softmax capping in attention.

## Related Concepts

- [[concepts/training-stability]] — the overarching topic
- [[concepts/mixed-precision-training]] — FP16 vs BFloat16 vs FP32
- [[concepts/learning-rate-schedules]] — warmup, cosine decay, WSD
- [[concepts/loss-spikes]] — the failure mode being prevented
