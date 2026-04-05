---
title: "Claim Extraction and Fact Decomposition"
type: concept
sources: ["[[sources/claimify-claim-extraction]]"]
related: ["[[concepts/information-extraction]]", "[[concepts/llm-summarization]]", "[[concepts/hallucination-contamination]]", "[[concepts/linting-and-health-checks]]", "[[entities/claimify]]"]
last_compiled: 2026-04-05
summary: "Breaking complex LLM outputs into atomic, independently verifiable claims — essential for fact-checking, wiki quality assurance, and preventing hallucination propagation."
---

## Overview

Claim extraction decomposes complex text into simple, independently verifiable statements ("atomic claims"). Given a paragraph about a research paper, claim extraction might produce:

- "GPT-NER was published at NAACL 2025"
- "GPT-NER uses special marker tokens @@/## to delimit entities"
- "GPT-NER achieves performance comparable to fully supervised baselines"

Each claim can then be independently verified against source material, making claim extraction the foundation of automated fact-checking.

## Why Claim Extraction Matters for Knowledge Bases

In the [[concepts/llm-knowledge-base]] system, every wiki article contains claims synthesized by the LLM from raw sources. If those claims are inaccurate or ambiguous, the error propagates through [[concepts/hallucination-contamination]]:

1. LLM extracts a wrong claim during [[concepts/wiki-compilation]]
2. Wrong claim appears in a concept article
3. Future Q&A queries cite the wrong claim
4. If the KB feeds fine-tuning, the error enters model weights

Claim extraction + verification is the defense against this cascade.

## Claimify: State of the Art

[[entities/claimify]] (Microsoft Research, ACL 2025) implements a four-stage pipeline:

| Stage | Purpose | Output |
|-------|---------|--------|
| Sentence Splitting | Segment with context | Individual sentences |
| Selection | Filter non-verifiable content | Only factual claims |
| Disambiguation | Detect and handle ambiguity | Flagged or resolved claims |
| Decomposition | Create standalone claims | Atomic, independent claims |

Key results: 99% of claims entailed by source sentences. First system to flag unresolvable ambiguity rather than guessing.

## Evaluation Metrics

Six metrics for claim extraction quality:

1. **Atomicity** — each claim contains exactly one piece of information
2. **Fluency** — claims are grammatically correct and readable
3. **Decontextualization** — claims are understandable without surrounding text
4. **Faithfulness** — claims are supported by the source
5. **Focus** — claims contain only verifiable content
6. **Coverage** — all important information is captured

## Atomic Fact Extraction and Verification (AFEV)

An alternative framework that progressively decomposes complex claims into simpler atomic facts, then verifies each via evidence reranking and adaptive validation. Useful for claims that contain multiple sub-claims or conditional statements.

## Applications in Wiki Compilation

Claim extraction could enhance the [[concepts/linting-and-health-checks]] operation:

1. Extract atomic claims from each wiki article
2. Trace each claim back to raw source material
3. Flag claims not supported by any source (potential hallucinations)
4. Identify contradictory claims across articles
5. Quantify wiki coverage (what percentage of source claims are captured?)

## Sources

- [[sources/claimify-claim-extraction]] — 4-stage pipeline, 99% entailment, ACL 2025

## Related Concepts

- [[concepts/information-extraction]] — claim extraction is an IE subtask
- [[concepts/llm-summarization]] — summarization produces claims that need verification
- [[concepts/hallucination-contamination]] — claim extraction is the defense
- [[concepts/linting-and-health-checks]] — claim verification powers wiki linting
- [[concepts/data-quality-bottleneck]] — claim quality determines KB quality
