---
title: "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"
source: "https://arxiv.org/abs/2408.03314"
author: "Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar"
date_published: 2024-08-06
date_ingested: 2026-04-05
tags: [test-time-compute, inference-scaling, reasoning, process-reward-models]
type: paper
status: raw
discovered_via: search
---

# Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

## Key Findings

1. A compute-optimal strategy can improve the efficiency of test-time compute scaling by more than 4x compared to a best-of-N baseline.
2. In a FLOPs-matched evaluation, test-time compute can be used to outperform a 14x larger model.
3. The effectiveness of different approaches critically varies depending on the difficulty of the prompt.

## Two Primary Mechanisms for Scaling Test-Time Compute

1. **Searching against process-based verifier reward models**: Generate multiple candidate solutions and use a trained verifier to select the best one. The verifier evaluates each reasoning step, not just the final answer.

2. **Updating the model's distribution adaptively**: Modify the model's response distribution at test time given the specific prompt, allocating more compute to harder problems.

## Compute-Optimal Scaling Strategy

- Adjusts test-time compute based on predicted task difficulty.
- Easy problems get minimal extra compute; hard problems get substantially more.
- Avoids inefficiencies of uniform compute allocation across all prompts.
- This adaptive approach is what yields the 4x efficiency improvement.

## Significance

This paper formalized the shift from "bigger models are better" to "smarter inference is better." It showed that the same compute budget could be more effectively spent at inference time than at training time, laying the theoretical groundwork for reasoning models like o1 and R1 that invest heavily in test-time computation. The 14x result is particularly striking -- a small model thinking harder can outperform a much larger model answering quickly.
