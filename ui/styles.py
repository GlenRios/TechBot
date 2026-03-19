"""ui/styles.py — Injects the global dark-theme CSS into the Streamlit page."""

import streamlit as st

_CSS = """
<style>
/* ── Fonts ──────────────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Space+Grotesk:wght@300;400;600;700&display=swap');

/* ── Design tokens ──────────────────────────────────────────────────────── */
:root {
    --bg-deep:   #0a0e1a;
    --bg-card:   #111827;
    --bg-input:  #1a2235;
    --accent:    #00d4ff;
    --accent2:   #7c3aed;
    --green:     #00ff88;
    --text:      #e2e8f0;
    --muted:     #64748b;
    --border:    rgba(0,212,255,0.18);
    --radius:    12px;
}

/* ── Global ─────────────────────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
    background-color: var(--bg-deep) !important;
    color: var(--text) !important;
}
.main .block-container {
    max-width: 820px;
    padding: 1.5rem 2rem 4rem;
    background: var(--bg-deep);
}

/* ── Header ─────────────────────────────────────────────────────────────── */
.techbot-header {
    text-align: center;
    padding: 2rem 0 1.2rem;
    background: linear-gradient(135deg, var(--bg-card) 0%, #0d1526 100%);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.techbot-header::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(ellipse at center, rgba(0,212,255,0.06) 0%, transparent 60%);
    pointer-events: none;
}
.techbot-header h1 {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 2.4rem !important;
    font-weight: 700 !important;
    letter-spacing: 6px !important;
    background: linear-gradient(90deg, var(--accent) 0%, var(--accent2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 !important;
}
.techbot-header p {
    color: var(--muted);
    font-size: 0.85rem;
    margin: 0.4rem 0 0;
    letter-spacing: 1px;
}

/* ── Chat messages ───────────────────────────────────────────────────────── */
.stChatMessage {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 0.9rem 1.1rem !important;
    margin-bottom: 0.6rem !important;
}
.stChatMessage[data-testid="user-message"] {
    border-color: rgba(124,58,237,0.35) !important;
    background: linear-gradient(135deg, #1a1535 0%, #111827 100%) !important;
}
.stChatMessage[data-testid="assistant-message"] {
    border-color: rgba(0,212,255,0.25) !important;
    background: linear-gradient(135deg, #0d1d2e 0%, #111827 100%) !important;
}
.stChatMessage p, .stChatMessage li, .stChatMessage span {
    color: var(--text) !important;
    font-size: 0.95rem !important;
    line-height: 1.65 !important;
}

/* ── Chat input ──────────────────────────────────────────────────────────── */
.stChatInputContainer {
    background: var(--bg-input) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
}
.stChatInputContainer textarea {
    background: transparent !important;
    color: var(--text) !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

/* ── Sidebar ─────────────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: var(--bg-card) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] * { color: var(--text) !important; }

/* ── Level badge ─────────────────────────────────────────────────────────── */
.level-badge {
    display: inline-block;
    padding: 0.25rem 0.8rem;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
}
.level-beginner     { background: rgba(0,255,136,0.12); color: #00ff88; border: 1px solid rgba(0,255,136,0.30); }
.level-intermediate { background: rgba(0,212,255,0.12); color: #00d4ff; border: 1px solid rgba(0,212,255,0.30); }
.level-advanced     { background: rgba(124,58,237,0.15); color: #a78bfa; border: 1px solid rgba(124,58,237,0.35); }

/* ── Stat cards ──────────────────────────────────────────────────────────── */
.stat-card {
    background: var(--bg-deep);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.6rem 0.9rem;
    margin-bottom: 0.5rem;
    font-size: 0.82rem;
    font-family: 'JetBrains Mono', monospace;
}
.stat-label { color: var(--muted); }
.stat-value { color: var(--accent); font-weight: 700; }

/* ── Scrollbar ───────────────────────────────────────────────────────────── */
::-webkit-scrollbar       { width: 5px; }
::-webkit-scrollbar-track { background: var(--bg-deep); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

/* ── Hide Streamlit chrome ───────────────────────────────────────────────── */
#MainMenu, footer, header { visibility: hidden; }
</style>
"""


def inject_styles() -> None:
    """Inject the custom dark-theme stylesheet into the page."""
    st.markdown(_CSS, unsafe_allow_html=True)