---
title: "Self-Consistency Prompting"
type: concept
sources: ["[[sources/promptingguide-self-consistency]]"]
related: ["[[concepts/prompt-engineering]]", "[[concepts/chain-of-thought-prompting]]", "[[concepts/tree-of-thoughts-prompting]]"]
last_compiled: 2026-04-05
summary: "Wang et al. (2022) technique that improves CoT by sampling multiple diverse reasoning paths and selecting the most frequent answer via majority voting — more reliable than single-path CoT."
---

## Overview

Self-consistency prompting, proposed by Wang et al. (2022), is an enhancement to [[concepts/chain-of-thought-prompting]] that replaces greedy single-path decoding with diverse multi-path sampling and majority voting. Instead of relying on one reasoning chain that might contain errors, self-consistency generates many independent reasoning paths and selects the answer that appears most frequently across them.

The insight is elegant: if multiple independent reasoning processes arrive at the same answer, that answer is more likely to be correct. This mirrors ensemble methods in machine learning, where aggregating diverse models outperforms any single model.

## How It Works

1. **Sample multiple responses**: Generate several (5-40) independent reasoning paths using [[concepts/chain-of-thought-prompting]] with temperature-based sampling
2. **Extract answers**: Identify the final answer from each reasoning path
3. **Majority vote**: Select the answer that appears most frequently

## Performance Characteristics

- Particularly effective for arithmetic and commonsense reasoning
- Performance increases with more samples, plateauing around 40 paths
- Diminishing returns beyond the plateau — the cost/benefit ratio drops
- Strictly improves over single-path CoT in virtually all tested scenarios

## Trade-offs

The main cost is computational: generating 20-40 reasoning paths means 20-40x the inference cost. This makes self-consistency most valuable for high-stakes tasks where correctness matters more than cost or latency (e.g., medical diagnosis, financial analysis, exam questions).

## Sources
- [[sources/promptingguide-self-consistency]] — Primary overview

## Related Concepts
- [[concepts/chain-of-thought-prompting]] — the foundation self-consistency builds on
- [[concepts/tree-of-thoughts-prompting]] — a more structured multi-path approach
- [[concepts/prompt-engineering]] — parent domain
