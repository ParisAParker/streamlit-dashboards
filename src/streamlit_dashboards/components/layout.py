"""Reusable page layouts."""
from collections.abc import Sequence
import streamlit as st
from .metrics import metric_card

def page_header(title: str, description: str | None = None) -> None:
    st.title(title)
    if description:
        st.caption(description)

def metric_row(metrics: Sequence[dict]) -> None:
    if not metrics:
        return
    for column, metric in zip(st.columns(len(metrics)), metrics):
        with column:
            metric_card(**metric)
