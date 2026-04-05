---
title: "Incremental ETL and Change Data Capture"
type: concept
sources: ["[[sources/airflow-mlops-orchestration]]", "[[sources/llamaindex-ingestion-pipeline]]"]
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/pipeline-orchestration]]", "[[concepts/wiki-compilation]]"]
last_compiled: 2026-04-05
summary: "Processing only new or changed data rather than full rebuilds: watermark-based tracking, CDC from database logs, append-only/upsert/SCD2 patterns, and LlamaIndex's docstore deduplication — reducing compute by 10-100x."
---

## Overview

Incremental ETL is the practice of processing only new or changed data rather than re-processing entire datasets. For [[concepts/document-processing-pipeline]] systems, this means detecting which documents are new, modified, or deleted since the last pipeline run, and processing only those changes.

This concept is directly relevant to [[concepts/wiki-compilation]]: this wiki's manifest (`_meta/manifest.md`) tracks which raw files have been compiled, enabling incremental updates rather than full rebuilds.

## Key Patterns

### Append-Only
Ideal for immutable data (event logs, sensor readings, financial transactions). Once written, records are final. Pipeline inserts new events since last run. Simplest pattern.

### Upsert (Insert or Update)
Check if a record exists; update if yes, insert if no. Standard for entities that change over time (user profiles, product catalogs, wiki articles).

### Slowly Changing Dimensions (SCD) Type 2
Instead of overwriting, mark old records as expired and insert new versions. Preserves complete history. Related to [[concepts/temporal-knowledge]] — tracking what was true when.

## State Tracking Mechanisms

### Watermarking
Most common technique. Pipeline records the latest timestamp or ID successfully processed in a metadata table. Next run queries source for records after that watermark. This wiki's manifest serves as a watermark.

### Change Data Capture (CDC)
Reads database transaction logs (WAL, binlog) to detect inserts, updates, and deletes. More efficient than querying the source — reads logs instead of tables. Tools: Debezium, AWS DMS, Fivetran.

CDC does not replace ETL but enhances it: makes extraction incremental and continuous, reduces compute overhead, eliminates batch window dependencies.

### Document ID Tracking
[[entities/llamaindex]]'s ingestion pipeline uses docstore-based deduplication: tracking `document.doc_id` and `node.ref_doc_id` to detect already-processed documents and skip them. This is the framework equivalent of watermarking.

## Benefits

- **10-100x compute reduction**: Process only deltas, not full corpus
- **Lower latency**: New content available faster (minutes vs. hours)
- **Reduced costs**: Less API calls, less compute, less storage churn
- **Better reliability**: Smaller batches fail less and recover faster

## Challenges

- **Schema evolution**: Source format changes require pipeline adaptation (metadata-driven models reduce cost by 35%)
- **Late-arriving data**: Events that arrive after the watermark has advanced
- **Delete detection**: Harder to detect removals than additions
- **State management**: Watermarks and checkpoints must be durable and consistent

## For Knowledge Base Pipelines

In LLM knowledge bases:
- Track ingested URLs in a manifest to avoid duplicate fetching
- Use file modification timestamps to detect changed raw sources
- Re-compile only affected wiki articles when sources change
- Maintain compilation metadata per article for targeted updates

## Sources
- [[sources/airflow-mlops-orchestration]] — event-driven scheduling for incremental pipelines
- [[sources/llamaindex-ingestion-pipeline]] — docstore deduplication as incremental ETL

## Related Concepts
- [[concepts/document-processing-pipeline]] — incremental ETL optimizes pipeline efficiency
- [[concepts/pipeline-orchestration]] — event-driven scheduling enables incremental triggers
- [[concepts/wiki-compilation]] — this wiki's manifest is an incremental ETL mechanism
- [[concepts/temporal-knowledge]] — SCD Type 2 relates to temporal fact tracking
