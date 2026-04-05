---
title: "Source: AB-MCTS -- Inference-Time Scaling and Collective Intelligence"
type: source-summary
source: "[[raw/sakana-ab-mcts-collective-inference]]"
related: ["[[concepts/mcts-llm-reasoning]]", "[[concepts/test-time-compute]]", "[[concepts/best-of-n-sampling]]"]
tags: [mcts, multi-model, collective-intelligence, inference-scaling]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Sakana AI's Adaptive Branching MCTS enables multi-LLM cooperation at inference time via Thompson Sampling over depth/width/model selection, achieving 30%+ on ARC-AGI-2 through collective intelligence."
---

## Key Points

- Adaptive Branching MCTS searches in depth (refine) and width (generate new solutions).
- Uses Thompson Sampling for probabilistic direction selection.
- Multi-LLM version adds model selection as a third search dimension.
- ARC-AGI-2: single o4-mini 23% -> AB-MCTS 27.5% -> Multi-LLM 30%+.
- Models build upon each other's work: failures from one model become inputs for another.

## Detailed Summary

Sakana AI's AB-MCTS extends [[concepts/mcts-llm-reasoning]] from single-model to multi-model inference. The algorithm searches across three dimensions: depth (refining a solution), width (generating alternatives), and model identity (which LLM to query). Thompson Sampling balances exploration and exploitation across all three.

This represents a form of collective intelligence at inference time: different models with different training backgrounds contribute distinct strengths. The 30%+ accuracy on ARC-AGI-2 (vs. 23% for single-model repeated sampling) demonstrates that systematic multi-model cooperation extracts more value from [[concepts/test-time-compute]] than simply running one model harder.

## Metadata

- **Author**: Sakana AI
- **Date Published**: 2025-06-15
- **Format**: article / research blog
- **URL**: https://sakana.ai/ab-mcts/
