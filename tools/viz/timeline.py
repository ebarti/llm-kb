#!/usr/bin/env python3
"""Timeline Generator - HTML timeline of source publication and ingestion dates."""

import json
import os
import re

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WIKI = os.path.join(BASE, "wiki")
OUTPUT = os.path.join(BASE, "output", "images")

COLORS = {
    "source-summary": "#4a90d9",
    "source": "#4a90d9",
    "concept": "#2ecc71",
    "entity": "#e67e22",
    "comparison": "#9b59b6",
}


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


def scan_dates():
    entries = []
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
            entry = {
                "id": rel,
                "title": fm.get("title", fn.replace(".md", "")),
                "type": fm.get("type", "concept"),
                "date_published": fm.get("date_published", ""),
                "date_ingested": fm.get("date_ingested", ""),
                "last_compiled": fm.get("last_compiled", ""),
            }
            # Use whatever date is available
            if entry["date_published"] or entry["date_ingested"] or entry["last_compiled"]:
                entries.append(entry)
    return entries


def generate_html(entries):
    data_js = json.dumps(entries)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Wiki Timeline</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #1a1a2e; color: #eee; }}
h1 {{ text-align: center; padding: 20px; font-size: 22px; color: #e94560; }}
#timeline {{ width: 90%; margin: 0 auto; padding-bottom: 40px; }}
#tooltip {{ position: fixed; display: none; background: #16213e; border: 1px solid #555; border-radius: 8px; padding: 12px; max-width: 350px; font-size: 13px; z-index: 20; pointer-events: none; box-shadow: 0 4px 20px rgba(0,0,0,.5); }}
.legend {{ display: flex; gap: 20px; justify-content: center; margin-bottom: 20px; font-size: 13px; }}
.legend-item {{ display: flex; align-items: center; gap: 6px; }}
.legend-dot {{ width: 12px; height: 12px; border-radius: 50%; }}
svg {{ overflow: visible; }}
</style>
</head>
<body>
<h1>Knowledge Base Timeline</h1>
<div class="legend">
  <div class="legend-item"><div class="legend-dot" style="background:#e94560"></div> Published</div>
  <div class="legend-item"><div class="legend-dot" style="background:#4a90d9"></div> Ingested</div>
  <div class="legend-item"><div class="legend-dot" style="background:#2ecc71"></div> Last Compiled</div>
</div>
<div id="tooltip"></div>
<div id="timeline"></div>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
const entries = {data_js};
const margin = {{top: 30, right: 40, bottom: 50, left: 240}};
const width = document.getElementById("timeline").clientWidth - margin.left - margin.right;

// Collect all dates
const allDates = [];
entries.forEach(e => {{
  ["date_published","date_ingested","last_compiled"].forEach(k => {{
    if (e[k]) allDates.push(new Date(e[k]));
  }});
}});

if (allDates.length === 0) {{
  document.getElementById("timeline").innerHTML = "<p style='text-align:center;padding:40px;color:#aaa;'>No date fields found in frontmatter. Add date_published, date_ingested, or last_compiled to wiki files.</p>";
}} else {{
  const minDate = d3.min(allDates);
  const maxDate = d3.max(allDates);
  // Pad by 5%
  const pad = (maxDate - minDate) * 0.05 || 86400000;
  const rowHeight = 36;
  const height = entries.length * rowHeight;

  const x = d3.scaleTime().domain([new Date(minDate - pad), new Date(+maxDate + pad)]).range([0, width]);
  const y = d3.scaleBand().domain(entries.map(e => e.id)).range([0, height]).padding(0.3);

  const svg = d3.select("#timeline").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g").attr("transform", `translate(${{margin.left}},${{margin.top}})`);

  // X axis
  svg.append("g").attr("transform", `translate(0,${{height}})`)
    .call(d3.axisBottom(x).ticks(6)).selectAll("text").style("fill", "#aaa");
  svg.selectAll(".domain, .tick line").style("stroke", "#444");

  // Y axis (article names)
  svg.append("g").call(d3.axisLeft(y).tickFormat(d => {{
    const e = entries.find(e => e.id === d);
    const t = e ? e.title : d;
    return t.length > 32 ? t.slice(0, 30) + "..." : t;
  }})).selectAll("text").style("fill", "#ccc").style("font-size", "11px");
  svg.selectAll(".domain, .tick line").style("stroke", "#444");

  // Grid lines
  svg.append("g").selectAll("line").data(entries).join("line")
    .attr("x1", 0).attr("x2", width)
    .attr("y1", d => y(d.id) + y.bandwidth() / 2)
    .attr("y2", d => y(d.id) + y.bandwidth() / 2)
    .attr("stroke", "#222").attr("stroke-dasharray", "2,4");

  const tooltip = document.getElementById("tooltip");
  function showTip(event, d, label, date) {{
    tooltip.innerHTML = `<strong>${{d.title}}</strong><br>${{label}}: ${{date}}<br><small>${{d.type}}</small>`;
    tooltip.style.display = "block";
    tooltip.style.left = (event.pageX + 12) + "px";
    tooltip.style.top = (event.pageY - 10) + "px";
  }}
  function hideTip() {{ tooltip.style.display = "none"; }}

  // Dots
  const dateTypes = [
    {{key: "date_published", color: "#e94560", label: "Published"}},
    {{key: "date_ingested", color: "#4a90d9", label: "Ingested"}},
    {{key: "last_compiled", color: "#2ecc71", label: "Compiled"}},
  ];

  dateTypes.forEach(dt => {{
    svg.selectAll(`.dot-${{dt.key}}`).data(entries.filter(e => e[dt.key])).join("circle")
      .attr("cx", d => x(new Date(d[dt.key])))
      .attr("cy", d => y(d.id) + y.bandwidth() / 2)
      .attr("r", 6)
      .attr("fill", dt.color)
      .attr("stroke", "#fff").attr("stroke-width", 1)
      .style("cursor", "pointer")
      .on("mouseover", (e, d) => showTip(e, d, dt.label, d[dt.key]))
      .on("mouseout", hideTip);
  }});

  // Connect published -> compiled for same entry
  entries.forEach(e => {{
    const dates = [];
    if (e.date_published) dates.push(new Date(e.date_published));
    if (e.date_ingested) dates.push(new Date(e.date_ingested));
    if (e.last_compiled) dates.push(new Date(e.last_compiled));
    if (dates.length >= 2) {{
      dates.sort((a, b) => a - b);
      svg.append("line")
        .attr("x1", x(dates[0])).attr("x2", x(dates[dates.length - 1]))
        .attr("y1", y(e.id) + y.bandwidth() / 2)
        .attr("y2", y(e.id) + y.bandwidth() / 2)
        .attr("stroke", "#555").attr("stroke-width", 1.5);
    }}
  }});
}}
</script>
</body>
</html>"""


def main():
    os.makedirs(OUTPUT, exist_ok=True)
    entries = scan_dates()
    html_path = os.path.join(OUTPUT, "timeline.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(generate_html(entries))
    print(f"Generated: {html_path}")
    print(f"  {len(entries)} entries with date fields")


if __name__ == "__main__":
    main()
