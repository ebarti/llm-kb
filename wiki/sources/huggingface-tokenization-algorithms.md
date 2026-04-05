---
title: "Source: Tokenization Algorithms — Hugging Face"
type: source-summary
source: "[[raw/huggingface-tokenization-algorithms]]"
related: ["[[concepts/byte-pair-encoding]]", "[[concepts/wordpiece]]", "[[concepts/unigram-tokenization]]", "[[concepts/sentencepiece]]", "[[concepts/subword-tokenization]]"]
last_compiled: 2026-04-05
summary: "Hugging Face's authoritative reference comparing BPE, WordPiece, Unigram, and SentencePiece tokenization algorithms with worked examples and model-to-algorithm mappings."
---

## Key Points

- Transformers support three subword algorithms: BPE, Unigram, and WordPiece
- BPE is the most popular (Llama, Gemma, Qwen2); Unigram is second (T5, BigBird, Pegasus); WordPiece is BERT-family
- BPE merges the most frequent adjacent pair; WordPiece merges the most informative pair (maximizing likelihood); Unigram starts large and prunes low-impact tokens
- Byte-level BPE uses 256 byte values as base vocabulary, eliminating unknown tokens entirely
- SentencePiece treats input as a raw byte stream, handling languages without whitespace (Chinese, Japanese)
- GPT-2 vocabulary: 50,257 tokens (256 bytes + 50,000 merges + end-of-text token)

## Detailed Summary

This Hugging Face documentation page provides the canonical comparison of tokenization algorithms used in transformer models. It walks through worked examples showing how BPE builds vocabulary through iterative greedy merging, how WordPiece uses a likelihood-based scoring formula `score(a,b) = freq(ab) / (freq(a) * freq(b))` to select more informative merges, and how Unigram takes the opposite approach — starting with a large candidate set and iteratively removing the tokens whose removal least increases the overall loss. [[concepts/sentencepiece]] is presented as a library wrapper that applies BPE or Unigram directly on raw text, critical for languages like Chinese and Japanese that lack whitespace word boundaries. The document also contrasts word-level tokenization (huge vocabulary, unknown token problem) with character-level (tiny vocabulary, long sequences, weak semantics).

## Related Concepts

- [[concepts/byte-pair-encoding]] — most popular algorithm, used by GPT/Llama/Gemma
- [[concepts/wordpiece]] — BERT-family algorithm, likelihood-based merging
- [[concepts/unigram-tokenization]] — probabilistic top-down pruning approach
- [[concepts/sentencepiece]] — language-agnostic tokenization library
- [[concepts/subword-tokenization]] — the paradigm all three algorithms implement
