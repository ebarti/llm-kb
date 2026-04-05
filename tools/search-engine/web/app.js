// ===== Wiki Search Engine - Frontend =====

const API = '';
let searchTimeout = null;
let currentView = 'search'; // search | article | graph
let graphInitialized = false;

// ===== Init =====

document.addEventListener('DOMContentLoaded', () => {
    loadStats();

    const input = document.getElementById('search-input');
    input.addEventListener('input', () => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(doSearch, 200);
    });
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            clearTimeout(searchTimeout);
            doSearch();
        }
    });

    document.getElementById('filter-type').addEventListener('change', doSearch);
});

// ===== Stats =====

async function loadStats() {
    try {
        const res = await fetch(`${API}/api/stats`);
        const data = await res.json();
        document.getElementById('stat-total').textContent = `${data.total} articles`;
        document.getElementById('stat-concepts').textContent = `${data.concepts} concepts`;
        document.getElementById('stat-sources').textContent = `${data.sources} sources`;
        document.getElementById('stat-entities').textContent = `${data.entities} entities`;
    } catch (e) {
        console.error('Failed to load stats:', e);
    }
}

// ===== Search =====

async function doSearch() {
    const query = document.getElementById('search-input').value.trim();
    const type = document.getElementById('filter-type').value;

    if (!query) {
        document.getElementById('results-list').innerHTML = '';
        document.getElementById('results-info').textContent = '';
        return;
    }

    const params = new URLSearchParams({ q: query, type: type, top: 20 });

    try {
        const res = await fetch(`${API}/api/search?${params}`);
        const data = await res.json();
        renderResults(data.results, query);
    } catch (e) {
        document.getElementById('results-info').textContent = 'Search error: ' + e.message;
    }
}

function renderResults(results, query) {
    const info = document.getElementById('results-info');
    const list = document.getElementById('results-list');

    if (results.length === 0) {
        info.textContent = `No results for "${query}"`;
        list.innerHTML = '';
        return;
    }

    info.textContent = `${results.length} results for "${query}"`;

    list.innerHTML = results.map(r => `
        <div class="result-card" onclick="openArticle('${r.id}')">
            <div class="result-header">
                <span class="result-title">${escapeHtml(r.title)}</span>
                <span class="result-type type-${r.type}">${r.type}</span>
            </div>
            ${r.summary ? `<div class="result-summary">${escapeHtml(r.summary).substring(0, 180)}${r.summary.length > 180 ? '...' : ''}</div>` : ''}
            ${r.snippet ? `<div class="result-snippet">${escapeHtml(r.snippet)}</div>` : ''}
            <div class="result-meta">
                <span class="result-score">score: ${r.score}</span>
                ${r.date ? `<span>date: ${r.date}</span>` : ''}
                ${r.backlinks && r.backlinks.length ? `<span>${r.backlinks.length} backlinks</span>` : ''}
            </div>
        </div>
    `).join('');
}

// ===== Article View =====

async function openArticle(docId) {
    try {
        const res = await fetch(`${API}/api/article?id=${encodeURIComponent(docId)}`);
        const data = await res.json();

        if (data.error) {
            alert(data.error);
            return;
        }

        renderArticle(data);
        showView('article');
    } catch (e) {
        console.error('Failed to load article:', e);
    }
}

function renderArticle(article) {
    const content = document.getElementById('article-content');

    let metaHtml = '<div class="article-meta">';
    metaHtml += `<span class="article-meta-item type-${article.type}">${article.type}</span>`;
    if (article.date) metaHtml += `<span class="article-meta-item">${article.date}</span>`;
    article.tags.forEach(t => {
        metaHtml += `<span class="article-meta-item">#${t}</span>`;
    });
    metaHtml += '</div>';

    content.innerHTML = `
        <h1>${escapeHtml(article.title)}</h1>
        ${metaHtml}
        ${article.summary ? `<p style="color:var(--text-muted);font-style:italic;margin-bottom:20px;">${escapeHtml(article.summary)}</p>` : ''}
        <div class="article-body">${article.body_html}</div>
    `;

    // Wire up wikilinks
    content.querySelectorAll('.wikilink').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const target = link.dataset.target;
            openArticle(target);
        });
    });

    // Related
    const relatedEl = document.getElementById('sidebar-related');
    if (article.related && article.related.length > 0) {
        relatedEl.innerHTML = `
            <div class="sidebar-title">Related Articles</div>
            ${article.related.map(r =>
                `<a class="sidebar-link" onclick="openArticle('${r.id}')">${escapeHtml(r.title)}</a>`
            ).join('')}
        `;
    } else {
        relatedEl.innerHTML = '<div class="sidebar-title">Related Articles</div><p style="color:var(--text-muted);font-size:0.85em;">None found</p>';
    }

    // Backlinks
    const backlinksEl = document.getElementById('sidebar-backlinks');
    if (article.backlinks && article.backlinks.length > 0) {
        backlinksEl.innerHTML = `
            <div class="sidebar-title">Backlinks</div>
            ${article.backlinks.map(b =>
                `<a class="sidebar-link" onclick="openArticle('${b.id}')">${escapeHtml(b.title)}</a>`
            ).join('')}
        `;
    } else {
        backlinksEl.innerHTML = '<div class="sidebar-title">Backlinks</div><p style="color:var(--text-muted);font-size:0.85em;">None found</p>';
    }
}

