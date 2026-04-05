---
title: "Source: Multi-modal ML with OpenAI's CLIP"
type: source-summary
source: "[[raw/pinecone-clip-multimodal-embeddings]]"
related: ["[[concepts/multimodal-embeddings]]", "[[entities/clip]]", "[[concepts/multimodal-rag]]", "[[concepts/image-understanding]]"]
last_compiled: 2026-04-05
summary: "Deep dive into CLIP architecture (dual text/image encoders, 512-dim shared space), contrastive learning mechanism, zero-shot capabilities, and applications in image search and classification."
---

## Key Points

- CLIP has dual encoders: 12-layer text transformer + ResNet/ViT for images, both producing 512-dim embeddings
- Contrastive learning: maximize similarity for matching image-text pairs, minimize for mismatches
- Zero-shot classification by comparing image embeddings to text label embeddings ("a photo of a [class]")
- Foundational for multimodal RAG, image search, and diffusion model guidance (DALL-E)
- Advanced successors: Jina CLIP v2 (0.9B params, 89 languages), Voyage AI voyage-multimodal-3 (32K token limit)

## Detailed Summary

This Pinecone guide provides the clearest explanation of how [[entities/clip]] works and why it matters. The core innovation is projecting images and text into a shared 512-dimensional vector space through contrastive learning, enabling cross-modal similarity search.

The architecture uses separate encoders that are trained jointly: a text transformer tokenizes and encodes language while a ViT or ResNet processes images. Both outputs are normalized before dot-product similarity comparison. This shared space enables remarkable zero-shot capabilities — classifying images by comparing to text descriptions without any task-specific training.

CLIP's influence extends far beyond classification: it underpins text-to-image search, guides diffusion models like DALL-E, and serves as the embedding backbone for [[concepts/multimodal-rag]] systems. The article also notes CLIP's philosophical significance — that language models need sensory grounding beyond text to progress meaningfully.

## Related Concepts

- [[concepts/multimodal-embeddings]] — CLIP as the foundational model
- [[concepts/multimodal-rag]] — CLIP embeddings enabling multimodal retrieval
- [[concepts/image-understanding]] — zero-shot visual understanding
- [[concepts/vision-language-models]] — CLIP as a precursor
