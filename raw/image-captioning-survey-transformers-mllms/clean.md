---
title: "Next-generation image captioning: A survey from transformers to Multimodal Large Language Models"
source: "https://www.sciencedirect.com/science/article/pii/S2949719125000354"
author: "ScienceDirect (survey)"
date_published: 2025-03-01
date_ingested: 2026-04-05
tags: [image-captioning, transformers, multimodal-LLMs, computer-vision, NLP, survey]
type: paper
status: raw
discovered_via: search
---

# Next-generation Image Captioning: From Transformers to Multimodal LLMs

## Overview

This survey examines the progression of image captioning from traditional approaches through deep learning to contemporary multimodal large language models (MLLMs).

## Evolution of Architectures

### Traditional to Deep Learning
The field transitioned from conventional methods (template-based, retrieval-based) to deep learning approaches that are "more efficient and sophisticated" in generating meaningful textual descriptions.

### Attention Mechanisms & Transformers
Key innovations include attention mechanisms and transformer-based architectures that enhance modeling of both language and visual data simultaneously. The attention mechanism allows models to focus on relevant image regions when generating each word.

### Encoder-Decoder Architecture
The dominant paradigm:
- **Encoder**: CNN (VGGNet, ResNet) or Vision Transformer extracts visual features
- **Decoder**: LSTM/GRU or Transformer generates text token by token
- Attention bridges the two, aligning image regions to words

### Multimodal Large Language Models
MLLMs incorporate textual and visual data, providing "improved captioning flexibility, generative capabilities, and reasoning" beyond single-modality systems. Models like GPT-4V, Gemini, and Claude can generate detailed, context-aware captions without task-specific fine-tuning.

## Core Challenges

1. **Long-tailed object recognition**: Handling rare or underrepresented objects
2. **Training data bias**: Skewed representation affecting model fairness
3. **Evaluation metric limitations**: Current metrics (BLEU, METEOR, CIDEr, SPICE) inadequately capture caption quality
4. **MLLM-specific issues**: Faithfulness to images, spatial grounding, and computational costs

## Evaluation Metrics

- **BLEU**: N-gram precision between generated and reference captions
- **METEOR**: Considers synonyms and paraphrases
- **CIDEr**: Consensus-based, weights informative n-grams
- **SPICE**: Semantic propositional content evaluation via scene graphs

## Standard Benchmark

MS-COCO is the standard benchmark for image captioning, with models evaluated on caption quality, diversity, and semantic accuracy.

## Future Directions

- Addressing emerging MLLM challenges
- Advancing reasoning capabilities in captioning
- Reducing computational requirements for practical deployment
- Better evaluation metrics that align with human judgment
