---
title: "FreshWiki"
type: entity
entity_type: dataset
sources: ["[[sources/storm-automated-wiki-creation]]"]
related: ["[[entities/storm]]", "[[concepts/automated-wiki-creation]]"]
last_compiled: 2026-04-06
summary: "An evaluation dataset of recent Wikipedia articles created after LLM training cutoffs, introduced by the STORM project to prevent data leakage in automated wiki generation benchmarks."
reading_time: "2 min"
---

## Overview

FreshWiki is an evaluation dataset introduced alongside the [[entities/storm]] system for benchmarking automated Wikipedia article generation. It consists of Wikipedia articles that were created after the training data cutoff dates of the LLMs being evaluated, ensuring that the models cannot have memorized the target articles during pre-training. This addresses a critical evaluation challenge: if an LLM has seen the Wikipedia article it is supposed to "generate" during training, the benchmark measures recall rather than genuine generation capability.

## Key Features

- **Temporal filtering**: Articles are selected based on creation dates that post-date LLM training cutoffs, providing a clean evaluation signal free of data leakage.

- **Wikipedia-quality reference**: Because the articles are actual Wikipedia entries, they meet Wikipedia's editorial standards for coverage, neutrality, verifiability, and structure -- providing high-quality reference outputs for comparison.

- **Multi-dimensional evaluation**: FreshWiki supports assessment through heading soft recall and entity recall (outline quality), ROUGE scores and entity recall (article quality), and expert rubrics from experienced Wikipedia editors evaluating interest, coherence, relevance, coverage, and verifiability.

## Role in LLM Knowledge Bases

FreshWiki is significant beyond the STORM project because it highlights a general problem in evaluating LLM-generated knowledge: distinguishing genuine synthesis from memorization. For LLM knowledge base systems like Karpathy's, this distinction matters during linting and quality assessment. An LLM that appears to generate accurate wiki content may simply be recalling training data rather than synthesizing from the provided raw sources. FreshWiki's temporal filtering methodology provides a blueprint for designing evaluations that test genuine compilation capability.

## Mentioned In

- [[sources/storm-automated-wiki-creation]] -- introduced as STORM's evaluation dataset to prevent data leakage in benchmarking
