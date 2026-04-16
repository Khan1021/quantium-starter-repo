import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

# Load the processed data
df = pd.read_csv("data/output.csv")
df["date"] = pd.to_datetime(df["date"])

# Build the Dash app
app = Dash(__name__)

app.layout = html.Div([

    html.Div([
        html.H1("🍬 Pink Morsel Sales Visualiser", style={
            "margin": "0",
            "fontSize": "2rem",
            "color": "#fff",
            "letterSpacing": "1px"
        }),
        html.P("Soul Foods · Sales Impact Analysis", style={
            "margin": "4px 0 0 0",
            "color": "#f0c4d4",
            "fontSize": "0.95rem"
        })
    ], style={
        "background": "linear-gradient(135deg, #c0396b, #e8789a)",
        "padding": "24px 40px",
        "boxShadow": "0 2px 8px rgba(0,0,0,0.15)"
    }),

    html.Div([

        html.Div([
            html.Label("Filter by Region", style={
                "fontWeight": "600",
                "color": "#c0396b",
                "marginBottom": "10px",
                "display": "block",
                "fontSize": "0.9rem",
                "textTransform": "uppercase",
                "letterSpacing": "1px"
            }),
            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": " All", "value": "all"},
                    {"label": " North", "value": "north"},
                    {"label": " South", "value": "south"},
                    {"label": " East", "value": "east"},
                    {"label": " West", "value": "west"},
                ],
                value="all",
                style={"display": "flex", "flexDirection": "column", "gap": "10px"},
                inputStyle={"marginRight": "8px", "accentColor": "#c0396b"},
                labelStyle={"fontSize": "1rem", "color": "#333"}
            )
        ], style={
            "background": "#fff",
            "borderRadius": "12px",
            "padding": "24px",
            "boxShadow": "0 2px 8px rgba(0,0,0,0.08)",
            "width": "180px",
            "flexShrink": "0"
        }),

        html.Div(
            dcc.Graph(id="sales-chart"),
            style={
                "background": "#fff",
                "borderRadius": "12px",
                "padding": "16px",
                "boxShadow": "0 2px 8px rgba(0,0,0,0.08)",
                "flex": "1"
            }
        )

    ], style={
        "display": "flex",
        "gap": "24px",
        "padding": "32px 40px",
        "alignItems": "flex-start",
        "background": "#fdf0f4",
        "minHeight": "calc(100vh - 90px)"
    })

], style={"fontFamily": "'Segoe UI', sans-serif", "margin": "0"})


@callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    filtered = df if region == "all" else df[df["region"] == region]
    grouped = filtered.groupby("date", as_index=False)["sales"].sum().sort_values("date")

    fig = px.line(
        grouped,
        x="date",
        y="sales",
        labels={"date": "Date", "sales": "Total Sales ($)"},
        color_discrete_sequence=["#c0396b"]
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="#888",
        annotation_text="Price Increase (Jan 15, 2021)",
        annotation_position="top left",
        annotation_font_color="#888"
    )

    fig.update_layout(
        plot_bgcolor="#fff",
        paper_bgcolor="#fff",
        font=dict(family="Segoe UI, sans-serif", color="#333"),
        title=dict(
            text=f"Sales Over Time — {'All Regions' if region == 'all' else region.capitalize()}",
            font=dict(size=18, color="#c0396b")
        ),
        xaxis=dict(showgrid=True, gridcolor="#f0e0e8"),
        yaxis=dict(showgrid=True, gridcolor="#f0e0e8"),
        hovermode="x unified"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)