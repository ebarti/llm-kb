---
title: "Source: Self-Consistency Prompting (Prompt Engineering Guide)"
type: source-summary
source: "[[raw/promptingguide-self-consistency]]"
related: ["[[concepts/self-consistency-prompting]]", "[[concepts/chain-of-thought-prompting]]", "[[concepts/prompt-engineering]]"]
last_compiled: 2026-04-05
summary: "DAIR.AI overview of self-consistency: Wang et al. (2022) technique sampling multiple CoT reasoning paths and selecting the most frequent answer via majority voting."
reading_time: "1 min"
---

## Key Points
- Replaces greedy decoding in CoT with diverse multi-path sampling and majority voting
- Generates multiple independent reasoning pathways, then selects the most frequent answer
- Particularly effective for arithmetic and commonsense reasoning
- Performance plateaus around 40 sampled paths — diminishing returns beyond that
- Builds upon and strictly improves CoT prompting

## Detailed Summary
Self-consistency is a natural extension of [[concepts/chain-of-thought-prompting]] that addresses CoT's fragility — a single reasoning path may contain errors. By sampling multiple diverse reasoning chains and taking a majority vote on the final answer, self-consistency produces more reliable outputs. The technique is especially powerful for tasks with a clear correct answer (arithmetic, classification).

## Related Concepts
- [[concepts/self-consistency-prompting]] — the core technique
- [[concepts/chain-of-thought-prompting]] — the foundation it builds on
- [[concepts/prompt-engineering]] — parent domain
