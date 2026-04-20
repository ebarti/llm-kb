---
title: "Chatbot Arena: Benchmarking LLMs in the Wild with Elo Ratings"
source: "https://lmarena.ai/"
author: "LMSYS / Arena AI"
date_published: 2023-05-03
date_ingested: 2026-04-05
tags: [chatbot-arena, elo-rating, human-evaluation, leaderboard, crowdsourced]
type: article
status: raw
discovered_via: search
---

# Chatbot Arena / Arena AI

## Overview

Benchmark platform for LLMs featuring anonymous, randomized battles in a crowdsourced manner. Users chat with two anonymous models side-by-side and vote for the better one.

## Current Top Rankings (April 2026)

1. claude-opus-4-6-thinking (Anthropic)
2. claude-opus-4-6 (Anthropic)
3. gemini-3.1-pro (Google)
4. gemini-3.1-pro-preview (Google)

## Scale

- 300+ models from major organizations
- 1.5M+ pairwise preferences collected
- Categories: Chat, Web Development, Image, Search

## Elo Rating System

Adopted from chess. After each game, rating updated according to difference between predicted and actual outcome. K parameter controls magnitude of rating changes.

### Methodology Evolution

- Initial: considerable variability with classic online algorithm
- Improvement: bootstrap-like technique sampling Elo scores from 1000 permutations
- Also adopted Bradley-Terry (BT) model: maximum likelihood estimate assuming fixed but unknown pairwise win-rate

## Key Advantages

- Computed asynchronously worldwide
- Allows performance to change dynamically
- Organic user queries (not predefined)
- Broad coverage of real use cases

## Known Vulnerabilities

Research has shown vote rigging can improve rankings, raising questions about leaderboard integrity. A 2025 Skywork review questioned reliability of the LMSYS leaderboard.
