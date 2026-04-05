---
title: "Claude Models Overview - Official API Documentation"
source: "https://platform.claude.com/docs/en/about-claude/models/overview"
author: "Anthropic"
date_published: 2026-04-05
date_ingested: 2026-04-05
tags: [claude, models, api, pricing, benchmarks]
type: article
status: raw
discovered_via: search
---

# Claude Models Overview - Official API Documentation

## Current Models (as of April 2026)

### Claude Opus 4.6
- API ID: claude-opus-4-6
- Context window: 1M tokens (~750K words)
- Max output: 128K tokens (300K via Batch API with beta header)
- Pricing: $5/MTok input, $25/MTok output
- Training data cutoff: August 2025
- Reliable knowledge cutoff: May 2025
- Extended thinking: Yes
- Adaptive thinking: Yes
- Description: "The most intelligent model for building agents and coding"

### Claude Sonnet 4.6
- API ID: claude-sonnet-4-6
- Context window: 1M tokens
- Max output: 64K tokens (300K via Batch API)
- Pricing: $3/MTok input, $15/MTok output
- Training data cutoff: January 2026
- Reliable knowledge cutoff: August 2025
- Extended thinking: Yes
- Adaptive thinking: Yes
- Description: "The best combination of speed and intelligence"

### Claude Haiku 4.5
- API ID: claude-haiku-4-5-20251001
- Context window: 200K tokens
- Max output: 64K tokens
- Pricing: $1/MTok input, $5/MTok output
- Training data cutoff: July 2025
- Reliable knowledge cutoff: February 2025
- Extended thinking: Yes
- Adaptive thinking: No
- Description: "The fastest model with near-frontier intelligence"

## Legacy Models

### Claude Sonnet 4.5 (September 29, 2025)
- 200K context, 64K output, $3/$15 per MTok

### Claude Opus 4.5 (November 24, 2025)
- 200K context, 64K output, $5/$25 per MTok

### Claude Opus 4.1 (August 5, 2025)
- 200K context, 32K output, $15/$75 per MTok

### Claude Sonnet 4 (May 14, 2025)
- 200K context, 64K output, $3/$15 per MTok

### Claude Opus 4 (May 14, 2025)
- 200K context, 32K output, $15/$75 per MTok

### Claude 3 Haiku (March 7, 2024) -- DEPRECATED, retiring April 19, 2026
- 200K context, 4K output, $0.25/$1.25 per MTok

## Key Capabilities (All Current Models)
- Text and image input
- Text output
- Multilingual capabilities
- Vision processing
- Available via Claude API, AWS Bedrock, and Google Vertex AI

## Pricing Evolution
Opus pricing dropped from $15/$75 (Opus 4/4.1) to $5/$25 (Opus 4.5/4.6) -- a 3x reduction while improving capabilities.
