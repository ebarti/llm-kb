"""
kb — LLM Knowledge Base CLI (Python rewrite).

Typed command-line interface for a Claude-powered personal knowledge base.
When `--budget` is set, hard token caps are enforced against Anthropic SDK
usage metadata; the fallback Claude CLI refuses hard budgets because it does
not expose machine-readable token usage. Every command supports `--json`
for machine-readable structured output.

See kb/cli.py for the command entrypoint, kb/commands/ for per-command
implementations, and kb/budget.py for budget enforcement.
"""

__version__ = "0.1.0"
