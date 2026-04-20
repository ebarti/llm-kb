#!/usr/bin/env python3
"""
Semantic chunker for markdown articles.

Splits at H1/H2/H3 heading boundaries while:
- Targeting ~300 tokens per chunk
- Preserving heading context (each chunk carries its breadcrumb path)
- Never splitting fenced code blocks
- Never splitting markdown tables

The goal is to produce chunks that stand on their own as semantic units
suitable for dense-vector retrieval.

Pure Python stdlib -- safe to import even when numpy/ML deps are missing.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field, asdict
from typing import Iterable

# Target token budget per chunk. Embedding models commonly tolerate 512 tokens;
# BGE-small has 512 max. 300 leaves slack for the heading breadcrumb.
TARGET_TOKENS = 300

# Hard floor: sections smaller than this merge with the next sibling when possible.
MIN_TOKENS = 40

# Hard ceiling: if a single leaf section exceeds this, we soft-split on paragraph
# boundaries. We never split inside code fences or tables.
MAX_TOKENS = 600

# Precompiled patterns
_HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$")
_FENCE_RE = re.compile(r"^(```|~~~)(.*)$")
_TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}")  # markdown table separator row


def _estimate_tokens(text: str) -> int:
    """
    Cheap token estimate. Matches how search.py / sentence-transformers roughly
    count: ~1 token per 4 characters is the common heuristic, but words are
    closer for English-heavy KB content. We split on whitespace then pad by 25%
    for subword expansion (BPE-ish).
    """
    if not text:
        return 0
    words = text.split()
    return int(len(words) * 1.25) + 1


def _is_table_row(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|") and len(stripped) >= 3


@dataclass
class Block:
    """A contiguous run of lines that must not be internally split."""
    kind: str       # 'text' | 'code' | 'table' | 'heading'
    lines: list     # original lines (no trailing \n)
    level: int = 0  # heading level (1-3) if kind == 'heading', else 0
    title: str = "" # heading title if kind == 'heading'

    @property
    def text(self) -> str:
        return "\n".join(self.lines)

    @property
    def tokens(self) -> int:
        return _estimate_tokens(self.text)


def _parse_blocks(body: str) -> list[Block]:
    """
    Walk the body line-by-line producing atomic Blocks. A Block is any of:
      - heading (single line, level 1-3)
      - code (fenced block, always kept intact)
      - table (consecutive pipe rows, always kept intact)
      - text (everything else, collected until a boundary)
    """
    blocks: list[Block] = []
    lines = body.split("\n")
    i = 0
    n = len(lines)

    text_buf: list[str] = []

    def flush_text():
        nonlocal text_buf
        if text_buf and any(l.strip() for l in text_buf):
            blocks.append(Block(kind="text", lines=text_buf[:]))
        text_buf = []

    while i < n:
        line = lines[i]

        # Fenced code block — scan until the closing fence
        fence = _FENCE_RE.match(line)
        if fence:
            flush_text()
            fence_marker = fence.group(1)
            buf = [line]
            i += 1
            while i < n:
                buf.append(lines[i])
                if lines[i].strip().startswith(fence_marker):
                    i += 1
                    break
                i += 1
            blocks.append(Block(kind="code", lines=buf))
            continue

        # Heading H1-H3 — treat H4+ as regular text so section granularity stays
        # coarse enough to hit the target token budget.
        h = _HEADING_RE.match(line)
        if h and len(h.group(1)) <= 3:
            flush_text()
            blocks.append(Block(
                kind="heading", lines=[line],
                level=len(h.group(1)), title=h.group(2).strip(),
            ))
            i += 1
            continue

        # Table — needs: header row, separator row, then body rows. We detect by
        # pairing "|...|" with a separator "| --- |" on the next line.
        if _is_table_row(line) and i + 1 < n and _TABLE_SEP_RE.match(lines[i + 1]):
            flush_text()
            buf = [line, lines[i + 1]]
            i += 2
            while i < n and _is_table_row(lines[i]):
                buf.append(lines[i])
                i += 1
            blocks.append(Block(kind="table", lines=buf))
            continue

        # Regular text line — accumulate
        text_buf.append(line)
        i += 1

    flush_text()
    return blocks


@dataclass
class Chunk:
    """A semantic chunk ready for embedding."""
    doc_id: str                  # e.g. "concepts/agent-planning"
    chunk_id: str                # e.g. "concepts/agent-planning#0003"
    heading_path: list = field(default_factory=list)   # breadcrumb of H1->H3 titles
    text: str = ""               # raw chunk text (no frontmatter)
    tokens: int = 0              # estimated token count
    content_hash: str = ""       # sha256 of text for incremental indexing

    @property
    def embed_text(self) -> str:
        """What we actually feed to the encoder: breadcrumb + body."""
        bc = " > ".join(self.heading_path) if self.heading_path else ""
        if bc:
            return f"{bc}\n\n{self.text}"
        return self.text

    def to_dict(self) -> dict:
        return asdict(self)


def _make_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _pack_blocks(
    blocks: Iterable[Block],
    heading_path: list,
    doc_id: str,
    start_idx: int,
) -> list[Chunk]:
    """
    Greedily pack blocks into chunks of ~TARGET_TOKENS under the given heading
    path. Atomic blocks (code, table) are never split; if one exceeds MAX_TOKENS
    on its own it still emits as a single chunk (exceeding budget is preferable
    to breaking structure).
    """
    chunks: list[Chunk] = []
    buf: list[Block] = []
    buf_tokens = 0

    def emit():
        nonlocal buf, buf_tokens
        if not buf:
            return
        text = "\n\n".join(b.text for b in buf).strip()
        if not text:
            buf = []
            buf_tokens = 0
            return
        idx = start_idx + len(chunks)
        chunk = Chunk(
            doc_id=doc_id,
            chunk_id=f"{doc_id}#{idx:04d}",
            heading_path=heading_path[:],
            text=text,
            tokens=_estimate_tokens(text),
            content_hash=_make_hash(text),
        )
        chunks.append(chunk)
        buf = []
        buf_tokens = 0

    for block in blocks:
        bt = block.tokens
        # A giant atomic block (>MAX): emit current buffer, then emit it solo.
        if bt > MAX_TOKENS and not buf:
            buf.append(block)
            buf_tokens += bt
            emit()
            continue
        # Adding this block would overflow? Emit first, then start new buffer.
        if buf and buf_tokens + bt > TARGET_TOKENS:
            emit()
        buf.append(block)
        buf_tokens += bt
        # If a text block alone filled us up nicely, emit eagerly.
        if buf_tokens >= TARGET_TOKENS:
            emit()

    emit()
    return chunks


def chunk_document(doc_id: str, body: str) -> list[Chunk]:
    """
    Split a markdown body into semantic chunks.

    Sections are defined by H1/H2/H3 headings. Each chunk carries the heading
    path it belongs to so the encoder sees breadcrumb context.

    Strategy:
      1. Parse body into atomic blocks (text/code/table/heading).
      2. Walk blocks, maintaining a heading-path stack.
      3. For each leaf section (content between headings), pack its blocks.
      4. If a short leaf would produce a tiny chunk, it still gets its own
         chunk — tiny chunks are rare in a well-structured wiki and keeping
         heading boundaries clean matters more than perfect packing.
    """
    blocks = _parse_blocks(body)
    if not blocks:
        return []

    chunks: list[Chunk] = []
    heading_stack: list[tuple[int, str]] = []  # [(level, title), ...]
    current_section: list[Block] = []

    def current_path() -> list:
        return [title for _, title in heading_stack]

    def flush_section():
        nonlocal current_section
        if not current_section:
            return
        new_chunks = _pack_blocks(
            current_section, current_path(), doc_id, start_idx=len(chunks),
        )
        chunks.extend(new_chunks)
        current_section = []

    for b in blocks:
        if b.kind == "heading":
            # Section boundary — flush anything pending under the prior path.
            flush_section()
            # Pop any deeper-or-equal levels off the stack.
            while heading_stack and heading_stack[-1][0] >= b.level:
                heading_stack.pop()
            heading_stack.append((b.level, b.title))
            # Heading text itself is not content, but we keep a leading context
            # line in the next chunk's breadcrumb -- the title suffices.
        else:
            current_section.append(b)

    flush_section()

    # Edge case: body that had no headings at all — still chunk the text.
    if not chunks and blocks:
        chunks = _pack_blocks(blocks, [], doc_id, start_idx=0)

    return chunks


__all__ = [
    "Chunk",
    "Block",
    "chunk_document",
    "TARGET_TOKENS",
    "MIN_TOKENS",
    "MAX_TOKENS",
]
