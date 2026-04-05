---
title: "Multi-modal ML with OpenAI's CLIP"
source: "https://www.pinecone.io/learn/series/image-search/clip/"
author: "Pinecone"
date_published: 2024-06-01
date_ingested: 2026-04-05
tags: [CLIP, multimodal-embeddings, contrastive-learning, image-search, zero-shot]
type: article
status: raw
discovered_via: search
---

# Multi-modal ML with OpenAI's CLIP

## Architecture

CLIP (Contrastive Language-Image Pretraining) consists of two parallel encoders:
- A 12-layer text transformer
- Either a ResNet or Vision Transformer (ViT) for images
- Both output 512-dimensional vector embeddings in a shared representation space

## Contrastive Learning Mechanism

Training uses image-text pairs where text describes images. The system maximizes similarity between matching pairs while minimizing similarity between mismatched pairs. Negative pairs are extracted directly from positive pairs by swapping components.

## Embedding Space

Both encoders project into a unified vector space. Similar concepts across text and images produce vectors positioned near each other. "Two dogs running across a frosty field" as text encodes similarly to an actual image of that scene.

## Text Encoding Process

1. Text preprocessed into token IDs
2. Passed through transformer layers
3. Attention mask helps focus on actual tokens vs padding
4. Resulting embeddings require normalization for similarity comparisons

## Image Encoding Process

1. Images resized to 224x224 pixels, three color channels
2. Normalized to [0,1] range
3. ViT or ResNet generates embeddings
4. Normalization required for dot product similarity

## Zero-Shot Capabilities

For classification: similarity scores between image embeddings and text labels (e.g., "a photo of a [class]") determine predictions without task-specific training.

For object detection: patch-based comparisons create relevance maps identifying objects matching natural language descriptions.

## Key Applications

- **Text-to-image search**: Content-based image retrieval using natural language queries
- **Image classification**: Zero-shot categorization via text embedding comparison
- **Object detection**: Locating specific objects using language prompts
- **DALL-E integration**: Text embeddings guide diffusion models in image generation

## Advanced Models

- **Jina CLIP v1/v2**: Outperforms OpenAI CLIP in text-image retrieval; 0.9B parameters; multilingual (89 languages); 512x512 image resolution; Matryoshka representations
- **Voyage AI voyage-multimodal-3**: 32,000 token limit (exceeding CLIP/ImageBind); 1024-dimensional output vectors

## Foundational Principle

Language models alone cannot fully grasp concepts without sensory grounding. Models need "other forms of data, such as visual input" beyond text to progress meaningfully in understanding.
