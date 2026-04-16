from app import app

# 1. Test to ensure the header is present and contains the correct text
def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)
    header_text = dash_duo.find_element("#header").text
    assert header_text == "Pink Morsel Sales Visualisation"

# 2. Test to ensure the visualisation (Graph) is presents
def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-graph", timeout=10)
    assert dash_duo.find_element("#sales-graph") is not None

# 3. Test to ensure the region picker (RadioItems) is present
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-picker", timeout=10)
    assert dash_duo.find_element("#region-picker") is not None