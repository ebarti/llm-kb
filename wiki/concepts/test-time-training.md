---
title: "Test-Time Training"
type: concept
sources: ["[[sources/ttrl-test-time-reinforcement-learning]]", "[[sources/hu-test-time-learning-llm]]"]
related: ["[[concepts/test-time-compute]]", "[[concepts/reinforcement-learning-for-reasoning]]", "[[concepts/reasoning-models]]", "[[entities/lora]]"]
last_compiled: 2026-04-05
summary: "Modifying model weights at inference time using unlabeled test data -- distinct from test-time scaling (which only changes inference procedure) -- via RL on majority-voted rewards (TTRL) or self-supervised perplexity minimization (TLM), achieving 20-211% improvements."
---

## Overview

Test-time training (TTT) is the practice of actually updating model weights during inference, adapting the model to the specific distribution or domain of test inputs. This is fundamentally different from [[concepts/test-time-compute]] (TTS), which allocates more compute without changing the model.

| Approach | Changes Weights? | Changes Procedure? | Key Method |
|----------|-----------------|-------------------|------------|
| Standard inference | No | No | Single forward pass |
| Test-Time Scaling (TTS) | No | Yes | Multiple samples, search, verification |
| Test-Time Training (TTT) | Yes | Yes | RL, self-supervised adaptation |

## Key Methods

### TTRL: Test-Time Reinforcement Learning

[[sources/ttrl-test-time-reinforcement-learning|Zuo et al. (NeurIPS 2025)]]:

1. Generate multiple solutions from the model.
2. Use **majority voting** (a TTS technique) to identify likely-correct answers.
3. Use this consensus as an RL reward signal for policy optimization.
4. The model improves using its own collective predictions.

Results: **211% improvement** for Qwen-2.5-Math-7B on AIME 2024. Crucially, TTRL surpasses the model's own majority voting ceiling -- demonstrating that TTT and TTS are complementary, not alternative.

### TLM: Test-Time Learning

[[sources/hu-test-time-learning-llm|Hu et al. (ICML 2025)]]:

1. Minimize input perplexity on unlabeled test data (self-supervised).
2. Focus adaptation on high-perplexity samples (most informative).
3. Use [[entities/lora|LoRA]] for lightweight updates, preventing catastrophic forgetting.

Results: **20%+ improvement** on domain knowledge adaptation without any labeled data.

### qTTT: Query-Only Test-Time Training

Uses test-time LoRA fine-tuning specifically for long-context retrieval tasks:
- 12.6-14.1 percentage point improvements on LongBench-v2 and ZeroScrolls.
- Combats score dilution in long-context scenarios.

## TTT + TTS: Complementary Strategies

The most powerful approach combines both:
- **TTS** (majority voting, search) provides diverse solutions.
- **TTT** (RL, self-supervised learning) improves the model using those solutions as training signal.
- TTRL demonstrates this synergy: majority voting provides the reward signal for RL that drives the model beyond what majority voting alone could achieve.

## Practical Considerations

- **Latency**: TTT adds significant latency (model must be updated before/during inference).
- **Compute**: Backpropagation at inference time is much more expensive than forward passes.
- **Stability**: Risk of catastrophic forgetting; LoRA helps but doesn't eliminate.
- **Generalization**: Adapted model may overfit to test distribution.

## Open Questions

- How many samples are needed for effective TTT?
- Can TTT be made fast enough for real-time applications?
- What is the optimal balance between TTT and TTS compute?
- Can TTT be combined with latent reasoning ([[concepts/latent-reasoning]])?

## Sources

- [[sources/ttrl-test-time-reinforcement-learning]] -- TTRL: RL with majority-voted rewards
- [[sources/hu-test-time-learning-llm]] -- TLM: self-supervised perplexity minimization

## Related Concepts

- [[concepts/test-time-compute]] -- the inference-compute-only alternative
- [[concepts/reinforcement-learning-for-reasoning]] -- RL as the TTT mechanism
- [[concepts/reasoning-models]] -- potential beneficiaries of TTT
