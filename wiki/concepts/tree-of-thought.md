---
title: "Tree of Thoughts"
type: concept
sources: ["[[sources/yao-tree-of-thoughts]]", "[[sources/li-system1-system2-reasoning-survey]]"]
related: ["[[concepts/chain-of-thought]]", "[[concepts/llm-reasoning]]", "[[concepts/test-time-compute]]", "[[concepts/system-1-system-2-thinking]]"]
last_compiled: 2026-04-05
summary: "A reasoning framework (NeurIPS 2023) that generalizes chain-of-thought by exploring multiple reasoning paths via tree search (BFS/DFS), enabling backtracking and self-evaluation -- achieving 74% on Game of 24 vs. CoT's 4%."
---

## Overview

Tree of Thoughts (ToT) is a framework for LLM reasoning introduced by Yao et al. (NeurIPS 2023) that addresses a fundamental limitation of [[concepts/chain-of-thought|chain-of-thought]] prompting: its inability to explore alternative reasoning paths. While CoT generates a single linear chain of reasoning, ToT organizes reasoning into a tree structure where the model can generate multiple candidate "thoughts" at each step, evaluate them, and use search algorithms to find the best solution path.

## How It Works

ToT has four key components:

### 1. Thought Decomposition
Problems are decomposed into intermediate "thoughts" -- coherent units of text (a sentence, a paragraph, a calculation step) that serve as nodes in the reasoning tree. The granularity is task-dependent.

### 2. Thought Generation
At each node, the LM generates multiple candidate next thoughts. This creates branches in the tree, enabling exploration of diverse reasoning strategies.

### 3. Thought Evaluation
The LM evaluates the promise of each candidate thought -- either by scoring it directly or by voting among alternatives. This self-evaluation enables pruning without external verifiers (though [[concepts/process-reward-models|process reward models]] can replace or supplement self-evaluation).

### 4. Search Algorithm
Classical search algorithms navigate the tree:
- **Breadth-First Search (BFS)**: Explore all candidates at each level before going deeper. Better for tasks where initial decisions are reversible.
- **Depth-First Search (DFS)**: Follow the most promising path deeply, backtracking on failure. Better for tasks with clear dead ends.

## Key Results

| Task | CoT (GPT-4) | ToT (GPT-4) | Improvement |
|------|-------------|-------------|-------------|
| Game of 24 | 4% | 74% | 18.5x |
| Creative Writing | baseline | improved | qualitative |
| Mini Crosswords | baseline | significantly improved | large |

The Game of 24 result is particularly striking because the task requires combining four numbers using arithmetic to make 24 -- a problem demanding planning and exploration that linear CoT cannot handle.

## Theoretical Foundations

ToT is explicitly inspired by:
- **Newell & Simon (1972)**: Problem-solving as search through a combinatorial space.
- **Kahneman's System 2**: Deliberate, effortful reasoning (see [[concepts/system-1-system-2-thinking]]).
- **Classical AI search**: BFS, DFS, and heuristic search applied to natural language reasoning.

This bridges the gap between neural language models and symbolic AI approaches to problem-solving.

## Relationship to Later Work

ToT was a precursor to several developments:
- **[[concepts/test-time-compute|Test-time compute scaling]]**: ToT demonstrated that spending more compute at inference (via search) improves reasoning.
- **[[concepts/reasoning-models|Reasoning models]]**: o3's test-time search (beam search, MCTS) is a descendant of ToT's approach.
- **[[concepts/process-reward-models|Process reward models]]**: Replaced ToT's LM self-evaluation with trained verifiers for more reliable path selection.

## Limitations

- **Compute cost**: Multiple generation + evaluation calls per node make ToT expensive.
- **LM-as-evaluator**: Self-evaluation quality is bounded by the model's own reasoning ability.
- **Task specificity**: The optimal thought granularity and search algorithm vary by task.

## Sources

- [[sources/yao-tree-of-thoughts]] -- the original NeurIPS 2023 paper
- [[sources/li-system1-system2-reasoning-survey]] -- ToT in the System 2 reasoning taxonomy

## Related Concepts

- [[concepts/chain-of-thought]] -- the single-path predecessor
- [[concepts/test-time-compute]] -- the broader paradigm ToT exemplifies
- [[concepts/process-reward-models]] -- learned verifiers that improve on self-evaluation
- [[concepts/system-1-system-2-thinking]] -- ToT as deliberate System 2 reasoning
- [[concepts/llm-reasoning]] -- the broader field
