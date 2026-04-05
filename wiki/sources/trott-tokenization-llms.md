---
title: "Source: Tokenization in Large Language Models"
type: source-summary
source: "[[raw/trott-tokenization-llms]]"
related: ["[[concepts/tokenization]]", "[[concepts/subword-tokenization]]", "[[concepts/byte-pair-encoding]]"]
last_compiled: 2026-04-05
summary: "Sean Trott explains how LLMs process tokens (not words), the disconnect between subword tokens and morphemes, and mixed research findings on morphological tokenization's impact on performance."
---

## Key Points

- LLMs predict tokens, not words — tokenization determines what linguistic units the model actually works with
- Subword tokens don't necessarily align with morphemes: "racket" → "rack"+"##et" (one morpheme, two tokens) vs. "dogs" (two morphemes, one token)
- Research on morphological tokenization impact is mixed: no effect on Spanish agreement tasks, but "alien tokenization leads to poorer generalizations" across BERT/RoBERTa/DeBERTa
- Despite tokens being opaque identifiers, models develop implicit character knowledge — GPT-J embeddings identify character presence with 80% accuracy
- Languages with richer inflectional morphology show different BPE learning patterns than analytic languages

## Detailed Summary

Trott provides an accessible overview of how [[concepts/tokenization]] works in modern LLMs, contrasting word-based (huge vocabulary, unknown token problem), character-based (tiny vocabulary, long sequences), and [[concepts/subword-tokenization]] (the modern hybrid). The most insightful section examines the disconnect between subword tokens and linguistic morphemes. While intuitively we'd want token boundaries to align with meaningful units, BPE splits are frequency-driven and often linguistically arbitrary. Research findings on whether this matters are mixed, suggesting the impact may be task- and language-dependent. An interesting finding: models develop implicit character-level knowledge despite never explicitly seeing characters, likely through learning relationships between different tokenizations of the same root word.

## Related Concepts

- [[concepts/tokenization]] — the core process explained accessibly
- [[concepts/subword-tokenization]] — the modern approach analyzed
- [[concepts/byte-pair-encoding]] — primary algorithm discussed
- [[concepts/multilingual-tokenization]] — cross-language implications noted
