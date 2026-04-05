---
title: "Multimodal Embeddings"
type: concept
sources: ["[[sources/pinecone-clip-multimodal-embeddings]]", "[[sources/nvidia-multimodal-rag-intro]]", "[[sources/multimodal-rag-images-text-guide]]"]
related: ["[[concepts/multimodal-rag]]", "[[concepts/multimodal-ai]]", "[[entities/clip]]", "[[concepts/vector-databases]]"]
last_compiled: 2026-04-05
summary: "Embedding models that map images and text into a shared vector space via contrastive learning, enabling cross-modal similarity search — foundational for multimodal RAG and image retrieval."
---

## Overview

Multimodal embeddings are vector representations that map different data types — images, text, audio — into a shared vector space where semantically similar content clusters together regardless of modality. A text description like "a golden retriever on a beach" and an actual photograph of a golden retriever on a beach would produce vectors that are close together in this shared space.

This capability is foundational for [[concepts/multimodal-rag]], cross-modal search, and zero-shot classification.

## How Contrastive Learning Works

The dominant training approach, pioneered by [[entities/clip]], is **contrastive learning**:

1. Start with a large dataset of image-text pairs (e.g., image captions from the web)
2. For each batch, compute embeddings for all images and all texts
3. **Positive pairs** (matching image-text): Push their embeddings closer together
4. **Negative pairs** (non-matching): Push embeddings apart
5. The loss function (InfoNCE / contrastive loss) optimizes this simultaneously across the batch

This produces encoders where the dot product between a text embedding and an image embedding reflects semantic similarity, even for combinations never seen in training.

## Architecture

The typical multimodal embedding model has:

- **Text encoder**: Transformer-based (BERT-like or custom), processes tokenized text into a fixed-dimension vector
- **Image encoder**: Vision Transformer (ViT) or CNN (ResNet), processes images into a fixed-dimension vector
- **Projection heads**: Linear layers that project both encoders' outputs into the same dimensionality
- **Shared space**: Both modalities live in one vector space (typically 512-1024 dimensions)

## Key Models

| Model | Dimensions | Training Data | Key Innovation |
|-------|-----------|---------------|----------------|
| CLIP (OpenAI, 2021) | 512 | 400M image-text pairs | First large-scale contrastive model |
| ALIGN (Google) | 640 | 1.8B noisy pairs | Scale over curation |
| SigLIP | 512-1024 | Varies | Sigmoid loss instead of softmax |
| Jina CLIP v2 | 1024 | Curated | 89 languages, Matryoshka representations |
| Voyage multimodal-3 | 1024 | Curated | 32K token limit, exceeding CLIP/ImageBind |
| ImageBind (Meta) | 1024 | Multiple modalities | 6 modalities in one space |

## Applications

1. **Cross-modal search**: Find images using text queries (or text using image queries)
2. **[[concepts/multimodal-rag]]**: Retrieve relevant images and text for LLM generation
3. **Zero-shot classification**: Classify images by comparing to text label embeddings
4. **Image generation guidance**: CLIP embeddings guide diffusion models (DALL-E, Stable Diffusion)
5. **Content deduplication**: Find near-duplicate images regardless of format or resolution

## Limitations

- Information-dense images (charts, diagrams with fine text) embed poorly compared to natural images
- Fixed dimension means lossy compression of complex visual scenes
- Training data biases (Western-centric, English-dominant) affect cross-cultural performance
- Image resolution constraints (typically 224-512px) lose fine details

## Relevance to Knowledge Bases

For an [[concepts/llm-knowledge-base]], multimodal embeddings enable:
- **Visual search**: Find images in the KB by describing them in natural language
- **Deduplication**: Detect when different sources reference the same diagram/chart
- **Clustering**: Group related images across different articles
- **Hybrid retrieval**: Combine with text-based search for comprehensive results

However, at the ~100-article scale where [[concepts/rag-vs-index-based-retrieval]] applies, generating text descriptions of images and searching those descriptions may be more practical than maintaining a multimodal embedding pipeline.

## Sources

- [[sources/pinecone-clip-multimodal-embeddings]] — detailed CLIP architecture and contrastive learning
- [[sources/nvidia-multimodal-rag-intro]] — multimodal embeddings in RAG context
- [[sources/multimodal-rag-images-text-guide]] — practical embedding strategies

## Related Concepts

- [[concepts/multimodal-rag]] — primary application of multimodal embeddings
- [[concepts/vector-databases]] — storage and retrieval infrastructure
- [[entities/clip]] — the foundational multimodal embedding model
