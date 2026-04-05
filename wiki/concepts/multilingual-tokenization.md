---
title: "Multilingual Tokenization"
type: concept
sources: ["[[sources/kamali-tokenization-killing-multilingual]]", "[[sources/ali-tokenizer-choice-negligible-crucial]]", "[[sources/rohan-paul-vocabulary-size-tradeoffs]]"]
related: ["[[concepts/tokenization]]", "[[concepts/vocabulary-size-tradeoffs]]", "[[concepts/sentencepiece]]", "[[concepts/byte-level-models]]", "[[concepts/byte-pair-encoding]]"]
last_compiled: 2026-04-05
summary: "The structural barrier preventing equitable LLM performance across languages — tokenizers trained on English-heavy corpora create 2-15x token overhead for low-resource languages, wasting context, compute, and model capacity."
---

## Overview

Multilingual tokenization is arguably the single biggest unsolved problem in making LLMs work equitably across the world's languages. Tokenizers trained predominantly on English text systematically disadvantage other languages, especially low-resource ones, by fragmenting their text into far more tokens. This isn't just an efficiency problem — it degrades model quality, wastes context windows, increases costs, and consumes model capacity that should be used for reasoning.

## Key Ideas

### The Fertility Problem

**Fertility** measures the average number of tokens per word. English text tokenized by GPT-style tokenizers typically has fertility near 1.0-1.3. Morphologically rich languages (Turkish, Finnish, Swahili) or languages with different scripts (Arabic, Hindi, Chinese) can have fertility 2-15x higher. This means the same semantic content in a low-resource language uses 2-15x more of the context window.

### The Four Compounding Taxes (Kamali)

[[sources/kamali-tokenization-killing-multilingual]] identifies four taxes that compound on low-resource languages:

1. **Fertility overhead**: More tokens per word wastes context window and compute
2. **Morphological incoherence**: Token boundaries don't respect morphemes, so the model wastes middle-layer capacity reconstructing grammatical structure. Example: Turkish "evlerden" (from the houses = ev+ler+den) split as "ev·lerd·en" destroys both plural and case information
3. **No variant recovery**: Typos, diacritics, and spelling variants become completely unrelated token sequences. In English, models learn to handle variants through co-occurrence; low-resource languages lack the data for this
4. **Capacity spillover**: All the above consume model capacity (context positions, layer depth, embedding dimensions) that should be available for reasoning

### The Runaway Effect

Low-resource languages face a vicious cycle:
- Less training data → worse tokenizer coverage → higher fertility
- Higher fertility → more data needed to compensate
- But collecting more data assumes fixed tokenization overhead that these languages can never afford

"You cannot data-scale your way out of a broken input pipeline."

### Cost Implications

[[sources/ali-tokenizer-choice-negligible-crucial]] quantifies the problem: English-centric tokenizers add **up to 68% additional training cost** for non-English languages. Since most LLM APIs charge per token, users of low-resource languages also pay 2-15x more for equivalent semantic content.

### Proposed Solutions

| Approach | Pros | Cons |
|----------|------|------|
| Per-language tokenizer | Better fertility locally | Destroys cross-lingual alignment |
| Large shared vocabulary (Gemma 250k) | Multilingual coverage | "A much dumber model" — shared budget |
| [[concepts/byte-level-models]] (EvaByte, BLT) | Equal treatment of all scripts | Longer sequences, need new architecture |
| Continuous pre-tokenization layer | Could retrofit existing models | Still research-stage |

### The Intelligence vs. Coverage Trade-off

[[sources/kamali-tokenization-killing-multilingual]] makes a provocative argument: large-vocabulary models (Gemma 250k, Qwen 3.5) achieve multilingual coverage at the cost of raw intelligence. "A 7B model isn't reasoning at 7B capacity — it's spending significant parameters reconstructing tokenization artifacts."

## Sources

- [[sources/kamali-tokenization-killing-multilingual]] — the most thorough critique, identifying four compounding taxes
- [[sources/ali-tokenizer-choice-negligible-crucial]] — 68% cost overhead quantified, vocabulary size recommendations
- [[sources/rohan-paul-vocabulary-size-tradeoffs]] — multilingual vocabulary needs analysis

## Related Concepts

- [[concepts/tokenization]] — the process whose failures create multilingual inequality
- [[concepts/vocabulary-size-tradeoffs]] — larger vocabularies help but aren't sufficient
- [[concepts/sentencepiece]] — the library designed for language-agnostic tokenization
- [[concepts/byte-level-models]] — the most promising long-term solution
- [[concepts/byte-pair-encoding]] — the algorithm whose English bias is the core problem
