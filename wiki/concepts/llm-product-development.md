---
title: "LLM Product Development"
type: concept
sources: ["[[sources/uxforai-12-llm-product-practices]]", "[[sources/sapphire-ai-native-applications]]"]
related: ["[[concepts/ai-native-design]]", "[[concepts/collaborative-ux]]", "[[concepts/copilot-pattern]]", "[[concepts/data-quality-bottleneck]]"]
last_compiled: 2026-04-05
summary: "Building LLM-powered products requires fundamentally different practices: thin-slice MVPs, provisional approvals over lengthy validation, Master LLM routing, customer-driven training, and first iterations focused on data collection rather than polish."
---

## Overview

LLM product development differs fundamentally from traditional software development. The non-deterministic nature of LLM outputs, rapid model improvement cycles, and the importance of user feedback loops demand different practices for scoping, designing, shipping, and iterating.

[[sources/uxforai-12-llm-product-practices]] distills this into 12 actionable practices, with the overarching theme: **"UX as a glue for the product development process"** — design thinking binds technical AI decisions to user outcomes.

## Key Practices

### Scoping
- **Thin-slice the MVP**: Find the smallest, highest-impact piece of the problem. "The tastiest slices are the thinnest-sliced fatty ones."
- **Don't forget the vision**: Run parallel tracks — one for the thin slice, one for future capabilities
- **Recognize AI is fundamentally different to ship**: Seek "provisional approvals" rather than comprehensive commitments

### Architecture
- **Master LLM routing**: A directing LLM routes queries to specialized task-specific models (explain, visualize, answer, generate)
- **Technology stack matters**: "The quality of the underlying AI model matters much more than anything else." Test multiple models and compare.
- **Prefer fine-tuning over prompt engineering**: Fine-tuning consistently outperforms prompt engineering in practice

### UX
- **Don't over-design tactical UX**: It will change rapidly post-launch. Simple is best for v1.
- **First iteration is for data collection**: Include prominent feedback mechanisms (thumbs up/down, expected-answer fields, verification buttons)
- **Use positive N-shot prompting**: Show desired behavior, not prohibited behavior

### Organization
- **Let customers train your model**: "The single most important point." Customer feedback directly improves the model.
- **Incentivize internal participation**: Launch internally first, gamify contributions to training data
- **Temperature management**: Low for consistency (SaaS default), higher for regeneration alternatives

## The Data Collection First Principle

The most contrarian practice: v1 is not built to impress but to learn. The first release is instrumented with:
- Feedback buttons on every AI output
- Thumbs up/down ratings
- "Expected answer" fields where users provide what they wanted
- Usage analytics on which features drive value
- Legal disclaimers acknowledging AI imperfection

This connects to [[concepts/data-quality-bottleneck]]: the quality of training data determines the quality of the product, and the best training data comes from real user interactions.

## Sources
- [[sources/uxforai-12-llm-product-practices]] — 12 practices framework
- [[sources/sapphire-ai-native-applications]] — continuous improvement in AI-native products

## Related Concepts
- [[concepts/ai-native-design]] — LLM product development builds AI-native products
- [[concepts/collaborative-ux]] — user feedback as product development input
- [[concepts/copilot-pattern]] — Master LLM routing implements copilot architecture
- [[concepts/data-quality-bottleneck]] — data collection first addresses quality
