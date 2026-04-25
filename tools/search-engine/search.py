#!/usr/bin/env python3
"""
Search engine for the LLM knowledge base wiki.
BM25 + TF-IDF ranking with fuzzy matching and frontmatter-aware filtering.
Pure Python stdlib implementation.
"""

import argparse
import json
import math
import os
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
WIKI_DIR = BASE_DIR.parent.parent / "wiki"
INDEX_DIR = BASE_DIR / ".index"
INDEX_FILE = INDEX_DIR / "index.json"

# BM25 Okapi parameters
BM25_K1 = 1.5
BM25_B = 0.75

# Fuzzy matching
MAX_EDIT_DISTANCE = 2

# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    """Parse YAML-like frontmatter from markdown text."""
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            body = parts[2]
            for line in fm_text.split("\n"):
                line = line.strip()
                if not line:
                    continue
                match = re.match(r'^(\w[\w_]*):\s*(.+)$', line)
                if match:
                    key, val = match.group(1), match.group(2).strip()
                    # Strip quotes
                    if val.startswith('"') and val.endswith('"'):
                        val = val[1:-1]
                    elif val.startswith("'") and val.endswith("'"):
                        val = val[1:-1]
                    # Parse arrays
                    if val.startswith("["):
                        items = re.findall(r'"([^"]*)"', val)
                        if not items:
                            items = re.findall(r"'([^']*)'", val)
                        if not items:
                            items = [v.strip() for v in val.strip("[]").split(",") if v.strip()]
                        val = items
                    meta[key] = val
    return meta, body


# ---------------------------------------------------------------------------
# Tokenization
# ---------------------------------------------------------------------------

STOP_WORDS = frozenset(
    "a an and are as at be by for from has have he in is it its of on or "
    "that the to was were will with this not but they them their what which "
    "who how when where can could would should may might do does did been "
    "being had has have having if into more most no nor only own same so "
    "such than too very just don t s re ve ll d m".split()
)


def tokenize(text):
    """Lowercase tokenize, remove stop words."""
    tokens = re.findall(r'[a-z0-9]+(?:[-_][a-z0-9]+)*', text.lower())
    return [t for t in tokens if t not in STOP_WORDS and len(t) > 1]


# ---------------------------------------------------------------------------
# Fuzzy matching (Levenshtein)
# ---------------------------------------------------------------------------

def edit_distance(s1, s2):
    """Compute Levenshtein edit distance."""
    if len(s1) < len(s2):
        return edit_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr = [i + 1]
        for j, c2 in enumerate(s2):
            cost = 0 if c1 == c2 else 1
            curr.append(min(curr[j] + 1, prev[j + 1] + 1, prev[j] + cost))
        prev = curr
    return prev[-1]


def fuzzy_expand(query_tokens, vocab, max_dist=MAX_EDIT_DISTANCE):
    """For each query token, find fuzzy matches in vocabulary."""
    expansions = {}
    for qt in query_tokens:
        matches = set()
        matches.add(qt)
        # Prefix matching
        for v in vocab:
            if v.startswith(qt) or qt.startswith(v):
                matches.add(v)
            elif len(qt) >= 4 and len(v) >= 4:
                d = edit_distance(qt, v)
                if d <= max_dist:
                    matches.add(v)
        expansions[qt] = matches
    return expansions


# ---------------------------------------------------------------------------
# Wikilink extraction
# ---------------------------------------------------------------------------

def extract_wikilinks(text):
    """Extract [[wikilinks]] from text."""
    return re.findall(r'\[\[([^\]]+)\]\]', text)


# ---------------------------------------------------------------------------
# Index building
# ---------------------------------------------------------------------------

def scan_documents():
    """Scan wiki directory for markdown files, return list of doc dicts."""
    docs = []
    subdirs = ["sources", "concepts", "entities", "comparisons"]
    for subdir in subdirs:
        d = WIKI_DIR / subdir
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            raw = f.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(raw)
            doc_id = f"{subdir}/{f.stem}"

            # Determine type from subdir or frontmatter
            doc_type = meta.get("type", subdir.rstrip("s"))
            if doc_type == "source-summary":
                doc_type = "source"

            # Extract tags
            tags = meta.get("tags", [])
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(",")]

            # Extract links
            links = extract_wikilinks(raw)

            # Date
            date = meta.get("last_compiled", meta.get("last_updated", meta.get("date", "")))

            docs.append({
                "id": doc_id,
                "path": str(f.relative_to(WIKI_DIR)),
                "abs_path": str(f),
                "title": meta.get("title", f.stem.replace("-", " ").title()),
                "type": doc_type,
                "tags": tags,
                "date": str(date),
                "summary": meta.get("summary", ""),
                "links": links,
                "related": meta.get("related", []),
                "sources": meta.get("sources", []),
                "body": body,
                "mtime": f.stat().st_mtime,
            })
    return docs


