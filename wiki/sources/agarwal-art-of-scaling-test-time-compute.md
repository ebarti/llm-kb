---
title: "Source: The Art of Scaling Test-Time Compute for LLMs"
type: source-summary
source: "[[raw/agarwal-art-of-scaling-test-time-compute]]"
related: ["[[concepts/test-time-compute]]", "[[concepts/adaptive-compute-allocation]]", "[[concepts/reasoning-models]]"]
tags: [test-time-compute, empirical-study, inference-scaling]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "First large-scale empirical study of TTS spanning 30B+ tokens across 8 open-source LLMs (7B-235B), finding no universal best strategy but monotonic scaling within model types, with practical selection recipes."
---

## Key Points

- First large-scale empirical study: 30 billion+ tokens generated across 8 open-source LLMs (7B to 235B).
- No single TTS strategy universally dominates -- strategy selection depends on problem difficulty, model type, and compute budget.
- Models fall into "short-horizon" and "long-horizon" groups based on reasoning trace patterns.
- Scaling is monotonic within a given model type -- more compute reliably yields better performance.
- Provides a practical recipe for matching strategy to context.

## Detailed Summary

Agarwal, Sengupta, and Chakraborty (2025) address a critical gap in [[concepts/test-time-compute]] research: most prior work studied individual strategies in isolation. This paper provides the first systematic cross-strategy comparison at scale.

The three key findings:
1. **No universal dominance**: Different strategies (majority voting, best-of-N, tree search, etc.) win under different conditions. This has profound practical implications -- there is no "set and forget" approach.
2. **Distinct model patterns**: Reasoning models exhibit different TTS response curves. "Short-horizon" models benefit most from parallel scaling on easier problems; "long-horizon" models benefit from sequential scaling on harder problems.
3. **Monotonic scaling**: Within a model type, more compute always helps, validating the general principle of [[concepts/test-time-compute]] scaling.

## Concepts Introduced or Discussed

- [[concepts/test-time-compute]] -- empirical validation of scaling properties
- [[concepts/adaptive-compute-allocation]] -- strategy selection based on difficulty

## Metadata

- **Author**: Aradhye Agarwal, Ayan Sengupta, Tanmoy Chakraborty
- **Date Published**: 2025-12-01
- **Format**: paper
- **URL**: https://arxiv.org/abs/2512.02008
