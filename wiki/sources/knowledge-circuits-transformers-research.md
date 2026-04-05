---
title: "Source: Knowledge Circuits in Pretrained Transformers"
type: source-summary
source: "[[raw/knowledge-circuits-transformers-research]]"
related: ["[[concepts/knowledge-storage-in-transformers]]", "[[concepts/knowledge-editing]]", "[[concepts/attention-mechanisms]]", "[[entities/rome-memit]]"]
tags: [knowledge-circuits, MLP-memory, transformer-interpretability, knowledge-editing]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "NeurIPS 2024 paper introducing Knowledge Circuits: tracing how factual knowledge flows through transformer layers — attention heads route information while MLP layers store facts as key-value memories, enabling surgical fact editing and swapping."
---

## Key Points

- Knowledge is primarily stored in MLP layers, which function as key-value neural memory
- Feed-Forward layers: first linear transformation = keys, second linear transformation = values
- Attention heads serve as retrieval/routing mechanisms, not storage — they identify relevant context
- Knowledge circuits are end-to-end paths from input to output traversing specific attention heads and MLP neurons
- MLP value vectors serve as fundamental units of knowledge storage
- Fact-storing MLPs can be swapped between models with no extra training and almost no performance loss
- Directly enables ROME (rank-one editing) and MEMIT (thousands of simultaneous edits)

## Detailed Summary

This NeurIPS 2024 paper by Yao, Zhang et al. introduces a framework for understanding how transformer-based LLMs store and retrieve factual knowledge. The central finding is a **division of labor** between attention and MLP layers:

**Attention heads** act as the **retrieval and routing** system. When a model processes a factual query like "The capital of France is ___", specific attention heads in middle layers identify the relevant entity ("France") and route that information to the appropriate MLP layers. Head ablation studies reveal that disabling specific attention heads disrupts specific knowledge circuits without affecting unrelated facts.

**MLP layers** act as the **storage** system. The Feed-Forward Network in each transformer layer operates as a key-value memory: the first linear projection maps inputs to keys, and the second projection maps keys to values. Each column in the value weight matrix can be thought of as storing a specific piece of knowledge.

The most striking finding is that **fact-storing MLPs are modular and swappable**. Researchers constructed minimal MLPs encoding specific fact sets, inserted them into transformer models replacing the original MLPs, and the models immediately produced the new facts with no fine-tuning and minimal performance degradation on unrelated tasks. This demonstrates that factual knowledge storage is highly localized and modular within the transformer architecture.

This understanding directly enables knowledge editing methods like [[entities/rome-memit]]: ROME uses causal tracing to identify which MLP layers store a specific fact, then makes a rank-one edit to the weight matrix to change that fact.

## Concepts Introduced or Discussed

- [[concepts/knowledge-storage-in-transformers]] — the core topic
- [[concepts/knowledge-editing]] — enabled by understanding knowledge circuits
- [[concepts/attention-mechanisms]] — attention's role as information router
- [[concepts/self-attention]] — the specific mechanism routing knowledge

## Metadata

- **Author**: Yunzhi Yao, Ningyu Zhang et al.
- **Date Published**: 2024-05-28
- **Format**: paper (NeurIPS 2024)
- **URL**: https://arxiv.org/abs/2405.17969
