---
title: "Knowledge Circuits in Pretrained Transformers"
source: "https://arxiv.org/html/2405.17969v1"
author: "Yunzhi Yao, Ningyu Zhang et al."
date_published: 2024-05-28
date_ingested: 2026-04-05
tags: [knowledge-storage, MLP-memory, transformer-interpretability, knowledge-circuits, knowledge-editing]
type: paper
status: raw
discovered_via: search
---

# Knowledge Circuits in Pretrained Transformers

## How LLMs Store Knowledge

Knowledge is primarily stored in the Multilayer Perceptrons (MLPs) of Transformer-based language models. These MLPs function as key-value neural memory, with knowledge stored in "knowledge neurons."

### MLP as Key-Value Memory

Large language models store factual knowledge as discrete key-value mappings within MLP parameters. The Feed-Forward layers act as key-value memories: the first linear transformation are keys and the second linear transformation are values.

An encoder MLP exactly maps keys to compressed intermediate values, and a decoder linear layer linearly decompresses the intermediate values.

## Knowledge Circuits Framework

Knowledge circuits trace how factual knowledge flows through transformer layers:

1. **Attention heads** serve as knowledge retrieval mechanisms — they identify relevant context and route information from earlier layers
2. **MLP layers** serve as knowledge storage — they contain the actual factual associations
3. **Knowledge circuits** are the end-to-end paths from input to output that traverse specific attention heads and MLP neurons

## Parameter Specialization

In the final layer of the MLP, each vector in the value matrix can serve as a fundamental unit for storing knowledge. By directly manipulating or disrupting these parameter vectors, specific knowledge can be edited or unlearned.

Fact-storing MLPs can be swapped with another one storing a different fact set, and the transformer immediately outputs the new facts — with no extra training and almost no performance loss.

## Constructing Efficient Fact-Storing MLPs

Research shows factual knowledge can be formalized as discrete maps between key and value embeddings. MLPs can be constructed to efficiently store these mappings, with implications for:
- Knowledge editing (ROME, MEMIT)
- Model compression
- Understanding how scale affects knowledge capacity
- Targeted fact insertion and removal

## Relationship to Knowledge Editing

This understanding of MLP-based knowledge storage directly enables:
- **ROME**: Locates factual knowledge via causal tracing, then makes rank-one edits to MLP weights
- **MEMIT**: Scales ROME to thousands of simultaneous edits
- **Knowledge unlearning**: Disrupting specific MLP value vectors to remove unwanted knowledge

## Attention Heads in Knowledge Retrieval

Attention heads play a complementary role to MLPs:
- They do not store facts themselves but route information to the MLPs that do
- Specific attention head patterns (e.g., "induction heads") are crucial for in-context learning
- Head ablation studies reveal which heads participate in specific knowledge circuits
