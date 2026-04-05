---
title: "SambaNova Systems"
type: entity
entity_type: org
url: "https://sambanova.ai"
related: ["[[concepts/ai-accelerators]]", "[[concepts/ai-hardware-landscape]]", "[[entities/cerebras]]", "[[entities/groq]]"]
tags: [sambanova, rdu, dataflow, asic, ai-hardware]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Reconfigurable DataFlow Unit (RDU) with up to 3TB memory per socket; SambaFlow compiler; deployed at Los Alamos and LLNL; Samba-1 (1T parameter) model; $676M Series D at ~$5B valuation."
---

## Overview

SambaNova Systems designs the Reconfigurable DataFlow Unit (RDU) — an AI chip whose compute fabric can be reshaped at compile time for different neural network layers. The key differentiator is memory capacity: up to 3TB per socket, making it the most memory-dense AI accelerator available. This suits workloads with extremely large models or massive embedding tables.

## Key Facts

- **Type**: Organization (AI chip startup)
- **Founded**: 2017
- **Flagship product**: SN30 RDU (Reconfigurable DataFlow Unit)
- **Valuation**: ~$5B
- **Funding**: $676M Series D (April 2021)
- **Key investors**: SoftBank Vision Fund, Google Ventures, Intel Capital
- **Software**: SambaFlow compiler (auto-partitions models into dataflow graphs)

## RDU Specifications

| Specification | Value |
|--------------|-------|
| Architecture | Tileable chiplet with compile-time reconfiguration |
| Process node | TSMC 7nm |
| Memory per socket | Up to 3 TB |
| HBM per SN30 board | 80 GB (8 stacks) |
| Power | 10-40 kW per quarter-rack |
| Focus | Training and inference |

## Performance

- GPT-3 (175B) throughput: ~32K tokens/sec per rack
- Llama 2 70B: 132 tokens/sec per rack
- LLaMA3 540B: >1,000 tokens/sec (AWS benchmark, ~2x 8x H100 GPUs)
- Claimed ability to train 1.3-trillion-parameter models using 54 "expert" partitions

## Key Deployments

- **Department of Energy**: Quiet deployments at Los Alamos and Lawrence Livermore National Labs
- **Samba-1**: Open-source 1-trillion-parameter model for enterprise fine-tuning
- **Biopharma**: Molecular language models with 10x faster drug design cycles
- **AWS Marketplace**: DataScale systems available through AWS Outposts

## Mentioned In

- [[sources/cerebras-vs-sambanova-vs-groq-chips]] — detailed technical comparison
