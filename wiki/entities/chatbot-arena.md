---
title: "Chatbot Arena (Arena AI)"
type: entity
entity_type: tool
sources: ["[[sources/chatbot-arena-methodology]]", "[[sources/cameron-wolfe-llm-as-judge]]", "[[sources/raschka-state-of-llms-2025]]"]
related: ["[[concepts/llm-benchmarks]]", "[[concepts/benchmark-saturation]]", "[[entities/mt-bench]]"]
last_compiled: 2026-04-05
summary: "Crowdsourced LLM evaluation platform: anonymous pairwise battles with 300+ models and 1.5M+ preferences, using Elo/Bradley-Terry scoring from organic user queries — the most widely-cited dynamic benchmark."
---

## Overview

Chatbot Arena (now rebranded as Arena AI) is a crowdsourced benchmark platform where users chat with two anonymous LLMs side-by-side and vote for the better response. With **300+ models** and **1.5M+ pairwise preferences**, it is the most widely-cited human-preference evaluation platform for LLMs.

## Methodology

### Anonymous Pairwise Battles
Users enter the arena, interact with two unknown models simultaneously, and vote for the one they prefer. The anonymous setup prevents brand-based bias.

### Elo / Bradley-Terry Rating
- **Elo rating**: Adapted from chess, updated after each battle based on predicted vs actual outcome
- **Bootstrap sampling**: 1000 permutations to reduce variability
- **Bradley-Terry model**: Maximum likelihood estimation of pairwise win rates

### Categories
Chat, Web Development, Image, Search — enabling modality-specific rankings.

## Current Top Rankings (April 2026)

1. Claude Opus 4.6 Thinking (Anthropic)
2. Claude Opus 4.6 (Anthropic)
3. Gemini 3.1 Pro (Google)

## Advantages

- **Organic queries**: Real user tasks, not predefined test sets
- **Continuous refresh**: New data daily, resisting [[concepts/benchmark-saturation]]
- **Broad coverage**: Diverse use cases from actual users
- **Dynamic**: Tracks capability changes over time

## Known Vulnerabilities

- **Vote rigging**: Research demonstrated that rankings can be manipulated
- **Selection bias**: Users who visit the Arena may not represent typical users
- **Verbosity preference**: Crowdsourced voters may exhibit [[concepts/evaluation-bias]] toward longer responses
- **Integrity questions**: A 2025 Skywork review questioned overall reliability

## Mentioned In

- [[sources/chatbot-arena-methodology]] — methodology and rankings
- [[sources/cameron-wolfe-llm-as-judge]] — as a key benchmark for LLM-as-Judge validation
- [[sources/raschka-state-of-llms-2025]] — as a counterweight to static benchmark saturation