def build_index(docs):
    """Build inverted index, doc frequency tables, etc."""
    # Tokenize all docs
    doc_tokens = {}
    doc_lengths = {}
    df = Counter()  # document frequency
    tf = {}  # term frequency per doc

    all_vocab = set()

    for doc in docs:
        text = f"{doc['title']} {doc['summary']} {doc['body']}"
        tokens = tokenize(text)
        doc_tokens[doc["id"]] = tokens
        doc_lengths[doc["id"]] = len(tokens)

        token_counts = Counter(tokens)
        tf[doc["id"]] = dict(token_counts)

        unique = set(token_counts.keys())
        all_vocab.update(unique)
        for t in unique:
            df[t] += 1

    N = len(docs)
    avg_dl = sum(doc_lengths.values()) / max(N, 1)

    # Compute IDF (BM25 variant)
    idf = {}
    for term, freq in df.items():
        idf[term] = math.log((N - freq + 0.5) / (freq + 0.5) + 1)

    # Backlinks
    backlinks = defaultdict(list)
    for doc in docs:
        for link in doc["links"]:
            # Normalize link
            link_clean = link.strip()
            if link_clean.startswith("[["):
                link_clean = link_clean[2:]
            if link_clean.endswith("]]"):
                link_clean = link_clean[:-2]
            backlinks[link_clean].append(doc["id"])

    index = {
        "built_at": time.time(),
        "num_docs": N,
        "avg_dl": avg_dl,
        "df": dict(df),
        "idf": idf,
        "tf": tf,
        "doc_lengths": doc_lengths,
        "vocab": sorted(all_vocab),
        "backlinks": dict(backlinks),
        "docs": {d["id"]: {
            "title": d["title"],
            "type": d["type"],
            "tags": d["tags"],
            "date": d["date"],
            "summary": d["summary"],
            "path": d["path"],
            "abs_path": d["abs_path"],
            "links": d["links"],
            "related": d.get("related", []),
            "sources": d.get("sources", []),
            "mtime": d["mtime"],
        } for d in docs},
    }
    return index


def save_index(index):
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_FILE.write_text(json.dumps(index, indent=2), encoding="utf-8")


def load_index():
    if INDEX_FILE.exists():
        return json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    return None


def index_needs_rebuild(index):
    """Check if any wiki file is newer than the index."""
    if index is None:
        return True
    built_at = index.get("built_at", 0)
    subdirs = ["sources", "concepts", "entities", "comparisons"]
    for subdir in subdirs:
        d = WIKI_DIR / subdir
        if not d.exists():
            continue
        for f in d.glob("*.md"):
            if f.stat().st_mtime > built_at:
                return True
    return False


def get_index(force_rebuild=False):
    """Load or rebuild index as needed."""
    index = load_index()
    if force_rebuild or index_needs_rebuild(index):
        docs = scan_documents()
        index = build_index(docs)
        save_index(index)
    return index


# ---------------------------------------------------------------------------
# Search / scoring
# ---------------------------------------------------------------------------

def bm25_score(query_tokens, doc_id, index, fuzzy_map=None):
    """Compute BM25 Okapi score for a document."""
    score = 0.0
    tf_doc = index["tf"].get(doc_id, {})
    dl = index["doc_lengths"].get(doc_id, 0)
    avg_dl = index["avg_dl"]

    for qt in query_tokens:
        # Get all terms to consider (fuzzy expanded)
        terms = fuzzy_map.get(qt, {qt}) if fuzzy_map else {qt}
        for term in terms:
            f = tf_doc.get(term, 0)
            if f == 0:
                continue
            idf_val = index["idf"].get(term, 0)
            # Discount fuzzy matches
            weight = 1.0 if term == qt else 0.6
            numerator = f * (BM25_K1 + 1)
            denominator = f + BM25_K1 * (1 - BM25_B + BM25_B * dl / max(avg_dl, 1))
            score += idf_val * (numerator / denominator) * weight
    return score


