---
title: "Needle in a Haystack (NIAH)"
type: concept
sources: ["[[sources/epoch-context-window-growth]]", "[[sources/magic-ltm-100m-context]]", "[[sources/lost-in-the-middle-paper]]"]
related: ["[[concepts/context-windows]]", "[[concepts/long-context-models]]", "[[concepts/lost-in-the-middle]]"]
last_compiled: 2026-04-05
summary: "The standard evaluation for long-context LLMs: embed a specific fact (needle) at varying depths within a large context (haystack) and test if the model can retrieve it."
---

## Overview

The Needle in a Haystack (NIAH) test is the canonical evaluation for long-context LLM performance. It works by embedding a specific, targeted piece of information (the "needle") within a larger body of text (the "haystack"), then testing whether the model can locate and use that information when queried.

## The Original Test

Designed to evaluate GPT-4 (128K) and Claude 2.1 (200K):
- **Needle**: "The best thing to do in San Francisco is eat a sandwich and sit in Dolores Park on a sunny day"
- **Haystack**: Essays by Paul Graham at varying lengths
- **Variables**: Depth (0-100% position) and context length (1K to model maximum)
- **Query**: "What is the best thing to do in San Francisco?"

Results are typically visualized as a heatmap with depth on one axis and context length on the other, with color indicating retrieval success.

## Key Results

- **Gemini 1.5 Pro**: >99.7% recall up to 1M tokens across text, video, and audio modalities
- **Most frontier models (2025-2026)**: Near-perfect on basic single-needle NIAH
- **Harder variants**: Performance degrades significantly, even for frontier models

## Limitations and Criticisms

The basic NIAH test has been criticized as too easy:
- Models can pass without truly processing the full context
- Single-needle retrieval doesn't test reasoning or multi-fact integration
- The needle is semantically distinct from the haystack, making it easier to find
- [[sources/magic-ltm-100m-context]]: Magic introduced **HashHop** as a harder alternative using incompressible random hash pairs

## Advanced Variants

| Variant | What It Tests | Difficulty |
|---------|--------------|-----------|
| **Multi-Needle (M-RT)** | Retrieving multiple facts | Medium |
| **Multi-Needle Reasoning (M-RS)** | Integrating multiple facts for reasoning | Hard |
| **Ancestral Trace Challenge (ATC)** | Multi-layer logical chains | Very Hard |
| **BABILong** | Distributed facts in arbitrarily long documents | Hard |
| **MMNeedle** | Visual needle in image haystack (multimodal) | Hard |
| **HashHop** | Incompressible hash pair retrieval/chains | Very Hard |
| **MRCR** | Multi-needle with distractor passages | Hard |

Even Gemini 2.5 Pro only scores >80% at 8K input on the hardest 8-needle MRCR variant ([[sources/epoch-context-window-growth]]).

## Relationship to Lost in the Middle

NIAH results often reveal the [[concepts/lost-in-the-middle]] pattern: retrieval success is highest when the needle is near the beginning or end and lowest in the middle, particularly at longer context lengths.

## Sources

- [[sources/epoch-context-window-growth]] — MRCR benchmark results across 49 models
- [[sources/magic-ltm-100m-context]] — HashHop as harder NIAH alternative
- [[sources/lost-in-the-middle-paper]] — NIAH-style experiments revealing positional bias

## Related Concepts

- [[concepts/context-windows]] — NIAH tests the practical limits of context windows
- [[concepts/long-context-models]] — NIAH is the primary evaluation for these models
- [[concepts/lost-in-the-middle]] — NIAH reveals this positional bias phenomenon
