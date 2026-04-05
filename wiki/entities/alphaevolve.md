---
title: "AlphaEvolve"
type: entity
entity_type: tool
url: "https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/"
related: ["[[concepts/ai-mathematical-reasoning]]", "[[concepts/llm-as-search-operator]]", "[[entities/funsearch]]", "[[entities/google-deepmind]]"]
tags: [alphaevolve, algorithm-discovery, gemini, evolutionary-search]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's Gemini-powered evolutionary coding agent. Broke Strassen's 56-year matrix multiplication record (48 vs 49 multiplications), recovers 0.7% of Google's global compute, and improved best-known solutions on 20% of 50+ open math problems."
---

## Overview

AlphaEvolve is [[entities/google-deepmind]]'s general-purpose evolutionary coding agent for algorithm discovery and optimization. It generalizes the [[entities/funsearch]] concept, using an ensemble of Gemini models (Flash for breadth, Pro for depth) with automated evaluators in a full evolutionary framework.

## Key Facts

- **Type**: AI system / algorithm discovery agent
- **Creator**: Google DeepMind
- **Published**: May 2025
- **Notable for**: Breaking Strassen's 56-year matrix multiplication record

## Key Achievements

| Discovery | Impact |
|-----------|--------|
| 48-multiplication algorithm for 4x4 complex matrices | Broke 56-year-old Strassen record |
| Borg data center heuristic | 0.7% Google global compute savings (in production 1+ year) |
| Gemini matrix multiplication kernel | 23% speedup, 1% training time reduction |
| FlashAttention optimization | 32.5% speedup |
| TPU arithmetic circuit | Verilog rewrite for upcoming TPU |
| Kissing number (11D) | New lower bound: 593 spheres |
| 50+ open math problems | Improved best-known in 20% of cases |

## Technical Architecture

1. **LLM Ensemble**: Gemini Flash (breadth exploration) + Gemini Pro (deep reasoning).
2. **Prompt Sampler**: Assembles context from problem specs and best prior solutions.
3. **Automated Evaluator**: Objective scoring of candidate code solutions.
4. **Evolutionary Selection**: Program database implementing selection and mutation.

## Mentioned In

- [[sources/alphaevolve-algorithm-discovery]] — detailed analysis

## External References

- [DeepMind blog](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- [AlphaEvolve paper (PDF)](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf)
