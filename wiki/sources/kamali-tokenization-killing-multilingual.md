---
title: "Source: Tokenization is Killing our Multilingual LLM Dream"
type: source-summary
source: "[[raw/kamali-tokenization-killing-multilingual]]"
related: ["[[concepts/multilingual-tokenization]]", "[[concepts/tokenization]]", "[[concepts/vocabulary-size-tradeoffs]]", "[[concepts/byte-level-models]]"]
last_compiled: 2026-04-05
summary: "Omar Kamali argues tokenization is the structural barrier preventing true multilingual LLMs, identifying four compounding 'taxes' on low-resource languages and proposing a continuous pre-tokenization layer."
---

## Key Points

- Poor tokenization systematically disadvantages low-resource languages through four compounding taxes: fertility overhead, morphological incoherence, no variant recovery, capacity spillover
- Custom per-language tokenizers destroy cross-lingual alignment and don't scale
- Fertility and compression ratio are insufficient evaluation metrics — morphological consistency F1 is more predictive
- Large vocabularies (Gemma 250k, Qwen 3.5) achieve coverage at the cost of model intelligence — "a much dumber model"
- A 7B model isn't reasoning at 7B capacity; significant parameters reconstruct tokenization artifacts
- Low-resource languages face a runaway effect: less data → worse tokenization → more data needed → but can't afford the overhead
- Proposes a continuous pre-tokenization layer mapping discrete tokens to smooth representation space

## Detailed Summary

Kamali presents the most thorough critique of [[concepts/multilingual-tokenization]] challenges. The core argument: when morphemes are split arbitrarily, the model wastes middle-layer capacity on reconstructing meaning rather than reasoning. He identifies four compounding taxes: (1) fertility overhead wastes context window, (2) morphological incoherence forces structural reconstruction, (3) no variant recovery means typos/diacritics create unrelated token sequences, and (4) capacity spillover means low-resource languages get systematically less reasoning capacity. The Turkish example ("evlerden" = ev+ler+den) illustrates how a bad tokenizer destroys grammatical information. Current solutions like [[concepts/byte-level-models]] require training from scratch. The proposed solution is a continuous pre-tokenization layer inspired by vision encoders — "the most robust tokenizer in production today might be a JPEG encoder."

## Notable Quotes

> "The tokenizer sets the morphological reconstruction bill. The middle layers pay it out of a shared budget."
> "You cannot data-scale your way out of a broken input pipeline."

## Related Concepts

- [[concepts/multilingual-tokenization]] — the core problem analyzed
- [[concepts/byte-level-models]] — one proposed solution (incomplete)
- [[concepts/vocabulary-size-tradeoffs]] — large vocab vs. model intelligence
- [[concepts/tokenization]] — fundamental process under critique
