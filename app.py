"""
TechBot — Entry point
Run: streamlit run app.py
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Carga el .env usando ruta absoluta al directorio de app.py
_ENV_PATH = Path(__file__).parent / ".env"
print(f"[DEBUG] Loading .env from: {_ENV_PATH}")
print(f"[DEBUG] .env exists: {_ENV_PATH.exists()}")
load_dotenv(dotenv_path=_ENV_PATH, override=True)
print(f"[DEBUG] CLOUDFLARE_ACCOUNT_ID = {'SET ✓' if os.environ.get('CLOUDFLARE_ACCOUNT_ID') else 'MISSING ✗'}")
print(f"[DEBUG] CLOUDFLARE_API_TOKEN  = {'SET ✓' if os.environ.get('CLOUDFLARE_API_TOKEN')  else 'MISSING ✗'}")

import streamlit as st
from state.session    import init_state, update_detected_level
from core.chat_engine import get_response
from ui.page          import configure_page
from ui.styles        import inject_styles
from ui.sidebar       import render_sidebar
from ui.header        import render_header
from ui.chat          import render_welcome, render_history

# ── Bootstrap ──────────────────────────────────────────────────────────────────
configure_page()
inject_styles()
init_state()

# ── Sidebar ────────────────────────────────────────────────────────────────────
render_sidebar()

# ── Main area ──────────────────────────────────────────────────────────────────
render_header()

if not st.session_state.messages:
    render_welcome()

render_history()

# ── Handle new user input ──────────────────────────────────────────────────────
if prompt := st.chat_input("Ask about any app, tool, or cloud service…"):

    update_detected_level(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.msg_count += 1

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        print("[DEBUG] Calling get_response()...")
        response = get_response()
        print(f"[DEBUG] Response received: {response[:80]}...")
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()