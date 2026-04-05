---
title: "Mathematical Reasoning in LLMs"
type: concept
sources: ["[[sources/mirzadeh-gsm-symbolic]]", "[[sources/lightman-lets-verify-step-by-step]]", "[[sources/adaline-inside-reasoning-models]]"]
related: ["[[concepts/llm-reasoning]]", "[[concepts/llm-reasoning-limitations]]", "[[concepts/chain-of-thought]]", "[[concepts/process-reward-models]]", "[[concepts/reasoning-models]]"]
last_compiled: 2026-04-05
summary: "The capacity of LLMs to solve mathematical problems -- from grade school (GSM8K) to competition level (AIME) -- with reasoning models achieving 96.7% on AIME, yet fundamental fragility persists: performance drops up to 65% with irrelevant information."
---

## Overview

Mathematical reasoning is the most extensively benchmarked domain of [[concepts/llm-reasoning|LLM reasoning]] and has been the primary proving ground for reasoning techniques from [[concepts/chain-of-thought|chain-of-thought prompting]] to [[concepts/reasoning-models|reasoning models]]. It provides clean, verifiable ground truth and allows precise measurement of reasoning quality.

## Benchmark Landscape

| Benchmark | Level | Best Performance (2025) | Model |
|-----------|-------|------------------------|-------|
| GSM8K | Grade school | >95% | Multiple models |
| MATH | Competition math | >97% | o3, R1 |
| AIME | Math olympiad | 96.7% | o3 |
| MATH-500 | Competition subset | 97.3% | R1 |
| GSM-Symbolic | Grade school (rigorous) | Variable (fragile) | All models |

## The Progress Narrative

1. **2022**: CoT prompting + PaLM 540B achieves SOTA on GSM8K (Wei et al.).
2. **2023**: Process supervision (PRMs) achieves 78% on MATH (Lightman et al.).
3. **2024**: Reasoning models push toward near-perfect on competition math. o1 shows major gains.
4. **2025**: o3 achieves 96.7% on AIME. R1 achieves 97.3% on MATH-500.

## The Fragility Counter-Narrative

Alongside impressive benchmark numbers, [[sources/mirzadeh-gsm-symbolic|GSM-Symbolic]] reveals fundamental fragility:

- **Numerical variation**: Changing numbers in structurally identical problems causes significant accuracy variance. A true reasoner would be invariant.
- **Distractor susceptibility**: Adding one irrelevant sentence drops performance up to 65%. Models incorporate irrelevant information rather than ignoring it.
- **Complexity degradation**: Performance drops sharply with more reasoning steps.
- **Probability dependence**: Accuracy correlates with answer probability, suggesting pattern matching.

The gap between benchmark scores and robustness suggests that high accuracy on standard benchmarks may overstate genuine mathematical reasoning capability.

## Why Math Is Hard for LLMs

1. **Exact computation**: Math requires precise calculation; approximate pattern matching fails on exact answers.
2. **Multi-step dependencies**: Each step depends on previous steps being exactly correct.
3. **Out-of-distribution generalization**: Novel problem structures require genuine understanding, not template matching.
4. **Verification is different from generation**: Models can sometimes solve problems they cannot verify, and vice versa.

## Code Integration Insight

Training on code improves mathematical reasoning: models with code pre-training showed up to 8.8% improvement on natural language reasoning tasks. This suggests that code's structured, logical nature transfers to mathematical reasoning capabilities.

## Sources

- [[sources/mirzadeh-gsm-symbolic]] -- evidence for fragility in mathematical reasoning
- [[sources/lightman-lets-verify-step-by-step]] -- process supervision for math solving
- [[sources/adaline-inside-reasoning-models]] -- benchmark performance of reasoning models

## Related Concepts

- [[concepts/llm-reasoning]] -- mathematical reasoning as a key subdomain
- [[concepts/llm-reasoning-limitations]] -- mathematical fragility as a specific case
- [[concepts/process-reward-models]] -- step-level verification improves math solving
- [[concepts/reasoning-models]] -- models achieving near-perfect math benchmark scores
