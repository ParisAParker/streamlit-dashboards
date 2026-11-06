"""Pluggable analytics tracking; no events are sent externally by default.

Configure an event sink with configure_event_sink(callable). The sink receives
an event dictionary and is responsible for persistence, retries, and privacy.
"""
from __future__ import annotations
from collections.abc import Callable
from datetime import datetime, timezone
from uuid import uuid4
import logging
import streamlit as st

logger = logging.getLogger(__name__)
_sink: Callable[[dict], None] | None = None

def configure_event_sink(sink: Callable[[dict], None] | None) -> None:
    global _sink
    _sink = sink

def get_session_id() -> str:
    if "_sd_session_id" not in st.session_state:
        st.session_state["_sd_session_id"] = str(uuid4())
    return st.session_state["_sd_session_id"]

def track_event(name: str, dashboard_id: str, properties: dict | None = None) -> dict:
    event = {
        "event_id": str(uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "session_id": get_session_id(),
        "dashboard_id": dashboard_id,
        "event_name": name,
        "properties": properties or {},
    }
    if _sink is not None:
        try:
            _sink(event)
        except Exception:
            logger.exception("Analytics event sink failed")
    return event

def track_page_view(dashboard_id: str, page_id: str) -> dict | None:
    """Track only when the active page changes within a Streamlit session."""
    page_key = f"{dashboard_id}:{page_id}"
    if st.session_state.get("_sd_last_page") == page_key:
        return None
    st.session_state["_sd_last_page"] = page_key
    return track_event("page_viewed", dashboard_id, {"page_id": page_id})
