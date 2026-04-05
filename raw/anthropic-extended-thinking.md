---
title: "Claude's Extended Thinking"
source: "https://www.anthropic.com/news/visible-extended-thinking"
author: "Anthropic"
date_published: 2025-02-24
date_ingested: 2026-04-05
tags: [claude, extended-thinking, reasoning, test-time-compute, anthropic]
type: article
status: raw
discovered_via: search
---

# Claude's Extended Thinking

## How It Works

Extended thinking allows Claude 3.7 Sonnet to allocate additional computational resources before generating responses. It uses "serial test-time compute" -- multiple sequential reasoning steps that accumulate before the final output. The same model is used; it simply gives itself more time and effort before answering.

## Thinking Budget

- Developers can set a configurable "thinking budget" to control how long Claude spends deliberating.
- Mathematical accuracy improves logarithmically as token allocation increases.
- Claude typically stops short of using the entire budget, suggesting efficient self-regulation.

## Hybrid Model

Claude 3.7 Sonnet is both an ordinary LLM and a reasoning model in one:
- Standard mode: functions as a regular LLM (upgraded Claude 3.5 Sonnet).
- Extended thinking mode: self-reflects before answering, improving complex task performance.
- Users/developers toggle between modes based on task needs.

## Performance

- **AIME 2024 (math)**: Performance scales predictably with increased thinking tokens.
- **GPQA (science)**: 84.8% overall; 96.5% on physics subset.
- **OSWorld**: Superior on multimodal agent evaluation.
- **Strongest domains**: Math, physics, competition coding, in-depth analysis, debugging.

## Visible Thinking

Anthropic chose to make Claude's thought process visible in raw form. Benefits:
- Enhanced trust through observable reasoning.
- Research value -- seeing AI cognition patterns.
- Alignment research capabilities.

Tradeoffs:
- Thoughts appear less polished than normal outputs.
- Questions about "faithfulness" -- whether displayed thinking reflects actual computation.
- Potential jailbreak vulnerability through thought manipulation.

## Parallel Compute

Researchers also experimented with generating multiple independent reasoning processes simultaneously, then selecting optimal responses through majority voting or learned scoring models.
