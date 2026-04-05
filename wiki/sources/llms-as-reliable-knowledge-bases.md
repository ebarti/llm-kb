---
title: "Source: Large Language Models as Reliable Knowledge Bases?"
type: source-summary
source: "[[raw/llms-as-reliable-knowledge-bases]]"
related: ["[[concepts/llms-as-knowledge-bases]]", "[[concepts/hallucination-contamination]]", "[[concepts/knowledge-representation]]", "[[concepts/neural-symbolic-integration]]"]
last_compiled: 2026-04-05
summary: "2024 evaluation finding LLMs cannot reliably replace traditional KBs: best model (gpt-3.5-turbo) achieved only 32% consistently correct rate, with fundamental trade-offs between seen/unseen knowledge and factuality/consistency."
---

## Key Points
- LLMs store knowledge probabilistically in parameters — fundamentally different from deterministic KBs
- Best model (gpt-3.5-turbo) achieved only 32% Net Consistently Correct Rate on seen knowledge
- Larger models: better on seen knowledge but worse on unseen — no free lunch
- Models consistent in correct answers are also consistent in wrong answers
- Hallucination, staleness, and inconsistency across paraphrased queries are fundamental limitations
- Conclusion: LLMs complement but cannot replace structured knowledge bases

## Detailed Summary

This paper rigorously evaluates whether LLMs can serve as reliable knowledge bases, measuring both factuality (are answers correct?) and consistency (are answers stable across equivalent queries?).

The findings are sobering for anyone hoping LLMs can replace traditional [[concepts/knowledge-representation]] systems. Even the best-performing model achieved only 32% consistently correct responses. Performance diverges sharply between familiar and unfamiliar knowledge domains, with no model excelling at both. Fine-tuning helps with unfamiliar knowledge but degrades performance on previously known facts.

Most concerning: models that are highly consistent in giving correct answers are also highly consistent in confidently giving wrong answers. This means reliability cannot be inferred from consistency alone.

The paper directly supports the hybrid approach motivating modern [[concepts/llm-knowledge-base]] systems: use structured, explicit knowledge representations (whether [[concepts/knowledge-graph]]s, markdown wikis, or traditional databases) as the source of truth, with LLMs providing the intelligence layer for querying, synthesis, and maintenance. This is precisely the architecture Karpathy's LLM-KB system implements and what [[entities/doug-lenat]]'s final paper proposed for [[entities/cyc-project]]+LLM integration.

## Related Concepts
- [[concepts/llms-as-knowledge-bases]] — the question this paper addresses
- [[concepts/hallucination-contamination]] — the core risk identified
- [[concepts/knowledge-representation]] — what LLMs are evaluated against
- [[concepts/llm-knowledge-base]] — the hybrid approach this motivates
- [[concepts/neural-symbolic-integration]] — the broader paradigm
