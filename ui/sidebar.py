"""ui/sidebar.py — Renders the settings & stats sidebar."""

import streamlit as st
from config.prompts import LEVELS
from state.session  import effective_level, reset_session


def render_sidebar() -> None:
    with st.sidebar:
        _render_level_selector()
        st.divider()
        _render_stats()
        st.divider()
        _render_clear_button()
        _render_footer()


# ── Private helpers ────────────────────────────────────────────────────────────

def _render_level_selector() -> None:
    st.markdown("## ⚙️ Settings")
    st.markdown("**Technical Level**")

    selected = st.radio(
        label="level_radio",
        options=list(LEVELS.keys()),
        format_func=lambda k: LEVELS[k],
        index=0,
        label_visibility="collapsed",
    )
    st.session_state.manual_level = selected


def _render_stats() -> None:
    st.markdown("**Session Stats**")

    detected = st.session_state.detected_level or "—"
    active   = effective_level()
    count    = st.session_state.msg_count

    st.markdown(
        f"""
        <div class="stat-card">
            <span class="stat-label">Detected level</span><br>
            <span class="stat-value">{detected}</span>
        </div>
        <div class="stat-card">
            <span class="stat-label">Active level</span><br>
            <span class="stat-value">{active}</span>
        </div>
        <div class="stat-card">
            <span class="stat-label">Messages</span><br>
            <span class="stat-value">{count}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_clear_button() -> None:
    if st.button("🗑️ Clear conversation", use_container_width=True):
        reset_session()
        st.rerun()


def _render_footer() -> None:
    st.markdown("---")
    st.markdown(
        "<small style='color:#64748b'>TechBot v1.0 · Powered by Claude</small>",
        unsafe_allow_html=True,
    )