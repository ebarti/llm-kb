---
title: "Collaborative UX"
type: concept
sources: ["[[sources/microsoft-copilot-ux-guidance]]", "[[sources/uxforai-12-llm-product-practices]]", "[[sources/schmidt-designing-human-ai-collaboration]]"]
related: ["[[concepts/human-ai-collaboration]]", "[[concepts/copilot-pattern]]", "[[concepts/trust-in-ai]]", "[[concepts/ai-ux-design-patterns]]"]
last_compiled: 2026-04-05
summary: "Microsoft's UX framework for productive human-AI interaction: tight input-output feedback loops, prompt/output history, appropriate friction at key moments, fact-checking through citations, and editable outputs — users guide AI toward their goals through iterative collaboration."
---

## Overview

Collaborative UX is [[entities/microsoft]]'s framework for designing AI interactions where users and AI work together iteratively. Rather than a single prompt-response exchange, collaborative UX creates a **continuous feedback loop** where input quality drives output quality, and users progressively guide the AI toward their desired outcome.

The framework is grounded in a key insight: AI copilots are "probabilistic" systems that will make mistakes. The UX must acknowledge this reality by empowering users to detect, correct, and refine AI outputs rather than hiding imperfection.

## Core Components

### Input Design
1. **Suggestions and affordances**: Help users form good inputs (large input boxes, character counters, promptbooks)
2. **Structured inputs**: Split one general prompt into multiple fields (title, details, images, tone)
3. **Customization**: Predefined tone options changeable within a conversation
4. **Multimodal**: Voice, text, and multi-lingual options

### Output Design
1. **Input-output together**: Tight feedback loop so users connect output quality to input choices
2. **History**: Timeline of outputs for comparison and reuse; users can try new inputs without losing previous good outputs
3. **Appropriate friction**: Slow users at save/share/copy to force review — counterintuitive but essential
4. **Citations**: References from source data, direct quotes, links to specific locations
5. **Editable outputs**: Users modify AI output to add context, personal touch, or correct errors
6. **Withholding**: Sometimes no answer is better than a harmful one
7. **Feedback mechanisms**: Accuracy ratings, correction options, thumbs up/down

### The Customer-as-Trainer Model
[[sources/uxforai-12-llm-product-practices]] extends collaborative UX to product development itself: user feedback directly improves the model. The first iteration explicitly prioritizes data collection over product perfection. This creates a virtuous cycle where the product gets better *because* users interact with it.

## Appropriate Friction

The most counterintuitive principle in collaborative UX. Traditional UX removes friction; AI UX **adds it at key moments**:

- **Before sharing**: "You're about to share AI-generated content. Review it first."
- **Before saving**: "This AI output may contain inaccuracies. Review before saving."
- **Before copying**: Remind users they take ownership of pasted content
- **AI disclaimers**: Persistent labels on AI-generated content

This friction serves [[concepts/trust-in-ai]] by preventing [[concepts/hallucination-contamination]] — users who automatically propagate AI errors undermine their own knowledge base.

## Sources
- [[sources/microsoft-copilot-ux-guidance]] — the collaborative UX framework
- [[sources/uxforai-12-llm-product-practices]] — customer-as-trainer model
- [[sources/schmidt-designing-human-ai-collaboration]] — resilience and co-creation principles

## Related Concepts
- [[concepts/human-ai-collaboration]] — the broader paradigm collaborative UX implements
- [[concepts/copilot-pattern]] — the architecture collaborative UX serves
- [[concepts/trust-in-ai]] — appropriate friction builds trust
- [[concepts/ai-ux-design-patterns]] — collaborative UX draws on multiple pattern categories
