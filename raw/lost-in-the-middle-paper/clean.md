---
title: "Lost in the Middle: How Language Models Use Long Contexts"
source: "https://arxiv.org/abs/2307.03172"
author: "Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang"
date_published: 2023-07-06
date_ingested: 2026-04-05
tags: [lost-in-the-middle, context-windows, attention, position-bias, evaluation]
type: paper
status: raw
discovered_via: search
---

# Lost in the Middle: How Language Models Use Long Contexts

## Key Findings

Language models struggle to effectively utilize information positioned in the middle of long contexts. The paper documents a **U-shaped performance curve**: models perform best when relevant information appears at the beginning or end of input sequences, with significant degradation when accessing middle content.

- Performance can degrade by **more than 30%** when relevant information shifts from start/end to middle positions.
- Even models explicitly designed for long-context processing exhibit this vulnerability.

## Why It Happens

1. **Attention accumulation**: Tokens at the beginning get attended to by every subsequent token. Token #1 is visible to tokens #2, #3... all the way to the end. Token #500 in the middle is only visible to tokens #501 onward. Earlier tokens accumulate more attention weight simply because they have more opportunities to be attended to.

2. **Task framing vs. fact retrieval**: The model uses context primarily to figure out what kind of task is being requested. Information at the beginning and end acts as strong signals for task identification, while middle content gets lost in the noise.

## Methodology

Two evaluation tasks:
- **Multi-document question answering**: Relevant document placed at various positions among distractor documents.
- **Key-value retrieval**: Specific key-value pairs placed at different positions within a list.

Both tasks require identifying and using relevant information from extended input contexts.

## Implications

- Establishes evaluation protocols for assessing future long-context language models.
- Suggests fundamental limitations in how current transformer architectures handle extended sequences.
- Motivates strategic ordering of retrieved documents in RAG systems.

## Solutions Developed

- **Strategic document ordering**: Position most relevant content at beginning/end of context.
- **Multi-scale Positional Encoding (Ms-PoE)**: Plug-and-play approach enhancing middle-context capacity without fine-tuning.
- **Reranking models**: Position most relevant content at optimal locations within the context window.

## Publication

Stanford, UC Berkeley, Samaya AI. Accepted TACL 2023. 18 pages, 16 figures.