// ===== Knowledge Graph =====

async function toggleGraph() {
    if (currentView === 'graph') {
        showSearch();
        return;
    }

    showView('graph');

    if (!graphInitialized) {
        await initGraph();
        graphInitialized = true;
    }
}

async function initGraph() {
    try {
        const res = await fetch(`${API}/api/graph`);
        const data = await res.json();
        renderGraph(data);
    } catch (e) {
        console.error('Failed to load graph:', e);
    }
}

function renderGraph(data) {
    const svg = d3.select('#graph-svg');
    const container = document.getElementById('graph-panel');
    const width = container.clientWidth;
    const height = container.clientHeight - 60;

    svg.attr('viewBox', [0, 0, width, height]);
    svg.selectAll('*').remove();

    const g = svg.append('g');

    // Zoom
    svg.call(d3.zoom()
        .scaleExtent([0.3, 4])
        .on('zoom', (event) => g.attr('transform', event.transform))
    );

    const typeColors = {
        concept: '#89b4fa',
        source: '#a6e3a1',
        entity: '#cba6f7',
        comparison: '#fab387',
    };

    const simulation = d3.forceSimulation(data.nodes)
        .force('link', d3.forceLink(data.edges).id(d => d.id).distance(80))
        .force('charge', d3.forceManyBody().strength(-200))
        .force('center', d3.forceCenter(width / 2, height / 2))
        .force('collision', d3.forceCollide().radius(30));

    const link = g.append('g')
        .selectAll('line')
        .data(data.edges)
        .join('line')
        .attr('class', 'graph-link');

    const node = g.append('g')
        .selectAll('g')
        .data(data.nodes)
        .join('g')
        .attr('class', 'graph-node')
        .call(d3.drag()
            .on('start', (event, d) => {
                if (!event.active) simulation.alphaTarget(0.3).restart();
                d.fx = d.x; d.fy = d.y;
            })
            .on('drag', (event, d) => { d.fx = event.x; d.fy = event.y; })
            .on('end', (event, d) => {
                if (!event.active) simulation.alphaTarget(0);
                d.fx = null; d.fy = null;
            })
        )
        .on('click', (event, d) => {
            openArticle(d.id);
        });

    node.append('circle')
        .attr('r', 7)
        .attr('fill', d => typeColors[d.type] || '#cdd6f4')
        .attr('stroke', d => typeColors[d.type] || '#cdd6f4');

    node.append('text')
        .attr('dx', 12)
        .attr('dy', 4)
        .text(d => d.title.length > 25 ? d.title.substring(0, 25) + '...' : d.title);

    // Add title tooltip
    node.append('title').text(d => `${d.title} [${d.type}]`);

    simulation.on('tick', () => {
        link
            .attr('x1', d => d.source.x)
            .attr('y1', d => d.source.y)
            .attr('x2', d => d.target.x)
            .attr('y2', d => d.target.y);
        node.attr('transform', d => `translate(${d.x},${d.y})`);
    });
}

// ===== View Management =====

function showView(view) {
    currentView = view;
    document.getElementById('search-panel').classList.toggle('hidden', view !== 'search');
    document.getElementById('results-panel').classList.toggle('hidden', view !== 'search');
    document.getElementById('article-panel').classList.toggle('hidden', view !== 'article');
    document.getElementById('graph-panel').classList.toggle('hidden', view !== 'graph');
}

function showSearch() {
    showView('search');
    document.getElementById('search-input').focus();
}

// ===== Utility =====

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
