---
title: "Claude Vision API Documentation"
source: "https://platform.claude.com/docs/en/build-with-claude/vision"
author: "Anthropic"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [claude, vision, multimodal, anthropic, API, image-understanding]
type: article
status: raw
discovered_via: search
---

# Claude Vision API Documentation

## Overview

Claude's vision capabilities allow it to understand and analyze images for multimodal interaction. Claude offers "best-in-class vision capabilities" among leading models, able to interpret images, charts, diagrams, perform OCR, analyze graphs/screenshots, and incorporate visual data into responses.

## Supported Formats

- JPEG, PNG, GIF, WebP
- Max 5 MB per image (API), 10 MB (claude.ai)
- Up to 600 images per API request (100 for 200k-token context models)
- Up to 20 images per turn on claude.ai
- Maximum image size: 8000x8000 px

## Image Sizing and Tokens

Images are resized if long edge exceeds 1568 pixels. Token calculation: `tokens = (width px * height px) / 750`.

| Aspect Ratio | Max Size (no resize) |
|-------------|---------------------|
| 1:1 | 1092x1092 px |
| 3:4 | 951x1268 px |
| 2:3 | 896x1344 px |
| 9:16 | 819x1456 px |
| 1:2 | 784x1568 px |

Cost examples (Claude Sonnet 4.6 at $3/M input tokens):
- 200x200 px: ~54 tokens, ~$0.00016/image
- 1000x1000 px: ~1334 tokens, ~$0.004/image
- 1092x1092 px: ~1590 tokens, ~$0.0048/image

## Three Input Methods

1. **Base64-encoded**: Inline image data in requests
2. **URL reference**: Direct URL to hosted images
3. **Files API**: Upload once, reference by file_id (best for multi-turn conversations to avoid re-sending image bytes each turn)

## Best Practices

- Place images before text/questions in prompts for best results
- Use clear, high-quality images (avoid blurry/pixelated)
- Ensure text in images is legible; don't crop key visual context to enlarge text
- Label multiple images with "Image 1:", "Image 2:", etc.
- For multi-turn conversations, use Files API to keep payloads small

## Benchmarks

- MMMLU: ~88-89% (comparable to Gemini, slightly above GPT-4.1)
- MMMU visual reasoning: ~76% (behind Gemini at 79.6% and OpenAI at 82.9%)
- Strongest at document understanding and reasoning tasks
- Superior structured data interpretation for financial statements and legal filings

## Limitations

- **People identification**: Cannot name people in images (policy restriction)
- **Accuracy**: May hallucinate on low-quality, rotated, or very small (<200px) images
- **Spatial reasoning**: Limited; struggles with precise localization, analog clock faces, chess positions
- **Counting**: Approximate counts only, especially for many small objects
- **AI-generated images**: Cannot reliably detect synthetic/AI-generated images
- **No image generation**: Understanding only, cannot generate/edit images
- **Healthcare**: Not designed for diagnostic scans (CT, MRI); not a substitute for professional diagnosis
- **No metadata parsing**: Does not read EXIF or other image metadata
