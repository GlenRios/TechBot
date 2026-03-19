"""state/session.py — Initialises and manages Streamlit session state."""

import streamlit as st
from core.level_detector import detect_level

# Re-detect level every N user messages when on auto mode
_REDETECT_EVERY = 5

_DEFAULTS: dict = {
    "messages":       [],    # list of {"role": str, "content": str}
    "detected_level": None,  # "beginner" | "intermediate" | "advanced" | None
    "manual_level":   "auto",
    "msg_count":      0,
}


def init_state() -> None:
    """Set default values for any missing session-state keys."""
    for key, value in _DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = value


def effective_level() -> str:
    """
    Return the level that should be used for the current response.
    Manual override wins; otherwise fall back to the auto-detected level
    (defaulting to 'intermediate' if nothing has been detected yet).
    """
    if st.session_state.manual_level != "auto":
        return st.session_state.manual_level
    return st.session_state.detected_level or "intermediate"


def update_detected_level(text: str) -> None:
    """
    Re-run level detection when the user is on auto mode and either:
    - no level has been detected yet (first message), or
    - the message counter hits the re-detect threshold.
    """
    if st.session_state.manual_level != "auto":
        return

    is_first_message  = st.session_state.detected_level is None
    hit_redetect_tick = (st.session_state.msg_count % _REDETECT_EVERY == 0)

    if is_first_message or hit_redetect_tick:
        st.session_state.detected_level = detect_level(text)


def reset_session() -> None:
    """Clear conversation history and reset detection state."""
    st.session_state.messages       = []
    st.session_state.detected_level = None
    st.session_state.msg_count      = 0