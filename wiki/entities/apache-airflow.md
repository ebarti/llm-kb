---
title: "Apache Airflow"
type: entity
entity_type: tool
sources: ["[[sources/airflow-mlops-orchestration]]"]
related: ["[[concepts/pipeline-orchestration]]", "[[concepts/document-processing-pipeline]]", "[[concepts/incremental-etl]]"]
last_compiled: 2026-04-05
summary: "Dominant workflow orchestration platform (35% of enterprise AI/ML pipelines): Python-native DAG definitions, event-driven scheduling (3.0), dynamic task mapping, and integrations with SageMaker/Databricks/vector DBs."
---

## Overview

Apache Airflow is the most widely-adopted open-source platform for [[concepts/pipeline-orchestration]], used by 35% of enterprises for AI/ML pipeline orchestration (State of Airflow 2025). It defines workflows as Directed Acyclic Graphs (DAGs) in Python, providing scheduling, monitoring, retry logic, and alerting for complex multi-stage pipelines.

## Key Features

- **DAGs**: Python-defined workflow graphs with task dependencies
- **Operators**: Reusable task templates (Python, Bash, Kubernetes, cloud services)
- **Sensors**: Wait for external conditions (file arrival, API response)
- **XComs**: Inter-task data passing
- **Connections**: Credential management for external services
- **UI**: Web-based monitoring dashboard

## Version 3.0 (April 2025)

Major evolution:
- **Event-driven scheduling**: DAGs triggered by external events (S3 files, Kafka messages)
- **Task SDK**: Improved developer experience
- **Dynamic task mapping**: Runtime parallelization without predefined task counts
- **Setup/teardown tasks**: Programmatic resource lifecycle management

## Integration Ecosystem

| Category | Tools |
|----------|-------|
| ML Platforms | SageMaker, Databricks, Azure ML |
| LLM Providers | OpenAI, Cohere |
| Vector DBs | Weaviate, Pinecone, Pgvector |
| Data Quality | Great Expectations, Soda Core |
| Experiment Tracking | Weights & Biases |

## Mentioned In
- [[sources/airflow-mlops-orchestration]] — MLOps best practices and patterns
