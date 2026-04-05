---
title: "BPE vs WordPiece vs Unigram"
type: comparison
subjects: ["[[concepts/byte-pair-encoding]]", "[[concepts/wordpiece]]", "[[concepts/unigram-tokenization]]"]
sources: ["[[sources/huggingface-tokenization-algorithms]]", "[[sources/ali-tokenizer-choice-negligible-crucial]]"]
last_compiled: 2026-04-05
summary: "Side-by-side comparison of the three dominant subword tokenization algorithms — BPE (frequency-based merging), WordPiece (likelihood-based merging), and Unigram (probabilistic pruning)."
---

## Overview

All three algorithms solve the same problem — converting text into a manageable vocabulary of subword tokens — but approach it differently. BPE and WordPiece build vocabularies bottom-up through merging; Unigram builds top-down through pruning. The choice matters: [[sources/ali-tokenizer-choice-negligible-crucial]] found up to 9 percentage points of accuracy difference between the best and worst tokenizer on individual tasks.

## Comparison Table

| Dimension | BPE | WordPiece | Unigram |
|-----------|-----|-----------|---------|
| **Direction** | Bottom-up (merge) | Bottom-up (merge) | Top-down (prune) |
| **Selection criterion** | Most frequent adjacent pair | Most informative pair (maximizes likelihood) | Remove tokens with least loss impact |
| **Determinism** | Deterministic | Deterministic | Probabilistic (multiple valid tokenizations) |
| **Key models** | GPT-2/3/4, Llama, Gemma, Qwen2 | BERT, DistilBERT, Electra | T5, BigBird, Pegasus |
| **Popularity** | #1 in Transformers | #3 (BERT-family only) | #2 in Transformers |
| **Compression** | ~2.5-3 tokens/instruction | ~4.5 tokens/instruction | ~2 tokens/instruction |
| **Accuracy (English, 33k)** | 50.81% (BPE-SP-33) | N/A in study | Lower at this vocab size |
| **Accuracy (multilingual, 100k)** | 41.44% (BPE-SP-100) | N/A in study | Lower at this vocab size |
| **Library** | tiktoken, HF Tokenizers, SentencePiece | HF Tokenizers | SentencePiece, HF Tokenizers |

## Key Differences Explained

### Merge Selection: Frequency vs. Likelihood

BPE simply merges the pair that appears most often. WordPiece uses the formula `score(a,b) = freq(ab) / (freq(a) * freq(b))`, which favors pairs that co-occur more than chance predicts. This means WordPiece prefers *informative* merges — two rare tokens that always appear together get merged before a very common but uninformative pair.

### Deterministic vs. Probabilistic

BPE and WordPiece always produce the same tokenization for a given input. Unigram can tokenize "hugs" as `["hug","s"]`, `["h","ug","s"]`, or `["h","u","g","s"]`, selecting the highest-probability option at inference. During training, this probabilistic nature provides implicit data augmentation — the same text can be tokenized differently in different epochs.

### Build vs. Prune

BPE and WordPiece start with characters and iteratively add new tokens through merging. Unigram starts with a large candidate set (often tens of thousands of substrings) and iteratively removes the least useful ones. This makes Unigram's vocabulary more globally optimized (each remaining token was specifically selected to minimize overall loss), while BPE's vocabulary reflects a greedy sequence of local decisions.

## When to Use Each

- **BPE**: Default choice for most LLM applications. Best empirical accuracy, most widely supported, simplest to understand and debug. Use BPE via [[concepts/sentencepiece]] for best results.
- **WordPiece**: Only if working with BERT-family models. Not commonly used for new models.
- **Unigram**: When better compression matters, when training on multilingual data (often paired with SentencePiece), or when the probabilistic tokenization augmentation effect is desired during training.

## The Surprising Finding

No single algorithm consistently dominates across all tasks and languages. Performance differences are often task-dependent and minor at standard vocabulary sizes. The choice of **library implementation** (SentencePiece vs. HuggingFace) and **vocabulary size** matter at least as much as the algorithm itself ([[sources/ali-tokenizer-choice-negligible-crucial]]).

## Sources

- [[sources/huggingface-tokenization-algorithms]] — canonical algorithm descriptions with worked examples
- [[sources/ali-tokenizer-choice-negligible-crucial]] — empirical performance across 24 models and 41 tasks
