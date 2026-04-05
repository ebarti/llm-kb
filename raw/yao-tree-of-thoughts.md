---
title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
source: "https://arxiv.org/abs/2305.10601"
author: "Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan"
date_published: 2023-05-17
date_ingested: 2026-04-05
tags: [tree-of-thoughts, reasoning, search, problem-solving, NeurIPS]
type: paper
status: raw
discovered_via: search
---

# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

NeurIPS 2023

## Key Findings

- Tree of Thoughts (ToT) generalizes chain-of-thought prompting by enabling exploration over coherent units of text ("thoughts") that serve as intermediate steps toward problem solving.
- ToT allows LMs to perform deliberate decision making by considering multiple different reasoning paths and self-evaluating choices to decide the next course of action.
- Unlike CoT's linear chain, ToT enables backtracking and lookahead -- the model can abandon unpromising paths and explore alternatives.

## Methodology

- Framework combines language-based capability to generate and evaluate diverse thoughts with search algorithms:
  - **Breadth-first search (BFS)**: Explore multiple branches at each level before going deeper.
  - **Depth-first search (DFS)**: Follow promising paths deeply before backtracking.
- The LM serves dual roles: generating candidate thoughts AND evaluating their promise.
- Thoughts are coherent language sequences (a sentence, a paragraph, a code block) rather than individual tokens.

## Results

| Task | CoT (GPT-4) | ToT (GPT-4) |
|------|-------------|-------------|
| Game of 24 | 4% | 74% |
| Creative Writing | baseline | improved coherence |
| Mini Crosswords | baseline | significantly improved |

- The Game of 24 result is the most dramatic: from 4% to 74% success rate, demonstrating that structured search over reasoning paths massively outperforms linear chain-of-thought on tasks requiring planning.

## Connection to Dual-Process Theory

ToT is explicitly inspired by research on human problem-solving (Newell & Simon, 1972), which views problem-solving as search through a combinatorial space. This connects to the System 2 (deliberate, effortful) mode of thinking from Kahneman's dual-process theory.

## Significance

ToT showed that the key limitation of CoT was its single-path, left-to-right generation. By introducing structured exploration, LLMs could tackle problems requiring genuine planning and search -- capabilities previously thought to require specialized symbolic AI systems.
