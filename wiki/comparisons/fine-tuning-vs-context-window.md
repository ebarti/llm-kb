---
title: "Fine-Tuning vs. Context Window"
type: comparison
subjects: ["[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/data-quality-bottleneck]]"]
sources: ["[[sources/pebblous-cheap-ontology]]", "[[sources/decodingai-second-brain-rag]]", "[[sources/karpathy-llm-knowledge-bases]]"]
last_compiled: 2026-04-06
summary: "Comparing two strategies for giving LLMs domain knowledge: fine-tuning (encoding knowledge in model weights) vs. context window retrieval (loading knowledge at query time)."
---

## Overview

When building an LLM knowledge base, a fundamental question is where the knowledge should live: in the model's weights (via fine-tuning) or in its context window (via retrieval at query time). Karpathy's current approach is firmly context-window-based -- the LLM reads wiki articles into context and synthesizes answers. But he explicitly identifies fine-tuning as a future direction: using the wiki to generate synthetic Q&A for training a domain-specific model that "knows" the corpus in its weights. The Decoding AI pipeline implements both, fine-tuning [[entities/llama]] 3.1 8B while also running a RAG pipeline.

The quantitative evidence from [[sources/pebblous-cheap-ontology]] is clear: fine-tuning achieves only 50.4% accuracy on new facts versus RAG's 87.5%. However, the hybrid RAFT approach (domain fine-tuning + RAG) achieves 86%, suggesting the optimal path combines both strategies.

## Comparison Table

| Dimension | Fine-Tuning (Weights) | Context Window (Retrieval) |
|-----------|---------------------|--------------------------|
| Knowledge location | Baked into model weights | Loaded at query time |
| New fact accuracy | 50.4% (Pebblous data) | 87.5% (RAG) / ~100% (index-based) |
| Update mechanism | Full retrain or LoRA update | Edit/recompile wiki files |
| Update speed | Hours to days | Immediate (file edit) |
| Cost | $2K-$20K per training run | API costs per query |
| Hallucination risk | Permanent (baked into weights) | Correctable (edit source files) |
| Knowledge freshness | Stale until retrained | Always current |
| Infrastructure | Training pipeline + GPU | LLM API + file system |
| Scale | Unlimited (in weights) | Limited by context window (~1M-2M tokens) |
| Auditability | None (black box) | High (source tracing) |
| Best for | Stable domain knowledge, style/format | Dynamic knowledge, factual accuracy |

## Detailed Analysis

**The accuracy gap**: The Pebblous analysis cites research showing fine-tuning achieves only 50.4% accuracy on new facts -- barely better than random for a knowledge base application. This is because fine-tuning optimizes for pattern reproduction rather than factual recall. The model learns the distribution of the training data, not the specific facts in it. RAG, by contrast, delivers the actual source text to the model at query time, achieving 87.5% accuracy.

**The permanence problem**: When you fine-tune on hallucinated or outdated data, the error is baked into weights permanently. Tanwar et al. (2024) demonstrated that fine-tuning on hallucinated data causes "poor calibration" that cannot be corrected without retraining. In a context window approach, correcting an error is as simple as editing the wiki article -- the next query will use the corrected version.

**The scale advantage**: Fine-tuning's unique advantage is scale. There is no context window limit -- the model can "know" an arbitrarily large corpus in its weights. For knowledge bases that grow far beyond 1M tokens (the approximate limit of current context windows), fine-tuning or RAG become necessary because index-based navigation no longer fits in context.

**The hybrid future**: The RAFT approach (Retrieval-Augmented Fine-Tuning) combines both: fine-tune the model on domain-specific data to teach it the domain's patterns and vocabulary, then augment with retrieval for specific factual queries. This achieves 86% accuracy -- nearly matching pure RAG while adding the benefits of domain familiarity. Karpathy's stated future direction of generating synthetic Q&A from the wiki for fine-tuning aligns with this hybrid strategy.

**Context window expansion**: The 1,000-fold expansion in context windows over five years (GPT-3's 2K to Gemini 2.0 Pro's 2M) continually shifts the crossover point. As context windows grow, the threshold at which fine-tuning becomes necessary moves higher, extending the viability of the simpler context-window approach.

## When to Use Each

**Use context window retrieval when:**
- Knowledge changes frequently (product info, competitive landscape)
- Factual accuracy is critical
- You need full auditability and source tracing
- Your knowledge base fits within context window limits
- You want immediate updates without retraining

**Use fine-tuning when:**
- Knowledge is stable and well-established (textbook domains)
- You need the model to adopt domain-specific patterns, style, or vocabulary
- Your corpus exceeds context window limits
- You want to reduce per-query token costs (smaller prompts)
- You are building a production model for a specific domain

**Use both (hybrid RAFT) when:**
- You need both domain familiarity and factual accuracy
- Some knowledge is stable (suitable for weights) while other knowledge changes (suitable for retrieval)
- You can afford the infrastructure for both training and retrieval pipelines

## Sources

- [[sources/pebblous-cheap-ontology]] -- quantitative accuracy comparison: RAG 87.5% vs. fine-tuning 50.4% vs. RAFT 86%
- [[sources/decodingai-second-brain-rag]] -- production implementation of fine-tuning (Llama 3.1 8B) + RAG (MongoDB vector search)
- [[sources/karpathy-llm-knowledge-bases]] -- identifies synthetic data generation + fine-tuning as future direction
