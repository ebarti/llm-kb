---
title: "Source: RAG Evaluation — Metrics, Benchmarks, and Enterprise Best Practices"
type: source-summary
source: "[[raw/rag-evaluation-metrics-benchmarks]]"
related: ["[[concepts/rag-evaluation]]", "[[concepts/retrieval-augmented-generation]]", "[[entities/ragas]]"]
last_compiled: 2026-04-05
summary: "Comprehensive guide to RAG evaluation covering retrieval metrics (Precision@k, MRR, nDCG), generation metrics (faithfulness, hallucination rate), benchmarks (RAGBench, CRAG), and frameworks (Ragas, ARES, LangSmith)."
reading_time: "1 min"
---

## Key Points

- Three evaluation dimensions: factual accuracy, retrieval relevance, operational performance
- Retrieval metrics: Precision@k, Recall@k, MRR, nDCG
- Generation metrics: Faithfulness, Answer Relevance, Citation Coverage, Hallucination Rate
- Key benchmarks: RAGBench (100k examples), CRAG, LegalBench-RAG, WixQA, T²-RAGBench
- Frameworks: Ragas (open-source), ARES (adversarial), LangSmith (experiment tracking), AWS Bedrock, Vertex AI
- Test sets: golden datasets + synthetic generation + human review
- Evaluation must be continuous in production via A/B tests and monitoring

## Detailed Summary

This article provides a structured framework for [[concepts/rag-evaluation]]. The three-tier evaluation model separates retrieval quality (did we find the right documents?), generation quality (did we produce a faithful answer?), and operational quality (is it fast, safe, and compliant enough?).

The benchmark landscape has matured significantly, with [[entities/ragas]] emerging as the dominant open-source evaluation framework. RAGBench offers 100,000 examples for general testing, while specialized benchmarks like LegalBench-RAG address domain-specific compliance needs.

## Related Concepts

- [[concepts/rag-evaluation]] — the discipline covered
- [[concepts/retrieval-augmented-generation]] — what's being evaluated
- [[entities/ragas]] — key evaluation framework
