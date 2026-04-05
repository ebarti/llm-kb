---
title: "Weights vs. Context Window: Where to Put Knowledge"
type: concept
sources: ["[[sources/raft-retrieval-augmented-fine-tuning]]", "[[sources/domain-adaptive-pretraining-dapt]]", "[[sources/lora-qlora-efficient-fine-tuning]]", "[[sources/rome-memit-knowledge-editing]]", "[[sources/ai-training-2026-synthetic-human-data]]"]
related: ["[[concepts/fine-tuning]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/knowledge-editing]]", "[[concepts/domain-adaptive-pretraining]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "The fundamental design question for LLM applications: which knowledge belongs in model weights (persistent, fast, opaque) vs. context windows (dynamic, traceable, limited) vs. external tools."
---

## Overview

Every LLM application must decide where knowledge lives. This is the central architectural question that Karpathy identified as a future direction for [[concepts/llm-knowledge-base]] systems: should domain knowledge be baked into model weights through [[concepts/fine-tuning]], injected at inference time through context windows (RAG), or some hybrid of both?

The answer depends on the nature of the knowledge, how often it changes, whether traceability matters, and available compute resources.

## The Three Knowledge Locations

### 1. Model Weights (Pretraining + Fine-Tuning)

Knowledge encoded in the model's parameters through training.

**Methods**: [[concepts/continued-pretraining]], [[concepts/domain-adaptive-pretraining]], [[concepts/fine-tuning]], [[concepts/parameter-efficient-fine-tuning|LoRA/QLoRA]], [[concepts/knowledge-editing|ROME/MEMIT]]

**Properties**:
- Persistent: available on every inference without additional retrieval
- Fast: no retrieval latency
- Opaque: no citation or traceability to source
- Expensive to update: requires retraining
- Risk of [[concepts/catastrophic-forgetting]]
- Risk of [[concepts/hallucination-contamination|hallucination]] — no grounding documents

**Best for**: Domain vocabulary, reasoning patterns, output formatting, stable foundational knowledge, professional conventions and tone

### 2. Context Window (RAG / In-Context Learning)

Knowledge injected at inference time through retrieved documents or user-provided context.

**Methods**: RAG, [[concepts/rag-vs-index-based-retrieval|index-based retrieval]], few-shot prompting, system prompts

**Properties**:
- Dynamic: updates instantly when source documents change
- Traceable: can cite specific passages and documents
- Limited: bounded by context window size
- Per-query cost: retrieval overhead on every inference
- Grounded: reduces hallucination by anchoring to source text

**Best for**: Current facts, frequently changing information, knowledge requiring citation, large knowledge bases that exceed what can be memorized in weights

### 3. External Tools (Function Calling / Agents)

Knowledge accessed through API calls, database queries, or tool use at inference time.

**Properties**:
- Real-time: always current (live databases, APIs)
- Unlimited scope: not bounded by context window or training data
- Structured: can access relational data, perform computation
- Highest latency: network calls and computation

**Best for**: Real-time data (stock prices, weather), computation, structured queries, actions (sending emails, updating records)

## The Decision Framework

| Dimension | Weights | Context | Tools |
|-----------|---------|---------|-------|
| Update frequency | Rarely | Frequently | Real-time |
| Latency | None | Medium | High |
| Traceability | None | Full | Full |
| Cost per query | Zero | Retrieval cost | API cost |
| Cost to update | Training cost | Zero (update docs) | Zero |
| Capacity | Bounded by params | Bounded by window | Unlimited |
| Hallucination risk | Higher | Lower (grounded) | Lowest |
| Offline capability | Full | Needs local store | No |

## The Three-Layer Architecture

The emerging best practice combines all three:

1. **[[concepts/domain-adaptive-pretraining]] + Fine-Tuning** → Stable domain expertise in weights
2. **RAG at inference** → Dynamic, traceable facts from document store
3. **Tool use** → Real-time data and computation

[[concepts/raft]] exemplifies this hybrid: fine-tune the model to be good at using retrieved documents, putting retrieval skills in weights and factual knowledge in context.

## For LLM Knowledge Bases Specifically

In Karpathy's [[concepts/llm-knowledge-base]] architecture:

- **Weights**: The LLM's general capabilities + potential domain fine-tuning for better compilation quality
- **Context**: The wiki articles, raw sources, and index files loaded during Q&A and compilation
- **Tools**: Search scripts, web fetch, file system operations

The current system is primarily context-window-based (the LLM reads wiki files). The future direction Karpathy suggested — [[concepts/synthetic-data-generation|generating synthetic training data]] from the KB and [[concepts/fine-tuning|fine-tuning]] on it — would shift some knowledge into weights, creating a model that "natively understands" the KB domain.

The key tension: knowledge in weights is faster and cheaper per query, but loses the traceability and auditability that makes the wiki trustworthy. The practical recommendation is to use weights for capabilities (how to compile, how to cite, how to structure articles) and context for facts (what the sources actually say).

## Sources

- [[sources/raft-retrieval-augmented-fine-tuning]] — hybrid weights + context approach
- [[sources/domain-adaptive-pretraining-dapt]] — putting domain knowledge in weights
- [[sources/lora-qlora-efficient-fine-tuning]] — practical methods for weight modification
- [[sources/rome-memit-knowledge-editing]] — surgical fact editing in weights
- [[sources/ai-training-2026-synthetic-human-data]] — the data needed to populate weights

## Related Concepts

- [[concepts/fine-tuning]] — primary method for putting knowledge in weights
- [[concepts/rag-vs-index-based-retrieval]] — primary method for knowledge in context
- [[concepts/knowledge-editing]] — surgical modification of weight-stored facts
- [[concepts/domain-adaptive-pretraining]] — deep domain knowledge in weights
- [[concepts/llm-knowledge-base]] — the system this architectural question applies to
