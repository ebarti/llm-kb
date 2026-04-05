---
title: "CoT vs Tree of Thoughts vs Self-Consistency"
type: comparison
subjects: ["[[concepts/chain-of-thought-prompting]]", "[[concepts/tree-of-thoughts-prompting]]", "[[concepts/self-consistency-prompting]]"]
sources: ["[[sources/promptingguide-chain-of-thought]]", "[[sources/promptingguide-tree-of-thoughts]]", "[[sources/promptingguide-self-consistency]]"]
last_compiled: 2026-04-05
summary: "Three reasoning techniques compared: CoT (single path, cheap), Self-Consistency (multiple independent paths + voting, moderate cost), and ToT (structured tree search with backtracking, expensive) — each suited to different complexity/budget trade-offs."
---

## Overview

These three techniques form a progression of increasingly powerful (and expensive) approaches to improving LLM reasoning. All share the core insight that making reasoning explicit improves accuracy, but they differ in how many reasoning paths are explored and how the final answer is selected.

## Comparison Table

| Dimension | Chain-of-Thought | Self-Consistency | Tree of Thoughts |
|-----------|-----------------|------------------|-----------------|
| **Paper** | Wei et al. (2022) | Wang et al. (2022) | Yao et al. (2023) |
| **Core idea** | Single reasoning path | Multiple independent paths + voting | Branching tree with search |
| **Path structure** | Linear | Multiple linear (independent) | Tree (branching, backtracking) |
| **Answer selection** | First (greedy) | Majority vote | Best via evaluation |
| **Search algorithm** | None | Random sampling | BFS/DFS/beam search |
| **LLM calls** | 1 | 5-40 | Many (generation + evaluation per node) |
| **Cost** | Low (1x) | Moderate (5-40x) | High (many multiples) |
| **Best for** | General reasoning | High-stakes accuracy | Planning, puzzles, strategy |
| **Game of 24** | ~4% | Better than CoT | ~74% (b=5) |
| **Zero-shot variant** | "Let's think step by step" | No | No |
| **Backtracking** | No | No | Yes |

## When to Use Each

### Chain-of-Thought
- **Default choice** for any reasoning task
- Low cost, simple to implement
- Try zero-shot CoT first ("Let's think step by step")
- Sufficient for most practical applications

### Self-Consistency
- When **correctness matters more than cost** (medical, financial, legal)
- Tasks with clear right/wrong answers (arithmetic, classification)
- 5-10 samples often sufficient; diminishing returns beyond 40
- Easy to implement: just sample multiple times and count

### Tree of Thoughts
- **Complex planning and strategic tasks** (game-playing, puzzles, code architecture)
- When backtracking is essential (exploring dead ends)
- Budget allows for many LLM calls
- NOT needed for routine NLP tasks — overkill for classification, summarization, etc.

## Progressive Upgrade Path

```
Zero-Shot → Zero-Shot CoT → Few-Shot CoT → Self-Consistency → Tree of Thoughts
(simplest)                                                      (most powerful)
```

Start simple, upgrade only when the simpler technique fails. This matches the practical recommendation across all sources: try zero-shot first, add complexity only as needed.

## Relationship to Reasoning Models

These three techniques represent the early (2022-2023) landscape of [[concepts/test-time-compute|test-time compute scaling]]. Modern [[concepts/reasoning-models|reasoning models]] (o1, o3, R1) have internalized aspects of all three through RL training: they generate extended reasoning chains (like CoT), can self-correct (like backtracking in ToT), and use [[concepts/process-reward-models|process reward models]] for verification (similar to ToT's self-evaluation but with trained verifiers).

## Sources
- [[sources/promptingguide-chain-of-thought]] — CoT fundamentals
- [[sources/promptingguide-tree-of-thoughts]] — ToT performance data
- [[sources/promptingguide-self-consistency]] — Self-consistency mechanism
- [[sources/wei-chain-of-thought-prompting]] — Original CoT paper
- [[sources/yao-tree-of-thoughts]] — Original ToT paper
- [[sources/raschka-state-of-reasoning-inference]] — Landscape comparison of techniques
