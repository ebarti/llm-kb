---
title: "Unigram Tokenization"
type: concept
sources: ["[[sources/huggingface-tokenization-algorithms]]", "[[sources/ali-tokenizer-choice-negligible-crucial]]"]
related: ["[[concepts/subword-tokenization]]", "[[concepts/byte-pair-encoding]]", "[[concepts/wordpiece]]", "[[concepts/sentencepiece]]"]
last_compiled: 2026-04-05
summary: "Top-down probabilistic tokenization algorithm that starts with a large candidate vocabulary and iteratively prunes the least impactful tokens — used by T5, BigBird, and Pegasus."
---

## Overview

Unigram tokenization, proposed by Taku Kudo (2018), takes the opposite approach from [[concepts/byte-pair-encoding]] and [[concepts/wordpiece]]. Instead of starting small and merging upward, Unigram starts with a **large set of candidate subwords** and iteratively removes the tokens whose removal causes the least increase in overall loss. It is the second most popular tokenization algorithm in Transformers, used by T5, BigBird, Pegasus, and more.

## Key Ideas

### The Algorithm

1. **Initialize**: Start with a large set of candidate subwords (all characters, common substrings, etc.), each assigned a probability based on corpus frequency
2. **Score**: Measure how well the current vocabulary tokenizes the training data (total log-likelihood)
3. **Prune**: For each token, compute how much the loss would increase if that token were removed. Remove the bottom 10-20% (those whose removal hurts least). Base characters always remain.
4. **Repeat**: Continue until reaching the target vocabulary size

### Probabilistic Tokenization

Unlike BPE (which is deterministic — always applying the same merge rules), Unigram can tokenize a word in multiple ways. "hugs" could become `["hug", "s"]`, `["h", "ug", "s"]`, or `["h", "u", "g", "s"]`. Unigram picks the **highest probability** tokenization at inference but can sample different tokenizations during training. This probabilistic nature provides a form of data augmentation.

### Compression Efficiency

Benchmarks show Unigram achieves better compression than BPE — averaging about 2 tokens per instruction vs. BPE's 2.5-3. However, this compression advantage doesn't always translate to better downstream task performance.

### Empirical Performance

[[sources/ali-tokenizer-choice-negligible-crucial]] found no single algorithm consistently dominates. BPE tends to achieve slightly higher accuracy as vocabulary size increases, while Unigram provides better compression. Performance differences are often task-dependent.

## Sources

- [[sources/huggingface-tokenization-algorithms]] — algorithm walkthrough with worked examples
- [[sources/ali-tokenizer-choice-negligible-crucial]] — empirical comparison across 24 models

## Related Concepts

- [[concepts/byte-pair-encoding]] — the bottom-up frequency-based alternative
- [[concepts/wordpiece]] — another bottom-up approach (likelihood-based)
- [[concepts/sentencepiece]] — library that implements Unigram alongside BPE
- [[concepts/subword-tokenization]] — the paradigm Unigram implements
