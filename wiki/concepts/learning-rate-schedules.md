---
title: "Learning Rate Schedules"
type: concept
sources: ["[[sources/rohan-paul-stabilizing-llm-training]]"]
related: ["[[concepts/training-stability]]", "[[concepts/llm-pretraining]]", "[[concepts/loss-spikes]]"]
last_compiled: 2026-04-05
summary: "How the learning rate varies during LLM training: warmup phase (linear ramp, 1-10% of steps), followed by cosine decay or the newer Warmup-Stable-Decay (WSD) schedule. Critical for both stability and final model quality."
---

## Overview

The learning rate schedule defines how the learning rate changes over the course of training. It is one of the most critical hyperparameters for LLM pretraining, directly affecting both [[concepts/training-stability]] and final model quality. Modern LLM training universally uses schedules with at least two phases: warmup and decay.

## Common Schedules

### Linear Warmup + Cosine Decay
The classic schedule for LLM training:
1. **Warmup**: Linear increase from ~0 to peak LR over 1-2% of total steps
2. **Cosine decay**: Smooth decrease following a cosine curve to a minimum LR (typically 10% of peak)

Used by GPT-3, Llama, and most models pre-2024. The cosine curve decreases slowly at first, faster in the middle, and slowly again near the end.

**Limitation**: Requires knowing the total training step count in advance, making it unsuitable for open-ended or continual training.

### Warmup-Stable-Decay (WSD)
A newer three-phase schedule becoming standard for large-scale training:
1. **Warmup**: Linear ramp to peak LR (same as above)
2. **Stable**: Constant learning rate for the majority of training
3. **Decay**: Rapid decay when a specific checkpoint is desired

**Advantages**:
- No need to pre-specify total training steps
- Can branch off at any point by applying decay
- Produces a "main branch" that trains indefinitely at constant LR
- During stable phase, loss is higher than cosine, but decay phase catches up
- Theoretically optimal for balancing risk reduction and noise forgetting

### Linear Warmup + Linear Decay
Simpler alternative used by some models. Linearly decreases LR after warmup.

## Key Parameters

| Parameter | Typical Value | Notes |
|-----------|--------------|-------|
| Peak learning rate | 1e-4 to 6e-4 (small models), 2.8e-5 (GPT-3 175B) | Decreases with model size |
| Warmup steps | 1-10% of total | More warmup for larger models |
| Minimum learning rate | 10% of peak | Prevents complete stalling |
| Warmup shape | Linear | Sometimes cosine or inverse sqrt |

## Interaction with Other Techniques

- **Batch size scaling**: Learning rate should scale with sqrt(batch_size) for stability
- **[[concepts/loss-spikes]]**: Higher learning rates increase spike risk; warmup prevents early instability
- **Sequence length warmup**: Complementary technique — start with short sequences and gradually increase
- **Gradient accumulation**: Affects effective batch size, indirectly interacting with LR

## Sources

- [[sources/rohan-paul-stabilizing-llm-training]] — warmup, cosine decay, SLW, practical guidance

## Related Concepts

- [[concepts/training-stability]] — LR schedule is a primary stability tool
- [[concepts/loss-spikes]] — LR too high triggers spikes
- [[concepts/llm-pretraining]] — the process being scheduled
