---
title: "Visual Question Answering"
type: concept
sources: ["[[sources/viso-visual-question-answering-2025]]", "[[sources/nvidia-multimodal-rag-intro]]", "[[sources/bentoml-vision-language-models-2026]]"]
related: ["[[concepts/image-understanding]]", "[[concepts/vision-language-models]]", "[[concepts/multimodal-ai]]", "[[concepts/multimodal-rag]]"]
last_compiled: 2026-04-05
summary: "AI task of answering natural language questions about images — considered 'AI-complete'; evolved from CNN+LSTM+attention to VLM-based approaches achieving 82%+ on key benchmarks."
---

## Overview

Visual Question Answering (VQA) is a multimodal AI task where a system takes an image and a natural language question as input and produces an answer. VQA is considered "AI-complete" — solving it fully is equivalent to achieving human-level machine intelligence, since it requires perception, language understanding, reasoning, and world knowledge.

## Architecture Evolution

### Classical VQA (2015-2020)
Three-component pipeline:
1. **Image encoder**: CNN (VGGNet, ResNet) extracts visual features
2. **Question encoder**: LSTM processes the natural language question
3. **Fusion + classifier**: Combines features via attention mechanisms, element-wise operations, or Bayesian modeling to predict an answer

### Modern VQA (2020-present)
[[concepts/vision-language-models]] subsume the classical pipeline:
- A single VLM takes image + question as multimodal input
- The language model reasons jointly over vision tokens and text tokens
- Answers are generated autoregressively, enabling open-ended responses

## Key Datasets

| Dataset | Size | Focus |
|---------|------|-------|
| VQA v2 | 1.1M questions, 204K images | General; balanced to reduce bias |
| CLEVR | 700K questions, 70K images | Compositional reasoning |
| Visual Genome | 1.7M Q&A pairs | Dense annotations |
| OK-VQA | 14K questions | Requires outside knowledge |
| ChartQA | Charts | Chart-specific Q&A |
| DocVQA | Documents | Document-specific Q&A |

## State of the Art (2025-2026)

Leading models per [[sources/viso-visual-question-answering-2025]]:
- **LLaMA3**: Superior on ActivityNet-QA, NextQA, LVBench
- **NVILA**: 82.2% on NeXT-QA, 70.1% on MLVU, 60.9% on ActivityNet-QA
- **Qwen3**: Surpasses DeepSeek-R1 and DeepSeek-V3

Performance gaps remain for culturally specific content: recognition tasks (73.6%) vs reasoning tasks (49.8%).

## Applications

- **Medical diagnostics**: Automated interpretation of radiology/pathology images
- **Assistive technology**: VizWiz and Be My Eyes for visually impaired users
- **E-commerce**: Product Q&A from images
- **Education**: Interactive visual learning tools
- **Content moderation**: Answering classification questions about images

## VQA in Knowledge Bases

For an [[concepts/llm-knowledge-base]], VQA enables:
- Answering questions about diagrams, charts, and figures stored in the KB
- During [[concepts/multimodal-rag]] inference, processing retrieved image chunks
- Quality checks: verifying that text descriptions of images are accurate
- Interactive exploration of visual content without needing to view images directly

## Sources

- [[sources/viso-visual-question-answering-2025]] — comprehensive VQA overview
- [[sources/nvidia-multimodal-rag-intro]] — VQA as part of multimodal RAG inference
- [[sources/bentoml-vision-language-models-2026]] — VQA as a VLM benchmark

## Related Concepts

- [[concepts/image-understanding]] — the broader capability VQA tests
- [[concepts/vision-language-models]] — the models that perform VQA
- [[concepts/multimodal-rag]] — VQA used during RAG inference
- [[concepts/image-captioning]] — related but distinct: descriptions vs answers
