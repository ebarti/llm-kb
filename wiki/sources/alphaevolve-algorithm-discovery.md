---
title: "Source: AlphaEvolve — Gemini-Powered Algorithm Discovery"
type: source-summary
source: "[[raw/alphaevolve-algorithm-discovery]]"
related: ["[[concepts/ai-mathematical-reasoning]]", "[[concepts/ai-for-scientific-discovery]]", "[[entities/alphaevolve]]", "[[entities/google-deepmind]]"]
tags: [alphaevolve, algorithm-discovery, mathematics, deepmind]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's AlphaEvolve uses Gemini Flash/Pro in an evolutionary framework with automated verification to discover algorithms. Broke Strassen's 56-year matrix multiplication record, recovers 0.7% of Google's global compute, and improved best-known solutions on 20% of 50+ open math problems."
---

## Key Points

- Evolutionary coding agent using Gemini Flash (breadth) + Gemini Pro (depth) with automated evaluation.
- Broke Strassen's 56-year-old matrix multiplication record: 48 scalar multiplications for 4x4 complex matrices (vs 49).
- Recovers 0.7% of Google's worldwide compute resources via data center heuristic (in production 1+ year).
- 23% speedup for Gemini's matrix multiplication kernel; 32.5% speedup for FlashAttention.
- Tested on 50+ open math problems: rediscovered SOTA in 75% of cases, improved best-known in 20%.
- New lower bound for kissing number in 11 dimensions (593 outer spheres).

## Detailed Summary

[[entities/alphaevolve]] represents a general-purpose evolution of the FunSearch concept. Where [[entities/funsearch]] used PaLM 2 for specific mathematical problems, AlphaEvolve pairs an ensemble of Gemini models with automated evaluators in a full evolutionary framework — a prompt sampler generates context, LLMs propose solutions as code, evaluators score them, and an evolutionary algorithm selects the best for future iterations.

The matrix multiplication breakthrough is historically significant: Strassen's 1969 algorithm was the long-standing benchmark for efficient matrix multiplication. AlphaEvolve's discovery of a 48-multiplication algorithm for 4x4 complex matrices breaks that record for the first time in 56 years.

Practical applications at Google are equally impressive: the Borg data center heuristic saves 0.7% of global compute (enormous at Google's scale), and kernel optimizations accelerate Gemini training itself — creating a recursive improvement loop where AI improves the AI that created it.

## Concepts Introduced or Discussed

- [[concepts/ai-mathematical-reasoning]] — algorithm discovery
- [[concepts/ai-for-scientific-discovery]] — scientific applications
- [[concepts/llm-as-search-operator]] — evolutionary LLM frameworks

## Metadata

- **Author**: Google DeepMind
- **Date Published**: May 2025
- **Format**: article
- **URL**: https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
