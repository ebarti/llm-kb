---
title: "OpenAI o3 vs DeepSeek R1 vs Claude Extended Thinking"
type: comparison
subjects: ["[[entities/openai]]", "[[entities/deepseek]]", "[[entities/claude]]"]
sources: ["[[sources/adaline-inside-reasoning-models]]", "[[sources/anthropic-extended-thinking]]", "[[sources/li-system1-system2-reasoning-survey]]"]
last_compiled: 2026-04-05
summary: "Head-to-head comparison of the three leading reasoning model approaches: o3 (dense transformer, hidden CoT, MCTS), R1 (MoE, visible CoT, GRPO), and Claude 3.7 (hybrid toggle, visible thinking, logarithmic budget scaling)."
---

## Overview

As of early 2025, three distinct approaches to [[concepts/reasoning-models|reasoning models]] have emerged from [[entities/openai|OpenAI]], [[entities/deepseek|DeepSeek]], and [[entities/anthropic|Anthropic]]. While all use [[concepts/reinforcement-learning-for-reasoning|reinforcement learning]] and [[concepts/test-time-compute|test-time compute]], they differ significantly in architecture, training, transparency, and design philosophy.

## Comparison Table

| Dimension | OpenAI o3 | DeepSeek R1 | Claude 3.7 (Extended Thinking) |
|-----------|-----------|-------------|-------------------------------|
| **Architecture** | Dense transformer | Mixture-of-Experts (671B) | Transformer (details undisclosed) |
| **CoT visibility** | Hidden | Visible (explicit) | Visible (raw thinking) |
| **Reasoning mode** | Always-on | Separate model | Toggle on/off |
| **Training method** | Scaled RL + deliberative alignment | 4-phase (SFT + GRPO + rejection + diverse RL) | Undisclosed |
| **Test-time search** | Beam search / MCTS | Standard generation | Serial test-time compute |
| **Thinking budget** | Fixed (low/medium/high modes) | N/A | Configurable (developer-set) |
| **Training cost** | 1.2M A100 GPU hours | 2.66M H800 GPU hours | Undisclosed |
| **Token overhead** | 3-5x | Variable | Self-regulated (often stops early) |
| **Open source** | No | Yes (weights available) | No |
| **Economy variant** | o3-mini (15x cheaper) | R1-Distill-32B | Standard mode (no thinking) |

## Benchmark Performance

| Benchmark | OpenAI o3 | DeepSeek R1 | Claude 3.7 |
|-----------|-----------|-------------|------------|
| AIME 2024 | **96.7%** | 79.8% | Scales with budget |
| MATH-500 | >97% | **97.3%** | -- |
| SWE-bench Verified | **71.7%** | ~49% | -- |
| GPQA Diamond | **~87.7%** | ~75% | 84.8% (96.5% physics) |
| Codeforces ELO | **~2727** | ~2000 | -- |

## Design Philosophy Differences

### OpenAI o3: Maximum Performance, Hidden Process
- Optimizes for raw benchmark scores.
- Hidden chain-of-thought -- users see only the final answer.
- Most expensive inference (MCTS over many candidates).
- Deliberative alignment: safety checking within the hidden reasoning chain.

### DeepSeek R1: Efficient, Transparent, Open
- MoE architecture for efficiency (only relevant experts activate).
- Visible, explicit chain-of-thought -- users can inspect reasoning.
- Open-source weights enable community research and deployment.
- R1-Zero proved that pure RL can produce emergent reasoning.

### Claude 3.7: Hybrid, Flexible, Pragmatic
- Same model toggles between fast (System 1) and deliberate (System 2) modes.
- Configurable thinking budget lets developers balance cost vs. quality.
- Visible thinking with self-regulation (stops when further thought won't help).
- Logarithmic scaling: transparent compute-quality tradeoff curve.

## When to Use Each

| Use Case | Best Choice | Why |
|----------|------------|-----|
| Maximum math/coding performance | o3 | Highest benchmark scores |
| Cost-sensitive deployment | R1 (MoE efficiency) or Claude standard mode | Lower inference costs |
| Transparent reasoning needed | R1 or Claude | Visible chain-of-thought |
| Variable difficulty queries | Claude 3.7 | Toggle thinking on/off per query |
| Self-hosted / open-source | R1 | Open weights |
| Safety-critical applications | o3 (deliberative alignment) or Claude | Built-in safety reasoning |
| Research / interpretability | R1 or Claude | Visible reasoning for analysis |

## Sources

- [[sources/adaline-inside-reasoning-models]] -- detailed o3 vs. R1 technical comparison
- [[sources/anthropic-extended-thinking]] -- Claude's extended thinking approach
- [[sources/li-system1-system2-reasoning-survey]] -- all three in the System 2 taxonomy
