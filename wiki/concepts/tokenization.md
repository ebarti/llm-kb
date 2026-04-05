---
title: "Tokenization"
type: concept
sources: ["[[sources/raschka-bpe-from-scratch]]", "[[sources/huggingface-tokenization-algorithms]]", "[[sources/trott-tokenization-llms]]", "[[sources/karpathy-minbpe-lecture]]", "[[sources/winder-token-count-practical-guide]]", "[[sources/ali-tokenizer-choice-negligible-crucial]]"]
related: ["[[concepts/subword-tokenization]]", "[[concepts/byte-pair-encoding]]", "[[concepts/vocabulary-size-tradeoffs]]", "[[concepts/multilingual-tokenization]]", "[[concepts/byte-level-models]]", "[[concepts/token-counting]]", "[[concepts/llm-pretraining]]", "[[concepts/next-token-prediction]]", "[[concepts/pretraining-data-pipeline]]"]
last_compiled: 2026-04-05
summary: "The process of converting raw text into discrete integer tokens that LLMs can process — the fundamental first step in all language model pipelines."
---

## Overview

Tokenization is the process of converting raw text into a sequence of discrete integer tokens that a language model can process. It is the very first step in any LLM pipeline — before attention, before embeddings, before any neural computation. As [[entities/andrej-karpathy]] emphasizes, many apparent LLM limitations (spelling failures, arithmetic struggles, poor multilingual performance) actually trace back to tokenization rather than the neural architecture itself.

Modern LLMs predict **tokens**, not words. The choice of tokenization strategy determines what linguistic units the model learns to handle, directly impacting its capabilities, costs, and failure modes.

## Key Ideas

### The Three Paradigms

1. **Word-level tokenization**: Split on whitespace/punctuation. Produces huge vocabularies (every unique word form gets its own ID), suffers from out-of-vocabulary (OOV) problems, and cannot handle novel words. Largely abandoned for LLMs.

2. **Character-level tokenization**: Each character is a token. Tiny vocabulary, no OOV problem, but sequences become very long and individual characters carry little semantic meaning. A single character like "l" carries far less meaning than the word "love."

3. **[[concepts/subword-tokenization]]**: The modern standard. Frequent words stay intact as single tokens; rare words decompose into meaningful subword pieces. Balances vocabulary size, sequence length, and coverage. Includes [[concepts/byte-pair-encoding]], [[concepts/wordpiece]], and [[concepts/unigram-tokenization]].

### Why Tokenization Matters

- **Context window efficiency**: Poor tokenization fragments text into more tokens, wasting precious context window space. A text that takes 500 tokens with one tokenizer might take 800 with another.
- **Computational cost**: Transformer attention scales quadratically with sequence length. Fewer tokens = faster training and inference.
- **Model capabilities**: [[sources/karpathy-minbpe-lecture]] catalogs LLM problems caused by tokenization — spelling errors, string reversal failures, arithmetic inconsistencies, and poor non-English performance all trace back to how text is split into tokens.
- **API costs**: Commercial LLMs charge per token. A model producing 20% fewer tokens for equivalent output reduces costs proportionally.
- **Multilingual fairness**: English text is tokenized 2-15x more efficiently than many other languages, creating systematic disadvantage (see [[concepts/multilingual-tokenization]]).

### The Tokenization Pipeline

1. **Pre-tokenization**: Split raw text on whitespace, punctuation, or other rules to produce word-level chunks
2. **Subword splitting**: Apply BPE/WordPiece/Unigram to break words into subword tokens
3. **Special token insertion**: Add model-specific tokens like `<|endoftext|>`, `[CLS]`, `[SEP]`
4. **ID mapping**: Convert token strings to integer IDs via the vocabulary lookup table

### Tokenization vs. Traditional NLP Preprocessing

Modern LLMs have largely eliminated the traditional NLP preprocessing pipeline. Stemming, lemmatization, stopword removal, and lowercasing — all standard in classical NLP — are unnecessary and often harmful for LLMs. [[concepts/subword-tokenization]] and learned embeddings handle what these manual steps used to do. As one analysis notes: "Modern language models increasingly treat preprocessing as a learned component rather than a fixed pipeline."

### The Ideal: Eliminating Tokenization

[[entities/andrej-karpathy]] suggests tokenization should ideally be eliminated entirely. [[concepts/byte-level-models]] like [[entities/evabyte]] and the Byte Latent Transformer are making this increasingly viable, processing raw UTF-8 bytes instead of subword tokens. The trade-off is longer sequences (3.8x on average), which requires architectural innovations to remain efficient.

## Sources

- [[sources/raschka-bpe-from-scratch]] — hands-on BPE implementation tutorial
- [[sources/huggingface-tokenization-algorithms]] — canonical comparison of BPE, WordPiece, Unigram
- [[sources/trott-tokenization-llms]] — accessible overview of tokenization's impact on LLM behavior
- [[sources/karpathy-minbpe-lecture]] — LLM problems traced back to tokenization
- [[sources/winder-token-count-practical-guide]] — practical token counting and cost management
- [[sources/ali-tokenizer-choice-negligible-crucial]] — empirical proof that tokenizer choice is crucial

## Related Concepts

- [[concepts/subword-tokenization]] — the dominant modern approach
- [[concepts/byte-pair-encoding]] — the most popular subword algorithm
- [[concepts/vocabulary-size-tradeoffs]] — how vocabulary size affects everything
- [[concepts/multilingual-tokenization]] — tokenization's unfairness across languages
- [[concepts/byte-level-models]] — the tokenization-free future
- [[concepts/token-counting]] — practical token management for API usage
