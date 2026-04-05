---
title: "Source: Claude Models Overview - Official API Docs"
type: source-summary
source: "[[raw/anthropic-claude-models-overview]]"
related: ["[[entities/claude]]", "[[concepts/claude-model-family-evolution]]", "[[concepts/extended-thinking]]", "[[concepts/llm-api-pricing]]"]
tags: [claude, api, models, pricing]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Official Anthropic API documentation listing all current and legacy Claude models with context windows, pricing, output limits, and capability flags."
---

## Key Points

- Three current models: Opus 4.6 (1M context, 128K output, $5/$25), Sonnet 4.6 (1M, 64K, $3/$15), Haiku 4.5 (200K, 64K, $1/$5)
- Opus 4.6 and Sonnet 4.6 both support adaptive thinking (dynamic reasoning allocation)
- Batch API supports up to 300K output tokens with beta header
- Six legacy models still available, ranging from Opus 4 to Claude 3 Haiku (deprecated April 2026)
- Pricing dropped 3x from Opus 4 ($15/$75) to Opus 4.6 ($5/$25) with improved capabilities
- All models available on Claude API, AWS Bedrock, and Google Vertex AI

## Detailed Summary

The official models overview page serves as the canonical reference for Claude's current lineup. It introduces each model with API IDs, pricing, context windows, output limits, knowledge cutoffs, and capability flags (extended thinking, adaptive thinking, priority tier). The page tracks the transition from 200K context windows (all Claude 4.x models through Opus 4.5) to 1M tokens (Opus 4.6 and Sonnet 4.6). Notable is the distinction between "reliable knowledge cutoff" (most extensive and reliable knowledge) and "training data cutoff" (broader date range).

## Metadata

- **Author**: Anthropic
- **Date Published**: 2026 (continuously updated)
- **Format**: API documentation
- **URL**: https://platform.claude.com/docs/en/about-claude/models/overview
