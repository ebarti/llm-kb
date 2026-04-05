---
title: "RAG vs. Fine-Tuning"
type: comparison
subjects: ["[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/fine-tuning]]"]
sources: ["[[sources/raft-retrieval-augmented-fine-tuning]]", "[[sources/domain-adaptive-pretraining-dapt]]", "[[sources/lora-qlora-efficient-fine-tuning]]", "[[sources/pebblous-cheap-ontology]]", "[[sources/rag-vs-finetuning-agriculture]]"]
last_compiled: 2026-04-05
summary: "RAG injects knowledge at inference time (dynamic, traceable, per-query cost); fine-tuning bakes knowledge into weights (persistent, fast, upfront cost) — hybrid approaches like RAFT combine both."
---

## Overview

The choice between Retrieval-Augmented Generation (RAG) and [[concepts/fine-tuning]] is the most common architectural decision in LLM application design. It maps directly to the [[concepts/weights-vs-context]] question: should domain knowledge live in model weights or be injected through context windows?

In practice, this is rarely an either/or choice. The best systems use both, and [[concepts/raft]] demonstrates that you can even fine-tune a model to be better at RAG.

## Comparison Table

| Dimension | RAG | Fine-Tuning | RAFT (Hybrid) |
|-----------|-----|-------------|---------------|
| **Knowledge location** | Context window | Model weights | Both |
| **Update mechanism** | Update document store | Retrain model | Retrain model |
| **Update cost** | Zero (swap docs) | Medium-high (GPU hours) | Medium-high |
| **Update latency** | Instant | Hours-days | Hours-days |
| **Per-query cost** | Retrieval overhead | Zero additional | Zero additional |
| **Upfront cost** | Index/embed documents | Training compute | Training compute |
| **Traceability** | Full (cite passages) | None | Partial (trained citations) |
| **Hallucination risk** | Lower (grounded) | Higher (memorized) | Lowest (grounded + trained) |
| **Offline capability** | Needs doc store | Full | Full |
| **Latency** | Higher (retrieval step) | Lower | Lower |
| **Context window usage** | Consumes tokens | None | Consumes tokens |
| **Domain accuracy** | Good | Very high | Highest |
| **Catastrophic forgetting** | N/A | Risk | Risk |

## When to Use RAG

- Knowledge changes frequently (news, product catalogs, regulations)
- Citation and traceability are required
- You don't have resources for training
- The knowledge base is too large to memorize
- You need to add knowledge without retraining
- Privacy: documents stay in your infrastructure

## When to Fine-Tune

- Domain-specific behavior needed (terminology, tone, reasoning patterns)
- Latency is critical (no retrieval step)
- Consistent structured outputs (JSON, SQL, domain formats)
- Offline or edge deployment
- Replacing expensive large model API with small fine-tuned model
- The domain is stable and doesn't change frequently

## When to Use Both (Hybrid)

- Maximum accuracy on domain-specific tasks
- Need both stable domain expertise and current facts
- Building a [[concepts/llm-knowledge-base]] that accumulates knowledge over time
- Healthcare, legal, or financial domains requiring both expertise and citation

## The Three-Layer Recommendation

Per the emerging best practice (see [[concepts/weights-vs-context]]):

1. **[[concepts/domain-adaptive-pretraining]]**: Broad domain knowledge in weights
2. **[[concepts/fine-tuning]] (LoRA)**: Task-specific skills in weights
3. **RAG**: Dynamic facts and citations in context

## Cost Comparison

| Resource | RAG | LoRA Fine-Tuning | Full Fine-Tuning |
|----------|-----|------------------|------------------|
| Upfront compute | Low (embedding) | Medium (6GB+ VRAM) | High (60GB+ VRAM) |
| Per-query | Retrieval + extra tokens | Standard inference | Standard inference |
| Data needed | Documents (any format) | Labeled examples (100s-10Ks) | Labeled examples (10Ks+) |
| Human effort | Document curation | Data labeling + evaluation | Data labeling + evaluation |
| Time to deploy | Hours | Days | Days-weeks |

## Connection to LLM Knowledge Bases

In [[concepts/llm-knowledge-base]] systems like Karpathy's:

The current approach is **context-window-based**: the LLM reads wiki articles, summaries, and indexes at query time. This is effectively RAG without a vector database (see [[concepts/rag-vs-index-based-retrieval]]).

The future direction Karpathy suggested is a **hybrid approach**: use the accumulated wiki content to generate [[concepts/synthetic-data-generation|synthetic training data]], then fine-tune a domain-specific model. This would put stable domain knowledge in weights while keeping dynamic facts in the wiki (context).

[[concepts/raft]] is the most promising methodology for this: fine-tune on wiki content with distractor documents, teaching the model to both know the domain and cite its sources.

## Sources

- [[sources/raft-retrieval-augmented-fine-tuning]] — hybrid approach with 35-76% improvements
- [[sources/domain-adaptive-pretraining-dapt]] — deep weight-based domain knowledge
- [[sources/lora-qlora-efficient-fine-tuning]] — practical fine-tuning methods
- [[sources/pebblous-cheap-ontology]] — RAG vs. fine-tuning in ontology context
