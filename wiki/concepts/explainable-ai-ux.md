---
title: "Explainable AI UX"
type: concept
sources: ["[[sources/smashing-practical-xai-ux]]", "[[sources/shapeof-ai-ux-patterns]]", "[[sources/arxiv-interface-design-human-ai-decisions]]"]
related: ["[[concepts/trust-in-ai]]", "[[concepts/trust-calibration]]", "[[concepts/progressive-disclosure-ai]]", "[[concepts/ai-ux-design-patterns]]"]
last_compiled: 2026-04-05
summary: "Four practical design patterns for making AI explainable in products: Because Statement, What-If Interactive, Highlight Reel, Push-and-Pull Visual — plus the warning that explanation can backfire if it creates excessive cognitive load."
---

## Overview

Explainable AI UX (XAI UX) bridges the gap between AI research on interpretability and practical product design. The core user question is simply: **"Why?"** — Why did the AI make this recommendation? Why was this result ranked first? Why was my request denied?

The challenge is that raw explanations from XAI research (attention maps, SHAP values, activation traces) are meaningless to most users. XAI UX translates these into interfaces that build [[concepts/trust-in-ai]] without requiring technical literacy.

## Two Core Techniques

### Feature Importance
Identifies the 2-3 most influential factors in an AI decision. Example: a churn prediction reveals "support calls in the last month" and "recent price increases" were most influential. Translates to: simple, prioritized reasons.

### Counterfactuals
Shows what would need to change for a different outcome. Example: "Your application would be approved if your credit score were 50 points higher." Translates to: actionable guidance.

## Four Design Patterns

### 1. The "Because" Statement
A single, clear, jargon-free sentence explaining the primary reason. Lowest cognitive cost. Always appropriate as Layer 1 in [[concepts/progressive-disclosure-ai]].

**Example**: "This article was ranked first because it mentions all three of your search terms and was published this week."

### 2. The "What-If" Interactive
Sliders, inputs, and toggles that let users explore how changing variables affects outcomes. Medium cognitive cost. Best for decisions users want to understand deeply (financial, medical, career).

**Example**: Loan calculator showing how different credit scores, income levels, or down payments change approval probability.

### 3. The Highlight Reel
Visual connections linking AI claims to source content. Highlighting relevant document sections, connecting citations to specific claims. Essential for knowledge products where [[concepts/hallucination-contamination]] is a risk.

**Example**: Perplexity's inline citations that highlight the specific passage in the source when clicked.

### 4. The Push-and-Pull Visual
Simple charts showing positive and negative influence factors. A visual representation of feature importance. Good for dashboards and analytics contexts.

**Example**: A horizontal bar chart showing which factors pushed a recommendation score up vs. down.

## The Explainability Paradox

[[sources/arxiv-interface-design-human-ai-decisions]] shows that **more explanation is not always better**. Cognitive forcing functions (mechanisms that make users engage more deeply with explanations) actually reduce performance in high-stakes decisions. The relationship between explanation depth and user performance is an inverted U-curve.

This means XAI UX must use [[concepts/progressive-disclosure-ai]] — simple explanations by default, deeper reasoning on demand — rather than forcing comprehensive transparency on all users.

## Explainability Washing

[[sources/smashing-practical-xai-ux]] warns about "explainability washing" — using oversimplified or strategically framed explanations to *appear* transparent while obscuring problematic behavior. Genuine XAI requires verifiable, meaningful explanations that actually help users make better decisions.

## Regulatory Context

The EU AI Act (applicable 2026) will enforce that users are informed when interacting with AI systems, creating a compliance floor for XAI UX that all products must meet.

## Sources
- [[sources/smashing-practical-xai-ux]] — four design patterns and Goldilocks Principle
- [[sources/shapeof-ai-ux-patterns]] — Governors patterns (Citations, Stream of Thought, Footprints)
- [[sources/arxiv-interface-design-human-ai-decisions]] — the explainability paradox

## Related Concepts
- [[concepts/trust-in-ai]] — XAI is a primary trust-building mechanism
- [[concepts/trust-calibration]] — explanations calibrate user reliance
- [[concepts/progressive-disclosure-ai]] — the delivery mechanism for explanations
- [[concepts/ai-ux-design-patterns]] — XAI patterns within the broader taxonomy
