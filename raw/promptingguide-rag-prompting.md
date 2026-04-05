---
title: "Retrieval Augmented Generation (RAG) Prompting"
source: "https://www.promptingguide.ai/techniques/rag"
author: "DAIR.AI / Prompt Engineering Guide"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [prompt-engineering, rag, retrieval, generation]
type: article
status: raw
discovered_via: search
---

# Retrieval Augmented Generation (RAG) Prompting

## Definition
RAG is a method that combines an information retrieval component with a text generator model for knowledge-intensive tasks. It enables language models to access external knowledge sources, improving factual consistency and reducing hallucinations.

## Core Mechanism
1. Input Retrieval: Takes an input and retrieves relevant supporting documents from a source
2. Context Integration: Concatenates retrieved documents as context with the original prompt
3. Output Generation: Feeds the combined input to a text generator for final response

## Key Advantages
- Adaptive Knowledge: Allows models to bypass retraining for latest information
- Efficiency: Internal knowledge can be modified without retraining
- Reliability: Produces more factual, specific, and diverse responses

## Technical Architecture (Lewis et al., 2021)
- Pre-trained seq2seq model as parametric memory
- Dense vector index of Wikipedia as non-parametric memory
- Neural pre-trained retriever for document access

## Prompting Techniques for RAG
- Query Rewriting: Query2Doc, ITER-RETGEN, HyDE
- N-shot Prompting: Examples showing how tasks should be handled
- Chain-of-Thought: Explicit intermediate reasoning steps
- Clear instructions on what to retrieve and how to use retrieved content

## Key Insight
"Many issues in a RAG pipeline come from prompts that are unclear, overloaded, or inconsistent. Weak retrieval makes things messy, but weak prompts make things unusable."
