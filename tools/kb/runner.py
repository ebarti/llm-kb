"""
LLM runner abstraction for kb.

We support two backends:

1. **Anthropic SDK** (preferred when ``ANTHROPIC_API_KEY`` is set and the
   ``anthropic`` package is importable). Responses carry a ``usage`` object
   we feed into :class:`~tools.kb.budget.BudgetTracker`, enabling
   hard-stop token budget enforcement.

2. **Claude CLI** (fallback, matching the bash kb's behaviour). We invoke
   ``claude --print --model ... --max-turns N`` as a subprocess. The CLI
   currently does not report token usage back to stdout in a machine-
   readable way, so it cannot hard-enforce token budgets. When a hard
   budget is requested, CLI mode fails fast and instructs the caller to
   use the SDK backend instead.

Callers typically use :func:`invoke_llm` which picks the best backend for
the current environment and returns a :class:`LLMResult` with the final
text response and accumulated :class:`TokenUsage`.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from dataclasses import dataclass, field
from typing import Any, Optional

from .budget import BudgetExceeded, BudgetTracker
from .models import TokenUsage


@dataclass
class LLMResult:
    text: str = ""
    backend: str = "cli"  # 'sdk' | 'cli' | 'dry-run'
    usage: TokenUsage = field(default_factory=TokenUsage)
    returncode: int = 0
    budget_exceeded: bool = False


# --------------------------------------------------------------------------- #
#  Public entry point
# --------------------------------------------------------------------------- #


def invoke_llm(
    prompt: str,
    *,
    model: str = "opus",
    budget: BudgetTracker,
    max_turns: Optional[int] = None,
    dry_run: bool = False,
    permission_mode: str = "bypassPermissions",
    force_backend: Optional[str] = None,
    verbose: bool = False,
) -> LLMResult:
    """Run a prompt through the best available backend.

    Parameters
    ----------
    prompt
        The user prompt.
    model
        Anthropic model name or Claude CLI alias (e.g. ``'opus'``, ``'sonnet'``).
    budget
        A :class:`~tools.kb.budget.BudgetTracker`. SDK responses feed into it.
    max_turns
        Advisory hint for the CLI backend (``--max-turns``). Not used by the SDK.
    dry_run
        When true, return an :class:`LLMResult` describing what would be run.
    permission_mode
        Claude CLI permission mode (default ``bypassPermissions`` matches
        the bash kb).
    force_backend
        Override auto-detection. Values: ``'sdk'``, ``'cli'``.
    """
    if dry_run:
        return LLMResult(
            text=f"[DRY RUN] model={model} budget={budget.limit} prompt={prompt[:120]}...",
            backend="dry-run",
        )

    backend = force_backend or _auto_backend()

    if backend == "sdk":
        try:
            return _invoke_sdk(
                prompt=prompt,
                model=model,
                budget=budget,
                verbose=verbose,
            )
        except ImportError:
            # Fall through to CLI if SDK isn't actually importable
            backend = "cli"

    return _invoke_cli(
        prompt=prompt,
        model=model,
        budget=budget,
        max_turns=max_turns,
        permission_mode=permission_mode,
        verbose=verbose,
    )


# --------------------------------------------------------------------------- #
#  Backend selection
# --------------------------------------------------------------------------- #


def _auto_backend() -> str:
    if os.environ.get("KB_FORCE_BACKEND"):
        return os.environ["KB_FORCE_BACKEND"]
    if os.environ.get("ANTHROPIC_API_KEY"):
        try:
            import anthropic  # noqa: F401
            return "sdk"
        except ImportError:
            pass
    if shutil.which("claude"):
        return "cli"
    # No SDK key, no CLI — default to cli so error is clear
    return "cli"


# --------------------------------------------------------------------------- #
#  SDK backend
# --------------------------------------------------------------------------- #


_SDK_MODEL_ALIASES = {
    "opus": "claude-opus-4-5",
    "sonnet": "claude-sonnet-4-5",
    "haiku": "claude-haiku-4-5",
}


def _resolve_sdk_model(name: str) -> str:
    return _SDK_MODEL_ALIASES.get(name, name)


def _invoke_sdk(
    *, prompt: str, model: str, budget: BudgetTracker, verbose: bool
) -> LLMResult:
    import anthropic  # type: ignore

    client = anthropic.Anthropic()
    sdk_model = _resolve_sdk_model(model)
    remaining_tokens = budget.remaining()

    if verbose:
        print(f"[kb] sdk backend | model={sdk_model} budget={budget.limit}")

    if remaining_tokens is not None and remaining_tokens <= 0:
        return LLMResult(
            text="ERROR: token budget exhausted before SDK call",
            backend="sdk",
            returncode=1,
            budget_exceeded=True,
        )

    try:
        response = client.messages.create(
            model=sdk_model,
            max_tokens=4096 if remaining_tokens is None else int(remaining_tokens),
            messages=[{"role": "user", "content": prompt}],
        )
    except Exception as exc:  # noqa: BLE001
        return LLMResult(
            text=f"ERROR: anthropic SDK call failed: {exc}",
            backend="sdk",
            returncode=1,
        )

    # Extract text
    try:
        text = "".join(
            getattr(block, "text", "") for block in (response.content or [])
        )
    except Exception:  # noqa: BLE001
        text = str(response)

    # Accumulate usage; may raise BudgetExceeded
    try:
        budget.add_from_response(response)
        budget_exceeded = False
    except BudgetExceeded:
        budget_exceeded = True

    return LLMResult(
        text=text,
        backend="sdk",
        # Explicit fields: ``**usage.__dict__`` leaks pydantic v2 private
        # attrs (``__pydantic_fields_set__`` et al.) into the constructor,
        # which fails validation at runtime. See review feedback on PR #23.
        usage=TokenUsage(
            input_tokens=budget.usage.input_tokens,
            output_tokens=budget.usage.output_tokens,
            cache_creation_input_tokens=budget.usage.cache_creation_input_tokens,
            cache_read_input_tokens=budget.usage.cache_read_input_tokens,
        ),
        returncode=0,
        budget_exceeded=budget_exceeded,
    )


# --------------------------------------------------------------------------- #
#  CLI backend
# --------------------------------------------------------------------------- #


def _invoke_cli(
    *,
    prompt: str,
    model: str,
    budget: BudgetTracker,
    max_turns: Optional[int],
    permission_mode: str,
    verbose: bool,
) -> LLMResult:
    if budget.limit is not None:
        return LLMResult(
            text=(
                "ERROR: hard token budgets require the Anthropic SDK backend; "
                "Claude CLI does not expose token usage."
            ),
            backend="cli",
            returncode=1,
            budget_exceeded=True,
        )

    if not shutil.which("claude"):
        api_key_set = bool(os.environ.get("ANTHROPIC_API_KEY"))
        try:
            import anthropic  # type: ignore  # noqa: F401
            sdk_importable = True
        except ImportError:
            sdk_importable = False

        if api_key_set and not sdk_importable:
            msg = (
                "ERROR: Claude CLI not found on PATH and SDK backend "
                "unavailable (install anthropic or ensure ANTHROPIC_API_KEY "
                "is set correctly)."
            )
        else:
            msg = "ERROR: Claude CLI not found on PATH and no ANTHROPIC_API_KEY set."

        return LLMResult(
            text=msg,
            backend="cli",
            returncode=1,
        )

    args = [
        "claude",
        "--print",
        "--permission-mode",
        permission_mode,
        "--model",
        model,
    ]
    # --effort max was hardcoded in the bash kb; keep it for parity
    args.extend(["--effort", "max"])
    if max_turns is not None:
        args.extend(["--max-turns", str(max_turns)])

    args.append(prompt)

    if verbose:
        print(f"[kb] cli backend | cmd={' '.join(args[:-1])} <prompt>")

    try:
        proc = subprocess.run(
            args,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return LLMResult(
            text="ERROR: 'claude' CLI not found.",
            backend="cli",
            returncode=1,
        )

    text = (proc.stdout or "") + ("\n" + proc.stderr if proc.stderr else "")
    # CLI backend does not expose per-response token counts reliably.
    return LLMResult(
        text=text,
        backend="cli",
        usage=budget.usage,
        returncode=proc.returncode,
    )
