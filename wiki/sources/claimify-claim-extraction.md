---
title: "Source: Claimify — Extracting High-Quality Claims from LLM Outputs"
type: source-summary
source: "[[raw/claimify-claim-extraction]]"
related: ["[[concepts/claim-extraction]]", "[[concepts/information-extraction]]", "[[entities/claimify]]"]
last_compiled: 2026-04-05
summary: "Microsoft's Claimify (ACL 2025) decomposes LLM outputs into independently verifiable atomic claims via a 4-stage pipeline, achieving 99% entailment with source sentences."
reading_time: "2 min"
---

## Key Points

- Accepted at ACL 2025 — premier NLP conference
- Four-stage pipeline: sentence splitting, selection (filter non-verifiable), disambiguation, decomposition
- 99% of extracted claims are entailed by their source sentence
- First system to flag multiple possible interpretations rather than arbitrarily resolving ambiguity
- Six evaluation metrics: Atomicity, Fluency, Decontextualization, Faithfulness, Focus, Coverage

## Detailed Summary

[[entities/claimify]] addresses a critical problem for [[concepts/information-extraction]] pipelines: when LLMs generate complex outputs, how do you break them into verifiable atomic statements? Traditional methods suffer from extracting non-verifiable opinions, omitting context, misrepresenting meaning, or creating ambiguous claims.

Claimify's four-stage pipeline is directly relevant to [[concepts/wiki-compilation]]:

1. **Sentence Splitting**: Segment text with surrounding context preserved
2. **Selection**: LLM identifies and removes non-verifiable content (opinions, hedges)
3. **Disambiguation**: Detects ambiguity; flags unresolvable cases rather than guessing
4. **Decomposition**: Creates standalone, independently verifiable claims

The disambiguation stage is the key innovation — recognizing when source text has multiple valid interpretations and extracting claims only with high confidence. This connects to [[concepts/hallucination-contamination]]: if claims are extracted ambiguously, fact-checking may produce misleading verdicts.

Beyond fact-checking, Claimify is being used to evaluate comprehensiveness and diversity in systems like GraphRAG — making it a general-purpose extraction quality tool.

## Related Concepts

- [[concepts/claim-extraction]] — the core task
- [[concepts/information-extraction]] — parent discipline
- [[concepts/hallucination-contamination]] — Claimify prevents ambiguous claims from corrupting downstream verification
- [[concepts/linting-and-health-checks]] — claim extraction could power wiki fact-checking
