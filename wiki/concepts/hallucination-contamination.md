---
title: "Hallucination Contamination"
type: concept
sources: ["[[sources/antigravity-post-code-ai-workflow]]", "[[sources/pebblous-cheap-ontology]]", "[[sources/glenrhodes-karpathy-workflow]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/data-quality-bottleneck]]", "[[concepts/vault-separation]]", "[[concepts/linting-and-health-checks]]"]
last_compiled: 2026-04-05
summary: "The risk that LLM-generated errors written into a wiki propagate into future queries and fine-tuning, corrupting the knowledge base over time."
---

## Overview

Hallucination contamination is the primary systemic risk in LLM-maintained knowledge bases. When an LLM generates an incorrect fact or fabricated connection and writes it into the wiki, that error becomes part of the knowledge substrate used to answer future queries — and, critically, to generate fine-tuning training data.

## Key Ideas

**The contamination cascade:**
1. LLM hallucinates a connection or fact during compilation
2. The error is written into a wiki article
3. Future queries reference this wiki article, propagating the error
4. If the wiki is used to generate synthetic Q&A for fine-tuning, the error is baked into model weights permanently

**Research backing:** Tanwar et al. (2024) demonstrated that fine-tuning on hallucinated data causes "poor calibration," permanently embedding errors into model weights. This is qualitatively worse than a runtime retrieval error — it's an irreversible weight corruption.

**Why it's worse than RAG hallucinations:** In traditional RAG, a hallucinated retrieval result affects one query. In an LLM wiki, it affects all future queries that touch that article, plus any downstream fine-tuning.

## Mitigation Strategies

1. **Vault separation** (Steph Ango, Obsidian CEO): Maintain human-curated content in a separate Obsidian vault from agent-generated content. Never let AI-generated knowledge contaminate your personal knowledge base.

2. **Provenance tracing**: All wiki claims should trace back to `raw/` source files. Unsourced assertions in wiki articles are a red flag.

3. **Linting / health checks**: LLM agents periodically scan the wiki for contradictions, verify claims against source documents, and flag unsupported assertions.

4. **Incremental verification**: When ingesting new sources, explicitly check new content against existing wiki claims for contradictions before writing.

5. **Data quality gates**: Validate raw input quality before ingestion — garbage in, garbage out. Low-quality sources generate low-quality wiki content.

## Sources
- [[sources/antigravity-post-code-ai-workflow]] — identifies hallucination contamination as the main risk; documents vault separation recommendation
- [[sources/pebblous-cheap-ontology]] — quantifies the risk cascade; cites Tanwar et al. on fine-tuning degradation
- [[sources/glenrhodes-karpathy-workflow]] — describes health checks as active mitigation

## Related Concepts
- [[concepts/data-quality-bottleneck]] — contamination starts with bad raw inputs
- [[concepts/vault-separation]] — key mitigation strategy
- [[concepts/linting-and-health-checks]] — active detection and correction
- [[concepts/llm-knowledge-base]] — the system at risk
