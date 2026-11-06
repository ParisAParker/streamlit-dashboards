"""Standardized Plotly charts."""
import pandas as pd
import plotly.express as px
import streamlit as st

def _render(fig) -> None:
    fig.update_layout(template="plotly_white", height=360, margin=dict(l=20, r=20, t=55, b=20))
    st.plotly_chart(fig, use_container_width=True)

def line_chart(data: pd.DataFrame, x: str, y: str, title: str | None = None) -> None:
    _render(px.line(data, x=x, y=y, title=title, markers=True))

def bar_chart(data: pd.DataFrame, x: str, y: str, title: str | None = None) -> None:
    _render(px.bar(data, x=x, y=y, title=title))
