---
title: "Source: Tree of Thoughts Prompting (Prompt Engineering Guide)"
type: source-summary
source: "[[raw/promptingguide-tree-of-thoughts]]"
related: ["[[concepts/tree-of-thoughts-prompting]]", "[[concepts/chain-of-thought-prompting]]", "[[concepts/prompt-engineering]]"]
last_compiled: 2026-04-05
summary: "DAIR.AI overview of ToT: Yao et al. (2023) framework generalizing CoT into tree-structured exploration with BFS/DFS search, achieving 25% gains over CoT on Game of 24."
reading_time: "1 min"
---

## Key Points
- ToT maintains a tree of thoughts as intermediate steps toward solving a problem
- Combines thought generation and self-evaluation with search algorithms (BFS, DFS, beam search)
- Two key components: propose prompts (generate solutions) and value prompts (evaluate paths)
- Beats CoT by 25% on Game of 24 and wins 20% of crossword games vs 1% for CoT
- Resource intensive — best suited for tasks requiring planning and deliberate decision-making

## Detailed Summary
Tree of Thoughts extends [[concepts/chain-of-thought-prompting]] from a linear reasoning chain to a branching exploration tree. The LLM generates multiple candidate thoughts, evaluates them (sure/likely/impossible), and uses search algorithms to systematically explore the solution space with lookahead and backtracking. This enables deliberate problem-solving that single-pass prompting cannot achieve.

Variations include Yao et al.'s generic search strategies, Long's RL-trained ToT Controller, and Hulbert's simpler single-prompt technique using multiple expert perspectives.

## Related Concepts
- [[concepts/tree-of-thoughts-prompting]] — the core technique
- [[concepts/chain-of-thought-prompting]] — the simpler predecessor
- [[concepts/self-consistency-prompting]] — another multi-path approach
- [[concepts/prompt-engineering]] — parent domain
