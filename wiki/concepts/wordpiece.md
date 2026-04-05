---
title: "WordPiece"
type: concept
sources: ["[[sources/huggingface-tokenization-algorithms]]"]
related: ["[[concepts/subword-tokenization]]", "[[concepts/byte-pair-encoding]]", "[[concepts/tokenization]]"]
last_compiled: 2026-04-05
summary: "BERT-family tokenization algorithm similar to BPE but merging token pairs that maximize training data likelihood rather than simple frequency — producing more linguistically informative merges."
---

## Overview

WordPiece is the tokenization algorithm used by BERT and its derivatives (DistilBERT, Electra, etc.). Developed at Google, it is structurally similar to [[concepts/byte-pair-encoding]] — both are bottom-up algorithms that iteratively merge character/subword pairs — but they differ in **how pairs are selected for merging**.

## Key Ideas

### Merge Selection: Frequency vs. Likelihood

BPE merges whichever pair appears most frequently. WordPiece merges the pair that **maximizes the likelihood of the training data**, using the scoring formula:

```
score(a, b) = frequency(ab) / (frequency(a) * frequency(b))
```

This favors merging tokens that appear together far more often than chance would predict. For example, if "g" and "s" co-occur more than their individual frequencies predict, they get merged before a more frequent but less informative pair.

### Practical Difference

The likelihood-based scoring means WordPiece prefers merges where the combination carries more information than the individual parts. BPE might merge a very common pair even if both parts appear frequently on their own. WordPiece surfaces more surprising, informative co-occurrences first.

### Prefix Notation

WordPiece tokens that continue a word (rather than starting one) are marked with `##`. For example, "tokenization" might become `["token", "##ization"]`. This distinguishes word-initial from word-internal subwords.

### Performance

In benchmarks from [[sources/ali-tokenizer-choice-negligible-crucial]], WordPiece generally follows BPE with solid but slightly lower performance, producing about 4.5 tokens per instruction vs. BPE's 2.5-3 (higher fertility).

## Sources

- [[sources/huggingface-tokenization-algorithms]] — canonical description with worked examples and scoring formula

## Related Concepts

- [[concepts/byte-pair-encoding]] — the frequency-based alternative WordPiece improves upon
- [[concepts/subword-tokenization]] — the paradigm both algorithms implement
- [[concepts/unigram-tokenization]] — the top-down alternative
- [[concepts/tokenization]] — broader context
