---
title: "Anthropic"
type: entity
entity_type: org
sources: ["[[sources/anthropic-claude-prompting-best-practices]]", "[[sources/lakera-prompt-injection-guide]]", "[[sources/claude-code-agentic-coding]]", "[[sources/mcp-model-context-protocol]]", "[[sources/fli-ai-safety-index-2025]]", "[[sources/anthropic-safety-research-directions-2025]]", "[[sources/ai-safety-alignment-progress-2025]]", "[[sources/cip-whitepaper-collective-intelligence]]", "[[sources/anthropic-mcp-announcement]]", "[[sources/anthropic-mcp-linux-foundation]]", "[[sources/anthropic-building-effective-agents]]", "[[sources/anthropic-code-execution-mcp]]", "[[sources/anthropic-extended-thinking]]"]
related: ["[[entities/claude]]", "[[concepts/prompt-engineering]]", "[[concepts/system-prompt-design]]", "[[entities/claude-code]]", "[[concepts/model-context-protocol]]", "[[concepts/agentic-coding]]", "[[concepts/constitutional-ai]]", "[[concepts/ai-alignment]]", "[[concepts/ai-safety]]", "[[concepts/scalable-oversight]]", "[[concepts/ai-alignment-democratic]]", "[[entities/collective-intelligence-project]]", "[[concepts/reasoning-models]]", "[[concepts/test-time-compute]]"]
last_compiled: 2026-04-05
summary: "AI safety company behind Claude models, Claude Code ($2.5B revenue), and the Model Context Protocol — leading in prompt engineering and agentic AI infrastructure."
---

## Overview

Anthropic is an AI safety company that develops the [[entities/claude]] family of large language models. Founded in 2021, Anthropic has become one of the leading frontier AI labs alongside OpenAI and Google DeepMind.

## Key Contributions to Prompt Engineering

Anthropic's official prompting best practices guide is one of the most comprehensive and well-maintained resources for [[concepts/prompt-engineering]]. Key contributions include:

- **XML tag structuring**: Anthropic popularized the use of XML tags (`<instructions>`, `<context>`, `<example>`) for unambiguous prompt structure
- **Adaptive thinking**: Claude 4.6 dynamically decides when and how much to reason, controlled by an effort parameter
- **Context engineering**: The 2025 "effective context engineering" framework shifts focus from individual prompt crafting to designing entire context assembly systems
- **RL-based injection defense**: Training Claude with reinforcement learning against simulated [[concepts/prompt-injection]] attacks, reducing attack success rates to ~1%

## Agentic AI Leadership

### Claude Code
[[entities/claude-code]] — agentic coding system reaching $2.5B annualized revenue by March 2026. At Anthropic, the majority of code is now written by Claude Code. Claude Opus 4.5 leads [[concepts/swe-bench]] Verified at 80.9%.

### Model Context Protocol (MCP)
Created and open-sourced [[concepts/model-context-protocol]] in November 2024 to standardize LLM-to-tool integration. Adopted by OpenAI (March 2025), Google DeepMind (April 2025), and Microsoft. Donated to Agentic AI Foundation (Linux Foundation) in December 2025. 97 million monthly SDK downloads.

### Computer Use (March 2026)
Claude can interact with desktop environments: opening files, navigating browsers, clicking buttons, filling forms — extending agent capability from code to full computer operation.

### Claude Opus 4.6 (February 2026)
Tops benchmarks in agentic coding, computer use, and [[concepts/tool-use]].

## AI Safety Leadership

### Constitutional AI
Developed [[concepts/constitutional-ai]] as an alternative to pure RLHF-based alignment. Uses explicit written principles to guide model self-critique, addressing RLHF's scalability bottleneck ([[sources/ai-safety-alignment-progress-2025]]). Extended to **Collective Constitutional AI** in partnership with the [[entities/collective-intelligence-project]]: ~1,000 Americans deliberated and drafted alignment principles for Claude, demonstrating [[concepts/ai-alignment-democratic]] at scale.

### Extended Reasoning and Transparency
Introduced configurable "thinking budgets" in Claude 3.7 Sonnet and published raw internal reasoning logs, enabling red teams to detect contradictions signaling misalignment or deceptive behavior.

### Safety Research Directions
Published 10 priority research areas: evaluating capabilities and alignment, understanding model cognition, CoT faithfulness, AI control strategies, [[concepts/scalable-oversight]], adversarial robustness, unlearning, and multi-agent governance ([[sources/anthropic-safety-research-directions-2025]]).

### Safety Ranking
Ranked **#1 in the FLI AI Safety Index** (Summer 2025) with C+ grade (2.64/4.0). Distinguished by human participant bio-risk trials and privacy protections ([[sources/fli-ai-safety-index-2025]]).

## Mentioned In
- [[sources/anthropic-claude-prompting-best-practices]] — Official prompting guide
- [[sources/lakera-prompt-injection-guide]] — Anthropic's RL-based prompt injection defense
- [[sources/claude-code-agentic-coding]] — Claude Code revenue, eight 2026 trends
- [[sources/mcp-model-context-protocol]] — MCP creation and industry adoption
- [[sources/fli-ai-safety-index-2025]] — highest-ranked company in safety evaluation
- [[sources/anthropic-safety-research-directions-2025]] — 10 research priorities from alignment team
- [[sources/ai-safety-alignment-progress-2025]] — CAI, extended reasoning, visible thought processes
- [[sources/cip-whitepaper-collective-intelligence]] — Collective Constitutional AI partnership with CIP
- [[sources/anthropic-mcp-announcement]] — original November 2024 MCP launch
- [[sources/anthropic-mcp-linux-foundation]] — MCP donation to Linux Foundation, December 2025
- [[sources/anthropic-building-effective-agents]] — canonical guide to agent design patterns
- [[sources/anthropic-code-execution-mcp]] — MCP code execution optimization pattern
- [[sources/anthropic-extended-thinking]] — Claude 3.7 Sonnet extended thinking announcement
