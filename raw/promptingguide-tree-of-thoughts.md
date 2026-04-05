---
title: "Tree of Thoughts Prompting"
source: "https://www.promptingguide.ai/techniques/tot"
author: "DAIR.AI / Prompt Engineering Guide"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [prompt-engineering, tree-of-thoughts, reasoning, search-algorithms]
type: article
status: raw
discovered_via: search
---

# Tree of Thoughts (ToT): Comprehensive Overview

## Definition
Tree-of-Thoughts (ToT) is a framework that generalizes over chain-of-thought prompting and encourages exploration over thoughts that serve as intermediate steps for general problem solving with language models. Proposed by Yao et al. (2023) and Long (2023).

## How It Works
ToT maintains a tree of thoughts, where thoughts represent coherent language sequences that serve as intermediate steps toward solving a problem. ToT allows LMs to perform deliberate decision making by considering multiple different reasoning paths and self-evaluating choices to decide the next course of action, as well as looking ahead or backtracking when necessary to make global choices.

The LM's ability to generate and evaluate thoughts is then combined with search algorithms (e.g., breadth-first search and depth-first search) to enable systematic exploration of thoughts with lookahead and backtracking.

## Key Components

Two key components:
- Propose prompts: generate possible solutions
- Value prompts: evaluate and guide the model toward the best path

Evaluation methods:
- Independent Evaluation: The LLM assesses each idea independently, assigning a value or classification (sure/likely/impossible)
- Voting Across Ideas: When direct evaluation is challenging (like in writing tasks), the model compares solutions and votes for the most promising one

## Search Algorithms Used
- Breadth-first search (BFS)
- Depth-first search (DFS)
- Beam search

## Performance Results
- In the "Game of 24" task: ToT with b=5 beats CoT by 25%
- In crossword puzzles: ToT significantly outperforms IO and CoT in word level success rate and wins 20% of games compared to 1% for CoT
- NeurIPS 2023 paper

## Variations
- Yao et al. (2023): Generic search strategies (DFS/BFS/beam)
- Long (2023): Reinforcement learning-trained "ToT Controller" for adaptive backtracking
- Tree-of-Thought Prompting (Hulbert, 2023): Simpler single-prompt technique where multiple expert perspectives evaluate intermediate thoughts sequentially

## Limitations
- Resource intensive (cost, number of requests)
- May not be efficient for common NLP tasks that are too easy for models like GPT-4
- Best suited for tasks requiring planning and deliberate decision-making
