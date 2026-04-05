---
title: "Trust in AI"
type: concept
sources: ["[[sources/schmidt-designing-human-ai-collaboration]]", "[[sources/smashing-practical-xai-ux]]", "[[sources/microsoft-copilot-ux-guidance]]", "[[sources/shapeof-ai-ux-patterns]]", "[[sources/arxiv-interface-design-human-ai-decisions]]"]
related: ["[[concepts/trust-calibration]]", "[[concepts/explainable-ai-ux]]", "[[concepts/human-in-the-loop]]", "[[concepts/hallucination-contamination]]", "[[concepts/ai-ux-design-patterns]]"]
last_compiled: 2026-04-05
summary: "Trust is the true currency of AI products — built through transparency, appropriate friction, citations, confidence signals, and consistent competence over time; both over-trust (automation bias) and under-trust are failure modes."
---

## Overview

Trust is the central design challenge of AI products. Unlike traditional software where trust is binary (it works or it doesn't), AI products require **calibrated trust** — users must trust the system enough to use it but not so much that they uncritically accept errors.

[[sources/schmidt-designing-human-ai-collaboration]] frames it most directly: **"Trust — not attention — is the true currency underlying every successful product."** This reframes AI product strategy from engagement metrics to trust metrics.

## The Trust Spectrum

| State | Behavior | Consequence |
|-------|----------|-------------|
| **Under-trust** | User ignores AI suggestions | Product provides no value |
| **Calibrated trust** | User evaluates and selectively accepts | Optimal human-AI performance |
| **Over-trust** | User uncritically accepts all AI output | [[concepts/hallucination-contamination]], automation bias |

[[sources/arxiv-interface-design-human-ai-decisions]] provides empirical evidence that over-trust is the more dangerous failure: "human + AI teams perform worse than AI alone" due to automation bias.

## How Trust Is Built

### 1. Transparency (What the AI did and why)
- [[concepts/explainable-ai-ux]]: "Because" statements, feature importance, counterfactuals
- Citations and source references
- Confidence levels and uncertainty signals
- Stream of Thought (visible reasoning traces)

### 2. Appropriate Friction (Slow users down at key moments)
[[sources/microsoft-copilot-ux-guidance]] advocates adding friction at save, share, copy, and paste — forcing users to take ownership of AI-generated content. This is counterintuitive in UX but essential for AI products.

### 3. Consistent Competence (Trust is cumulative)
Trust is not a feature — it is built through reliable performance over time. First-run experience sets expectations; consistent delivery sustains them.

### 4. Recovery Pathways (Graceful failure)
Systems must handle errors well: clear limitations, iterative refinement, undo/revert, and alternative suggestions. [[sources/schmidt-designing-human-ai-collaboration]] calls this "Resilience."

### 5. User Control (Agency preserves trust)
Users who feel in control trust more. Edit capabilities, override options, adjustable AI behavior settings, and feedback mechanisms all reinforce agency.

## Trust Builder Patterns

From [[sources/shapeof-ai-ux-patterns]]:
- **Caveat**: Inform users about model limitations upfront
- **Consent**: Only capture data with user knowledge/permission
- **Data Ownership**: Users control how their data is used
- **Disclosure**: Clearly mark AI-generated content
- **Footprints**: Let users trace from prompt to result
- **Incognito Mode**: Interact without memory
- **Watermark**: Mark AI content for downstream identification

## Implications for Knowledge Products

For [[concepts/knowledge-base-product-gap]], trust design is existential. A knowledge product that propagates errors into a user's personal knowledge base destroys its own value proposition. The product must:
1. Always show sources (Footprints + Citations)
2. Flag uncertainty (Caveat + Confidence levels)
3. Allow easy correction (Edit + Regenerate)
4. Separate AI-generated from human-curated content ([[concepts/vault-separation]])
5. Build trust incrementally through accurate, consistent performance

## Sources
- [[sources/schmidt-designing-human-ai-collaboration]] — "trust, not attention, is the true currency"
- [[sources/smashing-practical-xai-ux]] — XAI design patterns for trust
- [[sources/microsoft-copilot-ux-guidance]] — appropriate friction and trust lifecycle
- [[sources/shapeof-ai-ux-patterns]] — Trust Builder patterns
- [[sources/arxiv-interface-design-human-ai-decisions]] — empirical evidence on trust failures

## Related Concepts
- [[concepts/trust-calibration]] — the research field studying appropriate trust levels
- [[concepts/explainable-ai-ux]] — transparency mechanisms for trust
- [[concepts/hallucination-contamination]] — the consequence of over-trust
- [[concepts/human-in-the-loop]] — control mechanisms that support trust
