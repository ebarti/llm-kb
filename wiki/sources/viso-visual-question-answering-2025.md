---
title: "Source: Understanding Visual Question Answering (VQA) in 2025"
type: source-summary
source: "[[raw/viso-visual-question-answering-2025]]"
related: ["[[concepts/visual-question-answering]]", "[[concepts/multimodal-ai]]", "[[concepts/image-understanding]]"]
last_compiled: 2026-04-05
summary: "Comprehensive VQA overview: architecture (CNN + LSTM + attention), datasets (COCO-QA through Visual Genome), applications (medical, assistive, e-commerce), and state-of-the-art models (LLaMA3, NVILA, Qwen3)."
---

## Key Points

- VQA is a multimodal system accepting images + text questions, generating answers — considered "AI-complete"
- Architecture: CNN/ResNet for image features + LSTM for text + attention/fusion for integration
- Key datasets: COCO-QA, CLEVR, DAQUAR, Visual7W, Visual Genome (largest)
- Applications: medical diagnostics, assistive technology (VizWiz), e-commerce, content moderation
- Major challenges: dataset bias, novel question handling, video VQA, evaluation metrics
- State of the art: LLaMA3, NVILA (82.2% on NeXT-QA), Qwen3

## Detailed Summary

The article provides a thorough overview of [[concepts/visual-question-answering]], tracing it from early dataset creation through current transformer-based approaches. VQA is positioned as an "AI-complete" problem requiring integration of computer vision, natural language processing, and reasoning.

The core architecture involves three stages: image feature extraction (originally VGGNet, now ResNets/ViTs), question feature extraction (LSTMs or transformers), and feature integration (attention mechanisms being the dominant approach). The field has evolved from simple concatenation methods to sophisticated attention and Bayesian modeling.

Practical applications span medical diagnostics (reducing misdiagnosis), assistive technology (VizWiz and Be My Eyes for visually impaired users), e-commerce product Q&A, and content moderation. Cultural specificity remains a major weakness, with performance gaps between recognition (73.6%) and reasoning (49.8%) tasks.

## Related Concepts

- [[concepts/visual-question-answering]] — primary topic
- [[concepts/multimodal-ai]] — parent concept
- [[concepts/image-understanding]] — prerequisite capability
- [[concepts/vision-language-models]] — modern VLMs subsume traditional VQA
