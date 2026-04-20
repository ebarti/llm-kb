---
title: "The State of LLMs 2025: Progress, Progress, and Predictions"
source: "https://magazine.sebastianraschka.com/p/state-of-llms-2025"
author: "Sebastian Raschka"
date_published: 2025-12-01
date_ingested: 2026-04-05
tags: [llm-benchmarks, benchmaxxing, evaluation, reasoning, benchmark-saturation]
type: article
status: raw
discovered_via: search
---

# State of LLMs 2025: Evaluation and Benchmarks

## Benchmaxxing

The defining trend of 2025: "a strong focus on pushing leaderboard numbers, sometimes to the point where benchmark performance becomes a goal in itself rather than a proxy for general capability."

Critical problem: benchmark scores no longer reliably indicate real-world LLM performance. "Test set data is not only part of the training corpus (intentionally or unintentionally), but is also often directly optimized for during LLM development."

## Trustworthiness Crisis

"Benchmark numbers are no longer trustworthy indicators of LLM performance." Benchmarks serve as necessary thresholds: knowing an LLM scores below X reveals poor performance, but scoring above X doesn't reliably indicate superiority over competitors.

Parallel to 2019 image classification research showing benchmark inflation without ranking changes—LLM evaluation has deteriorated further.

## Evaluation Challenges

Fundamental difficulty: LLM diversity. Unlike image classifiers with single metrics, LLMs handle translation, summarization, code generation, brainstorming, math, and more simultaneously.

Solutions proposed:
- Continuous real-world testing
- Generating new benchmarks regularly
- Recognizing evaluation limitations

## Reasoning Model Achievements

Multiple reasoning models achieved "gold-level performance" in major math competitions (IMO-equivalent) in 2025, including OpenAI models, Gemini Deep Think, and DeepSeekMath-V2.

## Key Benchmarks Mentioned

- MMLU: Saturated above 88%, GPT-5.3 Codex at 93%
- MATH-500: Competition-level mathematical reasoning
- AIME 2025: Hardest math benchmark, scores up to 95.7
- LiveCodeBench v6: Best for tracking coding capability (anti-memorisation)
- GPQA, MMMU, TAU-bench Retail
- 15 major benchmarks in active use in 2026; only 4 reliably predict production outcomes
