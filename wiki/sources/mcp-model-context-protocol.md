---
title: "Source: Model Context Protocol (MCP) Specification and Announcement"
type: source-summary
source: "[[raw/mcp-model-context-protocol]]"
related: ["[[concepts/model-context-protocol]]", "[[concepts/tool-use]]", "[[entities/anthropic]]"]
last_compiled: 2026-04-05
summary: "MCP open standard for AI tool integration: JSON-RPC architecture with Hosts/Clients/Servers, adopted by OpenAI and Google, donated to Linux Foundation in 2025."
reading_time: "2 min"
---

## Key Points

- Open standard using JSON-RPC 2.0 for LLM-to-tool integration
- Three-tier: Hosts (LLM apps) → Clients (connectors) → Servers (tool/data providers)
- Server features: Resources, Prompts, Tools; Client features: Sampling, Roots, Elicitation
- Adopted by OpenAI (March 2025), Google DeepMind (April 2025)
- Donated to Agentic AI Foundation under Linux Foundation (December 2025)
- 97 million monthly SDK downloads by December 2025

## Detailed Summary

Anthropic introduced MCP in November 2024 to solve the "M x N" integration problem: every AI application previously needed custom integrations for every data source. MCP provides a universal standard, inspired by the Language Server Protocol that standardized programming language support.

The protocol's rapid industry adoption is remarkable: within 18 months, OpenAI, Google DeepMind, and Microsoft all adopted it. The November 2025 spec update added async operations, statelessness, server identity, and a community-driven registry. In December 2025, Anthropic donated MCP to a neutral foundation, signaling its transition from vendor project to industry standard.

Security principles are built into the spec: user consent for all operations, data privacy protections, tool safety gates, and LLM sampling controls.

## Related Concepts

- [[concepts/model-context-protocol]] — full concept article
- [[concepts/tool-use]] — MCP standardizes tool integration
- [[entities/anthropic]] — MCP creator
