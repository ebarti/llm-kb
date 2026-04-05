#!/usr/bin/env python3
"""Statistics Dashboard - Wiki metrics as JSON or interactive HTML dashboard."""

import json
import os
import re
import subprocess
import sys
from collections import Counter

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WIKI = os.path.join(BASE, "wiki")
RAW = os.path.join(BASE, "raw")
OUTPUT = os.path.join(BASE, "output", "images")


def parse_frontmatter(text):
    fm = {}
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return fm
    for line in m.group(1).split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def extract_wikilinks(text):
    body = re.sub(r"^---.*?---", "", text, count=1, flags=re.DOTALL)
    return re.findall(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]", body)


def extract_tags(text):
    fm_match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not fm_match:
        return []
    fm_text = fm_match.group(1)
    tags_match = re.search(r"tags:\s*\[([^\]]*)\]", fm_text)
    if tags_match:
        return [t.strip().strip('"').strip("'") for t in tags_match.group(1).split(",") if t.strip()]
    return []


def count_words(text):
    body = re.sub(r"^---.*?---", "", text, count=1, flags=re.DOTALL)
    return len(body.split())


def get_git_dates():
    """Try to get file creation dates from git log."""
    dates = {}
    try:
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--name-only", "--pretty=format:%aI", "--", "wiki/"],
            capture_output=True, text=True, cwd=BASE, timeout=10
        )
        if result.returncode == 0:
            current_date = None
            for line in result.stdout.split("\n"):
                line = line.strip()
                if not line:
                    continue
                if re.match(r"\d{4}-\d{2}-\d{2}", line):
                    current_date = line[:10]
                elif current_date and line.endswith(".md"):
                    dates[line] = current_date
    except Exception:
        pass
    return dates


def compute_stats():
    files_by_type = Counter()
    word_counts = {}
    link_counts = {}
    all_tags = Counter()
    connections = Counter()
    all_links = []
    dates_ingested = []
    orphans = []
    all_nodes = set()

    for dirpath, _, filenames in os.walk(WIKI):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fn)
            rel = os.path.relpath(fpath, WIKI).replace(".md", "")
            parent = rel.split("/")[0]
            if parent.startswith("_") or rel in ("log",):
                continue

            text = open(fpath, encoding="utf-8").read()
            fm = parse_frontmatter(text)
            node_type = fm.get("type", parent)
            files_by_type[node_type] += 1
            wc = count_words(text)
            word_counts[rel] = wc

            wikilinks = extract_wikilinks(text)
            link_counts[rel] = len(wikilinks)
            for link in wikilinks:
                link = link.strip()
                if link.startswith("raw/"):
                    continue
                connections[rel] += 1
                connections[link] += 1
                all_links.append((rel, link))
            all_nodes.add(rel)

            tags = extract_tags(text)
            all_tags.update(tags)

            di = fm.get("date_ingested", fm.get("last_compiled", ""))
            if di:
                dates_ingested.append({"file": rel, "date": di})

    # Count raw files
    raw_count = 0
    if os.path.isdir(RAW):
        for _, _, fns in os.walk(RAW):
            raw_count += len([f for f in fns if f.endswith(".md")])

    # Orphans: nodes with 0 links in or out
    linked_nodes = set()
    for src, tgt in all_links:
        linked_nodes.add(src)
        linked_nodes.add(tgt)
    orphans = sorted(all_nodes - linked_nodes)

    # Coverage: concepts per source, sources per concept
    sources = [n for n in all_nodes if n.startswith("sources/")]
    concepts = [n for n in all_nodes if n.startswith("concepts/")]
    src_concept_links = [(s, t) for s, t in all_links if s.startswith("sources/") and t.startswith("concepts/")]
    concepts_per_src = {}
    sources_per_concept = {}
    for s, c in src_concept_links:
        concepts_per_src.setdefault(s, set()).add(c)
        sources_per_concept.setdefault(c, set()).add(s)

    avg_concepts_per_source = sum(len(v) for v in concepts_per_src.values()) / max(len(sources), 1)
    avg_sources_per_concept = sum(len(v) for v in sources_per_concept.values()) / max(len(concepts), 1)

    # Top connected
    top_connected = sorted(connections.items(), key=lambda x: x[1], reverse=True)[:10]

    # Growth over time
    git_dates = get_git_dates()
    growth = Counter()
    for entry in dates_ingested:
        growth[entry["date"][:7]] += 1  # monthly
    for f, d in git_dates.items():
        growth[d[:7]] += 0  # ensure months present

    total_words = sum(word_counts.values())
    avg_links = sum(link_counts.values()) / max(len(link_counts), 1)

    return {
        "files_by_type": dict(files_by_type),
        "raw_files": raw_count,
        "total_wiki_files": len(word_counts),
        "total_words": total_words,
        "avg_words_per_file": round(total_words / max(len(word_counts), 1)),
        "word_counts_top10": sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10],
        "total_links": len(all_links),
        "avg_links_per_article": round(avg_links, 1),
        "link_density_top10": sorted(link_counts.items(), key=lambda x: x[1], reverse=True)[:10],
        "avg_concepts_per_source": round(avg_concepts_per_source, 1),
        "avg_sources_per_concept": round(avg_sources_per_concept, 1),
        "top_connected": top_connected,
        "orphans": orphans,
        "tag_frequency": dict(all_tags.most_common(20)),
        "growth_by_month": dict(sorted(growth.items())),
    }


def generate_html(stats):
    data_js = json.dumps(stats)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Wiki Statistics Dashboard</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #1a1a2e; color: #eee; padding: 20px; }}