def tfidf_score(query_tokens, doc_id, index, fuzzy_map=None):
    """Secondary TF-IDF score."""
    score = 0.0
    tf_doc = index["tf"].get(doc_id, {})
    dl = index["doc_lengths"].get(doc_id, 1)

    for qt in query_tokens:
        terms = fuzzy_map.get(qt, {qt}) if fuzzy_map else {qt}
        for term in terms:
            f = tf_doc.get(term, 0)
            if f == 0:
                continue
            idf_val = index["idf"].get(term, 0)
            weight = 1.0 if term == qt else 0.5
            tf_val = f / dl
            score += tf_val * idf_val * weight
    return score


def title_boost(query_tokens, doc_info, fuzzy_map=None):
    """Boost score if query terms appear in title."""
    title_tokens = set(tokenize(doc_info.get("title", "")))
    boost = 0.0
    for qt in query_tokens:
        terms = fuzzy_map.get(qt, {qt}) if fuzzy_map else {qt}
        for term in terms:
            if term in title_tokens:
                boost += 2.0 if term == qt else 1.0
    return boost


def extract_snippet(query_tokens, doc_id, body_text, max_len=200):
    """Extract a contextual snippet around the first match."""
    lower_body = body_text.lower()
    best_pos = len(body_text)
    for qt in query_tokens:
        pos = lower_body.find(qt)
        if pos != -1 and pos < best_pos:
            best_pos = pos

    if best_pos >= len(body_text):
        # No direct match, return beginning
        return body_text[:max_len].strip().replace("\n", " ") + ("..." if len(body_text) > max_len else "")

    start = max(0, best_pos - 60)
    end = min(len(body_text), best_pos + max_len - 60)
    snippet = body_text[start:end].strip().replace("\n", " ")
    if start > 0:
        snippet = "..." + snippet
    if end < len(body_text):
        snippet = snippet + "..."
    return snippet


def search(query, index, doc_type=None, tags=None, date_from=None, date_to=None,
           top_n=10, fuzzy=True):
    """
    Search the index. Returns list of result dicts ranked by relevance.
    """
    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    vocab = set(index.get("vocab", []))
    fuzzy_map = fuzzy_expand(query_tokens, vocab) if fuzzy else None

    results = []
    for doc_id, doc_info in index["docs"].items():
        # Filter by type
        if doc_type and doc_info["type"] != doc_type:
            continue
        # Filter by tags
        if tags:
            doc_tags = set(doc_info.get("tags", []))
            if not doc_tags.intersection(set(tags)):
                continue
        # Filter by date
        doc_date = doc_info.get("date", "")
        if date_from and doc_date and doc_date < date_from:
            continue
        if date_to and doc_date and doc_date > date_to:
            continue

        bm25 = bm25_score(query_tokens, doc_id, index, fuzzy_map)
        tfidf = tfidf_score(query_tokens, doc_id, index, fuzzy_map)
        tboost = title_boost(query_tokens, doc_info, fuzzy_map)

        total = bm25 + 0.3 * tfidf + tboost

        if total > 0:
            results.append({
                "id": doc_id,
                "title": doc_info["title"],
                "type": doc_info["type"],
                "tags": doc_info.get("tags", []),
                "date": doc_info.get("date", ""),
                "summary": doc_info.get("summary", ""),
                "path": doc_info["path"],
                "score": round(total, 4),
                "bm25": round(bm25, 4),
                "tfidf": round(tfidf, 4),
                "links": doc_info.get("links", []),
                "related": doc_info.get("related", []),
                "sources": doc_info.get("sources", []),
                "backlinks": index["backlinks"].get(doc_id, []),
            })

    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:top_n]


def load_body(doc_id):
    """Load the body text for snippet extraction."""
    path = WIKI_DIR / (doc_id + ".md")
    if not path.exists():
        return ""
    raw = path.read_text(encoding="utf-8")
    _, body = parse_frontmatter(raw)
    return body


