# streamlit-dashboards

Reusable components and event instrumentation for standardized Streamlit dashboards.

## Install locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -e '.[dev]'
streamlit run examples/app.py
```

## Use in another dashboard

After pushing this repository to GitHub and creating a tag named `v0.1.0`, add to the dashboard's `requirements.txt`:

```text
streamlit-dashboards @ git+ssh://git@github.com/YOUR-ORG/streamlit-dashboards.git@v0.1.0
```

Then:

```bash
pip install -r requirements.txt
```

```python
from streamlit_dashboards import page_header, metric_row, line_chart, track_page_view

track_page_view("insurance", "overview")
page_header("Insurance Dashboard")
metric_row([{"label": "Settlements", "value": "120"}])
```

## Package structure

- `components/metrics.py`: standardized KPI cards
- `components/charts.py`: standardized charts
- `components/layout.py`: page headers and metric rows
- `analytics/tracker.py`: event creation and optional sink
- `examples/app.py`: runnable demo

## Analytics integration

Tracking is opt-in. By default, events are returned but **not persisted**. Configure a sink at app startup:

```python
from streamlit_dashboards.analytics.tracker import configure_event_sink
configure_event_sink(my_database_or_queue_writer)
```

Use an approved ingestion service for production, avoid personal/sensitive event properties, and do not use a synchronous print sink for production. `track_page_view` deduplicates ordinary reruns, but does not implement session timeout or cross-device identity.

## Test and build

```bash
python -m pytest -q
python -m build
```

## Release

Update `version` in `pyproject.toml`, commit, then tag and push:

```bash
git tag v0.1.0
git push origin main --tags
```

This starter does not include Snowflake credentials or persistence. Add those behind a configurable event sink after agreeing on event taxonomy and privacy controls.
