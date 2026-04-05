---
title: "Source: STORM — Automating Wikipedia Article Creation with LLMs"
type: source-summary
source: "[[raw/storm-automated-wiki-creation]]"
related: ["[[concepts/automated-wiki-creation]]", "[[concepts/llm-knowledge-base]]", "[[concepts/wiki-compilation]]"]
last_compiled: 2026-04-05
summary: "STORM system: multi-perspective question-asking + retrieval → automated Wikipedia-style article generation with FreshWiki evaluation dataset, contrasting single-shot creation vs. Karpathy's accumulating KB."
---

## Key Points
- STORM = Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking
- Three phases: perspective discovery (from related Wikipedia ToCs) → multi-turn expert conversations → outline synthesis
- Introduced **FreshWiki** dataset: recent Wikipedia articles after LLM training cutoffs (prevents data leakage)
- Metrics: heading/entity recall for outlines; ROUGE + entity recall for articles; expert Wikipedia editor rubrics
- Remaining challenges: source bias, red herring fallacy, multi-modal content, balanced retrieval

## Detailed Summary

STORM tackles the pre-writing phase of Wikipedia article creation — research and outline generation — rather than just text production. By simulating conversations between LLMs playing different perspectives, it generates more comprehensive and balanced coverage.

The key innovation vs. naive retrieval: simulating N perspectives (identified from related Wikipedia ToCs) as distinct "expert" personas that ask different questions about the topic. This mirrors human research behavior (consulting multiple experts) and produces richer outlines.

FreshWiki addresses a critical evaluation problem: LLMs trained before a Wikipedia article was written can't have "leaked" knowledge of it, making it a fair test of generation quality.

**Contrast with Karpathy's approach:**
- STORM: single-shot article generation from web search, no persistent KB, produces one article per run
- Karpathy/LLM-KB: persistent, accumulating, incrementally updated knowledge base
- STORM: better for standalone reference articles; LLM-KB better for compounding research knowledge

## Related Concepts
- [[concepts/automated-wiki-creation]] — STORM's core contribution
- [[concepts/wiki-compilation]] — related process in LLM-KB
- [[concepts/llm-knowledge-base]] — the contrasting persistent approach
