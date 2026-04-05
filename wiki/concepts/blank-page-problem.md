---
title: "Blank Page Problem"
type: concept
sources: ["[[sources/zhuo-conversational-interfaces]]", "[[sources/shapeof-ai-ux-patterns]]", "[[sources/microsoft-copilot-ux-guidance]]"]
related: ["[[concepts/conversational-ui-vs-structured-ui]]", "[[concepts/ai-ux-design-patterns]]", "[[concepts/copilot-pattern]]"]
last_compiled: 2026-04-05
summary: "The UX failure where a blank chat box provides no affordance for what an AI system can do, putting the burden on users to discover capabilities — solved by Wayfinder patterns like Suggestions, Templates, and Gallery."
---

## Overview

The Blank Page Problem is the first critical failure mode of conversational AI interfaces. An empty text box — the default UI of ChatGPT, Claude, and most AI products — provides **no signal** about what the system can do, how well it can do it, or how to get the best results.

[[entities/julie-zhuo]] names this explicitly: "A blank page box puts the burden on the user to learn what to use it for." Social media learned this lesson years ago — starting with content to react to works far better than empty feeds.

## Why It Matters

The blank page problem is particularly damaging for the [[concepts/knowledge-base-product-gap]] product because:
1. Non-technical users (the target market) do not know what to ask
2. The system's most powerful capabilities are invisible
3. First impressions determine adoption — a blank page signals "I don't know what to do here"
4. Users default to simple queries ("what is X?") when the system can do complex synthesis

## Solutions: Wayfinder Patterns

[[sources/shapeof-ai-ux-patterns]] catalogs eight Wayfinder patterns that solve this:

| Pattern | How It Helps |
|---------|-------------|
| **Suggestions** | Prompt starters showing representative capabilities |
| **Templates** | Structured starting points for common workflows |
| **Gallery** | Example outputs demonstrating quality and range |
| **Randomize** | Low-barrier "surprise me" for exploration |
| **Nudges** | Contextual alerts about available AI actions |
| **Follow-up** | AI asks clarifying questions when intent is unclear |
| **Prompt Details** | Shows what is happening behind the scenes |
| **Initial CTA** | Designed first-interaction experience |

## Microsoft's Approach

[[sources/microsoft-copilot-ux-guidance]] recommends: "Make clear what the system can do. Help the user understand what the AI system is capable of doing." Their studies show users prefer an experience that explains capabilities and gives suggestions on how to begin. Specific tactics: promptbooks (pre-built query templates), suggestion chips, and onboarding walkthroughs.

## Sources
- [[sources/zhuo-conversational-interfaces]] — names and analyzes the problem
- [[sources/shapeof-ai-ux-patterns]] — eight Wayfinder patterns
- [[sources/microsoft-copilot-ux-guidance]] — first-run experience guidance

## Related Concepts
- [[concepts/conversational-ui-vs-structured-ui]] — the blank page is chat's first failure
- [[concepts/ai-ux-design-patterns]] — Wayfinders are the first pattern category
- [[concepts/copilot-pattern]] — product architecture must address onboarding
