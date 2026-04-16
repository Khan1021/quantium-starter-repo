import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load the processed data
df = pd.read_csv("data/output.csv")
df["date"] = pd.to_datetime(df["date"])

# Aggregate sales by date (sum across all regions)
df_grouped = df.groupby("date", as_index=False)["sales"].sum()
df_grouped = df_grouped.sort_values("date")

# Create the line chart
fig = px.line(
    df_grouped,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

# Add a vertical line for the price increase date
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase",
    annotation_position="top left"
)

# Build the Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)