def search_with_snippets(query, index, **kwargs):
    """Search and add snippets to results."""
    results = search(query, index, **kwargs)
    query_tokens = tokenize(query)
    for r in results:
        body = load_body(r["id"])
        r["snippet"] = extract_snippet(query_tokens, r["id"], body)
    return results


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_pretty(results, query):
    """Pretty-print results for terminal."""
    if not results:
        return f"No results for: {query}"
    lines = [f"Search results for: \"{query}\" ({len(results)} hits)\n"]
    for i, r in enumerate(results, 1):
        # Show the score that actually determined the ordering so the headline
        # matches the ranking. Hybrid and reranked paths sort by rrf_score /
        # rerank_score while leaving the BM25 `score` in place (or 0.0 for
        # vector-only hits), which can otherwise look contradictory here.
        if "rerank_score" in r:
            score_label = f"rerank: {r['rerank_score']}"
        elif "rrf_score" in r:
            score_label = f"rrf: {r['rrf_score']}"
        else:
            score_label = f"score: {r['score']}"
        lines.append(f"  {i}. [{r['type'].upper()}] {r['title']}  ({score_label})")
        if r.get("summary"):
            lines.append(f"     {r['summary'][:120]}...")
        if r.get("snippet"):
            lines.append(f"     > {r['snippet'][:150]}")
        lines.append(f"     path: {r['path']}")
        if r.get("backlinks"):
            lines.append(f"     backlinks: {', '.join(r['backlinks'][:5])}")
        lines.append("")
    return "\n".join(lines)


