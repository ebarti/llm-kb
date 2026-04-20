---
title: "Increasing the Thinking Budget is Not All You Need"
source: "https://arxiv.org/abs/2512.19585"
author: "Ignacio Iacobacci, Zhaozhi Qian, Faroq AL-Tam, Muhammad AL-Qurishi, Riad Souissi"
date_published: 2025-12-30
date_ingested: 2026-04-05
tags: [test-time-compute, thinking-budget, overthinking, reasoning, efficiency]
type: paper
status: raw
discovered_via: search
---

# Increasing the Thinking Budget is Not All You Need

## Core Finding
Simply increasing the thinking budget is not the most effective use of compute. Performance fluctuates across budgets and shows signs of plateau, especially for weaker models.

## Results by Model Capability
- Stronger models (Qwen3-8B) showed some capacity to leverage extended thinking.
- Weaker models struggled substantially to benefit from extended reasoning phases.
- No clear "overthinking" where thinking actively degraded results, but budgets failed to deliver proportional improvements.

## Practical Recommendations
1. **Summary approach** (generating multiple diverse outputs and consolidating) proved more effective than naive budget increases.
2. **Self-consistency** (majority voting across multiple runs) showed competitive results.
3. Even without thinking enabled, ensemble methods substantially outperformed single-run approaches.

## Key Insight
Strategic configuration matters more than computational volume alone. The allocation strategy (how compute is distributed across parallel vs. sequential) matters more than raw budget size.

## Significance
Challenges the assumption that reasoning models will improve monotonically with more thinking tokens. Suggests investment in smarter allocation (parallel sampling, aggregation) over simply extending sequential reasoning length.
