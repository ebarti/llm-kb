---
title: "Source: What, How, Where, and How Well? A Survey on Test-Time Scaling in LLMs"
type: source-summary
source: "[[raw/zhang-test-time-scaling-survey]]"
related: ["[[concepts/test-time-compute]]", "[[concepts/reasoning-models]]", "[[concepts/process-reward-models]]", "[[concepts/mcts-llm-reasoning]]", "[[concepts/adaptive-compute-allocation]]", "[[concepts/best-of-n-sampling]]", "[[concepts/latent-reasoning]]"]
tags: [test-time-compute, inference-scaling, survey, reasoning]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Definitive 2025 survey organizing test-time scaling along four dimensions (what/how/where/how well), cataloguing 30+ techniques from parallel sampling to internal scaling, establishing the field's taxonomy."
---

## Key Points

- Organizes TTS research into four dimensions: What to Scale, How to Scale, Where to Scale, How Well to Scale.
- Identifies four scaling types: parallel, sequential, hybrid, and internal.
- Catalogues 30+ major papers and techniques.
- Covers tuning methods (SFT, RL) and inference methods (stimulation, verification, search, aggregation).
- Finds that multi-agent approaches are emerging as effective for both verification and generation.
- Establishes that TTS enables breakthroughs in math, coding, and general-purpose tasks alike.

## Detailed Summary

This comprehensive survey (arXiv 2503.24235) provides the most complete taxonomy of test-time scaling to date. It organizes the field around four questions:

**What to scale**: The survey distinguishes parallel scaling (generate multiple outputs, aggregate), sequential scaling (direct later steps from intermediate results), hybrid scaling (combining both), and internal scaling (models autonomously decide how much compute to allocate). Internal scaling represents the most recent evolution, embodied by [[concepts/reasoning-models]] like o1/o3 and R1 that natively determine their own reasoning depth.

**How to scale**: Methods fall into tuning-based (SFT on extended CoT data, RL training) and inference-based categories. Inference methods are further broken into stimulation (encouraging longer/more outputs), verification (using [[concepts/process-reward-models]] or outcome reward models to select/guide), search (beam search, [[concepts/mcts-llm-reasoning]], tree search), and aggregation (majority voting, weighted consensus).

**Where to scale**: Originally focused on math and code, TTS now extends to science, game strategy, medical reasoning, open-ended Q&A, agent tasks, and multimodal reasoning.

**How well to scale**: Evaluated across performance (accuracy), efficiency (cost-benefit), controllability (budget adherence), and scalability (improvement rate with more compute).

## Concepts Introduced or Discussed

- [[concepts/test-time-compute]] -- the central paradigm
- [[concepts/adaptive-compute-allocation]] -- internal scaling where models self-regulate
- [[concepts/best-of-n-sampling]] -- parallel scaling baseline
- [[concepts/mcts-llm-reasoning]] -- search-based scaling
- [[concepts/process-reward-models]] -- verification-based scaling

## Metadata

- **Author**: Zhang et al.
- **Date Published**: 2025-03-31
- **Format**: paper (survey)
- **URL**: https://arxiv.org/abs/2503.24235
