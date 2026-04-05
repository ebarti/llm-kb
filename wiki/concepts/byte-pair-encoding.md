---
title: "Byte Pair Encoding (BPE)"
type: concept
sources: ["[[sources/raschka-bpe-from-scratch]]", "[[sources/huggingface-tokenization-algorithms]]", "[[sources/karpathy-minbpe-lecture]]", "[[sources/github-faster-bpe-tokenizer]]", "[[sources/ali-tokenizer-choice-negligible-crucial]]"]
related: ["[[concepts/tokenization]]", "[[concepts/subword-tokenization]]", "[[concepts/wordpiece]]", "[[concepts/unigram-tokenization]]", "[[concepts/sentencepiece]]", "[[concepts/vocabulary-size-tradeoffs]]"]
last_compiled: 2026-04-05
summary: "The most popular tokenization algorithm for LLMs — iteratively merges the most frequent adjacent byte/character pairs to build a subword vocabulary, used by GPT, Llama, Gemma, and Qwen."
---

## Overview

Byte Pair Encoding (BPE) is the dominant tokenization algorithm in modern large language models. Originally a compression algorithm invented by Philip Gage in 1994, it was adapted for NLP tokenization and popularized by OpenAI's GPT-2 paper in 2019. BPE is used by GPT-2/3/4, Llama, Gemma, Qwen2, and most other leading LLMs.

The algorithm works bottom-up: start with individual bytes (or characters), find the most frequently co-occurring adjacent pair, merge them into a new token, and repeat until the vocabulary reaches the desired size.

## Key Ideas

### The Algorithm

1. **Initialize base vocabulary**: Start with 256 byte values (for byte-level BPE) or all unique characters in the training corpus
2. **Count pair frequencies**: Scan the corpus for the most common adjacent token pair
3. **Merge and record**: Replace all occurrences of that pair with a new token ID; record the merge rule
4. **Repeat**: Continue until reaching the target vocabulary size

The vocabulary size equals the base vocabulary size plus the number of merges. GPT-2 uses 50,257 tokens (256 bytes + 50,000 merges + 1 special token).

### Byte-Level BPE

Standard BPE on Unicode characters would produce an enormous base vocabulary. **Byte-level BPE** operates on raw bytes (256 possible values), ensuring every possible text can be tokenized without unknown tokens. This is the approach used by GPT-2 and most modern models.

### Compression Efficiency

The compression is dramatic: a 17-character phrase "This is some text" requires 17 tokens at the character level but only 4 tokens with GPT-2's BPE ([[sources/raschka-bpe-from-scratch]]). This efficiency is critical for fitting longer documents into fixed-size context windows.

### BPE vs. Other Algorithms

| Dimension | BPE | [[concepts/wordpiece]] | [[concepts/unigram-tokenization]] |
|-----------|-----|-----------|---------|
| Direction | Bottom-up (merge) | Bottom-up (merge) | Top-down (prune) |
| Selection | Most frequent pair | Most informative pair (likelihood) | Remove tokens with least loss impact |
| Determinism | Deterministic | Deterministic | Probabilistic |
| Used by | GPT, Llama, Gemma | BERT, DistilBERT, Electra | T5, BigBird, Pegasus |

According to [[sources/ali-tokenizer-choice-negligible-crucial]], BPE consistently achieves the highest or near-highest prediction accuracy, especially as vocabulary size increases. The best-performing configuration for English was BPE with SentencePiece at 33k vocabulary (50.81% average across 41 tasks).

### Performance Optimization

Traditional BPE implementations have quadratic worst-case time complexity. [[sources/github-faster-bpe-tokenizer]] describes a breakthrough: using an Aho-Corasick automaton and incremental left-to-right encoding to achieve **linear time complexity**, running 4x faster than [[entities/tiktoken]] and 10x faster than HuggingFace Tokenizers. This matters for production systems processing untrusted input where pathological cases could cause quadratic slowdowns.

### Limitations

- Token boundaries don't respect morpheme boundaries — "racket" might split as "rack"+"et" despite being a single morpheme ([[sources/trott-tokenization-llms]])
- Numbers are tokenized inconsistently — 677 becomes " 6"+"77" while 127 stays whole ([[sources/karpathy-minbpe-lecture]])
- Whitespace changes dramatically affect tokenization but are invisible to users
- Systematically disadvantages low-resource languages with higher fertility ([[concepts/multilingual-tokenization]])

## Sources

- [[sources/raschka-bpe-from-scratch]] — step-by-step implementation tutorial
- [[sources/huggingface-tokenization-algorithms]] — canonical algorithm comparison
- [[sources/karpathy-minbpe-lecture]] — educational lecture building BPE from scratch
- [[sources/github-faster-bpe-tokenizer]] — production-grade linear-time BPE
- [[sources/ali-tokenizer-choice-negligible-crucial]] — empirical performance comparison

## Related Concepts

- [[concepts/tokenization]] — BPE is the most popular tokenization algorithm
- [[concepts/subword-tokenization]] — the paradigm BPE implements
- [[concepts/wordpiece]] — similar bottom-up approach with likelihood-based merging
- [[concepts/unigram-tokenization]] — the opposite top-down approach
- [[concepts/sentencepiece]] — library that can run BPE on raw byte streams
- [[concepts/vocabulary-size-tradeoffs]] — number of BPE merges is a critical hyperparameter
