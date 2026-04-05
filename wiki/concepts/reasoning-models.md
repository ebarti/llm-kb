---
title: "Reasoning Models"
type: concept
sources: ["[[sources/adaline-inside-reasoning-models]]", "[[sources/anthropic-extended-thinking]]", "[[sources/li-system1-system2-reasoning-survey]]", "[[sources/raschka-state-of-reasoning-inference]]"]
related: ["[[concepts/llm-reasoning]]", "[[concepts/test-time-compute]]", "[[concepts/chain-of-thought]]", "[[concepts/reinforcement-learning-for-reasoning]]", "[[concepts/process-reward-models]]"]
last_compiled: 2026-04-05
summary: "LLMs specifically trained (via RL) to perform extended deliberation before answering -- including OpenAI o1/o3, DeepSeek R1, and Claude 3.7 with extended thinking -- representing the internalization of chain-of-thought reasoning through reinforcement learning."
---

## Overview

Reasoning models (also called "thinking models" or "Large Reasoning Models") are LLMs that have been trained, primarily through reinforcement learning, to engage in extended step-by-step deliberation before producing a final answer. They represent the culmination of the trajectory from [[concepts/chain-of-thought|chain-of-thought prompting]] (reasoning via prompt engineering) to internalized reasoning (reasoning via training).

The key distinction from standard LLMs: reasoning models natively generate internal chains of thought without being prompted to do so, and they have been trained to self-verify, backtrack, and refine their reasoning.

## Major Reasoning Models

### OpenAI o1 / o3 (2024-2025)

- **Architecture**: Dense transformer (all parameters active).
- **Training**: Pre-training on CoT tuples, then scaled RL with hundreds/thousands of candidate reasoning paths evaluated by verifier models. Deliberative alignment adds safety checking within the reasoning chain.
- **Inference**: Test-time search via beam search or Monte Carlo Tree Search. Hidden chain-of-thought (not shown to users).
- **Benchmarks**: AIME 96.7%, SWE-bench 71.7%, Codeforces ELO ~2727, GPQA Diamond ~87.7%.
- **Cost**: 1.2M A100 GPU hours to train. 3-5x token overhead at inference.
- **o3-mini**: 15x cheaper and 5x faster than o1 with comparable performance.

### DeepSeek R1 (2025)

- **Architecture**: Mixture-of-Experts (671B parameters, MoE gating activates only relevant experts).
- **Training**: 4-phase pipeline:
  1. Cold start: SFT on ~1,000 reasoning samples.
  2. GRPO (Group Relative Policy Optimization): Rule-based RL with accuracy rewards.
  3. Rejection sampling: Generate 600K samples, filter, combine with 200K general examples.
  4. Diverse RL: Rule-based + LLM-based reward models.
- **Inference**: Explicit, visible chain-of-thought.
- **Benchmarks**: AIME 79.8%, MATH-500 97.3%, SWE-bench ~49%.
- **Notable**: R1-Zero showed that pure RL (no SFT) can produce emergent reasoning.

### Claude 3.7 Sonnet with Extended Thinking (2025)

- **Architecture**: Hybrid model -- same model operates as standard LLM or reasoning model.
- **Mechanism**: Configurable "thinking budget" controls serial [[concepts/test-time-compute|test-time compute]].
- **Key feature**: Toggle between System 1 (standard) and System 2 (extended thinking) modes.
- **Benchmarks**: GPQA 84.8% (96.5% physics), strong AIME scaling with token budget.
- **Transparency**: Thinking process visible to users (unlike o3's hidden CoT).
- **Insight**: Math accuracy scales logarithmically with thinking tokens; model self-regulates.

## How Reasoning Models Work

The core mechanism combines three innovations:

1. **Reinforcement learning**: Models are rewarded for correct final answers and penalized for incorrect ones, learning to develop reasoning strategies that lead to correct solutions. Unlike SFT, RL allows the model to discover novel reasoning patterns.

2. **Chain-of-thought internalization**: Rather than being prompted to reason step-by-step, reasoning models generate reasoning tokens natively. These "thinking tokens" serve as working memory.

3. **Self-verification**: Models learn to check their own work, identify errors, and revise before committing to an answer. This is the key qualitative difference from standard CoT.

## Performance Comparison

| Benchmark | GPT-4 | DeepSeek R1 | OpenAI o3 | Claude 3.7 (extended) |
|-----------|-------|-------------|-----------|----------------------|
| AIME 2024 | ~30% | 79.8% | 96.7% | scales with budget |
| MATH-500 | ~70% | 97.3% | >97% | -- |
| SWE-bench | ~35% | ~49% | 71.7% | -- |
| GPQA | ~55% | ~75% | ~87.7% | 84.8% |

## Limitations

- **Compute overhead**: 3-5x more tokens generated, significant latency increase.
- **Overkill on simple tasks**: Reasoning models apply full deliberation even to trivial questions.
- **Safety-performance tradeoff**: Safety alignment training can degrade reasoning accuracy (R1: -12% on Chinese SimpleQA after safety RL).
- **Multi-turn fragmentation**: Extended conversations can fragment reasoning coherence.
- **Still not true reasoning**: Even reasoning models show fragility on adversarial benchmarks like [[sources/mirzadeh-gsm-symbolic|GSM-Symbolic]].

## The RL Foundation

Reinforcement learning is central to reasoning model training. The parallel to AlphaGo is instructive: just as RL enabled Go play beyond human capability, RL enables reasoning beyond what supervised learning on human examples can achieve. DeepSeek R1-Zero's pure RL result (no supervised data at all) is particularly striking -- it suggests reasoning can emerge purely from optimization pressure.

## Sources

- [[sources/adaline-inside-reasoning-models]] -- detailed technical comparison of o3 and R1
- [[sources/anthropic-extended-thinking]] -- Claude's hybrid approach
- [[sources/li-system1-system2-reasoning-survey]] -- reasoning models as System 2
- [[sources/raschka-state-of-reasoning-inference]] -- practical landscape of inference techniques

## Related Concepts

- [[concepts/llm-reasoning]] -- the broader capability
- [[concepts/test-time-compute]] -- the computational paradigm
- [[concepts/chain-of-thought]] -- the prompting technique reasoning models internalize
- [[concepts/reinforcement-learning-for-reasoning]] -- the training methodology
- [[concepts/process-reward-models]] -- step-level verification used in training and inference
- [[concepts/system-1-system-2-thinking]] -- reasoning models as System 2
