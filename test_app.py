import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def dash_app(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    return dash_duo

def test_header_present(dash_app):
    dash_app.wait_for_element("h1", timeout=10)
    assert dash_app.find_element("h1").text == "🍬 Pink Morsel Sales Visualiser"

def test_chart_present(dash_app):
    dash_app.wait_for_element("#sales-chart", timeout=10)
    assert dash_app.find_element("#sales-chart")

def test_region_picker_present(dash_app):
    dash_app.wait_for_element("#region-filter", timeout=10)
    assert dash_app.find_element("#region-filter")