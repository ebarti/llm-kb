---
title: "Source: Creating a Dynamic UX — Microsoft Copilot Guidance"
type: source-summary
source: "[[raw/microsoft-copilot-ux-guidance]]"
related: ["[[concepts/copilot-pattern]]", "[[concepts/collaborative-ux]]", "[[concepts/human-in-the-loop]]", "[[entities/microsoft]]"]
last_compiled: 2026-04-05
summary: "Microsoft's official UX guidance for building copilot-style AI: three focus frameworks (Immersive/Assistive/Embedded), three foundational principles (Human in Control, No Anthropomorphizing, Stakeholder Consideration), and detailed input/output design tips."
---

## Key Points
- Three UX focus frameworks: Immersive (full-screen KB), Assistive (side panel), Embedded (inline popup)
- "The more important the task, the more real estate required"
- Principle 1: Human in control — "The human is the pilot." Language matters: "Summarize with copilot" not "Copilot, summarize"
- Principle 2: Avoid anthropomorphizing — no "understand," "think," "feel"; use "processing," "analyzing"
- Principle 3: Design for all stakeholders, including indirect ones impacted by AI outputs
- **Collaborative UX** through tight input-output feedback loops, history, appropriate friction, and fact-checking with citations
- "Add appropriate friction" at save/share/copy — better to slow users than let them propagate AI errors

## Detailed Summary

This is [[entities/microsoft]]'s official guidance for ISVs building generative AI applications, grounded in the [[entities/hax-toolkit]] (Human-AI Experience) research.

The three focus frameworks directly address product architecture decisions for any [[concepts/copilot-pattern]] product:

**Immersive** (full-screen) suits knowledge base exploration, AI dashboards, and security analysis. This is closest to the [[concepts/llm-knowledge-base]] product Karpathy envisions.

**Assistive** (side panel) integrates into existing workflow without context switching. This is GitHub Copilot's model.

**Embedded** (inline) provides context-aware help on specific items. This is Notion AI's inline approach.

The **Collaborative UX** framework is particularly relevant to [[concepts/knowledge-base-product-gap]]. Microsoft frames the user-AI interaction as a tight feedback loop where input quality drives output quality, history enables safe experimentation, and appropriate friction prevents error propagation — echoing the [[concepts/hallucination-contamination]] concern.

## Notable Quotes
> "A copilot is simply a tool to support the user. The human is the pilot."
> "Add AI notices and disclaimers with each output that clearly express AI-generated content may be incorrect."
> "Sometimes it's better for a copilot to give no answer instead of outputting something potentially inappropriate."

## Related Concepts
- [[concepts/copilot-pattern]] — the entire article operationalizes this pattern
- [[concepts/collaborative-ux]] — Microsoft's framework for productive human-AI interaction
- [[concepts/human-in-the-loop]] — Principle 1 and the Governors framework
- [[concepts/trust-in-ai]] — friction, citations, and error handling all serve trust
- [[concepts/hallucination-contamination]] — appropriate friction prevents propagation
