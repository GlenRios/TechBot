"""ui/header.py — Renders the top header and active-level badge."""

import streamlit as st
from state.session import effective_level


def render_header() -> None:
    _render_title_block()
    _render_level_badge()


# ── Private helpers ────────────────────────────────────────────────────────────

def _render_title_block() -> None:
    st.markdown(
        """
        <div class="techbot-header">
            <h1>TECHBOT</h1>
            <p>Apps · Software · Cloud Services · AI Tools</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_level_badge() -> None:
    level = effective_level()
    _, center, _ = st.columns([1, 2, 1])

    with center:
        st.markdown(
            f"<div style='text-align:center;margin-bottom:1rem'>"
            f"<span class='level-badge level-{level}'>● {level.capitalize()}</span>"
            f"</div>",
            unsafe_allow_html=True,
        )