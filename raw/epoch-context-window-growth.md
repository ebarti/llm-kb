---
title: "LLMs Now Accept Longer Inputs, and the Best Models Can Use Them More Effectively"
source: "https://epoch.ai/data-insights/context-windows/"
author: "Epoch AI"
date_published: 2025-06-05
date_ingested: 2026-04-05
tags: [context-windows, benchmarks, long-context, frontier-models]
type: article
status: raw
discovered_via: search
---

# LLMs Now Accept Longer Inputs — Epoch AI Analysis

## Key Growth Metrics

- Frontier LLM context windows have grown approximately **30x annually** since mid-2023, with a confidence interval of 10x-50x based on bootstrap analysis of 123 models.
- Effective usage growth is even faster: the input length where top performers reach 80% accuracy has increased over **250x in nine months** (200x-20,000x range).

## Benchmarks Used

Two primary evaluations tracked:
- **Fiction.liveBench** (37 models): Measures narrative comprehension across documents.
- **MRCR** (49 models): Tests context-dependent information retrieval; analysis used the 2-needle setting with single distractor passage.

## Model Performance Notes

- Gemini 2.5 Pro (released 06-05) represents current performance leader but "only scores above 80% on the 8K input length setting" in the most challenging 8-needle MRCR variant.
- Even frontier models show degradation on harder multi-needle retrieval tasks at long context lengths.

## Key Limitation

The analysis acknowledges these benchmarks represent "moderately challenging" tasks rather than comprehensive long-context testing. Many real-world applications likely exceed current evaluation difficulties.

## Data Sources

Analysis draws from Artificial Analysis (context window sizes), Epoch's AI Models database (123 models tracked), and benchmark platforms including Context Arena and Fiction.liveBench.
