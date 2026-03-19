"""ui/page.py — Streamlit page-level configuration."""

import streamlit as st


def configure_page() -> None:
    st.set_page_config(
        page_title="TechBot",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="expanded",
    )