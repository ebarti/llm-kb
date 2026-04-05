---
title: "Vocabulary Size Tradeoffs"
type: concept
sources: ["[[sources/rohan-paul-vocabulary-size-tradeoffs]]", "[[sources/ali-tokenizer-choice-negligible-crucial]]", "[[sources/kamali-tokenization-killing-multilingual]]"]
related: ["[[concepts/tokenization]]", "[[concepts/byte-pair-encoding]]", "[[concepts/multilingual-tokenization]]", "[[concepts/subword-tokenization]]"]
last_compiled: 2026-04-05
summary: "The fundamental tension between vocabulary size, sequence length, embedding overhead, and language coverage — with modern LLMs trending from 32k toward 100k-131k tokens."
---

## Overview

Vocabulary size is one of the most consequential hyperparameters in LLM design. It creates a fundamental tension: larger vocabularies produce shorter token sequences (reducing attention cost and fitting more into context windows) but require larger embedding matrices and increase per-token computation. The trend in modern LLMs is unmistakably upward, from 32k-50k toward 100k-131k.

## Key Ideas

### Modern LLM Vocabulary Sizes

| Model | Vocabulary Size | Generation |
|-------|----------------|------------|
| GPT-2 | 50,257 | Early |
| GPT-3 | ~50,000 | Mid |
| GPT-4 | ~100,000 | Current |
| LLaMA 1/2 | 32,000 | Mid |
| LLaMA 3 | ~128,000 | Current |
| Mistral (early) | 32,000 | Mid |
| Mistral (recent) | ~131,000 | Current |
| Gemma | ~250,000 | Current |

### The Core Trade-off

**Smaller vocabulary (32k)**:
- More subword splits → longer token sequences → more attention computation (quadratic cost)
- Better OOV handling via subword composition
- Smaller embedding matrix (~130M parameters at 4,096 dimensions)
- Better for monolingual English (per [[sources/ali-tokenizer-choice-negligible-crucial]])

**Larger vocabulary (100k+)**:
- Fewer tokens per text → shorter sequences → fits more into context windows
- Larger embedding matrix (~500M+ parameters at 4,096 dimensions)
- Better for multilingual models (non-Latin script fertility improves significantly)
- Diminishing perplexity returns beyond ~100k

### Diminishing Returns

Performance improvements show clear diminishing returns. Expanding from 8k to 32k tokens yields substantial gains in perplexity. Going from 32k to 100k helps noticeably. Beyond 100k, improvements are marginal relative to the memory and compute costs of a larger embedding layer.

### Training Budget Interaction

- **Fixed token budget** (e.g., 1 trillion tokens): larger vocabulary means more training passes over the same text, since fewer tokens represent equivalent content
- **Fixed epoch budget**: smaller vocabulary generates more total tokens, increasing compute but potentially improving performance through greater exposure

### Multilingual Demands

[[sources/ali-tokenizer-choice-negligible-crucial]] found multilingual tokenizers need **3x the vocabulary** of English-only. English-centric tokenizers applied to multilingual training add up to 68% training cost for non-English languages. [[sources/kamali-tokenization-killing-multilingual]] argues that large vocabularies (Gemma 250k) achieve multilingual coverage "at the cost of raw intelligence" — the model becomes dumber to handle more languages.

### Emerging Approaches

- **Vocabulary curriculum learning**: dynamically merging predictable tokens during training, adapting vocabulary alongside model capabilities
- **[[concepts/byte-level-models]]**: the extreme — 256-320 tokens, eliminating vocabulary size as a concern entirely

## Sources

- [[sources/rohan-paul-vocabulary-size-tradeoffs]] — comprehensive analysis with embedding parameter counts
- [[sources/ali-tokenizer-choice-negligible-crucial]] — empirical evidence: 33k best for English, 100k for multilingual
- [[sources/kamali-tokenization-killing-multilingual]] — large vocab = dumber model argument

## Related Concepts

- [[concepts/tokenization]] — vocabulary size is a core tokenization design choice
- [[concepts/byte-pair-encoding]] — vocabulary size = base + number of merges
- [[concepts/multilingual-tokenization]] — multilingual needs drive larger vocabularies
- [[concepts/byte-level-models]] — eliminate vocabulary size tradeoffs entirely
