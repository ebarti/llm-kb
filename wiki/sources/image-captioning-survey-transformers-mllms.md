---
title: "Source: Next-generation Image Captioning — From Transformers to MLLMs"
type: source-summary
source: "[[raw/image-captioning-survey-transformers-mllms]]"
related: ["[[concepts/image-captioning]]", "[[concepts/vision-language-models]]", "[[concepts/multimodal-ai]]"]
last_compiled: 2026-04-05
summary: "Survey tracing image captioning from CNN+LSTM through transformers to multimodal LLMs; covers evaluation metrics (BLEU, CIDEr, SPICE), persistent challenges (long-tail objects, bias), and MLLM advantages."
---

## Key Points

- Architecture evolution: template-based → CNN+LSTM → attention → transformers → multimodal LLMs
- Encoder-decoder paradigm dominates: visual encoder (CNN/ViT) + text decoder (LSTM/Transformer)
- MLLMs provide "improved captioning flexibility, generative capabilities, and reasoning"
- Evaluation metrics: BLEU (n-gram precision), METEOR (synonyms), CIDEr (consensus), SPICE (semantic)
- Persistent challenges: long-tailed objects, training data bias, evaluation limitations, MLLM faithfulness
- MS-COCO remains the standard benchmark

## Detailed Summary

This survey provides the historical arc of [[concepts/image-captioning]], showing how the field has evolved through distinct architectural generations. The encoder-decoder paradigm — where a visual encoder extracts image features and a text decoder generates captions — has remained constant, but the components have changed dramatically.

Early systems used template-based or retrieval-based methods. Deep learning introduced CNN encoders (VGGNet, ResNet) paired with LSTM decoders. Attention mechanisms then allowed models to focus on relevant image regions when generating each word. Transformers brought parallel processing and better long-range dependencies. Now, multimodal LLMs like GPT-4V and Claude can generate detailed, context-aware captions without task-specific fine-tuning.

The survey notes that evaluation remains a fundamental challenge: existing metrics (BLEU, METEOR, CIDEr, SPICE) inadequately capture caption quality, and the field lacks metrics that align with human judgment of good descriptions.

## Related Concepts

- [[concepts/image-captioning]] — primary topic
- [[concepts/vision-language-models]] — current state of the art
- [[concepts/image-understanding]] — prerequisite for captioning
- [[concepts/multimodal-ai]] — broader context
