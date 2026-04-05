---
title: "Tokenization Algorithms — Hugging Face Transformers Documentation"
source: "https://huggingface.co/docs/transformers/tokenizer_summary"
author: "Hugging Face"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [tokenization, bpe, wordpiece, unigram, sentencepiece, comparison]
type: article
status: raw
discovered_via: search
---

# Tokenization Algorithms

Transformers support three subword tokenization algorithms: Byte pair encoding (BPE), Unigram, and WordPiece. They split text into units between words and characters, keeping the vocabulary compact while still capturing meaningful pieces. Common words stay intact as single tokens, and rare or unknown words decompose into subwords.

For instance, `annoyingly` might be split into `["annoying", "ly"]` or `["annoy", "ing", "ly"]` depending on the vocabulary.

## Byte Pair Encoding (BPE)

BPE is the most popular tokenization algorithm in Transformers, used by models like Llama, Gemma, Qwen2, and more.

1. A pre-tokenizer splits text on whitespace or other rules, producing a set of unique words and their frequencies.
2. The BPE algorithm creates a base vocabulary from all the characters.
3. BPE starts with individual characters and iteratively merges the most frequent adjacent pair.
4. The process continues learning merge rules until it reaches the target vocabulary size (base vocabulary size + number of merges).

GPT uses BPE with a vocabulary size of 40,478 (478 base tokens + 40,000 merges).

### Byte-Level BPE

Including all Unicode characters would make the base vocabulary enormous. Byte-level BPE uses 256 byte values as the base vocabulary instead, ensuring every word can be tokenized without the unknown token. GPT-2 uses byte-level BPE with a vocabulary size of 50,257 (256 byte tokens + 50,000 merges + special end-of-text token).

## Unigram

Unigram is the second most popular tokenization algorithm in Transformers, used by models like T5, BigBird, Pegasus, and more.

1. Unigram starts with a large set of candidate subwords, each with a probability score based on frequency.
2. At each step, Unigram scores how well the current vocabulary tokenizes training data.
3. For every token, Unigram measures how much removing the token would increase the overall loss.
4. Tokens with the lowest loss increase (bottom 10-20%) are removed. Base characters always remain.
5. Steps repeat until the vocabulary reaches target size.

During inference, Unigram can tokenize a word in several ways and picks the highest probability tokenization. Unlike BPE, which is deterministic, Unigram is probabilistic and can sample different tokenizations during training.

## SentencePiece

SentencePiece is a tokenization library that applies BPE or Unigram directly on raw text. Standard BPE and Unigram assume whitespace separates words, which doesn't work for languages like Chinese and Japanese that don't use spaces.

SentencePiece treats the input text as a raw byte or character stream and includes the space character, represented as "▁", in the vocabulary.

## WordPiece

WordPiece is the tokenization algorithm for BERT-family models like DistilBERT and Electra. It's similar to BPE and iteratively merges pairs from the bottom up, but differs in how it selects pairs.

WordPiece merges pairs that maximize the likelihood of the training data:

```
score("u", "g") = frequency("ug") / (frequency("u") × frequency("g"))
```

BPE simply merges whichever pair appears the most. WordPiece measures how *informative* each merge is. Two tokens that appear together far more than chance predicts get merged first.

## Word-Level Tokenization

Vocabulary size becomes extremely large because every unique word requires its own token. The resulting embedding matrix is enormous. Words not in the vocabulary map to an unknown token.

## Character-Level Tokenization

The vocabulary is small and every word can be represented, so there's no unknown token problem. But sequences become much longer. A character like "l" carries far less meaning than "love", so performance suffers.
