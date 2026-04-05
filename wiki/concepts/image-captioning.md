---
title: "Image Captioning"
type: concept
sources: ["[[sources/image-captioning-survey-transformers-mllms]]", "[[sources/bentoml-vision-language-models-2026]]", "[[sources/nvidia-multimodal-rag-intro]]"]
related: ["[[concepts/image-understanding]]", "[[concepts/vision-language-models]]", "[[concepts/multimodal-rag]]", "[[concepts/multimodal-ai]]"]
last_compiled: 2026-04-05
summary: "Automatically generating natural language descriptions of images; evolved from CNN+LSTM through attention/transformers to multimodal LLMs; critical for making visual content searchable in knowledge bases."
---

## Overview

Image captioning is the task of automatically generating natural language descriptions of visual content. It bridges computer vision (understanding what is in an image) and natural language processing (expressing that understanding in words). For [[concepts/llm-knowledge-base]] systems, captioning is the key mechanism for making images searchable and integrable with text-based knowledge.

## Architecture Evolution

Per [[sources/image-captioning-survey-transformers-mllms]], the field has progressed through distinct generations:

### Generation 1: Template-Based (Pre-2015)
- Detect objects and attributes
- Fill in predefined sentence templates ("A [color] [object] is [action]")
- Rigid, limited vocabulary

### Generation 2: CNN + LSTM (2015-2018)
- **Encoder**: CNN (VGGNet, ResNet) extracts image feature vectors
- **Decoder**: LSTM generates caption word by word
- The CNN's final hidden layer serves as the "image embedding" fed to the LSTM

### Generation 3: Attention Mechanisms (2018-2020)
- Attention allows the decoder to focus on different image regions for each generated word
- Producing "a dog" focuses on the dog region; "on the grass" shifts attention to the background
- Dramatically improved specificity and accuracy

### Generation 4: Transformers (2020-2023)
- Replace LSTMs with transformer decoders
- Parallel processing, better long-range dependencies
- Vision Transformers (ViT) replace CNN encoders
- Models: BLIP, BLIP-2, GIT

### Generation 5: Multimodal LLMs (2023-present)
- General-purpose VLMs generate captions without task-specific fine-tuning
- GPT-4V, Claude, Gemini produce detailed, context-aware descriptions
- "Improved captioning flexibility, generative capabilities, and reasoning"
- Can be prompted for different styles: brief, detailed, technical, accessibility-focused

## Evaluation Metrics

| Metric | What It Measures | Limitation |
|--------|-----------------|------------|
| BLEU | N-gram precision vs reference | Misses synonyms and paraphrases |
| METEOR | Includes synonyms, stemming | Still correlates poorly with human judgment |
| CIDEr | Consensus among reference captions | Biased toward common phrasings |
| SPICE | Semantic content via scene graphs | Ignores fluency and style |

All metrics inadequately capture caption quality — a known open problem in the field.

## Captioning for Knowledge Bases

Image captioning is arguably the most important multimodal capability for the current [[concepts/llm-knowledge-base]] architecture:

1. **During ingest**: Generate text descriptions of all images in source materials
2. **Searchability**: Captions make images discoverable via text search in the wiki
3. **Wiki compilation**: Include captions as part of wiki articles, providing context for visual content
4. **Accessibility**: Serve as alt text for images referenced in the wiki
5. **Multimodal RAG bridge**: Captions enable the "text grounding" approach to [[concepts/multimodal-rag]] — the simplest path to making images part of a text-based retrieval system

### Practical Implementation

When ingesting a source with images:
```
1. Extract images from the source
2. Send each image to a VLM (Claude Vision, GPT-4V) with prompt:
   "Describe this image in detail. Include: type of visual (photo, chart, diagram),
    key content, any text visible, and what information it conveys."
3. Store the description in the raw file alongside the image reference
4. Include descriptions in wiki articles as part of compilation
```

## Sources

- [[sources/image-captioning-survey-transformers-mllms]] — evolution and challenges
- [[sources/bentoml-vision-language-models-2026]] — VLMs as captioning engines
- [[sources/nvidia-multimodal-rag-intro]] — captioning in RAG preprocessing

## Related Concepts

- [[concepts/image-understanding]] — captioning as a form of image understanding
- [[concepts/visual-question-answering]] — related but interactive (answers vs descriptions)
- [[concepts/multimodal-rag]] — captioning enables text-grounded multimodal retrieval
- [[concepts/vision-language-models]] — the models that perform modern captioning
