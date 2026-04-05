---
title: "Source: Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
type: source-summary
source: "[[raw/yao-tree-of-thoughts]]"
related: ["[[concepts/tree-of-thought]]", "[[concepts/chain-of-thought]]", "[[concepts/llm-reasoning]]", "[[concepts/test-time-compute]]"]
last_compiled: 2026-04-05
summary: "NeurIPS 2023 paper introducing Tree of Thoughts (ToT), a framework that generalizes CoT by exploring multiple reasoning paths with search algorithms, achieving 74% on Game of 24 vs. CoT's 4%."
---

## Key Points

- ToT enables LLMs to explore multiple reasoning paths, self-evaluate, backtrack, and look ahead -- unlike CoT's single linear chain.
- Combines LM-generated "thoughts" (coherent text units) with search algorithms (BFS, DFS).
- Game of 24: GPT-4 + CoT solved 4%; GPT-4 + ToT solved 74%.
- Inspired by Newell & Simon's (1972) problem-solving theory -- viewing reasoning as search through a combinatorial space.

## Detailed Summary

Yao et al. (2023) identified a fundamental limitation of [[concepts/chain-of-thought|chain-of-thought]] prompting: its left-to-right, single-path generation cannot handle tasks requiring planning, exploration, or backtracking. ToT addresses this by allowing the LM to generate multiple candidate "thoughts" at each step, evaluate them, and use classical search algorithms to navigate the solution space.

The LM serves dual roles: (1) generating candidate next steps and (2) evaluating their promise. This self-evaluation enables pruning of unpromising branches without external verifiers. Search can proceed via breadth-first (explore many options at each level) or depth-first (follow promising paths deeply, backtracking on failure).

The results on Game of 24 are the paper's strongest evidence: the task requires combining four numbers using arithmetic to reach 24, and the jump from 4% to 74% demonstrates that structured search over reasoning paths is qualitatively different from linear chain-of-thought.

## Related Concepts

- [[concepts/tree-of-thought]] -- the framework introduced
- [[concepts/chain-of-thought]] -- the predecessor technique ToT generalizes
- [[concepts/test-time-compute]] -- ToT is an early form of scaling inference-time computation
- [[concepts/system-1-system-2-thinking]] -- ToT maps to System 2 deliberate reasoning
- [[concepts/process-reward-models]] -- later work uses learned verifiers instead of LM self-evaluation
