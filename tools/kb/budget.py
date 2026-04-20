"""
Token budget tracking and enforcement.

The Anthropic SDK returns a `usage` field on every Messages response with
input_tokens, output_tokens, and cache_* counters. BudgetTracker accumulates
these across a single command invocation and raises BudgetExceeded the moment
the cap is crossed so the caller can exit cleanly with code 2.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from .models import TokenUsage


DEFAULT_BUDGET_TOKENS = 50_000


class BudgetExceeded(RuntimeError):
    """Raised when accumulated token usage crosses the configured limit.

    Attributes
    ----------
    usage : TokenUsage
        The accumulated usage at the moment the cap was crossed.
    limit : int
        The configured token ceiling.
    """

    def __init__(self, usage: TokenUsage, limit: int):
        self.usage = usage
        self.limit = limit
        super().__init__(
            f"Budget exceeded: {usage.total} tokens used, limit was {limit}"
        )


@dataclass
class BudgetTracker:
    """Accumulates Anthropic SDK token usage and enforces a hard cap.

    The tracker treats the sum of input, output, cache-creation and
    cache-read tokens as "total tokens used" for the command. Callers
    should invoke :meth:`add_from_response` after each Anthropic SDK
    response and :meth:`check` whenever they want to short-circuit.

    Parameters
    ----------
    limit : int | None
        Hard cap in tokens. ``None`` disables enforcement (still tracks).
    """

    limit: Optional[int] = DEFAULT_BUDGET_TOKENS
    usage: TokenUsage = field(default_factory=TokenUsage)

    # ------------------------------------------------------------------ #
    #  Accounting
    # ------------------------------------------------------------------ #

    def add(
        self,
        input_tokens: int = 0,
        output_tokens: int = 0,
        cache_creation_input_tokens: int = 0,
        cache_read_input_tokens: int = 0,
    ) -> TokenUsage:
        """Add raw token counts to the running total and check the cap."""
        self.usage.input_tokens += int(input_tokens or 0)
        self.usage.output_tokens += int(output_tokens or 0)
        self.usage.cache_creation_input_tokens += int(
            cache_creation_input_tokens or 0
        )
        self.usage.cache_read_input_tokens += int(cache_read_input_tokens or 0)
        self.check()
        return self.usage

    def add_from_response(self, response: Any) -> TokenUsage:
        """Accept either an anthropic SDK Message object or a dict-like.

        The SDK exposes ``response.usage`` with attributes ``input_tokens``,
        ``output_tokens``, ``cache_creation_input_tokens``,
        ``cache_read_input_tokens``. Dict responses (e.g. mocked in tests)
        expose the same keys.
        """
        usage_obj = (
            response.get("usage") if isinstance(response, dict) else getattr(response, "usage", None)
        )
        if usage_obj is None:
            return self.usage

        def _get(name: str) -> int:
            if isinstance(usage_obj, dict):
                return int(usage_obj.get(name, 0) or 0)
            return int(getattr(usage_obj, name, 0) or 0)

        return self.add(
            input_tokens=_get("input_tokens"),
            output_tokens=_get("output_tokens"),
            cache_creation_input_tokens=_get("cache_creation_input_tokens"),
            cache_read_input_tokens=_get("cache_read_input_tokens"),
        )

    def check(self) -> None:
        """Raise :class:`BudgetExceeded` if the cap has been crossed."""
        if self.limit is not None and self.usage.total > self.limit:
            raise BudgetExceeded(self.usage, self.limit)

    # ------------------------------------------------------------------ #
    #  Reporting
    # ------------------------------------------------------------------ #

    def remaining(self) -> Optional[int]:
        """Return tokens remaining under the cap, or ``None`` if unbounded."""
        if self.limit is None:
            return None
        return max(0, self.limit - self.usage.total)

    def summary(self) -> dict[str, Any]:
        """Produce a plain-dict summary suitable for JSON rendering."""
        return {
            "limit": self.limit,
            "used": self.usage.total,
            "remaining": self.remaining(),
            "input_tokens": self.usage.input_tokens,
            "output_tokens": self.usage.output_tokens,
            "cache_creation_input_tokens": self.usage.cache_creation_input_tokens,
            "cache_read_input_tokens": self.usage.cache_read_input_tokens,
        }
