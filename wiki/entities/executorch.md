---
title: "ExecuTorch"
type: entity
entity_type: tool
sources: ["[[sources/on-device-llms-2026]]"]
related: ["[[concepts/edge-inference]]", "[[concepts/quantization]]", "[[entities/llama-cpp]]"]
last_compiled: 2026-04-05
summary: "Meta's production on-device inference framework: 50KB base footprint, 12+ hardware backends, reached 1.0 GA in October 2025, serving billions of users across Meta's mobile apps."
---

## Overview

ExecuTorch is Meta's open-source framework for deploying AI models on edge devices. It reached 1.0 General Availability in October 2025, marking production readiness for [[concepts/edge-inference|on-device LLM inference]].

## Key Features

- **50KB base footprint** — minimal binary size for resource-constrained devices
- **12+ hardware backends** — supports diverse accelerators across mobile platforms
- **Over 80% of popular edge LLMs** work out of the box
- Serves **billions of users** across Meta's apps (Instagram, WhatsApp, Facebook)

## Target Hardware

Works with mobile NPUs including:
- Apple A-series (via CoreML/MPS backends)
- Qualcomm Snapdragon (via QNN backend)
- MediaTek Dimensity (via NeuroPilot backend)
- Also supports microcontrollers and embedded devices

## Mentioned In
- [[sources/on-device-llms-2026]] — identified as the leading production mobile inference framework
