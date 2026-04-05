---
title: "AI UX Design Patterns"
type: concept
sources: ["[[sources/shapeof-ai-ux-patterns]]", "[[sources/microsoft-copilot-ux-guidance]]", "[[sources/progressive-disclosure-ai-pattern]]", "[[sources/smashing-practical-xai-ux]]"]
related: ["[[concepts/copilot-pattern]]", "[[concepts/progressive-disclosure-ai]]", "[[concepts/human-in-the-loop]]", "[[concepts/conversational-ui-vs-structured-ui]]", "[[concepts/trust-in-ai]]", "[[concepts/collaborative-ux]]"]
last_compiled: 2026-04-05
summary: "Emerging taxonomy of 57+ interaction patterns for AI products, organized into Wayfinders, Prompt Actions, Tuners, Governors, Trust Builders, and Identifiers — covering the full lifecycle from onboarding to oversight."
---

## Overview

AI UX design patterns are reusable interaction solutions for the unique challenges AI products pose: non-deterministic outputs, user uncertainty about capabilities, trust calibration, and the need for human oversight. Unlike traditional UX patterns (buttons, forms, navigation), AI patterns must handle probabilistic behavior, reasoning transparency, and adaptive personalization.

The field is maturing from ad-hoc design to systematic taxonomies. The most comprehensive catalog is [[sources/shapeof-ai-ux-patterns]] (The Shape of AI), which identifies **57 named patterns** across six categories. [[sources/microsoft-copilot-ux-guidance]] provides Microsoft's official framework. [[sources/smashing-practical-xai-ux]] adds four explanation-specific patterns.

## The Six Categories

### 1. Wayfinders (Solving the Blank Page)
Patterns that help users get started: Gallery, Suggestions, Templates, Randomize, Follow-up, Nudges, Initial CTA, Prompt Details. These address the [[concepts/blank-page-problem]] that [[entities/julie-zhuo]] identifies as the first critical failure of chat interfaces.

### 2. Prompt Actions (What AI Can Do)
The atomic operations of AI products: Expand, Summarize, Synthesize, Transform, Restructure, Restyle, Regenerate, Auto-fill, Chained Action, Inline Action, Inpainting, Madlibs. These define the capability surface of a [[concepts/copilot-pattern]] product.

### 3. Tuners (User Control Over Context)
Patterns for adjusting AI behavior: Attachments, Connectors, Filters, Model Management, Modes, Parameters, Preset Styles, Saved Styles, Voice and Tone, Prompt Enhancer. This is where [[concepts/personalization-in-ai]] lives architecturally.

### 4. Governors (Human-in-the-Loop Oversight)
The critical control layer: Action Plan (preview before execution), Verification (confirm before proceeding), Stream of Thought (transparent reasoning), Citations, Controls, Cost Estimates, Draft Mode, Memory, References, Sample Response, Shared Vision, Branches, Variations. These implement [[concepts/human-in-the-loop]] control and address [[concepts/trust-calibration]].

### 5. Trust Builders (Confidence and Ethics)
Patterns for building user confidence: Caveat, Consent, Data Ownership, Disclosure, Footprints, Incognito Mode, Watermark. These address [[concepts/trust-in-ai]] as a first-class design concern.

### 6. Identifiers (AI Brand and Personality)
Visual and verbal identity: Avatar, Color, Iconography, Name, Personality. How the AI is perceived and recognized across the product.

## Key Principles Across Patterns

1. **Progressive disclosure** ([[concepts/progressive-disclosure-ai]]): Reveal complexity in 2-3 layers maximum. Show the essential first, details on demand.

2. **Appropriate friction**: Slow users down at critical moments (save, share, copy) to prevent error propagation — counterintuitive in an era that celebrates frictionless UX.

3. **Hybrid interaction**: Combine [[concepts/conversational-ui-vs-structured-ui]] — conversation for intent, structured UI for refinement.

4. **Explanation by design**: The four XAI patterns from [[sources/smashing-practical-xai-ux]] (Because Statement, What-If Interactive, Highlight Reel, Push-and-Pull Visual) should be integrated, not bolted on.

## Implications for Knowledge Products

For the "incredible new product" [[entities/andrej-karpathy]] envisions, the pattern taxonomy suggests a product that combines:
- **Wayfinders** (Templates + Suggestions) for onboarding non-technical users
- **Prompt Actions** (Summarize + Synthesize + Expand) for knowledge work
- **Tuners** (Connectors + Modes) for personal knowledge context
- **Governors** (Citations + Stream of Thought + Verification) for trust
- **Trust Builders** (Disclosure + Footprints) for transparency

## Sources
- [[sources/shapeof-ai-ux-patterns]] — the 57-pattern taxonomy
- [[sources/microsoft-copilot-ux-guidance]] — Microsoft's copilot UX framework
- [[sources/progressive-disclosure-ai-pattern]] — progressive disclosure applied to AI
- [[sources/smashing-practical-xai-ux]] — four XAI design patterns

## Related Concepts
- [[concepts/copilot-pattern]] — the dominant AI product architecture these patterns serve
- [[concepts/progressive-disclosure-ai]] — foundational pattern across all categories
- [[concepts/human-in-the-loop]] — the Governors category
- [[concepts/conversational-ui-vs-structured-ui]] — the hybrid interaction question
- [[concepts/trust-in-ai]] — Trust Builders + Governors
- [[concepts/collaborative-ux]] — the overarching interaction model
