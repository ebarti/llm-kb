---
title: "Source: Claude Vision API Documentation"
type: source-summary
source: "[[raw/claude-vision-capabilities]]"
related: ["[[concepts/vision-language-models]]", "[[concepts/image-understanding]]", "[[entities/claude]]", "[[concepts/document-ai-ocr]]"]
last_compiled: 2026-04-05
summary: "Anthropic's official vision docs: supported formats (JPEG/PNG/GIF/WebP), token costs (~1334 tokens per 1MP image), three input methods (base64/URL/Files API), limitations (no people ID, limited spatial reasoning), and best practices."
---

## Key Points

- Supports JPEG, PNG, GIF, WebP; max 5 MB (API) / 10 MB (claude.ai)
- Up to 600 images per API request; images auto-resized if >1568px on long edge
- Token cost formula: `tokens = (width * height) / 750`; ~$4.80 per 1K images at 1092x1092
- Three input methods: base64 inline, URL reference, Files API (best for multi-turn)
- Benchmarks: MMMLU ~88-89%, MMMU ~76%, strongest at document understanding
- Limitations: no people identification, approximate counting, limited spatial reasoning, no image generation

## Detailed Summary

The official Anthropic documentation provides technical specifications for [[concepts/image-understanding]] with Claude. The system processes images by converting them to tokens, with a straightforward cost model.

A notable practical detail: placing images before text in prompts yields best results, analogous to placing long documents before queries in text prompts. The Files API is recommended for multi-turn conversations since it avoids re-sending full image bytes each turn.

Claude's vision is positioned as strongest for document intelligence — financial statements, legal filings, structured layouts — rather than pure visual reasoning (where it trails Gemini and GPT-4o on MMMU). The limitations section is notably honest about spatial reasoning, counting accuracy, and the inability to detect AI-generated images.

## Related Concepts

- [[concepts/vision-language-models]] — Claude as a leading VLM
- [[concepts/image-understanding]] — core capability documented here
- [[concepts/document-ai-ocr]] — Claude's particular strength
- [[concepts/multimodal-ai]] — broader context
