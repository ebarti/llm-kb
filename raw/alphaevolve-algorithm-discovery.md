---
title: "AlphaEvolve: A Gemini-Powered Coding Agent for Designing Advanced Algorithms"
source: "https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/"
author: "Google DeepMind"
date_published: 2025-05-15
date_ingested: 2026-04-05
tags: [alphaevolve, algorithm-discovery, mathematics, deepmind, gemini]
type: article
status: raw
discovered_via: search
---

# AlphaEvolve: Gemini-Powered Algorithm Discovery Agent

## How It Works

Three core components:
1. **LLM Ensemble**: Gemini Flash (breadth) + Gemini Pro (depth) generate computer programs implementing algorithmic solutions.
2. **Evolutionary Framework**: Prompt sampler assembles prompts; automated evaluation verifies, runs, and scores each proposal; program database implements evolutionary algorithm determining which solutions inform future iterations.
3. **Verification**: Automated evaluation metrics providing objective, quantifiable assessment of each solution's accuracy and quality.

## Major Discoveries

### Matrix Multiplication Breakthrough
- Found an algorithm to multiply 4x4 complex-valued matrices using 48 scalar multiplications.
- Improved upon Strassen's 1969 algorithm (49 multiplications) — breaking a 56-year-old record.

### Data Center Optimization
- Discovered heuristic for Google's Borg orchestration system.
- Continuously recovers 0.7% of Google's worldwide compute resources.
- In production for over a year; human-readable code.

### Hardware Design
- Proposed Verilog rewrite eliminating unnecessary bits in arithmetic circuits for matrix multiplication.
- Integrated into an upcoming Tensor Processing Unit (TPU).

### AI Training Acceleration
- Matrix multiplication kernel: 23% speedup in Gemini's architecture, leading to 1% reduction in Gemini's training time.
- FlashAttention optimization: up to 32.5% speedup.
- Reduced kernel optimization time from weeks of expert effort to days.

### Mathematical Problems
- Tested on 50+ open problems in analysis, geometry, combinatorics, number theory.
- Rediscovered state-of-the-art in ~75% of cases.
- Improved best-known solutions in 20% of cases.
- **Kissing Number Problem**: Discovered configuration of 593 outer spheres, establishing new lower bound in 11 dimensions.

## Future Directions

Building user interface for broader access. Early Access Program for selected academic users. Exploring applications in materials science, drug discovery, sustainability.
