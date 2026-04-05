---
title: "Automated Fact-Checking"
type: concept
sources: ["[[sources/openfactcheck-factuality-framework]]", "[[sources/datadog-hallucination-detection]]", "[[sources/confident-ai-llm-evaluation-metrics]]"]
related: ["[[concepts/hallucination-detection]]", "[[concepts/faithfulness-and-groundedness]]", "[[concepts/llm-as-judge]]", "[[concepts/llm-knowledge-base]]", "[[entities/openfactcheck]]"]
last_compiled: 2026-04-05
summary: "Automated verification of LLM-generated claims against external knowledge: claim decomposition, evidence retrieval, verdict generation — using frameworks like OpenFactCheck, FIRE, and VERIFAID to complement faithfulness checking."
---

## Overview

Automated fact-checking verifies whether claims made by LLMs are **factually true**, not just consistent with provided context. This goes beyond [[concepts/faithfulness-and-groundedness]] (which only checks consistency with retrieved documents) to verify claims against external knowledge sources.

The distinction matters: a response can be perfectly faithful to its context but factually wrong if the source material contains errors. For [[concepts/llm-knowledge-base]] systems, automated fact-checking is the defense against errors in raw sources propagating into the wiki.

## The Fact-Checking Pipeline

Most automated fact-checking systems follow a three-step pipeline:

### 1. Claim Decomposition
Break complex statements into individual, verifiable claims. [[entities/openfactcheck]]'s Claim Processor supports multiple decomposition strategies from different systems (RARR, FacTool, FactCheckGPT).

### 2. Evidence Retrieval
For each claim, gather relevant evidence from authoritative sources. Methods include:
- Web search for real-time information
- Knowledge graph lookup for structured facts
- Database queries for domain-specific knowledge
- RAG over curated document collections

### 3. Verdict Generation
Compare each claim against retrieved evidence and classify as supported, contradicted, or insufficient evidence. Methods include:
- NLI models (entailment/contradiction/neutral)
- LLM-as-judge with evidence context
- Ensemble approaches combining multiple signals

## Key Systems

### OpenFactCheck
[[entities/openfactcheck]] unifies LLM factuality evaluation with three modules:
- **ResponseEvaluator**: Modular claim-process-retrieve-verify pipeline
- **LLMEvaluator**: FactQA dataset (6,480 examples, 482 domains)
- **FactCheckerEvaluator**: FactBench (4,507 human-annotated examples)

### FIRE (Fact-checking with Iterative Retrieval)
Reduces computational costs dramatically: **7.6x less LLM computation** and **16.5x less search cost** through iterative rather than exhaustive retrieval.

### VERIFAID
RAG-based framework using automatically generated and dynamically growing datasets for fake news detection.

### Knowledge Graph Verification
FactCheck combines RAG with an ensemble of LLMs to verify facts within knowledge graphs, enabling structured fact verification.

## Challenges

1. **Time-sensitivity**: Facts change; yesterday's truth may be today's falsehood
2. **Subjectivity**: Many claims involve judgment, not just facts
3. **Scale**: Verifying every claim in a large KB is computationally expensive
4. **Source reliability**: Evidence sources may themselves be unreliable
5. **Nuance**: Claims may be partially true, true in context, or true with caveats

## Application to LLM Knowledge Bases

For [[concepts/llm-knowledge-base]] systems, automated fact-checking should be layered:

1. **During ingestion**: Spot-check raw source claims against external evidence
2. **During compilation**: Verify synthesized claims that combine information across sources
3. **During linting**: Periodically re-check existing wiki content for factual currency
4. **On query**: Flag low-confidence factual claims in answers

This layered approach complements [[concepts/faithfulness-and-groundedness]] checking (which ensures articles are consistent with their sources) with external verification (which ensures sources themselves are accurate).

## Sources

- [[sources/openfactcheck-factuality-framework]] — unified evaluation framework
- [[sources/datadog-hallucination-detection]] — production fact-checking approach
- [[sources/confident-ai-llm-evaluation-metrics]] — factuality as an evaluation metric

## Related Concepts

- [[concepts/hallucination-detection]] — detecting fabricated content (often confused with fact-checking)
- [[concepts/faithfulness-and-groundedness]] — context-relative consistency (narrower than factuality)
- [[concepts/hallucination-contamination]] — what happens when fact-checking fails
- [[concepts/linting-and-health-checks]] — KB maintenance that should include fact-checking
