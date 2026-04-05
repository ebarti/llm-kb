---
title: "Lost in the Middle (Paper)"
type: entity
entity_type: paper
sources: ["[[sources/lost-in-the-middle-paper]]"]
related: ["[[concepts/lost-in-the-middle]]", "[[concepts/context-windows]]", "[[concepts/needle-in-a-haystack]]"]
last_compiled: 2026-04-05
summary: "Liu et al. (Stanford/UC Berkeley, TACL 2023): landmark paper documenting the U-shaped performance curve where LLMs perform best on beginning/end information and >30% worse on middle-positioned content."
---

## Overview

"Lost in the Middle: How Language Models Use Long Contexts" is a landmark paper by Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang, published at TACL in 2023.

## Key Contribution

The paper established the **U-shaped performance curve** as a fundamental characteristic of transformer-based language models: performance is highest when relevant information appears at the beginning or end of context, with more than 30% degradation for middle-positioned content.

## Methodology

- **Tasks**: Multi-document question answering and key-value retrieval
- **Variables**: Position of relevant information (beginning to end), context length
- **Models tested**: Multiple LLMs including those designed for long-context processing

## Impact

- Cited extensively in RAG system design (motivating document reranking)
- Inspired Multi-scale Positional Encoding (Ms-PoE) as a mitigation
- Established evaluation protocols for future long-context models
- Fundamentally changed how practitioners structure context for LLM applications

## Publication

- **arXiv**: 2307.03172
- **Venue**: Transactions of the Association for Computational Linguistics (TACL), 2023
- **Institutions**: Stanford, UC Berkeley, Samaya AI
- 18 pages, 16 figures

## Mentioned In

- [[sources/lost-in-the-middle-paper]] — full source summary
