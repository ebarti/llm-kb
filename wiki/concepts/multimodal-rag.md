---
title: "Multimodal RAG"
type: concept
sources: ["[[sources/nvidia-multimodal-rag-intro]]", "[[sources/multimodal-rag-images-text-guide]]", "[[sources/pinecone-clip-multimodal-embeddings]]", "[[sources/ragflow-rag-review-2025]]", "[[sources/colbert-late-interaction]]"]
related: ["[[concepts/multimodal-ai]]", "[[concepts/multimodal-embeddings]]", "[[concepts/vector-databases]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/vision-language-models]]", "[[entities/clip]]", "[[concepts/colbert]]", "[[concepts/late-interaction-retrieval]]", "[[concepts/retrieval-augmented-generation]]"]
last_compiled: 2026-04-05
summary: "Extending RAG to retrieve and reason over images alongside text; three architectures (unified embeddings, text grounding, separate stores with re-ranking) with tradeoffs between simplicity and fidelity."
---

## Overview

Multimodal Retrieval-Augmented Generation (Multimodal RAG) extends traditional text-only [[concepts/rag-vs-index-based-retrieval]] systems to handle images, charts, diagrams, and other visual data alongside text. Instead of retrieving only text passages relevant to a query, multimodal RAG can find and present relevant images, figures, and visual content — then pass everything to a vision-capable LLM for generation.

This is directly relevant to [[concepts/llm-knowledge-base]] systems that handle images alongside text. When a knowledge base contains scientific figures, architecture diagrams, screenshots, or charts, multimodal RAG enables querying across all content types.

## Three Architectural Approaches

### 1. Unified Vector Space Embedding

Models like [[entities/clip]] or Voyage AI's voyage-multimodal-3 encode both images and text into the same vector space. A text query can retrieve relevant images (or vice versa) through standard vector similarity search.

**Pros**: Simple infrastructure, single embedding model, standard retrieval pipeline
**Cons**: Embedding model must capture nuanced details across all modalities; current models struggle with information-dense images (charts, dense text)

### 2. Primary Modality Grounding (Text-First)

Convert all non-text modalities to text before embedding:
- Use multimodal LLMs (GPT-4V, Claude) to generate detailed image descriptions
- Embed the text descriptions using standard text embedding models
- Retrieve based on text similarity

**Pros**: Uses existing text infrastructure; no multimodal embedding model needed; metadata from descriptions aids objective Q&A
**Cons**: Loses visual nuance in translation; adds upfront LLM cost for summarization

### 3. Separate Stores with Multimodal Re-ranking

Maintain separate vector databases for each modality. Queries retrieve top-N results from each store, then a multimodal re-ranker orders combined results.

**Pros**: Specialized embeddings per modality; simplifies individual model alignment
**Cons**: Most complex; requires re-ranking logic; multiple indices to maintain

## Implementation Pipeline

Per [[sources/nvidia-multimodal-rag-intro]], the full pipeline involves:

### Preprocessing
1. **Separate** images and text from source documents
2. **Classify** images by type (charts/graphs vs general images) using MLLMs
3. **Process charts** with specialized tools (DePlot) for linearized tabular text
4. **Generate descriptions** of general images using MLLMs
5. **Embed** all content and store with metadata

### Inference
1. **Encode query** as vector embedding
2. **Retrieve** top-N relevant chunks via semantic search
3. **Route by type**: image chunks to MLLM for VQA; chart chunks include linearized data; text chunks pass directly
4. **Generate** answer combining all retrieved context with citations

## Embedding Models for Multimodal RAG

| Model | Dimensions | Special Features |
|-------|-----------|-----------------|
| [[entities/clip]] (OpenAI) | 512 | Original, widely supported |
| Jina CLIP v2 | 1024 | 89 languages, 512x512 images |
| Voyage multimodal-3 | 1024 | 32K token limit |
| ColPali | Varies | Late-interaction for documents |

## Connection to Knowledge Bases

For an [[concepts/llm-knowledge-base]], multimodal RAG solves the problem of making visual content queryable. However, the current KB approach using [[concepts/rag-vs-index-based-retrieval]] (index-based navigation at ~100-article scale) may not need full vector-based multimodal RAG. A simpler approach:

1. Use VLMs to generate text descriptions of all images during ingest
2. Include descriptions in the wiki alongside the images
3. Rely on existing text-based index navigation to find relevant visual content
4. Pass original images to a VLM when answering image-specific questions

This is essentially the "primary modality grounding" approach, adapted for a markdown-based wiki rather than a vector database.

## Sources

- [[sources/nvidia-multimodal-rag-intro]] — three architectural approaches with full pipeline detail
- [[sources/multimodal-rag-images-text-guide]] — practical implementation with two embedding strategies
- [[sources/pinecone-clip-multimodal-embeddings]] — CLIP as the foundational embedding model

## Related Concepts

- [[concepts/rag-vs-index-based-retrieval]] — text-only RAG vs index-based approaches
- [[concepts/multimodal-embeddings]] — the embedding models that enable cross-modal retrieval
- [[concepts/vector-databases]] — storage infrastructure for multimodal RAG
- [[concepts/vision-language-models]] — used in both preprocessing and generation phases
