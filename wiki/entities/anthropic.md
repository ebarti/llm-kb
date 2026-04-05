---
title: "Anthropic"
type: entity
entity_type: org
sources: ["[[sources/anthropic-claude-prompting-best-practices]]", "[[sources/lakera-prompt-injection-guide]]", "[[sources/claude-code-agentic-coding]]", "[[sources/mcp-model-context-protocol]]", "[[sources/fli-ai-safety-index-2025]]", "[[sources/anthropic-safety-research-directions-2025]]", "[[sources/ai-safety-alignment-progress-2025]]", "[[sources/cip-whitepaper-collective-intelligence]]", "[[sources/anthropic-mcp-announcement]]", "[[sources/anthropic-mcp-linux-foundation]]", "[[sources/anthropic-building-effective-agents]]", "[[sources/anthropic-code-execution-mcp]]", "[[sources/anthropic-extended-thinking]]", "[[sources/wikipedia-anthropic]]", "[[sources/anthropic-rsp-v3]]", "[[sources/dario-amodei-machines-of-loving-grace]]"]
related: ["[[entities/claude]]", "[[entities/dario-amodei]]", "[[entities/daniela-amodei]]", "[[concepts/prompt-engineering]]", "[[concepts/system-prompt-design]]", "[[entities/claude-code]]", "[[concepts/model-context-protocol]]", "[[concepts/agentic-coding]]", "[[concepts/constitutional-ai]]", "[[concepts/ai-alignment]]", "[[concepts/ai-safety]]", "[[concepts/scalable-oversight]]", "[[concepts/ai-alignment-democratic]]", "[[entities/collective-intelligence-project]]", "[[concepts/reasoning-models]]", "[[concepts/test-time-compute]]", "[[concepts/responsible-scaling-policy]]", "[[concepts/claude-model-family-evolution]]"]
last_compiled: 2026-04-05
summary: "AI safety PBC founded 2021 by 7 ex-OpenAI researchers (Dario & Daniela Amodei + 5); $380B valuation; builds Claude models, Claude Code ($2.5B ARR), and MCP; ranked #1 in FLI AI Safety Index."
---

## Overview

Anthropic is an AI safety company that develops the [[entities/claude]] family of large language models. Founded in 2021 by [[entities/dario-amodei]] (CEO), [[entities/daniela-amodei]] (President), and five other former OpenAI researchers -- Jared Kaplan, Jack Clark, Chris Olah, Ben Mann, Sam McCandlish, and Tom Brown -- who left over concerns about OpenAI's commitment to safety. Structured as a **public benefit corporation** (PBC) headquartered in San Francisco, with a Long-Term Benefit Trust enabling the board to legally prioritize safety over shareholder profits.

As of February 2026, Anthropic has a **$380 billion valuation**, ~2,500 employees, and has raised over $60B in funding from Amazon ($8B), Google ($2B), Microsoft/Nvidia ($15B), and others.

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

### Responsible Scaling Policy (RSP)
Created the [[concepts/responsible-scaling-policy]] (September 2023), the first major voluntary safety governance framework from a frontier AI lab. Uses AI Safety Levels (ASL-1 through ASL-5) modeled after biosafety levels, requiring escalating safeguards proportional to model capabilities. ASL-3 safeguards activated May 2025. RSP v3.0 (February 2026) separated unilateral commitments from industry-wide recommendations. Influenced OpenAI, Google DeepMind, California SB 53, and EU AI Act ([[sources/anthropic-rsp-v3]]).

### "Machines of Loving Grace" Vision
CEO [[entities/dario-amodei]] published a 50+ page essay (October 2024) articulating AI's transformative upside across biology, neuroscience, economic development, governance, and work. Defines powerful AI as "a country of geniuses in a datacenter" and argues Anthropic focuses on risks because they're the obstacles between us and a fundamentally positive future ([[sources/dario-amodei-machines-of-loving-grace]]).

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
- [[sources/anthropic-extended-thinking]] -- Claude 3.7 Sonnet extended thinking announcement
- [[sources/wikipedia-anthropic]] -- founding story, corporate structure, funding history
- [[sources/anthropic-rsp-v3]] -- Responsible Scaling Policy v3.0 details
- [[sources/dario-amodei-machines-of-loving-grace]] -- CEO's vision essay on AI's positive potential
