---
title: "Source: Balancing Vocabulary Size in Modern LLMs"
type: source-summary
source: "[[raw/rohan-paul-vocabulary-size-tradeoffs]]"
related: ["[[concepts/vocabulary-size-tradeoffs]]", "[[concepts/tokenization]]", "[[concepts/subword-tokenization]]"]
last_compiled: 2026-04-05
summary: "Rohan Paul analyzes vocabulary size trade-offs across GPT-4 (~100k), LLaMA 3 (~128k), and Mistral (~131k), showing diminishing returns beyond 100k tokens and the tension between sequence length and embedding overhead."
---

## Key Points

- GPT-4 ~100k tokens, LLaMA 3 ~128k, Mistral ~131k — all trending upward from 32k-50k ranges
- Smaller vocabularies: no OOV issues but longer sequences exhaust context windows
- Larger vocabularies: shorter sequences but massive embedding layers (32k vocab = ~130M params; 128k = ~500M params at 4,096 dims)
- Diminishing returns beyond ~100k tokens for perplexity improvements
- Fixed token budget: larger vocab = more training passes over same text
- Fixed epoch budget: smaller vocab = more tokens generated, more compute needed
- Multilingual models benefit significantly from expanded vocabularies (non-Latin fertility improves)
- Emerging approach: vocabulary curriculum learning — dynamically merging predictable tokens during training

## Detailed Summary

Paul provides the most data-rich analysis of [[concepts/vocabulary-size-tradeoffs]]. The core tension: larger vocabularies compress text into fewer tokens (reducing attention's quadratic cost and fitting more into context windows) but increase the embedding matrix size and per-step softmax computation. At GPT-4's 100k vocabulary with 4,096 embedding dimensions, the embedding layer alone has ~410M parameters. The practical sweet spot for English is 33k-50k; multilingual models need 100k+. The most forward-looking insight is vocabulary curriculum learning, which adapts the vocabulary alongside model capabilities during training rather than fixing it before training begins.

## Related Concepts

- [[concepts/vocabulary-size-tradeoffs]] — the core analysis
- [[concepts/tokenization]] — vocabulary size is a key tokenization design choice
- [[concepts/multilingual-tokenization]] — multilingual demands drive larger vocabularies
- [[concepts/subword-tokenization]] — all modern approaches use subword methods
