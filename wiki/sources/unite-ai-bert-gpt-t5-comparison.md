---
title: "Source: NLP Rise with Transformer Models — T5, BERT, GPT Comparison"
type: source-summary
source: "[[raw/unite-ai-bert-gpt-t5-comparison]]"
related: ["[[concepts/transformer-architecture]]", "[[entities/bert]]", "[[entities/gpt]]", "[[entities/t5]]", "[[comparisons/encoder-only-vs-decoder-only-vs-encoder-decoder]]"]
last_compiled: 2026-04-05
summary: "Comprehensive comparison of the three transformer variant families: BERT (encoder-only, bidirectional MLM), GPT (decoder-only, causal LM), T5 (encoder-decoder, text-to-text denoising) — covering architecture, training, tokenization, and use cases."
---

## Key Points

- BERT: encoder-only, bidirectional, Masked Language Modeling + Next Sentence Prediction
- GPT: decoder-only, unidirectional, Causal Language Modeling
- T5: encoder-decoder, text-to-text framework, span denoising objective
- BERT uses WordPiece (30K tokens), GPT uses BPE (175K for GPT-3), T5 uses SentencePiece
- BERT: absolute positional encodings; GPT: absolute; T5: relative position biases
- BERT cannot generate free-form text; GPT specializes in generation; T5 handles all tasks uniformly

## Detailed Summary

This source provides a clean three-way comparison of the dominant [[concepts/transformer-architecture]] variants. The architectural choice (encoder-only, decoder-only, encoder-decoder) determines the model's capabilities and optimal use cases.

[[entities/bert]] (2018) processes the full input bidirectionally, making it excellent for understanding tasks (classification, NER, QA) but incapable of generation. [[entities/gpt]] processes left-to-right, making it the dominant architecture for text generation — this decoder-only approach now powers virtually all frontier LLMs. [[entities/t5]] (2019) uses the full encoder-decoder and converts every NLP task into text-to-text format, providing maximum flexibility but at higher parameter cost.

The training objectives differ fundamentally: BERT masks random tokens and predicts them (MLM), GPT predicts the next token given all previous tokens (CLM), and T5 replaces spans of tokens with sentinels and predicts the original spans.

## Related Concepts

- [[concepts/transformer-architecture]] — the shared foundation
- [[concepts/self-attention]] — used differently in each variant
- [[concepts/causal-attention]] — GPT's masked attention
- [[comparisons/encoder-only-vs-decoder-only-vs-encoder-decoder]] — the comparison this enables
