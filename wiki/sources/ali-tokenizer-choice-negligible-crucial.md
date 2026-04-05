---
title: "Source: Tokenizer Choice For LLM Training — Negligible or Crucial?"
type: source-summary
source: "[[raw/ali-tokenizer-choice-negligible-crucial]]"
related: ["[[concepts/tokenization]]", "[[concepts/vocabulary-size-tradeoffs]]", "[[concepts/multilingual-tokenization]]", "[[concepts/byte-pair-encoding]]", "[[concepts/unigram-tokenization]]"]
last_compiled: 2026-04-05
summary: "Ali et al. train 24 LLMs varying tokenizer algorithm/library/vocab-size, finding tokenizer choice is crucial: up to 9pp accuracy spread on tasks, 68% cost overhead for multilingual, and fertility metrics are unreliable."
---

## Key Points

- Trained 24 decoder-only 2.6B models systematically varying BPE vs. Unigram, HuggingFace vs. SentencePiece, 33k-100k vocabulary
- Fertility and parity metrics are "not always predictive of model downstream performance"
- English: smaller vocabularies (33k) perform best; multilingual: larger (100k) wins
- Multilingual tokenizers need 3x the vocabulary of English-only
- English-centric tokenizers add up to 68% training cost for non-English languages
- Task-specific performance spread: up to 9 percentage points (ARC-Easy) between best and worst tokenizer
- Library implementation differences matter even with identical algorithms
- Best English: BPE-SentencePiece-33k (50.81%); Best multilingual: BPE-SentencePiece-100k (41.44%)

## Detailed Summary

This is the most rigorous empirical study of tokenizer impact on LLM performance. Ali et al. challenged the common assumption that tokenizer choice is a minor detail by systematically training 24 models across two algorithm families ([[concepts/byte-pair-encoding]] and [[concepts/unigram-tokenization]]), two libraries (HuggingFace Tokenizers and [[concepts/sentencepiece]]), and three vocabulary sizes (33k, 50k, 100k). The most surprising finding: traditional evaluation metrics (fertility, parity) are unreliable predictors of downstream performance. Low fertility is necessary but not sufficient. The monolingual vs. multilingual split is stark — what works for English (smaller vocab) actively hurts multilingual models. The 68% training cost overhead for non-English languages with English-centric tokenizers has environmental and democratization implications.

## Related Concepts

- [[concepts/tokenization]] — the design choice proven crucial
- [[concepts/vocabulary-size-tradeoffs]] — empirical evidence for optimal sizes
- [[concepts/multilingual-tokenization]] — the cost of English-centric tokenizers
- [[concepts/byte-pair-encoding]] — consistently best-performing algorithm
