---
title: "MCP Security"
type: concept
sources: ["[[sources/pento-year-of-mcp-review]]", "[[sources/wikipedia-model-context-protocol]]", "[[sources/descope-mcp-vs-function-calling]]"]
related: ["[[concepts/model-context-protocol]]", "[[concepts/hallucination-contamination]]", "[[concepts/tool-use-standards]]"]
last_compiled: 2026-04-05
summary: "Security vulnerabilities and mitigations for MCP: prompt injection through tool descriptions, tool spoofing/lookalike attacks, OAuth token vulnerabilities, toxic agent data exfiltration, and per-server isolation as defense-in-depth."
---

## Overview

While the [[concepts/model-context-protocol]] provides significant security improvements over [[concepts/function-calling]] through per-server credential isolation and least-privilege defaults, security researchers have identified several classes of vulnerabilities that require careful attention in production deployments.

## Identified Vulnerabilities

### Prompt Injection via Tool Descriptions
MCP servers advertise tool descriptions that are consumed by LLMs. Malicious or compromised servers can embed prompt injection attacks in these descriptions, potentially causing the LLM to take unintended actions with other tools.

### Tool Spoofing / Lookalike Tools
Malicious MCP servers can expose tools with names similar to trusted tools (e.g., "read_file" vs "read_flie"), silently replacing legitimate tool calls. This is especially dangerous when multiple MCP servers are connected simultaneously.

### OAuth Token Vulnerabilities
The initial MCP specification provided minimal authentication guidance. OAuth token storage at the server level can be exploited if server processes are compromised, potentially giving attackers access to user credentials for connected services.

### Toxic Agent Workflows
Through creative tool chaining, malicious tool descriptions can guide an agent into exfiltrating data — for example, reading sensitive data from one tool and sending it via another tool to an attacker-controlled endpoint.

### Minimal Authentication Guidance
The original MCP specification focused on functionality over security, with authentication left largely to implementers. This has led to inconsistent security practices across the ecosystem.

## MCP Security Advantages over Function Calling

Despite these challenges, MCP's architecture provides meaningful security improvements:

| Dimension | Function Calling | MCP |
|-----------|-----------------|-----|
| Credential isolation | All credentials in one process | Per-server credential isolation |
| Access control | Application-level (all-or-nothing) | Server-level (granular, least-privilege) |
| Audit logging | Manual implementation | Protocol-level support |
| Attack surface | Entire application | Per-server isolation |
| Process isolation | Single process | Independent processes per server |

## Recommended Mitigations

1. **Server auditing** — Audit MCP servers before deployment; verify source and reputation
2. **Tool allowlisting** — Explicitly whitelist approved tools rather than accepting all advertised tools
3. **Sandboxed environments** — Run MCP servers in sandboxed containers with restricted permissions
4. **Least-privilege implementation** — Grant each server only the minimum permissions needed
5. **Comprehensive logging** — Log all tool invocations with full request/response details
6. **RBAC** — Implement role-based access control at the server level
7. **Input validation** — Validate and sanitize all tool inputs and outputs

## Sources
- [[sources/pento-year-of-mcp-review]] — security landscape and vulnerability inventory
- [[sources/wikipedia-model-context-protocol]] — April 2025 security research findings
- [[sources/descope-mcp-vs-function-calling]] — security comparison with function calling

## Related Concepts
- [[concepts/model-context-protocol]] — the protocol these concerns apply to
- [[concepts/hallucination-contamination]] — related risk of LLM-generated errors propagating
- [[concepts/tool-use-standards]] — security as a key gap across all tool standards
