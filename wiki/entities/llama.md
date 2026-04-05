---
title: "Llama"
type: entity
entity_type: tool
sources: ["[[sources/decodingai-second-brain-rag]]", "[[sources/jeremy-jordan-distributed-training]]", "[[sources/raschka-pretraining-post-training-paradigms]]", "[[sources/training-costs-2026-analysis]]"]
related: ["[[concepts/second-brain]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/data-quality-bottleneck]]", "[[concepts/llm-pretraining]]", "[[concepts/3d-parallelism]]", "[[concepts/multi-stage-pretraining]]", "[[concepts/distributed-training]]"]
last_compiled: 2026-04-06
summary: "Meta's open-source LLM family, with Llama 3.1 8B used in the Decoding AI second-brain RAG pipeline as the fine-tuned summarization model."
reading_time: "2 min"
---

## Overview

Llama is a family of open-source large language models developed and released by Meta AI. The Llama model family has become one of the most widely adopted open-weight LLM series, enabling organizations to fine-tune and deploy language models on their own infrastructure rather than relying solely on API-based proprietary models. Llama models are available in various sizes (7B, 8B, 13B, 70B, 405B parameters) and have been fine-tuned by the community for a wide range of tasks.

In the context of this knowledge base, Llama 3.1 8B appears as the fine-tuned model in the Decoding AI second-brain RAG pipeline. The Decoding AI course fine-tunes this relatively small model on summarization tasks using distillation techniques and the Unsloth optimization library, then deploys it to Hugging Face Dedicated Endpoints for real-time summarization inference.

## Key Features

- **Open weights**: Unlike proprietary models from OpenAI or Anthropic, Llama weights are downloadable and can be fine-tuned, quantized, and deployed on custom infrastructure.

- **Fine-tuning ecosystem**: Llama's open nature has spawned a rich ecosystem of fine-tuning tools (Unsloth, LoRA, QLoRA), making it practical to create domain-specific models from the base weights.

- **Size efficiency**: The 8B parameter variant used in Decoding AI demonstrates that relatively small models, when fine-tuned on high-quality data, can perform specialized tasks (summarization) effectively -- supporting the [[concepts/data-quality-bottleneck]] thesis that data quality matters more than model scale.

## Role in LLM Knowledge Bases

Llama represents the fine-tuning pathway that Karpathy identifies as a future direction for LLM knowledge bases. Rather than relying solely on context window retrieval (loading wiki articles into the prompt), a fine-tuned Llama model could "know" the corpus in its weights. The Decoding AI pipeline demonstrates this with summarization, but the concept extends to general Q&A over a knowledge base.

The tradeoff is significant: fine-tuning achieves only 50.4% accuracy on new facts (per the Pebblous analysis), compared to RAG's 87.5%. This makes fine-tuning a poor choice for knowledge that changes frequently but potentially valuable for stable domain knowledge. The hybrid RAFT approach (domain fine-tuning + RAG) achieving 86% accuracy suggests the eventual path forward may combine both.

## Mentioned In

- [[sources/decodingai-second-brain-rag]] -- Llama 3.1 8B fine-tuned for summarization using Unsloth, deployed on Hugging Face Dedicated Endpoints
