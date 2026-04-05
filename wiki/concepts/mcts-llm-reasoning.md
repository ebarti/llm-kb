---
title: "MCTS for LLM Reasoning"
type: concept
sources: ["[[sources/sakana-ab-mcts]]", "[[sources/zhang-test-time-scaling-survey]]", "[[sources/adaline-inside-reasoning-models]]", "[[sources/introl-inference-time-scaling-paradigm-shift]]"]
related: ["[[concepts/test-time-compute]]", "[[concepts/process-reward-models]]", "[[concepts/best-of-n-sampling]]", "[[concepts/reasoning-models]]"]
last_compiled: 2026-04-05
summary: "Monte Carlo Tree Search adapted for LLM inference: systematic exploration of reasoning paths via selection, expansion, simulation, and backpropagation -- used in o3 at inference time and for training data generation, with multi-model variants achieving 30%+ on ARC-AGI-2."
---

## Overview

Monte Carlo Tree Search (MCTS), the algorithm behind AlphaGo's superhuman Go play, has been adapted for LLM reasoning. Rather than exploring game positions, LLM-MCTS explores partial reasoning chains, using reward models to evaluate promising directions and backpropagation to update path values.

## The Four Stages

Applied to LLM reasoning:

1. **Selection**: Choose the most promising partial reasoning chain to extend (UCB balances exploration vs. exploitation).
2. **Expansion**: Generate one or more next reasoning steps from the selected chain.
3. **Simulation**: Complete the reasoning chain (rollout) and evaluate the final answer.
4. **Backpropagation**: Update the values of all nodes on the path based on the outcome.

## Applications

### Inference-Time Search (o3)
OpenAI's o3 is believed to use MCTS or a variant at inference time, exploring multiple reasoning paths and selecting the best. This is the most compute-intensive [[concepts/test-time-compute]] strategy but also the highest quality.

### Training Data Generation
MCTS can generate high-quality preference data for [[concepts/reinforcement-learning-for-reasoning|RL training]]:
- rStar-Math uses MCTS with [[concepts/process-reward-models]] for mathematical reasoning training.
- MCTS provides step-level reward signals by decomposing outcome rewards into per-step values via backpropagation.

### Multi-LLM Collective Intelligence
[[sources/sakana-ab-mcts|AB-MCTS (Sakana AI)]]:
- Searches in three dimensions: depth (refine), width (new solutions), and model identity.
- Uses Thompson Sampling for probabilistic direction selection.
- Multiple frontier models collaborate: ARC-AGI-2 accuracy goes from 23% (single model) to 30%+ (multi-model).

## Performance

MCTS approaches outperform baselines on mathematical reasoning:
- GSM8K: +5.9%
- MATH: +5.8%
- ARC-C: +15.8%

SC-MCTS improves both accuracy and speed over standard MCTS.

## The Reward Model Bottleneck

The reward model is the most crucial component. MCTS quality is bounded by verifier quality:
- Strong [[concepts/process-reward-models|PRMs]] enable effective tree pruning.
- Weak verifiers lead to misspent compute on dead-end paths.
- [[sources/introl-inference-time-scaling-paradigm-shift|Crosley (2025)]]: DeepSeek-R1 explicitly found MCTS less effective than pure RL, possibly due to reward model limitations.

## MCTS vs. Simpler Methods

| Method | Compute Cost | Quality | Parallelizability | Infrastructure |
|--------|-------------|---------|-------------------|---------------|
| [[concepts/best-of-n-sampling]] | Low-Medium | Good at scale | Highly parallel | Simple |
| Beam search | Medium | Good | Moderately parallel | Moderate |
| MCTS | High-Very High | Highest | Sequential (tree) | Complex |

MCTS wins when: problems are very hard, compute budgets are generous, and strong reward models are available. BoN wins when: problems are easier, parallelism matters, and simpler infrastructure is preferred.

## Open Questions

- Can MCTS overhead be reduced through learned search policies?
- How does MCTS interact with [[concepts/latent-reasoning]]?
- Will multi-model MCTS ([[sources/sakana-ab-mcts|AB-MCTS]]) become standard?
- Can MCTS be made real-time for interactive applications?

## Sources

- [[sources/sakana-ab-mcts]] -- AB-MCTS multi-model collective intelligence
- [[sources/zhang-test-time-scaling-survey]] -- MCTS in the TTS taxonomy
- [[sources/adaline-inside-reasoning-models]] -- MCTS in o3
- [[sources/introl-inference-time-scaling-paradigm-shift]] -- R1's MCTS findings

## Related Concepts

- [[concepts/test-time-compute]] -- the paradigm MCTS implements
- [[concepts/process-reward-models]] -- the verifiers guiding MCTS
- [[concepts/best-of-n-sampling]] -- the simpler alternative
- [[concepts/reasoning-models]] -- the models using MCTS
