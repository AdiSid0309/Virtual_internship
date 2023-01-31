from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

data = pd.read_csv('C:/Users/eryas/Jupyter/Virtual_internship/formatted_data.csv')

df = pd.DataFrame(data)

COLORS = {
    "primary": "#65DA3E",
    "secondary": "#0FDBC0",
    "font": "#141412"
}

def generate_figure(df):
    fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales")
    fig.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return fig

visual = dcc.Graph(
    id="visual",
    figure=generate_figure(df)
)

header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)

region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)
region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        "font-size": "150%"
    }
)

@app.callback(
    Output(visual, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    if region == "all":
        trimmed_data = df
    else:
        trimmed_data = df[df["region"] == region]

    figure = generate_figure(trimmed_data)
    return figure

app.layout = html.Div(
    [
        header,
        visual,
        region_picker_wrapper
    ],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "20px"
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)