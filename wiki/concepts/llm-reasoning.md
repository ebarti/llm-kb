---
title: "LLM Reasoning"
type: concept
sources: ["[[sources/wei-chain-of-thought-prompting]]", "[[sources/yao-tree-of-thoughts]]", "[[sources/mirzadeh-gsm-symbolic]]", "[[sources/song-llm-reasoning-failures-survey]]", "[[sources/li-system1-system2-reasoning-survey]]", "[[sources/raschka-state-of-reasoning-inference]]"]
related: ["[[concepts/chain-of-thought]]", "[[concepts/tree-of-thought]]", "[[concepts/reasoning-models]]", "[[concepts/test-time-compute]]", "[[concepts/llm-reasoning-limitations]]", "[[concepts/emergent-abilities]]"]
last_compiled: 2026-04-05
summary: "The ability of large language models to perform multi-step inference, logical deduction, and problem-solving -- achieved through prompting techniques (CoT, ToT), training methods (RL), and inference-time scaling, though the nature and limits of this reasoning remain deeply debated."
---

## Overview

LLM reasoning refers to the capacity of large language models to solve problems requiring multi-step inference, logical deduction, mathematical computation, or strategic planning. It is one of the most consequential and debated topics in AI research: the extent to which LLMs genuinely "reason" versus perform sophisticated pattern matching determines whether they can be trusted for high-stakes decision-making.

The field has evolved rapidly from simple prompting tricks (2022) to dedicated [[concepts/reasoning-models|reasoning models]] trained via reinforcement learning (2024-2025), representing one of the fastest-moving areas in AI research.

## The Reasoning Landscape

### Prompting-Based Approaches (No Weight Changes)

1. **[[concepts/chain-of-thought|Chain-of-Thought (CoT)]]** (Wei et al., 2022): Add step-by-step reasoning exemplars to prompts. The foundational technique that unlocked reasoning in LLMs.

2. **[[concepts/tree-of-thought|Tree of Thoughts (ToT)]]** (Yao et al., 2023): Generalize CoT to explore multiple reasoning paths with search algorithms (BFS/DFS). Enables backtracking and lookahead.

3. **[[concepts/self-consistency|Self-Consistency]]** (Wang et al., 2023): Generate multiple CoT solutions and take the majority vote. Simple but effective.

### Training-Based Approaches (Weight Changes)

4. **Supervised fine-tuning on reasoning traces**: Train on examples of step-by-step solutions.

5. **[[concepts/reinforcement-learning-for-reasoning|Reinforcement learning]]**: Train models to develop reasoning through RL with verifiable rewards. The approach behind [[concepts/reasoning-models|o1, o3, R1]].

6. **Distillation**: Transfer reasoning capabilities from large models to smaller ones via training on the larger model's reasoning traces.

### Inference-Time Approaches

7. **[[concepts/test-time-compute|Test-time compute scaling]]**: Allocate more computation at inference -- generate multiple candidates, use verifiers, employ search algorithms.

8. **[[concepts/process-reward-models|Process Reward Models]]**: Trained verifiers that evaluate each reasoning step, enabling selection of the best reasoning path.

## Key Benchmarks

| Benchmark | Domain | Notable Results |
|-----------|--------|-----------------|
| GSM8K | Grade school math | CoT + PaLM 540B achieved SOTA (2022) |
| MATH | Competition math | PRM achieved 78% (2023); o3 >97% (2025) |
| AIME | Math olympiad | o3: 96.7%, R1: 79.8% |
| GPQA | PhD-level science | Claude 3.7: 84.8% (96.5% physics) |
| Game of 24 | Arithmetic planning | CoT: 4%, ToT: 74% |
| ARC-AGI | Abstract reasoning | o3 made significant progress (2024) |

## The Central Debate

The nature of LLM reasoning is fiercely debated. Evidence exists on both sides:

**Evidence for genuine reasoning:**
- Performance on novel problems not in training data
- Scaling curves showing phase transitions ([[concepts/emergent-abilities|emergence]])
- Internal representations suggesting world models (Othello-GPT)
- Ability to combine skills in novel ways (SkillMix test)

**Evidence for sophisticated pattern matching:**
- Fragility to irrelevant information (up to 65% drops -- [[sources/mirzadeh-gsm-symbolic|GSM-Symbolic]])
- Sensitivity to numerical variations in identical problem structures
- Systematic failures on compositional and disjunctive reasoning
- Architecture optimized for next-token prediction, not constraint satisfaction

See [[concepts/stochastic-parrot-debate]] for the full debate and [[concepts/llm-reasoning-limitations]] for a detailed catalogue of failure modes.

## The System 1 / System 2 Framework

The most productive framework for understanding LLM reasoning maps to Kahneman's dual-process theory (see [[concepts/system-1-system-2-thinking]]):

- **System 1**: Standard LLM inference -- fast, intuitive, pattern-based. Good for routine tasks.
- **System 2**: Reasoning models with extended thinking -- slow, deliberate, step-by-step. Better for complex, multi-step problems.

The evolution from System 1 to System 2 has proceeded through four stages: pre-trained LLMs, CoT prompting, fine-tuned reasoners, and RL-trained reasoning models.

## Sources

- [[sources/wei-chain-of-thought-prompting]] -- foundational CoT paper
- [[sources/yao-tree-of-thoughts]] -- tree-structured reasoning exploration
- [[sources/mirzadeh-gsm-symbolic]] -- evidence for fragility of mathematical reasoning
- [[sources/song-llm-reasoning-failures-survey]] -- comprehensive failure taxonomy
- [[sources/li-system1-system2-reasoning-survey]] -- dual-process theory applied to LLMs
- [[sources/raschka-state-of-reasoning-inference]] -- practical survey of inference-time techniques

## Related Concepts

- [[concepts/chain-of-thought]] -- the foundational prompting technique
- [[concepts/reasoning-models]] -- dedicated models trained for reasoning
- [[concepts/test-time-compute]] -- the computational mechanism behind reasoning improvements
- [[concepts/llm-reasoning-limitations]] -- systematic catalogue of what goes wrong
- [[concepts/emergent-abilities]] -- reasoning as an emergent capability
- [[concepts/stochastic-parrot-debate]] -- the philosophical debate about whether LLMs truly reason
