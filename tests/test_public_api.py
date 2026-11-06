from streamlit_dashboards import bar_chart, line_chart, metric_card, metric_row, page_header, track_event, track_page_view

def test_public_api_callable():
    assert all(callable(x) for x in (bar_chart, line_chart, metric_card, metric_row, page_header, track_event, track_page_view))
