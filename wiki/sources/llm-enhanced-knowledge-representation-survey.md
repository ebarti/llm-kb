---
title: "Source: LLM-Enhanced Knowledge Representation Learning Survey"
type: source-summary
source: "[[raw/llm-enhanced-knowledge-representation-survey]]"
related: ["[[concepts/knowledge-representation]]", "[[concepts/knowledge-graph]]", "[[concepts/neural-symbolic-integration]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "2024 survey taxonomizing how LLMs enhance knowledge graph embeddings through encoder-based, encoder-decoder, and decoder-based methods — bridging symbolic KG structure with neural semantic richness."
---

## Key Points
- Classical KG embeddings (TransE, RESCAL) modeled only structural information
- LLMs address KG sparseness by incorporating textual semantics alongside graph structure
- Three-part taxonomy: encoder-based (BERT), encoder-decoder (T5/BART), decoder-based (LLaMA/GPT-4)
- Trend: shift from encoder-only to generative decoder-based approaches (2023-2024)
- LLM-enhanced methods excel on zero-shot and low-resource scenarios
- Demonstrates symbolic KGs and neural LLMs as complementary

## Detailed Summary

This survey catalogs how Large Language Models enhance Knowledge Representation Learning (KRL) — the task of projecting [[concepts/knowledge-graph]] entities and relations into vector spaces while preserving semantic meaning.

The classical era used purely structural methods: TransE (translation-based), RESCAL (tensor decomposition), and similar approaches that modeled only graph topology. These suffered from information sparsity, especially for rare entities.

The LLM era introduces three approach families:

**Encoder-based** (BERT, RoBERTa): KG-BERT treats triples as text sequences. StAR separates head+relation from tail for scoring. KEPLER uses entity descriptions to mitigate frequency bias, achieving 76.20% F1 on entity typing.

**Encoder-decoder** (T5, BART): GenKGC uses relation-guided demonstrations. KGT5 balances link prediction with QA tasks through a unified Seq2Seq architecture.

**Decoder-based** (LLaMA, GPT-4): The newest trend. Methods include description generation (enriching triplets via prompts), prompt engineering (formulating KG tasks as natural language QA), and structural fine-tuning (KoPA's prefix adapters integrating graph embeddings).

The key trend: early dominance of encoder-based architectures gave way to growing encoder-decoder adoption, with decoder-based LLMs emerging strongly in 2023-2024. This signals a shift toward leveraging generative and reasoning capabilities rather than just encoding.

The survey's conclusion underscores that symbolic KGs provide structure while LLMs provide semantic richness — joint approaches address the "information sparsity" limitation through textual entity descriptions and relation-aware prompting.

## Related Concepts
- [[concepts/knowledge-representation]] — the foundational field
- [[concepts/knowledge-graph]] — the structured substrate being enhanced
- [[concepts/neural-symbolic-integration]] — the broader paradigm
- [[concepts/llm-knowledge-base]] — practical application of LLM+structure
