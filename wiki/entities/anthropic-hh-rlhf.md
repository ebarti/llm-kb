---
title: "Anthropic HH-RLHF Dataset"
type: entity
entity_type: dataset
sources: ["[[sources/rlhf-preference-data-collection]]"]
related: ["[[concepts/preference-data]]", "[[concepts/rlhf]]"]
last_compiled: 2026-04-05
summary: "Foundational open preference dataset with 170K human comparisons for training helpful and harmless AI assistants — collected via Amazon Mechanical Turk, using chosen/rejected pair format."
---

## Overview

The Anthropic Helpfulness and Harmlessness (HH-RLHF) dataset is the foundational open preference dataset for RLHF research. It contains approximately 170,000 human preference comparisons collected for training helpful and harmless AI assistants, plus human-generated red teaming data.

## Format

Simple JSONL format where each line contains a pair of texts: one "chosen" and one "rejected." The data is designed for training preference (reward) models for subsequent RLHF training, NOT for supervised fine-tuning of dialogue agents.

## Components

- **Helpfulness comparisons**: human judgments on which response is more helpful
- **Harmlessness comparisons**: human judgments on which response is less harmful
- **Red teaming data**: adversarial prompts designed to elicit harmful behavior

## Collection

Collected primarily via Amazon Mechanical Turk using a chat tool interface. Annotators compared pairs of model-generated responses for the same prompt.

## Availability

Hosted on HuggingFace at https://huggingface.co/datasets/Anthropic/hh-rlhf and on GitHub at https://github.com/anthropics/hh-rlhf.

## Significance

As the first large-scale open preference dataset, HH-RLHF established the standard data format (chosen/rejected pairs) that most subsequent preference datasets follow. It demonstrated that RLHF could meaningfully improve model helpfulness while reducing harmful outputs.

## Mentioned In

- [[sources/rlhf-preference-data-collection]] — referenced as a major public dataset
