---
title: "Trust Calibration"
type: concept
sources: ["[[sources/arxiv-interface-design-human-ai-decisions]]", "[[sources/smashing-practical-xai-ux]]", "[[sources/schmidt-designing-human-ai-collaboration]]"]
related: ["[[concepts/trust-in-ai]]", "[[concepts/explainable-ai-ux]]", "[[concepts/progressive-disclosure-ai]]", "[[concepts/human-ai-collaboration]]"]
last_compiled: 2026-04-05
summary: "The research field studying how to match user reliance on AI with actual AI reliability — the engagement-overload paradox means more explanation can backfire, requiring careful interface calibration."
---

## Overview

Trust calibration is the alignment between user reliance on AI and the AI system's actual reliability. Proper calibration means users trust AI output proportionally to its accuracy — trusting high-confidence correct outputs and questioning low-confidence or incorrect ones.

The field has grown dramatically since 2012, driven by increasing AI complexity and deployment in high-stakes domains (healthcare, legal, finance).

## The Engagement-Overload Paradox

[[sources/arxiv-interface-design-human-ai-decisions]] reveals the central design tension: **mechanisms that prompt deeper engagement often create excessive cognitive burden, paradoxically harming decision outcomes.**

In a 108-participant study:
- **AI confidence levels** improved calibration (simple signal, low cognitive cost)
- **Text explanations** improved trust and decisions (brief reasoning)
- **Cognitive forcing functions** (reflection prompts) *reduced* performance by increasing cognitive load
- **Higher cognitive effort damaged trust** — an inverted U-curve

This means: you cannot just show more reasoning and expect better outcomes. [[concepts/progressive-disclosure-ai]] is the solution — show simple confidence signals by default, elaborate reasoning on demand.

## Calibration Mechanisms

### Low Cognitive Cost (Always Show)
- Confidence levels (numeric or visual)
- Simple "Because" statements ([[sources/smashing-practical-xai-ux]])
- Source citations
- AI vs. human content labels

### Medium Cognitive Cost (On Demand)
- Feature importance explanations
- Counterfactual alternatives ("would be approved if...")
- Reasoning traces
- Source comparison

### High Cognitive Cost (Deep Dive Only)
- Full chain-of-thought reasoning
- Model comparison
- Data provenance exploration
- Manual verification workflows

## Failure Modes

### Over-Trust (Automation Bias)
Users follow AI recommendations regardless of accuracy. Most common with:
- High-confidence AI outputs (even when wrong)
- Time pressure
- Low domain expertise
- Anthropomorphized AI personalities

### Under-Trust (Automation Disuse)
Users ignore AI even when it is correct. Most common with:
- Previous negative experiences
- Excessive error messaging
- Unfamiliar technology
- Over-complex explanations that reduce comprehension

## Design Implications for Knowledge Products

For [[concepts/knowledge-base-product-gap]], trust calibration means:
1. **Default to simplicity**: Show answers with inline citations, not reasoning chains
2. **Confidence signals**: Indicate when synthesis is well-supported vs. speculative
3. **Source accessibility**: One click from claim to source — the "Highlight Reel" pattern
4. **Progressive depth**: Summary → sources → raw material (3 layers max)
5. **Error acknowledgment**: Actively flag when information may be outdated or conflicting

## Sources
- [[sources/arxiv-interface-design-human-ai-decisions]] — the engagement-overload paradox
- [[sources/smashing-practical-xai-ux]] — practical XAI calibration patterns
- [[sources/schmidt-designing-human-ai-collaboration]] — trust as cumulative experience

## Related Concepts
- [[concepts/trust-in-ai]] — the broader trust framework
- [[concepts/explainable-ai-ux]] — the mechanisms for calibration
- [[concepts/progressive-disclosure-ai]] — the UX solution to the paradox
- [[concepts/human-ai-collaboration]] — calibration enables effective collaboration
