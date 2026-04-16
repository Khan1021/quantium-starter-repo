from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load the processed sales data
DATA_PATH = "output.csv"
df = pd.read_csv(DATA_PATH)
df = df.sort_values(by="date")

app = Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualisation", id="header", style={"textAlign": "center", "color": "#2c3e50"}),

    html.Div([
        html.Label("Select Region: ", style={"fontWeight": "bold"}),
        dcc.RadioItems(
            id="region-picker",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"}
            ],
            value="all",
            inline=True
        )
    ], style={"textAlign": "center", "padding": "20px", "backgroundColor": "#f8f9fa"}),

    dcc.Graph(id="sales-graph"),
], style={"fontFamily": "Arial, sans-serif", "padding": "20px"})


# Callback to update the visualisation based on the selected region
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-picker", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Sales Trend - {selected_region.capitalize()} Region",
        labels={"sales": "Total Sales ($)", "date": "Date"}
    )

    fig.update_layout(template="plotly_white")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)