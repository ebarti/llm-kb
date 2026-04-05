---
title: "Subword Tokenization"
type: concept
sources: ["[[sources/huggingface-tokenization-algorithms]]", "[[sources/trott-tokenization-llms]]", "[[sources/ali-tokenizer-choice-negligible-crucial]]"]
related: ["[[concepts/tokenization]]", "[[concepts/byte-pair-encoding]]", "[[concepts/wordpiece]]", "[[concepts/unigram-tokenization]]", "[[concepts/sentencepiece]]", "[[concepts/byte-level-models]]"]
last_compiled: 2026-04-05
summary: "The dominant tokenization paradigm for modern LLMs — splitting text into units between words and characters, keeping frequent words intact while decomposing rare words into meaningful subword pieces."
---

## Overview

Subword tokenization is the standard approach used by virtually all modern large language models. It occupies the sweet spot between word-level tokenization (huge vocabulary, OOV problems) and character-level tokenization (tiny vocabulary, very long sequences, weak semantics). Common words remain intact as single tokens, while rare or novel words decompose into shorter subword pieces that the model has seen in other contexts.

For example, "annoyingly" might tokenize as `["annoying", "ly"]` or `["annoy", "ing", "ly"]` depending on the learned vocabulary. The word "unaffordable" might become `["un", "afford", "able"]`, allowing the model to leverage its understanding of each component.

## Key Ideas

### The Three Algorithms

Modern transformers use three subword tokenization algorithms:

1. **[[concepts/byte-pair-encoding]]** (BPE) — The most popular. Iteratively merges the most frequent adjacent pair. Bottom-up, deterministic, greedy. Used by GPT, Llama, Gemma, Qwen2.

2. **[[concepts/wordpiece]]** — Similar to BPE but merges the most *informative* pair (maximizing training data likelihood rather than raw frequency). Used by BERT, DistilBERT, Electra.

3. **[[concepts/unigram-tokenization]]** — The opposite direction: starts with a large candidate vocabulary and iteratively prunes tokens whose removal least increases the overall loss. Probabilistic — can sample different tokenizations during training. Used by T5, BigBird, Pegasus.

### Subwords vs. Morphemes

A critical insight from [[sources/trott-tokenization-llms]]: subword tokens are frequency-driven and **do not necessarily align with linguistic morphemes**. The word "racket" (one morpheme) might tokenize as "rack"+"##et" (two tokens), while "dogs" (two morphemes: dog+s) might stay as one token. This mismatch is a fundamental limitation — the model's atomic units don't correspond to meaningful linguistic units.

Research on whether morphological alignment matters for performance is mixed. Some studies show no impact on agreement tasks, while others find "alien tokenization leads to poorer generalizations" across multiple architectures.

### Why Subword Beats Alternatives

| Approach | Vocabulary Size | Sequence Length | OOV Handling | Semantics |
|----------|----------------|-----------------|--------------|-----------|
| Word-level | Very large (~500k+) | Short | Poor (unknown tokens) | Strong per token |
| Character-level | Tiny (~256) | Very long | Perfect | Weak per token |
| **Subword** | **Moderate (32k-128k)** | **Medium** | **Good (subword fallback)** | **Good** |

### The Pre-tokenization Step

Before subword splitting, most tokenizers apply a pre-tokenization step that splits text on whitespace and/or punctuation to produce word-level chunks. BPE and WordPiece then operate within these chunks. [[concepts/sentencepiece]] is notable for skipping this step entirely, treating input as a raw stream — critical for languages like Chinese and Japanese that don't use whitespace.

### Empirical Performance Comparison

[[sources/ali-tokenizer-choice-negligible-crucial]] tested BPE and Unigram across 24 models and 41 tasks. No single algorithm consistently dominates across all tasks and languages. BPE tends to achieve the highest accuracy as vocabulary size increases, while Unigram averages about 2 tokens per instruction vs. BPE's 2.5-3 (better compression). Performance differences are often task-dependent and minor among leading methods at standard vocabulary sizes.

## Sources

- [[sources/huggingface-tokenization-algorithms]] — canonical comparison with worked examples
- [[sources/trott-tokenization-llms]] — subword-morpheme disconnect analysis
- [[sources/ali-tokenizer-choice-negligible-crucial]] — empirical performance across 24 models

## Related Concepts

- [[concepts/tokenization]] — subword tokenization is the dominant paradigm
- [[concepts/byte-pair-encoding]] — most popular subword algorithm
- [[concepts/wordpiece]] — BERT-family variant
- [[concepts/unigram-tokenization]] — probabilistic alternative
- [[concepts/sentencepiece]] — language-agnostic implementation
- [[concepts/byte-level-models]] — the emerging alternative that eliminates subword tokenization entirely
