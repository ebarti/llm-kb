---
title: "Source: Progressive Disclosure in AI — Design Pattern"
type: source-summary
source: "[[raw/progressive-disclosure-ai-pattern]]"
related: ["[[concepts/progressive-disclosure-ai]]", "[[concepts/ai-ux-design-patterns]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "Progressive disclosure as AI design pattern: reveal complexity gradually in 2-3 layers max; RAG itself is a progressive disclosure pattern; designs beyond 2 levels have low usability."
---

## Key Points
- Progressive disclosure reveals complexity gradually — simple features first, advanced capabilities as needed
- Limit to 2-3 layers maximum — beyond 2 levels, users get lost
- RAG is fundamentally a progressive disclosure pattern (retrieve relevant chunks vs. front-loading all context)
- Core trade-off: latency vs. accuracy — front-loading gives immediate availability but noise; on-demand keeps context clean but risks missing information
- Real-world examples: Loom (AI transcription), ChatGPT (settings), Google Docs (AI writing suggestions)

## Detailed Summary

This AI UX Design Guide article establishes [[concepts/progressive-disclosure-ai]] as a foundational pattern for managing the complexity inherent in AI products. The key insight is that AI features are inherently complex — models, parameters, confidence levels, reasoning traces — and dumping all of this on users simultaneously causes abandonment.

The implementation approach: present essential information first, offer advanced features through clear interaction triggers (buttons, expandable sections, tooltips).

The connection to [[concepts/rag-vs-index-based-retrieval]] is particularly insightful: RAG itself is progressive disclosure at the data layer. Instead of fine-tuning with all knowledge, retrieve only what is relevant to the current query. This parallels the UI pattern — show only what is relevant to the current interaction.

The 2-3 layer limit from usability research is a hard constraint for product design. For [[concepts/knowledge-base-product-gap]], this means: show the answer first, offer sources second, allow deep-dive into raw material third — and no more.

## Related Concepts
- [[concepts/progressive-disclosure-ai]] — primary topic
- [[concepts/ai-ux-design-patterns]] — one pattern in the broader taxonomy
- [[concepts/rag-vs-index-based-retrieval]] — RAG as progressive disclosure at the data layer
- [[concepts/trust-calibration]] — progressive disclosure calibrates how much reasoning to show
