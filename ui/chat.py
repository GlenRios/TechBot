"""ui/chat.py — Chat area components: welcome message, history, and input."""

import streamlit as st

_WELCOME = (
    "👋 **Hello! I'm TechBot.**\n\n"
    "I specialize in recommending **apps, software, and cloud services** "
    "tailored to your needs. Just tell me what you're trying to do and "
    "I'll suggest the best tools — free or paid.\n\n"
    "**Example questions:**\n"
    "- *What's the best project management tool for a small team?*\n"
    "- *Recommend a CI/CD pipeline for a Node.js microservices project.*\n"
    "- *I need a free tool to edit videos on my phone.*"
)


def render_welcome() -> None:
    """Show the intro message when the conversation is empty."""
    with st.chat_message("assistant"):
        st.markdown(_WELCOME)


def render_history() -> None:
    """Re-render all messages stored in session state."""
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])