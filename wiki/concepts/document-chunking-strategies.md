---
title: "Document Chunking Strategies"
type: concept
sources: ["[[sources/rag-chunking-strategies-dasroot]]", "[[sources/stackoverflow-chunking-rag]]", "[[sources/unstructured-io-document-etl]]", "[[sources/llamaindex-ingestion-pipeline]]"]
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/pdf-parsing-tools]]"]
last_compiled: 2026-04-05
summary: "Techniques for splitting documents into retrieval-optimized segments: fixed-size (simplest), recursive, semantic boundary, sliding window, context-aware, adaptive (ML-based), and metadata-enriched — with 18-40% accuracy improvements from semantic chunking."
---

## Overview

Document chunking is the process of splitting large documents into smaller segments optimized for retrieval, embedding, and LLM processing. It is a critical stage in any [[concepts/document-processing-pipeline]] and directly impacts the quality of [[concepts/rag-vs-index-based-retrieval]] systems. Poor chunking fragments coherent ideas across multiple segments, while optimal chunking preserves semantic units that align with user queries.

Research indicates that semantic-aware chunking can improve retrieval accuracy by 18-40% compared to naive fixed-size approaches.

## Strategy Taxonomy

### 1. Fixed-Size Chunking
Split text into uniform segments by token or character count. Simplest and fastest. 512 tokens is the most common size, achieving 92% recall on technical documents versus 86% at 256 tokens. Best for homogeneous content (news articles, blog posts).

### 2. Recursive Character Splitting
LangChain's default approach. Iterates through separators ["\n\n", "\n", " ", ""] until producing the target chunk size. Keeps paragraphs, then sentences, then words together as much as possible. A good default for most use cases.

### 3. Semantic Boundary Splitting
Splits at natural semantic boundaries: section headings, paragraph breaks, topic transitions. RAGFlow v1.8 achieves 95% contextual coherence with this approach. Best for structured documents like legal contracts (85% retrieval accuracy, up from 55% with fixed-size) and research papers.

### 4. Sliding Window / Overlapping Chunks
Creates intentional overlap (typically 10-20% of chunk size) between consecutive segments. Improves retrieval accuracy by up to 9% in complex documents by preserving cross-boundary context. Tradeoff: increased storage and processing overhead.

### 5. Context-Aware Chunking
Leverages semantic markers (punctuation, markdown headers, HTML tags) to create coherent units. Stack Overflow treats questions, answers, and comments as discrete semantic chunks in their own RAG system. Requires domain knowledge about document structure.

### 6. Adaptive / ML-Based Chunking
Uses machine learning to determine optimal chunk sizes and boundaries per document. Most compute-intensive but produces the best quality. Analyzes content complexity to dynamically adjust parameters.

### 7. Metadata-Enriched Chunking
Attaches contextual metadata (section headers, document type, semantic density scores) to each chunk. Enables nuanced filtering and ranking during retrieval. [[entities/unstructured-io]] pioneered this with its typed Element system.

### 8. Hybrid Approaches
Combine multiple strategies: semantic boundaries first, then token-limit enforcement. Dify v2.3 achieves 94% accuracy with 30% latency reduction on 50,000 unstructured documents using this approach.

## Performance Benchmarks

| Strategy | Accuracy/Recall | Latency | Best For |
|----------|----------------|---------|----------|
| Fixed 512 tokens | 92% recall | Lowest | Homogeneous content |
| Semantic boundary | 95% coherence | Moderate | Structured documents |
| Overlapping (10-20%) | +9% accuracy | Higher | Complex documents |
| Hybrid (Dify v2.3) | 94% accuracy | -30% latency | Enterprise scale |
| Paragraph-level legal | 85% accuracy | Moderate | Legal contracts |

## Framework Implementations

- **LangChain**: `RecursiveCharacterTextSplitter` with configurable `chunk_size` and `chunk_overlap`
- **LlamaIndex**: Node parsers (sentence, token, HTML, JSON) + ingestion pipeline
- **Unstructured**: Element-based chunking using document structure understanding
- **RAGFlow v1.8**: Deep document parsing with semantic boundary detection
- **Dify v2.3**: Visual workflow editor for custom chunking rules

## Best Practices

1. **Match chunk size to query length** — mismatches reduce cosine similarity scoring accuracy
2. **Use overlap (10-20%)** for complex documents to preserve cross-boundary context
3. **Leverage document structure** when available (headers, sections, tables)
4. **Test against real queries** using human review and LLM evaluators
5. **Monitor retrieval metrics** (precision, recall, NDCG) and iterate
6. **Don't over-chunk** — smaller is not always better; chunks need enough context to be meaningful

## Sources
- [[sources/rag-chunking-strategies-dasroot]] — data-rich benchmark of five strategies
- [[sources/stackoverflow-chunking-rag]] — five-level taxonomy with practical recommendations
- [[sources/unstructured-io-document-etl]] — element-based structural chunking
- [[sources/llamaindex-ingestion-pipeline]] — node parser implementations

## Related Concepts
- [[concepts/document-processing-pipeline]] — chunking is stage 2 of the pipeline
- [[concepts/rag-vs-index-based-retrieval]] — chunking quality directly affects retrieval
- [[concepts/pdf-parsing-tools]] — parsing quality determines what chunking receives
