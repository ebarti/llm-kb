---
title: "AI for Mathematical Reasoning"
type: concept
sources: ["[[sources/funsearch-mathematical-discovery]]", "[[sources/alphaevolve-algorithm-discovery]]", "[[sources/gemini-deep-think-scientific-discovery]]"]
related: ["[[concepts/ai-for-scientific-discovery]]", "[[concepts/llm-as-search-operator]]", "[[concepts/test-time-compute]]", "[[entities/funsearch]]", "[[entities/alphaevolve]]"]
tags: [mathematics, theorem-proving, algorithm-discovery, ai-reasoning]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "AI mathematical reasoning has advanced from struggling with arithmetic to winning IMO gold medals (Gemini Deep Think, DeepSeekMath-V2), solving open Erdos conjectures, breaking 56-year records (AlphaEvolve on matrix multiplication), and producing genuine mathematical discoveries (FunSearch on cap sets)."
---

## Overview

AI mathematical reasoning encompasses three distinct capabilities: competition-level problem solving, theorem proving and conjecture resolution, and algorithm discovery. The field has progressed extraordinarily rapidly — from LLMs struggling with basic arithmetic to winning International Mathematical Olympiad gold medals within roughly two years (2023-2025).

## Three Paradigms

### 1. Competition Problem Solving (Brute Reasoning)

Direct application of powerful reasoning models to mathematical problems:

- **Gemini Deep Think** (2025): IMO Gold, 35/42 points, 5/6 problems solved perfectly. ICPC World Finals success. IMO-ProofBench Advanced: 90%.
- **DeepSeekMath-V2** (2025): 5/6 IMO 2025 problems. Gold in both IMO 2025 and CMO 2024.
- **PhD-level**: Gemini Deep Think scores 38% on FutureMath Basic (PhD-level exercises) — significant but shows the gap between competition math and research math.

### 2. LLMs as Search Operators (Evolutionary Discovery)

Using LLMs to generate candidate solutions in evolutionary loops with automated verification:

- **[[entities/funsearch]]** (2023): PaLM 2 + evaluator. First LLM-derived solution to a long-standing mathematical puzzle (cap set problem). Also discovered superior bin-packing algorithms.
- **[[entities/alphaevolve]]** (2025): Gemini Flash + Pro ensemble. Broke Strassen's 56-year matrix multiplication record (48 vs 49 scalar multiplications for 4x4 complex matrices). Improved best-known solutions on 20% of 50+ open problems. Discovered new kissing number lower bound in 11 dimensions.

Key pattern: LLMs provide creative candidate generation; automated evaluators provide objective verification. This [[concepts/llm-as-search-operator|LLM-as-search-operator]] paradigm filters out hallucinations while leveraging LLM creativity.

### 3. AI-Assisted Research (Human-AI Collaboration)

Using AI as a "force multiplier for human intellect":

- **Aletheia** (Gemini Deep Think research agent): Natural language verification, iterative revision, web search integration, failure acknowledgment.
- **"Vibe-Proving"**: Iterative human-AI cycles using balanced prompting (requesting simultaneous proof or refutation) and code-assisted verification.
- **Autonomous discoveries**: 4 open Erdos conjectures solved autonomously; Erdos-1051 generalized into peer-reviewed publication.
- **Cross-domain breakthroughs**: Network optimization (Max-Cut, Steiner Tree via measure theory), settling a 2015 conjecture in submodular optimization, cosmic string singularity solutions.

## The Interpretability Advantage

A crucial property of FunSearch and AlphaEvolve: outputs are human-readable code, not black-box answers. This enables:
- Researchers to understand *why* solutions work.
- Discovery of new mathematical insights (e.g., symmetries in FunSearch outputs).
- Trust and verification by the mathematical community.

## Real-World Impact Beyond Mathematics

AlphaEvolve's discoveries have immediate practical applications:
- **Data center optimization**: 0.7% of Google's global compute recovered via Borg heuristic.
- **AI training**: 23% speedup in Gemini matrix multiplication kernel; 32.5% FlashAttention speedup.
- **Hardware design**: Verilog optimizations integrated into upcoming TPU designs.

## Open Questions

- Can AI produce genuinely novel mathematical theories (not just solutions to known problems)?
- Will "Vibe-Proving" become standard practice in mathematical research?
- How will the mathematical community handle AI-assisted proofs for publication?
- Can evolutionary LLM approaches transfer from combinatorics to analysis and geometry?

## Sources

- [[sources/funsearch-mathematical-discovery]] — Cap set discovery and LLM-evaluator paradigm
- [[sources/alphaevolve-algorithm-discovery]] — Matrix multiplication and 50+ open problems
- [[sources/gemini-deep-think-scientific-discovery]] — IMO gold, Erdos conjectures, Vibe-Proving

## Related Concepts

- [[concepts/ai-for-scientific-discovery]] — broader context
- [[concepts/llm-as-search-operator]] — evolutionary LLM frameworks
- [[concepts/test-time-compute]] — inference-time scaling for reasoning
