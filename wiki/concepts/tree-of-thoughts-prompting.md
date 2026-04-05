---
title: "Tree of Thoughts Prompting"
type: concept
sources: ["[[sources/promptingguide-tree-of-thoughts]]"]
related: ["[[concepts/prompt-engineering]]", "[[concepts/chain-of-thought-prompting]]", "[[concepts/self-consistency-prompting]]"]
last_compiled: 2026-04-05
summary: "Yao et al. (2023) framework that generalizes CoT into a tree-structured exploration of reasoning paths with search algorithms (BFS/DFS), enabling deliberate problem-solving with lookahead and backtracking."
---

## Overview

Tree of Thoughts (ToT) is a framework that extends [[concepts/chain-of-thought-prompting]] from a single linear reasoning path to a branching tree of candidate solutions. Proposed by Yao et al. (2023) and published at NeurIPS 2023, ToT enables LLMs to perform deliberate problem-solving by generating multiple reasoning branches, evaluating them, and using search algorithms to systematically explore the solution space.

Where CoT follows a single path forward and [[concepts/self-consistency-prompting]] samples multiple independent paths, ToT maintains a structured tree that allows lookahead and backtracking — the model can abandon unpromising paths and explore alternatives.

## How It Works

ToT operates through three integrated components:

**1. Thought Generation (Propose Prompts)**
The LLM generates multiple candidate "thoughts" — coherent language sequences representing intermediate reasoning steps. For a math problem, these might be candidate equations; for writing, they might be paragraph plans.

**2. Thought Evaluation (Value Prompts)**
The LLM evaluates each generated thought:
- **Independent evaluation**: Each thought rated as sure/likely/impossible
- **Voting**: When direct evaluation is hard (e.g., creative writing), the model compares and votes across candidates

**3. Search Algorithm**
Standard search algorithms navigate the thought tree:
- **Breadth-first search (BFS)**: Explore all candidates at each level before going deeper
- **Depth-first search (DFS)**: Follow promising paths deeply, backtrack on failure
- **Beam search**: Keep top-k candidates at each level

## Performance Results

| Task | CoT Performance | ToT Performance | Improvement |
|------|----------------|-----------------|-------------|
| Game of 24 | ~4% solve rate | ~74% (b=5) | +25% over CoT |
| Crossword puzzles | 1% game wins | 20% game wins | 20x improvement |

## Variations

- **Yao et al. (2023)**: Generic BFS/DFS/beam search
- **Long (2023)**: RL-trained "ToT Controller" for adaptive backtracking
- **Hulbert (2023)**: Simplified single-prompt technique with multiple expert perspectives

## Limitations

ToT is resource-intensive: each thought requires LLM generation and evaluation, and search multiplies the number of calls. It is best reserved for tasks requiring genuine planning and deliberation (puzzles, strategic decisions, complex code generation) rather than routine NLP tasks.

## Sources
- [[sources/promptingguide-tree-of-thoughts]] — Primary overview with performance data

## Related Concepts
- [[concepts/chain-of-thought-prompting]] — the simpler single-path predecessor
- [[concepts/self-consistency-prompting]] — another multi-path approach (without tree structure)
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/multi-agent-systems]] — ToT's search can be viewed as agent coordination
