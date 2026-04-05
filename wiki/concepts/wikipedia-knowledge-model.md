---
title: "Wikipedia Knowledge Model"
type: concept
sources: ["[[sources/ai-in-wikimedia-projects]]", "[[sources/wikiedu-ai-wikipedia-editing-2025]]", "[[sources/reeves-automated-wikipedia-content-review]]", "[[sources/federated-wiki-cunningham]]", "[[sources/knowledge-commons-overview]]", "[[sources/wisdom-of-the-crowd]]"]
related: ["[[concepts/collective-intelligence]]", "[[concepts/collaborative-knowledge-building]]", "[[concepts/knowledge-commons]]", "[[concepts/ai-generated-content-risks]]", "[[concepts/federated-knowledge]]", "[[concepts/automated-wiki-creation]]"]
last_compiled: 2026-04-05
summary: "Wikipedia's collaborative editorial model — anyone can edit, consensus-driven quality improvement, verifiability over truth, no original research — represents the most successful collective knowledge creation system in history, now under unprecedented stress from AI."
---

## Overview

Wikipedia's knowledge creation model is the most successful implementation of [[concepts/collective-intelligence]] applied to encyclopedic knowledge. Founded on the principle that "anyone can write an encyclopedia," it uses open collaborative editing, community-generated policies, and consensus-driven quality improvement to produce a resource of 60+ million articles in 300+ languages.

The model rests on three core policies: **verifiability** (all claims must be sourceable), **neutral point of view** (no advocacy), and **no original research** (Wikipedia summarizes, not discovers). These policies are enforced not by a central authority but by a distributed community of volunteer editors — a key condition for [[concepts/wisdom-of-crowds]] effects.

## Key Ideas

### The Editorial Process

Wikipedia's quality emerges through an iterative process: "Perfection is not required, as Wikipedia is a work in progress. Collaborative editing means that incomplete or poorly written first drafts can evolve over time into excellent articles." This contrasts with traditional encyclopedias (expert-written, static) and with AI-generated articles ([[concepts/automated-wiki-creation]]) which attempt single-shot perfection.

The process is fundamentally **adversarial-cooperative**: editors with diverse perspectives debate, revert, and refine until strong consensus emerges. Every edit is publicly recorded, creating accountability and institutional memory. This transparent revision history is itself a knowledge artifact — a record of how knowledge was constructed and contested.

### Quality Control Mechanisms

- **Speedy deletion**: For clearly unacceptable content (since August 2025, includes suspected AI-generated articles)
- **Articles for deletion**: Community deliberation on borderline cases
- **Automated tools**: ClueBot NG (vandalism detection via neural networks), ORES (edit quality grading)
- **Community norms**: Notability guidelines, reliable source requirements, citation standards

### Bot History (Pre-LLM)

Wikipedia has a long history with automation, largely positive:
- **rambot** (2002): Created U.S. town articles from census data
- **ClueBot NG** (2010): Neural network vandalism detection
- **ORES** (2015): AI-powered edit quality assessment

These bots augmented editors by handling repetitive tasks while leaving editorial judgment to humans.

### The LLM Disruption (2022-2026)

The post-ChatGPT era fundamentally challenged the model:
- **Princeton study (2024)**: ~5% of new articles showed AI involvement
- **Wiki Education audit**: 5.8% of reviewed articles AI-generated; two-thirds failed verification
- **August 2025**: Speedy deletion for AI-generated articles
- **March 2026**: Prohibited AI content generation entirely (exceptions: copyediting, translation)
- **AI agent controversy**: Tom-Assistant autonomously editing Wikipedia in 2025

The key issue is not that AI produces uniformly bad content — 87% of editors found AI helpful for research — but that AI-generated text violates the core policy architecture: it cannot reliably be verified, tends toward promotional language, and produces subtle misattributions rather than outright fabrications.

### Wikipedia as AI Training Data

Wikipedia occupies a paradoxical position: it is "the mother lode for human-generated text available for machine learning" and simultaneously the system most threatened by AI outputs fed back into it. An 8% visitor decrease in 2025 was attributed to AI summaries, and the Wikimedia Foundation now charges for API access to recover scraping costs.

## Comparison with Alternative Models

| Dimension | Wikipedia | [[concepts/federated-knowledge]] | [[concepts/automated-wiki-creation]] (STORM) | [[concepts/llm-knowledge-base]] (Karpathy) |
|-----------|-----------|---------------------|---------------------|---------------------|
| Authority | Consensus | Distributed/individual | AI (single-shot) | LLM (persistent) |
| Perspective | Neutral POV | Multi-POV | Multi-perspective input | Owner-defined |
| Scale | 60M+ articles | Varies per instance | Per-query | ~100 articles |
| Verification | Community review | Self-governed | Source-attributed | Source traceable |
| AI role | Contested | N/A (pre-AI) | Core creator | Core compiler |

## Sources

- [[sources/ai-in-wikimedia-projects]] — full history of AI in Wikipedia
- [[sources/wikiedu-ai-wikipedia-editing-2025]] — audit of AI-generated content quality
- [[sources/reeves-automated-wikipedia-content-review]] — systematic review of automation research
- [[sources/federated-wiki-cunningham]] — the alternative multi-POV model
- [[sources/wisdom-of-the-crowd]] — WoC conditions Wikipedia satisfies

## Related Concepts

- [[concepts/collective-intelligence]] — Wikipedia as the paradigmatic CI system
- [[concepts/collaborative-knowledge-building]] — the process Wikipedia implements
- [[concepts/knowledge-commons]] — Wikipedia as the largest knowledge commons
- [[concepts/ai-generated-content-risks]] — the current threat to the model
- [[concepts/federated-knowledge]] — the alternative distributed approach
- [[concepts/automated-wiki-creation]] — AI attempting Wikipedia's function
- [[concepts/hallucination-contamination]] — AI errors entering the encyclopedic record
