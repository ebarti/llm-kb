---
title: "LLM as Search Operator"
type: concept
sources: ["[[sources/funsearch-mathematical-discovery]]", "[[sources/alphaevolve-algorithm-discovery]]"]
related: ["[[concepts/ai-mathematical-reasoning]]", "[[concepts/ai-for-scientific-discovery]]", "[[entities/funsearch]]", "[[entities/alphaevolve]]"]
tags: [llm, evolutionary-search, algorithm-discovery, funsearch]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "A paradigm where LLMs generate creative candidate solutions in evolutionary loops while automated evaluators verify correctness — filtering hallucinations while leveraging creativity. FunSearch and AlphaEvolve demonstrate this produces genuine scientific discoveries."
---

## Overview

The LLM-as-search-operator paradigm uses large language models not as answer-generators but as creative candidate generators within an evolutionary optimization framework. An automated evaluator provides objective verification, creating a system that leverages LLM creativity while filtering out hallucinations through rigorous testing.

This pattern was established by [[entities/funsearch]] (2023) and generalized by [[entities/alphaevolve]] (2025). It addresses a fundamental limitation of LLMs: they are creative but unreliable. By pairing creativity with verification, the paradigm produces genuinely novel and provably correct discoveries.

## How It Works

1. **Prompt Assembly**: A sampler creates context from the problem specification and high-scoring previous solutions.
2. **LLM Generation**: The model generates candidate solutions as computer code (functions).
3. **Automated Evaluation**: An evaluator runs the code, measures performance against objective criteria, and scores it.
4. **Evolutionary Selection**: High-scoring solutions re-enter the pool; low-scoring ones are discarded.
5. **Iteration**: The cycle repeats, with each generation building on the best of previous ones.

## Key Properties

- **Hallucination Filtering**: Unlike direct LLM answers, every candidate is verified before acceptance.
- **Interpretability**: Outputs are human-readable code, not black-box answers.
- **Scalability**: Can leverage faster models (Gemini Flash) for breadth and powerful models (Gemini Pro) for depth.
- **Domain Generality**: Applicable wherever solutions can be expressed as code and evaluated automatically.

## Demonstrated Results

| System | Discovery | Significance |
|--------|-----------|-------------|
| FunSearch | Cap set problem solution | Largest advance in 20 years |
| FunSearch | Bin-packing algorithms | Beat human-designed heuristics |
| AlphaEvolve | 48-multiplication 4x4 complex matrix algorithm | Broke 56-year Strassen record |
| AlphaEvolve | Data center heuristic | 0.7% Google compute savings |
| AlphaEvolve | Kissing number in 11D | New lower bound (593 spheres) |
| AlphaEvolve | 50+ open math problems | Improved 20% of best-known solutions |

## Broader Implications

This paradigm may be the most transferable contribution of AI to scientific discovery. It works whenever:
1. Solutions can be expressed as executable code.
2. Objective evaluation criteria exist (even approximate ones).
3. The search space is too large for exhaustive enumeration.
4. Human creativity would help but is too slow.

Potential applications beyond mathematics include materials discovery, drug candidate screening, circuit design, and algorithm optimization for any computational system.

## Sources

- [[sources/funsearch-mathematical-discovery]] — Original paradigm demonstration
- [[sources/alphaevolve-algorithm-discovery]] — Generalized and industrialized version

## Related Concepts

- [[concepts/ai-mathematical-reasoning]] — primary application domain
- [[concepts/ai-for-scientific-discovery]] — broader context
