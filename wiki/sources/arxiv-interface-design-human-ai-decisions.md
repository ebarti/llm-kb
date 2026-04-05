---
title: "Source: How Interface Design Shapes Human-AI Collaboration in High-Stakes Decision-Making"
type: source-summary
source: "[[raw/arxiv-interface-design-human-ai-decisions]]"
related: ["[[concepts/trust-calibration]]", "[[concepts/human-ai-collaboration]]", "[[concepts/explainable-ai-ux]]"]
last_compiled: 2026-04-05
summary: "arXiv study finds human+AI teams perform worse than AI alone due to automation bias; confidence levels and text explanations help, but cognitive forcing functions paradoxically reduce performance by increasing cognitive load."
---

## Key Points
- "Human + AI teams perform worse than AI alone" due to automation bias
- AI confidence levels and text explanations improve collaborative performance
- Cognitive forcing functions (reflection prompts) increase cognitive load and *reduce* performance
- Higher cognitive effort damages trust — an inverted U-curve relationship
- Design must balance engagement depth with cognitive burden

## Detailed Summary

This arXiv paper (2025) provides empirical evidence for a critical insight in [[concepts/trust-calibration]]: more explanation is not always better. In a 108-participant diabetes management study, the researchers tested six decision-support mechanisms.

The finding that **human+AI teams perform worse than AI alone** is the central challenge for all [[concepts/human-ai-collaboration]] product design. The cause is automation bias — users follow AI recommendations even when incorrect.

Mechanisms that worked: **AI confidence levels** (a simple numeric signal) and **text explanations** (brief reasoning). These give users calibration information without excessive cognitive burden.

Mechanisms that backfired: **cognitive forcing functions** — prompts designed to make users think more carefully. While they increased engagement, they increased cognitive load to the point where performance dropped and trust was damaged.

This creates a design paradox directly relevant to [[concepts/knowledge-base-product-gap]]: if you build a knowledge product that shows too much reasoning (e.g., elaborate chain-of-thought traces), you may actually harm user performance. The [[concepts/progressive-disclosure-ai]] pattern is the solution — show simple confidence signals by default, elaborate reasoning on demand.

## Notable Quotes
> "Human + AI teams have been shown to perform worse than AI alone"
> "Strike a balance in CFF and XAI design"

## Related Concepts
- [[concepts/trust-calibration]] — the core research question
- [[concepts/human-ai-collaboration]] — empirical evidence for design tension
- [[concepts/explainable-ai-ux]] — what works vs. what backfires
- [[concepts/progressive-disclosure-ai]] — the solution to the engagement-overload paradox
