---
title: "Source: 12 LLM Product Development Practices"
type: source-summary
source: "[[raw/uxforai-12-llm-product-practices]]"
related: ["[[concepts/llm-product-development]]", "[[concepts/collaborative-ux]]", "[[concepts/copilot-pattern]]"]
last_compiled: 2026-04-05
summary: "Twelve actionable practices for shipping LLM products: thin-slice MVPs, master-LLM routing, customer-driven model training, data collection first iteration, and temperature management — with UX as the glue."
---

## Key Points
- Thin-slice the MVP: smallest impactful piece, not comprehensive solution
- Don't over-design tactical UX — it will change rapidly post-launch
- Use "Master LLM" routing to specialized task-specific models
- "Let customers train your model" — the single most important practice
- First iteration is for data collection, not perfection
- Fine-tuning consistently outperforms prompt engineering
- Use positive N-shot prompting (what to do, not what to avoid)
- Temperature management: low for consistency, higher for regeneration

## Detailed Summary

This practitioner-oriented guide positions [[concepts/llm-product-development]] as fundamentally different from traditional software development. The overarching theme is "UX as glue" — design thinking binds technical AI decisions to user outcomes.

The **thin-slice MVP** approach directly addresses [[concepts/knowledge-base-product-gap]]: rather than building a full knowledge management platform, find the single biggest pain point (e.g., "I need to find information scattered across documents") and solve that first.

The **Master LLM** architecture pattern is relevant to multi-modal AI products: a routing model directs queries to specialized models for explanation, visualization, Q&A, etc. This maps to the [[concepts/copilot-pattern]] where different capabilities require different underlying approaches.

**"Let customers train your model"** is described as the most important practice. The feedback loop between user corrections and model improvement is the engine of [[concepts/collaborative-ux]] — users are not just consumers but co-creators of the system's intelligence.

The emphasis on **first iteration as data collection** reframes launch expectations: v1 is instrumented to learn, not to impress. Include prominent feedback mechanisms (thumbs up/down, expected-answer fields) and legal disclaimers.

## Notable Quotes
> "The tastiest slices are the thinnest-sliced fatty ones"
> "Likely the single most important point" (on letting customers train your model)
> "The quality of the underlying AI model matters much more than anything else"

## Related Concepts
- [[concepts/llm-product-development]] — primary topic
- [[concepts/collaborative-ux]] — customer-as-trainer paradigm
- [[concepts/copilot-pattern]] — Master LLM routing maps to copilot architecture
- [[concepts/data-quality-bottleneck]] — first iteration as data collection
