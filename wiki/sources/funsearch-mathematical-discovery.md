---
title: "Source: FunSearch — Mathematical Discoveries Using LLMs"
type: source-summary
source: "[[raw/funsearch-deepmind-mathematical-discovery]]"
related: ["[[concepts/ai-mathematical-reasoning]]", "[[concepts/ai-for-scientific-discovery]]", "[[entities/funsearch]]", "[[entities/google-deepmind]]"]
tags: [funsearch, mathematics, ai-discovery, llm]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's FunSearch pairs PaLM 2 with an automated evaluator in an evolutionary loop to generate interpretable code solutions — cracking the cap set problem (largest advance in 20 years) and outperforming human heuristics on bin packing."
---

## Key Points

- FunSearch pairs an LLM (PaLM 2) with an automated evaluator in an evolutionary loop.
- First time an LLM was used to discover a solution to a long-standing mathematical puzzle (cap set problem).
- Achieved the largest increase in cap set sizes in the past 20 years.
- Key innovation: outputs readable code explaining how solutions work, not black-box answers.
- Also discovered superior bin-packing algorithms with practical data center applications.

## Detailed Summary

[[entities/funsearch]] represents a paradigm for using LLMs in [[concepts/ai-mathematical-reasoning]]. Rather than asking the LLM to directly solve problems, FunSearch has it generate candidate programs (functions), which are then evaluated against objective criteria. High-scoring programs re-enter the evolutionary pool, creating an iterative improvement loop that filters out hallucinations.

The cap set problem asks for the largest set of points in high-dimensional grids where no three points are collinear. Terence Tao and other mathematicians have studied it for decades. FunSearch produced the largest improvement in 20 years, with Professor Jordan Ellenberg calling the solutions "far conceptually richer than a mere list of numbers."

The interpretability advantage is crucial: because outputs are human-readable code, researchers identified symmetries that generated new mathematical insights. This distinguishes FunSearch from black-box optimization and makes it a genuine tool for [[concepts/ai-for-scientific-discovery|scientific discovery]] rather than mere computation.

## Concepts Introduced or Discussed

- [[concepts/ai-mathematical-reasoning]] — using LLMs for math
- [[concepts/ai-for-scientific-discovery]] — broader framing
- [[concepts/llm-as-search-operator]] — LLMs generating candidates in evolutionary loops

## Metadata

- **Author**: Google DeepMind
- **Date Published**: December 2023
- **Format**: article
- **URL**: https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/
