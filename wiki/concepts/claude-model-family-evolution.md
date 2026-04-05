---
title: "Claude Model Family Evolution"
type: concept
sources: ["[[sources/wikipedia-claude-language-model]]", "[[sources/anthropic-claude-models-overview]]", "[[sources/anthropic-claude-3-family-announcement]]", "[[sources/anthropic-claude-4-announcement]]"]
related: ["[[entities/claude]]", "[[entities/anthropic]]", "[[concepts/extended-thinking]]", "[[concepts/constitutional-ai]]", "[[concepts/reasoning-models]]", "[[concepts/long-context-models]]", "[[concepts/llm-api-pricing]]"]
tags: [claude, model-evolution, anthropic, timeline]
last_compiled: 2026-04-05
summary: "Complete timeline of Claude model releases from Claude 1 (March 2023) through Claude 4.6 (February 2026), tracking the expansion of context windows (9K to 1M), capabilities, and pricing."
---

## Overview

The Claude model family has evolved through four major generations in three years, with each generation bringing substantial improvements in reasoning, context window size, output length, and agentic capabilities. The three-tier system (Haiku/Sonnet/Opus) introduced with Claude 3 has become the standard organizational framework.

## Complete Release Timeline

| Version | Date | Context | Max Output | Key Innovation |
|---------|------|---------|------------|----------------|
| Claude 1 | Mar 14, 2023 | 9K | ~4K | First public release |
| Claude 1 (100K) | May 2023 | 100K | ~4K | 11x context expansion |
| Claude 2 | Jul 11, 2023 | 100K | ~4K | First publicly available |
| Claude 2.1 | Nov 21, 2023 | 200K | ~4K | Doubled context to 200K |
| Claude 3 Haiku | Mar 4, 2024 | 200K | 4K | Three-tier system introduced |
| Claude 3 Sonnet | Mar 4, 2024 | 200K | 4K | Balanced speed/intelligence |
| Claude 3 Opus | Mar 4, 2024 | 200K | 4K | First to surpass GPT-4 |
| Claude 3.5 Sonnet | Jun 20, 2024 | 200K | 8K | Artifacts feature; outperformed Opus at lower cost |
| Claude 3.5 Sonnet v2 | Oct 22, 2024 | 200K | 8K | Computer use capability |
| Claude Sonnet 4 | May 22, 2025 | 200K | 64K | 72.7% SWE-bench; extended thinking w/ tools |
| Claude Opus 4 | May 22, 2025 | 200K | 32K | 72.5% SWE-bench; "world's best coding model" |
| Claude Opus 4.1 | Aug 5, 2025 | 200K | 32K | 74.5% SWE-bench; improved agentic tasks |
| Claude Sonnet 4.5 | Sep 29, 2025 | 200K | 64K | Optimized for agents/coding |
| Claude Haiku 4.5 | Oct 15, 2025 | 200K | 64K | Cost-effective near-frontier |
| Claude Opus 4.5 | Nov 24, 2025 | 200K | 64K | Infinite Chats; 80.9% SWE-bench |
| Claude Opus 4.6 | Feb 5, 2026 | 1M | 128K | Adaptive thinking; agent teams; 1M context |
| Claude Sonnet 4.6 | Feb 17, 2026 | 1M | 64K | Full upgrade across all capabilities |

## Key Evolutionary Trends

### 1. Context Window Expansion
The context window grew 111x in three years: 9K (Claude 1) to 100K (May 2023) to 200K (Claude 2.1) to 1M tokens (Claude 4.6). This trajectory tracks the broader [[concepts/context-windows]] growth Epoch AI measured at ~30x/year.

### 2. Output Length Growth
Maximum output tokens grew 32x: from 4K (Claude 3) to 128K (Opus 4.6), with Batch API supporting up to 300K. This enables generation of complete documents, codebases, and multi-file outputs in a single response.

### 3. Pricing Deflation
Opus-tier pricing dropped 3x: from $15/$75 per MTok (Opus 4/4.1) to $5/$25 (Opus 4.5/4.6). Sonnet pricing held steady at $3/$15 while capabilities improved dramatically. This mirrors the broader [[concepts/llm-cost-optimization]] trend.

### 4. Reasoning Evolution
- Claude 3: Standard inference only
- Claude 3.5 Sonnet: Improved reasoning at lower cost than Opus
- Claude 4: Extended thinking with explicit budget_tokens
- Claude 4.6: Adaptive thinking -- model dynamically allocates reasoning effort

### 5. Agentic Capabilities
Each generation added agentic features:
- Claude 3.5: Computer use (screen navigation)
- Claude 4: Extended thinking with tools, parallel tool execution, memory files
- Claude 4.6: Agent teams, adaptive thinking, subagent orchestration

### 6. Constitutional AI Maturation
The constitution grew from initial principles (2022) to 75 guidelines (2023) to 23,000 words (2026), reflecting increasingly nuanced behavioral guidance ([[concepts/constitutional-ai]]).

## Naming Convention Shift

Claude 3 used the pattern "Claude 3 [Tier]" (e.g., Claude 3 Opus). Starting with Claude 4, the naming shifted to "Claude [Tier] [Version]" (e.g., Claude Opus 4). This change decoupled the tier name from the generation number, allowing independent version progression for each tier.

## Benchmark Trajectory

SWE-bench Verified (real-world GitHub issue resolution) across Opus releases:
- Opus 4: 72.5%
- Opus 4.1: 74.5%
- Opus 4.5: 80.9%

METR task-completion time horizon (50% success):
- Opus 4.5: 14 hours 30 minutes
- This metric measures how long a task can be before the model completes it successfully 50% of the time -- a proxy for sustained autonomous work capacity.

## Sources

- [[sources/wikipedia-claude-language-model]] -- complete release timeline and capabilities
- [[sources/anthropic-claude-models-overview]] -- official API specs, pricing, and model IDs
- [[sources/anthropic-claude-3-family-announcement]] -- Claude 3 launch details and benchmarks
- [[sources/anthropic-claude-4-announcement]] -- Claude 4 launch details and features

## Related Concepts

- [[concepts/extended-thinking]] -- the reasoning capability that evolved across generations
- [[concepts/reasoning-models]] -- Claude's position in the reasoning model landscape
- [[concepts/long-context-models]] -- Claude's 1M token context in the broader context window race
- [[concepts/llm-api-pricing]] -- pricing trends across model generations
- [[entities/claude]] -- the model family entity page
- [[entities/anthropic]] -- the organization behind Claude
