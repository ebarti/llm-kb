---
title: "Guide to Multimodal RAG for Images and Text"
source: "https://medium.com/kx-systems/guide-to-multimodal-rag-for-images-and-text-10dab36e3117"
author: "Ryan Siegler"
date_published: 2025-08-01
date_ingested: 2026-04-05
tags: [multimodal-rag, image-retrieval, embeddings, vector-databases, implementation]
type: article
status: raw
discovered_via: search
---

# Guide to Multimodal RAG for Images and Text

## Core Architecture

Multimodal RAG follows a two-phase pipeline:
1. **Retrieval Phase**: Embed diverse data types and store in vector databases, then retrieve via semantic similarity
2. **Generation Phase**: Pass retrieved multimodal context to LLMs for response generation

## Two Primary Embedding Strategies

### Strategy 1: Unified Multimodal Embeddings
Use embedding models that process both text and images into a single vector space. Example: Voyage AI's voyage-multimodal-3 with 32,000 token limit and 1024-dimensional output vectors.

### Strategy 2: LLM-Based Image Summarization
Transform all data to text before embedding:
- Use multimodal LLMs (GPT-4V) to generate detailed image descriptions
- Embed summaries using text-only models (text-embedding-3-small, 1536 dimensions)
- Simpler vector database schemas but loses some image nuance

## Implementation Steps

1. Extract and prepare images/text files
2. Generate embeddings (direct or via summarization)
3. Create vector database tables with metadata columns
4. Configure similarity indices (qFlat, HNSW, IVFPQ options)
5. Execute similarity searches on user queries
6. Retrieve top-k results and inject into LLM prompts

## Database Schema

- Path (file location)
- Media type (image/text classifier)
- Embeddings (vector representations)
- Optional raw text/summaries

## Vector Index Selection

qFlat indexing is "an on-disk version of a flat index, perfect for highly accurate searches in memory constrained environments" with cosine similarity as default metric.

## Generation Phase

Two approaches:
- **Multimodal LLMs** (Gemini 1.5): Accept images + text directly
- **Text-based LLMs** (GPT-4): Require image summaries passed as text

## Practical Considerations

Strategy 2 involves "an additional cost of initially summarizing other types of data" requiring LLM API calls upfront but simplifying downstream processing. Strategy 1 is more direct but requires multimodal embedding models.