h1 {{ text-align: center; color: #e94560; margin-bottom: 24px; font-size: 24px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 16px; max-width: 1400px; margin: 0 auto; }}
.card {{ background: #16213e; border: 1px solid #333; border-radius: 10px; padding: 18px; }}
.card h2 {{ color: #e94560; font-size: 15px; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px; }}
.metric {{ display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid #222; font-size: 14px; }}
.metric .value {{ color: #4a90d9; font-weight: bold; }}
.bar-chart {{ margin-top: 8px; }}
.bar-row {{ display: flex; align-items: center; margin: 4px 0; font-size: 12px; }}
.bar-label {{ width: 180px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: #aaa; }}
.bar {{ height: 18px; border-radius: 3px; margin-left: 8px; min-width: 2px; display: flex; align-items: center; padding-left: 6px; font-size: 11px; color: #fff; }}
.orphan-list {{ font-size: 12px; color: #e67e22; line-height: 1.8; }}
.stat-number {{ font-size: 36px; font-weight: bold; color: #4a90d9; text-align: center; }}
.stat-label {{ font-size: 12px; color: #888; text-align: center; margin-top: 4px; }}
.stat-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }}
</style>
</head>
<body>
<h1>Wiki Statistics Dashboard</h1>
<div class="grid" id="dashboard"></div>
<script>
const S = {data_js};

function el(tag, props, ...children) {{
  const e = document.createElement(tag);
  if (props) Object.entries(props).forEach(([k,v]) => {{ if (k === "innerHTML") e.innerHTML = v; else if (k === "style") Object.assign(e.style, v); else e[k] = v; }});
  children.forEach(c => {{ if (typeof c === "string") e.appendChild(document.createTextNode(c)); else if (c) e.appendChild(c); }});
  return e;
}}

function card(title, ...children) {{
  const c = el("div", {{className: "card"}}, el("h2", null, title));
  children.forEach(ch => c.appendChild(ch));
  return c;
}}

function metric(label, value) {{
  return el("div", {{className: "metric"}}, el("span", null, label), el("span", {{className: "value"}}, String(value)));
}}

function barChart(items, color, maxVal) {{
  const div = el("div", {{className: "bar-chart"}});
  if (!maxVal) maxVal = Math.max(...items.map(i => i[1]), 1);
  items.forEach(([label, val]) => {{
    const row = el("div", {{className: "bar-row"}});
    row.appendChild(el("span", {{className: "bar-label", title: label}}, label.split("/").pop()));
    const pct = Math.max(2, (val / maxVal) * 100);
    row.appendChild(el("div", {{className: "bar", style: {{width: pct + "%", background: color}}}}, String(val)));
    div.appendChild(row);
  }});
  return div;
}}

const dash = document.getElementById("dashboard");

// Overview card
const overview = card("Overview");
const sg = el("div", {{className: "stat-grid"}});
[["Total Files", S.total_wiki_files], ["Total Words", S.total_words.toLocaleString()], ["Total Links", S.total_links],
 ["Avg Words/File", S.avg_words_per_file], ["Avg Links/File", S.avg_links_per_article], ["Raw Files", S.raw_files]].forEach(([l,v]) => {{
  const d = el("div");
  d.appendChild(el("div", {{className: "stat-number", style: {{fontSize: "24px"}}}}, String(v)));
  d.appendChild(el("div", {{className: "stat-label"}}, l));
  sg.appendChild(d);
}});
overview.appendChild(sg);
dash.appendChild(overview);

// Files by type
const typeCard = card("Files by Type");
Object.entries(S.files_by_type).sort((a,b) => b[1]-a[1]).forEach(([t,c]) => typeCard.appendChild(metric(t, c)));
dash.appendChild(typeCard);

// Coverage
const covCard = card("Coverage Metrics");
covCard.appendChild(metric("Concepts per Source (avg)", S.avg_concepts_per_source));
covCard.appendChild(metric("Sources per Concept (avg)", S.avg_sources_per_concept));
dash.appendChild(covCard);

// Top connected
dash.appendChild(card("Top Connected Nodes (Hub Articles)", barChart(S.top_connected, "#e94560")));

// Word counts
dash.appendChild(card("Longest Articles (Words)", barChart(S.word_counts_top10, "#4a90d9")));

// Link density
dash.appendChild(card("Most Linked Articles", barChart(S.link_density_top10, "#2ecc71")));

// Tags
if (Object.keys(S.tag_frequency).length > 0) {{
  dash.appendChild(card("Tag Frequency", barChart(Object.entries(S.tag_frequency), "#9b59b6")));
}}

// Growth
if (Object.keys(S.growth_by_month).length > 0) {{
  dash.appendChild(card("Growth by Month", barChart(Object.entries(S.growth_by_month), "#e67e22")));
}}

// Orphans
if (S.orphans.length > 0) {{
  const oCard = card("Orphan Articles (No Links)");
  oCard.appendChild(el("div", {{className: "orphan-list", innerHTML: S.orphans.map(o => o.split("/").pop()).join(", ")}}));
  dash.appendChild(oCard);
}} else {{
  dash.appendChild(card("Orphan Detection", el("div", {{style: {{color: "#2ecc71", textAlign: "center", padding: "12px"}}}}, "No orphan articles detected.")));
}}
</script>
</body>
</html>"""


def main():
    os.makedirs(OUTPUT, exist_ok=True)
    stats = compute_stats()

    if "--html" in sys.argv:
        html_path = os.path.join(OUTPUT, "stats-dashboard.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(generate_html(stats))
        print(f"Generated: {html_path}")
    else:
        # Always generate HTML too
        html_path = os.path.join(OUTPUT, "stats-dashboard.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(generate_html(stats))
        print(f"Generated: {html_path}")
        # Also print JSON to stdout
        print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
