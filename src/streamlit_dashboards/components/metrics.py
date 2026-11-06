"""Standard KPI components."""
import streamlit as st

def metric_card(label: str, value: str | int | float, delta: str | None = None, help_text: str | None = None) -> None:
    st.metric(label=label, value=value, delta=delta, help=help_text, border=True)
