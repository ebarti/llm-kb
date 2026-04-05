---
title: "OpenAI Embeddings"
type: entity
entity_type: tool
sources: ["[[sources/pinecone-embedding-models-rundown]]", "[[sources/modal-mteb-leaderboard]]"]
related: ["[[concepts/text-embeddings]]", "[[concepts/matryoshka-representation-learning]]", "[[entities/mteb]]"]
last_compiled: 2026-04-05
summary: "OpenAI's embedding API models: text-embedding-ada-002 (1536 dims, legacy), text-embedding-3-small/large (native Matryoshka, up to 3072 dims) — widely used but increasingly matched by open-source alternatives."
---

## Overview

OpenAI's embedding models are among the most widely used proprietary [[concepts/text-embeddings]] services. They provide a simple API for generating dense vector representations of text.

## Model Lineup

| Model | Dimensions | Max Tokens | Notes |
|-------|-----------|-----------|-------|
| text-embedding-ada-002 | 1536 | 8191 | Legacy, still widely used |
| text-embedding-3-small | 1536 (truncatable) | 8191 | Native MRL support |
| text-embedding-3-large | 3072 (truncatable) | 8191 | Highest quality, native MRL |

The v3 models support [[concepts/matryoshka-representation-learning]], allowing truncation to any lower dimension (e.g., 256, 512, 1024) with graceful quality degradation.

## Performance Context

- ada-002 took 9:07 to embed ~42K chunks via API (compared to E5-base-v2 at 3:53 on GPU)
- ada-002 reached 88.8% accuracy on context understanding tasks
- Open-source models like BGE-M3, Qwen3-Embedding-8B now match or exceed OpenAI on [[entities/mteb]] benchmarks
- The v3 models improved significantly over ada-002

## Advantages

- **Simple API**: No infrastructure to manage
- **Automatic scaling**: Handles any volume without GPU provisioning
- **Consistent quality**: Well-tested, widely deployed

## Limitations

- **Cost at scale**: Per-API-call pricing compounds at high volume
- **No fine-tuning**: Cannot adapt to domain-specific data
- **Privacy**: Data sent to OpenAI's servers
- **Competition**: Open-source models increasingly match performance

## Mentioned In

- [[sources/pinecone-embedding-models-rundown]] — practical speed and quality comparison
- [[sources/modal-mteb-leaderboard]] — benchmark context showing open-source catch-up