def format_llm(results, query):
    """Concise format optimized for LLM consumption."""
    if not results:
        return f"No results for: {query}"
    lines = [f"# Search: \"{query}\" — {len(results)} results\n"]
    for i, r in enumerate(results, 1):
        # Prefer rerank > rrf > bm25 as the headline score so users see what
        # actually determined the ordering.
        if "rerank_score" in r:
            headline = f"rerank={r['rerank_score']}"
        elif "rrf_score" in r:
            headline = f"rrf={r['rrf_score']}"
        else:
            headline = f"score={r['score']}"
        lines.append(f"{i}. **{r['title']}** [{r['type']}] {headline}")
        if r.get("summary"):
            lines.append(f"   {r['summary'][:200]}")
        # Hybrid path: show the chunk snippet it matched on when available.
        snip = r.get("chunk_snippet")
        if isinstance(snip, dict) and snip.get("text"):
            bc = " > ".join(snip.get("heading_path") or [])
            if bc:
                lines.append(f"   section: {bc}")
            text = snip["text"].replace("\n", " ")
            lines.append(f"   > {text[:200]}")
        lines.append(f"   file: {r['path']}")
        if r.get("backlinks"):
            lines.append(f"   backlinks: {', '.join(r['backlinks'][:5])}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _run_hybrid(query, index, args):
    """
    Execute the hybrid (BM25 + dense) retrieval path, optionally followed by a
    cross-encoder rerank. Emits a user-friendly error and falls back to BM25 if
    ML deps are missing.
    """
    if not tokenize(query):
        return []

    try:
        import embeddings
        import hybrid
    except ImportError as e:
        print(f"Hybrid search unavailable: {e}", file=sys.stderr)
        print("Falling back to BM25.", file=sys.stderr)
        return search_with_snippets(
            query, index,
            doc_type=args.type, tags=args.tags,
            date_from=args.date_from, date_to=args.date_to,
            top_n=args.top, fuzzy=not args.no_fuzzy,
        )

    ok, msg = embeddings.is_available()
    if not ok:
        print(f"Hybrid search unavailable: {msg}", file=sys.stderr)
        print("Falling back to BM25.", file=sys.stderr)
        return search_with_snippets(
            query, index,
            doc_type=args.type, tags=args.tags,
            date_from=args.date_from, date_to=args.date_to,
            top_n=args.top, fuzzy=not args.no_fuzzy,
        )

    vector_index = embeddings.VectorIndex.load()
    if vector_index is None or vector_index.vectors.shape[0] == 0:
        print(
            "No vector index found. Run: python3 tools/search-engine/build-index.py --vectors",
            file=sys.stderr,
        )
        print("Falling back to BM25.", file=sys.stderr)
        return search_with_snippets(
            query, index,
            doc_type=args.type, tags=args.tags,
            date_from=args.date_from, date_to=args.date_to,
            top_n=args.top, fuzzy=not args.no_fuzzy,
        )

    # BM25 auto-rebuilds when wiki files change; the dense index does not.
    # If it has fallen behind, fused results would silently reflect outdated
    # content -- surface a warning AND fall back to BM25-only so the user gets
    # a correct answer now and a clear nudge to rebuild.
    if embeddings.vectors_are_stale(vector_index, WIKI_DIR):
        print(
            "Warning: vector index is stale relative to wiki content. "
            "Falling back to BM25-only. Rebuild with: "
            "python3 tools/search-engine/build-index.py --vectors",
            file=sys.stderr,
        )
        return search_with_snippets(
            query, index,
            doc_type=args.type, tags=args.tags,
            date_from=args.date_from, date_to=args.date_to,
            top_n=args.top, fuzzy=not args.no_fuzzy,
        )

    encoder = embeddings.Encoder(vector_index.model_name)

    # Pull a deep pool when reranking so the cross-encoder has something to
    # reorder; otherwise just grab the final top_n.
    hybrid_top = max(args.top, 50) if args.rerank else args.top
    # Feed the same pool depth to both retrievers so --top > 50 actually widens
    # the candidate set rather than silently capping at the default 50.
    pool = max(50, hybrid_top)

    results = hybrid.hybrid_search(
        query, index,
        vector_index=vector_index,
        encoder=encoder,
        top_n=hybrid_top,
        bm25_k=pool,
        vector_k=pool,
        bm25_search=search,
        doc_type=args.type, tags=args.tags,
        date_from=args.date_from, date_to=args.date_to,
        fuzzy=not args.no_fuzzy,
    )

    if args.rerank:
        try:
            import rerank as rerank_mod
        except ImportError as e:
            print(f"Reranker unavailable: {e}", file=sys.stderr)
        else:
            ok, msg = rerank_mod.is_available()
            if not ok:
                print(f"Reranker unavailable: {msg}", file=sys.stderr)
            else:
                reranker = rerank_mod.CrossEncoderReranker()
                results = rerank_mod.rerank_results(
                    query,
                    results,
                    reranker=reranker,
                    pool=hybrid_top,
                )

    # Always attach BM25-style snippets too for readability.
    query_tokens = tokenize(query)
    for r in results[: args.top]:
        body = load_body(r["id"])
        r["snippet"] = extract_snippet(query_tokens, r["id"], body)

    return results[: args.top]


def main():
    parser = argparse.ArgumentParser(description="Search the LLM knowledge base wiki")
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--type", choices=["concept", "source", "entity", "comparison"],
                        help="Filter by document type")
    parser.add_argument("--tags", nargs="+", help="Filter by tags")
    parser.add_argument("--date-from", help="Filter: date >= YYYY-MM-DD")
    parser.add_argument("--date-to", help="Filter: date <= YYYY-MM-DD")
    parser.add_argument("--top", type=int, default=10, help="Number of results (default: 10)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--llm", action="store_true", help="LLM-friendly output format")
    parser.add_argument("--no-fuzzy", action="store_true", help="Disable fuzzy matching")
    parser.add_argument("--rebuild", action="store_true", help="Force index rebuild")
    parser.add_argument("--stats", action="store_true", help="Show index stats")
    parser.add_argument(
        "--hybrid", action="store_true",
        help="BM25 + dense-vector hybrid retrieval with RRF fusion",
    )
    parser.add_argument(
        "--rerank", action="store_true",
        help="Apply cross-encoder rerank after hybrid retrieval (implies --hybrid)",
    )

    args = parser.parse_args()

    index = get_index(force_rebuild=args.rebuild)

    if args.stats:
        docs = index["docs"]
        types = Counter(d["type"] for d in docs.values())
        print(f"Total articles: {len(docs)}")
        for t, c in sorted(types.items()):
            print(f"  {t}: {c}")
        print(f"Vocabulary size: {len(index.get('vocab', []))}")
        print(f"Index built: {time.ctime(index.get('built_at', 0))}")
        return

    if not args.query:
        parser.print_help()
        return

    # --rerank is meaningless without hybrid candidates; auto-enable hybrid.
    if args.rerank:
        args.hybrid = True

    if args.hybrid:
        results = _run_hybrid(args.query, index, args)
    else:
        results = search_with_snippets(
            args.query, index,
            doc_type=args.type,
            tags=args.tags,
            date_from=args.date_from,
            date_to=args.date_to,
            top_n=args.top,
            fuzzy=not args.no_fuzzy,
        )

    if args.json:
        print(json.dumps(results, indent=2))
    elif args.llm:
        print(format_llm(results, args.query))
    else:
        print(format_pretty(results, args.query))


if __name__ == "__main__":
    main()
