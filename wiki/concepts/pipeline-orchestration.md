---
title: "Pipeline Orchestration"
type: concept
sources: ["[[sources/airflow-mlops-orchestration]]"]
related: ["[[concepts/document-processing-pipeline]]", "[[concepts/incremental-etl]]", "[[entities/apache-airflow]]"]
last_compiled: 2026-04-05
summary: "Scheduling, monitoring, and managing multi-stage data/ML pipelines: Apache Airflow dominates (35% of enterprises), with Airflow 3.0 adding event-driven scheduling, dynamic task mapping, and real-time reactive orchestration."
---

## Overview

Pipeline orchestration is the coordination layer that schedules, monitors, retries, and manages the execution of multi-stage [[concepts/document-processing-pipeline]] systems. Without orchestration, pipelines are fragile scripts; with it, they become production systems with SLAs, monitoring, and automatic recovery.

According to Gartner (2024), by 2026 over 70% of organizations will treat data pipelines as products with SLAs, not just internal plumbing.

## Apache Airflow

[[entities/apache-airflow]] is the dominant orchestration tool, with 35% of enterprises using it for AI/ML pipelines (State of Airflow 2025).

### Core Concepts
- **DAGs** (Directed Acyclic Graphs): Define pipeline topology — which tasks depend on which
- **Operators**: Reusable task templates (PythonOperator, BashOperator, KubernetesPodOperator)
- **Sensors**: Wait for external conditions (file arrival, API response, time)
- **XComs**: Pass data between tasks
- **Connections**: Manage credentials for external services

### Three Orchestration Patterns for ML/AI

1. **External tool orchestration**: Airflow triggers specialized platforms (MLFlow, SageMaker, Databricks) — Airflow as conductor
2. **Hybrid**: Mix external tools with in-Airflow Python tasks
3. **Native Python**: All operations as Python code within Airflow tasks — maximum simplicity

### Airflow 3.0 (April 2025)
- **Event-driven scheduling**: DAGs triggered by external events (new files in S3, Kafka messages)
- **Task SDK**: Better developer experience for defining tasks
- **Dynamic task mapping**: Runtime parallelization without predefined task counts
- **Setup/teardown tasks**: Programmatic resource provisioning and cleanup

### Integration Ecosystem
- ML platforms: SageMaker, Databricks, Azure ML
- LLM providers: OpenAI, Cohere
- Vector DBs: Weaviate, Pinecone, Pgvector
- Data quality: Great Expectations, Soda Core
- Experiment tracking: Weights & Biases

## Alternatives to Airflow

- **Prefect**: Python-native, less boilerplate, better for modern Python workflows
- **Dagster**: Software-defined assets, strong data lineage
- **Mage AI**: Visual pipeline builder, good for data engineers new to orchestration
- **Temporal**: Code-first, strong for long-running workflows
- **ZenML**: MLOps-specific orchestration (used in [[sources/decodingai-second-brain-rag]])

## For Knowledge Base Pipelines

For LLM knowledge base systems like this one, orchestration handles:
- **Scheduled ingestion**: Periodically check sources for new content
- **Triggered compilation**: Re-compile wiki when new raw files appear
- **Quality checks**: Run [[concepts/linting-and-health-checks]] on schedule
- **Monitoring**: Track ingestion success rates and processing times

## Sources
- [[sources/airflow-mlops-orchestration]] — Astronomer's MLOps best practices

## Related Concepts
- [[concepts/document-processing-pipeline]] — what orchestration coordinates
- [[concepts/incremental-etl]] — event-driven scheduling enables incremental processing
- [[entities/apache-airflow]] — dominant orchestration tool
