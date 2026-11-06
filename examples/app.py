"""Run: streamlit run examples/app.py"""
import pandas as pd
import streamlit as st
from streamlit_dashboards import page_header, metric_row, line_chart, track_page_view, track_event
from streamlit_dashboards.analytics.tracker import configure_event_sink

st.set_page_config(page_title="Dealer Forecast Demo", layout="wide")

# Demo only: write event records to the server log. Replace with an approved
# database/queue sink before production. No user PII is captured here.
configure_event_sink(lambda event: print("ANALYTICS EVENT:", event))
track_page_view("dealer_forecast", "overview")
page_header("Dealer Forecast", "Example using the streamlit-dashboards package")
metric_row([
    {"label": "Expected Units", "value": "1,245", "delta": "+8.2%"},
    {"label": "Active Dealers", "value": "82"},
    {"label": "Booking Rate", "value": "72%"},
])
df = pd.DataFrame({"month": ["Jan", "Feb", "Mar", "Apr"], "expected_units": [950, 1100, 1245, 1320]})
line_chart(df, "month", "expected_units", "Expected Units by Month")
if st.button("Generate Forecast"):
    track_event("forecast_generated", "dealer_forecast", {"scenario": "demo"})
    st.success("Demo forecast generated; event logged to server output.")
