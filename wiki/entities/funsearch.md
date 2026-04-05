---
title: "FunSearch"
type: entity
entity_type: tool
url: "https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/"
related: ["[[concepts/ai-mathematical-reasoning]]", "[[concepts/llm-as-search-operator]]", "[[entities/alphaevolve]]", "[[entities/google-deepmind]]"]
tags: [funsearch, mathematics, llm, evolutionary-search]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's system pairing PaLM 2 with automated evaluators in evolutionary loops to make mathematical discoveries. First LLM to solve a long-standing math puzzle (cap set problem). Produces interpretable code, not black-box answers."
---

## Overview

FunSearch is [[entities/google-deepmind]]'s method for using LLMs to make genuine mathematical discoveries. It pairs a large language model (PaLM 2) with an automated evaluator in an evolutionary loop, generating human-readable code that represents solutions to mathematical and optimization problems.

## Key Facts

- **Type**: AI system / mathematical discovery tool
- **Creator**: Google DeepMind
- **Published**: Nature, December 2023
- **Notable for**: First LLM-derived solution to a long-standing mathematical puzzle

## How It Works

1. LLM generates candidate programs (functions in code).
2. Automated evaluator runs and scores each candidate.
3. High-scoring programs re-enter the evolutionary pool.
4. Iterative improvement filters hallucinations and refines solutions.

## Key Discoveries

- **Cap set problem**: Largest increase in cap set sizes in 20 years.
- **Bin packing**: Algorithms outperforming established human-designed heuristics.

## Significance

FunSearch established the [[concepts/llm-as-search-operator]] paradigm — using LLMs for creative candidate generation with objective verification. This was later generalized by [[entities/alphaevolve]] to a broader range of problems.

## Mentioned In

- [[sources/funsearch-mathematical-discovery]] — detailed analysis

## External References

- [DeepMind blog](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/)
- [MIT Technology Review coverage](https://www.technologyreview.com/2023/12/14/1085318/google-deepmind-large-language-model-solve-unsolvable-math-problem-cap-set/)
