---
title: "Loss Spikes"
type: concept
sources: ["[[sources/spike-no-more-training-stability]]", "[[sources/rohan-paul-stabilizing-llm-training]]"]
related: ["[[concepts/training-stability]]", "[[concepts/llm-pretraining]]", "[[concepts/learning-rate-schedules]]"]
last_compiled: 2026-04-05
summary: "Sudden catastrophic increases in training loss caused by gradient norm explosions (up to 1000x normal), which can degrade or ruin expensive LLM pretraining runs. Preventable through proper initialization, embedding normalization, and gradient clipping."
---

## Overview

Loss spikes are sudden, dramatic increases in the training loss during LLM pretraining. They manifest as the loss jumping far above the smooth downward trend, sometimes permanently degrading model quality or forcing a restart from an earlier checkpoint. Given that frontier training runs cost $100M+ and run for weeks, loss spikes represent significant economic risk.

## Root Causes

### Gradient Norm Explosions
The primary mechanism. Gradient norms suddenly spike to magnitudes 1000x larger than typical values, causing catastrophic parameter updates. Two specific sources in transformers:

1. **Shortcut (residual) explosion**: With standard initialization, FFN output standard deviations grow unbounded through residual connections, amplifying gradients exponentially during backpropagation.

2. **LayerNorm gradient explosion**: When LayerNorm inputs have very small standard deviations (common with scaled initialization), the LN gradient becomes inversely proportional: ||dLN/dx|| = O(sqrt(d)/||x||). Particularly affects shallow layers.

### Pathological Data
PaLM (540B) training revealed that rare tokens and pathological data sequences can trigger instabilities, leading to pre-screening approaches.

### Numerical Overflow
FP16 precision overflow (ceiling ~6.5x10^4) can produce infinity/NaN values that propagate through the network.

## Interventions

| Technique | Mechanism | Effect |
|-----------|-----------|--------|
| Embed LN | Normalize embedding vectors | Prevents LN gradient explosion |
| Scaled Embed | Multiply embeddings by sqrt(d) | Maintains LN input magnitudes |
| Gradient clipping | Cap gradient norms at threshold | Prevents extreme updates |
| SPAM optimizer | Spike-aware clipping + momentum reset | Blocks spike propagation |
| BFloat16 | Wider exponent range than FP16 | Prevents numerical overflow |
| Sequence length warmup | Start with short sequences | Reduces early gradient variance |

## Recovery Strategies

When spikes occur despite prevention:
- Roll back to a checkpoint from before the spike
- Skip the problematic data batch
- Reduce learning rate temporarily
- Restart with lower learning rate and retry

## Sources

- [[sources/spike-no-more-training-stability]] — theoretical analysis of two explosion mechanisms
- [[sources/rohan-paul-stabilizing-llm-training]] — practical guide with SPAM, framework implementations

## Related Concepts

- [[concepts/training-stability]] — the broader stability topic
- [[concepts/mixed-precision-training]] — numerical causes
- [[concepts/learning-rate-schedules]] — interaction with stability
