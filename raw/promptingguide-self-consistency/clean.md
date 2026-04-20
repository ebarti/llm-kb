---
title: "Self-Consistency Prompting"
source: "https://www.promptingguide.ai/techniques/consistency"
author: "DAIR.AI / Prompt Engineering Guide"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [prompt-engineering, self-consistency, reasoning, majority-voting]
type: article
status: raw
discovered_via: search
---

# Self-Consistency Prompting: Complete Overview

## Definition
Self-consistency is an advanced prompt engineering technique proposed by Wang et al. (2022) that aims to replace the naive greedy decoding used in chain-of-thought prompting. Rather than relying on a single reasoning path, it generates multiple diverse outputs and selects the most consistently supported answer.

## How It Works

1. Multiple Sampling: Generate several reasoning pathways using few-shot chain-of-thought examples
2. Diverse Outputs: Collect multiple independent responses to the same query
3. Consensus Selection: Identify and select the most frequently occurring correct answer across all generations (majority voting)

## Relationship to Chain-of-Thought
Self-consistency builds upon and improves CoT prompting. Rather than accepting the first generated reasoning path, it leverages the diversity of multiple CoT outputs to achieve more reliable results through a voting mechanism.

## Performance
- Particularly strengthens performance on arithmetic and commonsense reasoning
- Increasing the number of sampled reasoning paths increases performance up until a plateau around 40
- Diminishing returns as you generate more responses
- Boosts the performance of CoT prompting by aggregating multiple responses that tend to be more reliable and accurate than individual CoT completions
