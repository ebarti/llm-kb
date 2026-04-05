---
title: "Source: Inside Reasoning Models: OpenAI o3 and DeepSeek R1"
type: source-summary
source: "[[raw/adaline-inside-reasoning-models]]"
related: ["[[concepts/reasoning-models]]", "[[concepts/test-time-compute]]", "[[entities/openai]]", "[[entities/deepseek]]"]
last_compiled: 2026-04-05
summary: "Deep technical analysis of o3 and R1 training pipelines, architectures (dense transformer vs. MoE), RL methodologies, benchmark comparisons, and computational costs -- positioning RL as the foundation of future reasoning models."
---

## Key Points

- DeepSeek R1: 4-phase pipeline (cold start, GRPO RL, rejection sampling, diverse RL) on 671B MoE architecture.
- OpenAI o3: dense transformer with scaled RL, deliberative alignment, and test-time search (beam search / MCTS).
- o3 outperforms R1 across all major benchmarks (AIME: 96.7% vs 79.8%, SWE-bench: 71.7% vs 49%).
- Training costs: o3 used 1.2M A100 GPU hours; R1 used 2.66M H800 GPU hours.
- Key architectural split: o3 uses hidden CoT; R1 uses visible/explicit CoT.

## Detailed Summary

This article provides the most detailed publicly available comparison of the two leading [[concepts/reasoning-models|reasoning models]]. The key insight is that while both use reinforcement learning as their core training methodology, they differ significantly in architecture and approach:

**DeepSeek R1** uses a Mixture-of-Experts architecture where only relevant expert sub-networks activate per input. Its training pipeline starts with supervised fine-tuning on just ~1,000 reasoning samples, then progresses through Group Relative Policy Optimization (GRPO) with rule-based rewards, rejection sampling to generate 600K filtered examples, and finally diverse RL combining rule-based and LLM-based rewards.

**OpenAI o3** uses a dense transformer (all parameters active). Its training emphasizes scaled RL where hundreds/thousands of candidate reasoning paths are generated and screened by an evaluator model. At inference time, o3 employs beam search or Monte Carlo Tree Search to select among multiple candidate chains-of-thought.

The computational costs are staggering: o3's CoT generation adds 3-5x token overhead, and training required over a million A100 GPU hours. Despite R1 being cheaper to serve (due to MoE efficiency), o3 achieves superior benchmark performance across the board.

## Related Concepts

- [[concepts/reasoning-models]] -- the models analyzed
- [[concepts/test-time-compute]] -- how inference-time computation drives performance
- [[concepts/process-reward-models]] -- used in o3's test-time search
- [[concepts/reinforcement-learning-for-reasoning]] -- the central training methodology
