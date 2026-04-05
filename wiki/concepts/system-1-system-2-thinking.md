---
title: "System 1 / System 2 Thinking in LLMs"
type: concept
sources: ["[[sources/li-system1-system2-reasoning-survey]]", "[[sources/anthropic-extended-thinking]]", "[[sources/adaline-inside-reasoning-models]]"]
related: ["[[concepts/llm-reasoning]]", "[[concepts/reasoning-models]]", "[[concepts/chain-of-thought]]", "[[concepts/test-time-compute]]"]
last_compiled: 2026-04-05
summary: "Applying Kahneman's dual-process theory to LLMs: standard models as System 1 (fast, intuitive, cheap) vs. reasoning models as System 2 (slow, deliberate, expensive) -- with hybrid toggle approaches emerging as the practical optimum."
---

## Overview

Daniel Kahneman's dual-process theory distinguishes two modes of human cognition:
- **System 1**: Fast, automatic, intuitive, effortless. Pattern recognition, gut reactions.
- **System 2**: Slow, deliberate, analytical, effortful. Logical reasoning, planning, calculation.

This framework has become the dominant lens for understanding the landscape of LLM reasoning approaches, as mapped comprehensively by [[sources/li-system1-system2-reasoning-survey|Li et al. (2025)]].

## Mapping to LLMs

### System 1 LLMs
Standard large language models operate in System 1 mode:
- Input passes through transformer layers to produce output directly.
- Fast inference, low cost.
- Good for: factual recall, text generation, simple tasks, commonsense reasoning.
- Bad for: multi-step logic, mathematical proof, planning, constraint satisfaction.
- This is how GPT-4, Claude 3.5, Llama 3 operate by default.

### System 2 LLMs
[[concepts/reasoning-models|Reasoning models]] operate in System 2 mode:
- Generate intermediate reasoning steps before the final answer.
- Slower inference, higher cost.
- Good for: mathematics, competitive programming, formal logic, complex analysis.
- This is how o1, o3, R1 operate, and how Claude 3.7 operates with extended thinking.

## The Evolution (Four Stages)

1. **Pre-trained LLMs (System 1 only)**: GPT-3, BERT-era. No deliberation.
2. **CoT prompting (System 2 via prompting)**: [[concepts/chain-of-thought|Chain-of-thought]] forces step-by-step reasoning without weight changes. External scaffolding for System 2.
3. **Fine-tuned reasoners (System 2 via SFT)**: Models trained on reasoning traces. Internalized System 2 patterns.
4. **RL-trained reasoners (System 2 via RL)**: [[concepts/reasoning-models|o1, o3, R1]]. Deepest internalization through reinforcement learning. Self-verification, backtracking, and error correction emerge.

## The Hybrid Approach

The most practical approach is hybrid -- choose System 1 or System 2 based on the task:

**Claude 3.7 Sonnet** exemplifies this: the same model operates in standard (System 1) or extended thinking (System 2) mode, toggled by the user or developer. Simple factual questions get fast answers; complex math problems get deep deliberation.

This "thinking on demand" pattern is becoming industry standard, with configurable thinking budgets letting developers trade off between latency/cost and reasoning quality.

## Performance Comparison

| Task Domain | System 1 (Standard LLM) | System 2 (Reasoning Model) |
|-------------|------------------------|-----------------------------|
| Arithmetic/Math | Moderate, fragile | High, more robust |
| Competitive programming | Low-moderate | High |
| Commonsense reasoning | Good | Sometimes overkill |
| Creative writing | Good | Mixed (can overthink) |
| Simple factual Q&A | Fast, good | Unnecessarily slow |
| Complex analysis | Shallow | Deep, nuanced |

## Limitations of the Analogy

The System 1/2 mapping is useful but imperfect:
- Human System 2 reasoning can be truly novel and creative; LLM System 2 is still constrained by training distribution.
- Human System 1 is deeply embodied (sensory, emotional); LLM System 1 is purely linguistic.
- Humans flexibly switch between systems unconsciously; LLMs require explicit mode selection.

## Sources

- [[sources/li-system1-system2-reasoning-survey]] -- comprehensive dual-process framework for LLMs
- [[sources/anthropic-extended-thinking]] -- Claude's hybrid System 1/2 implementation
- [[sources/adaline-inside-reasoning-models]] -- how o3 and R1 implement System 2

## Related Concepts

- [[concepts/llm-reasoning]] -- the broader landscape
- [[concepts/reasoning-models]] -- practical System 2 implementations
- [[concepts/chain-of-thought]] -- the first bridge from System 1 to System 2
- [[concepts/test-time-compute]] -- the computational cost of System 2
