from dash import Dash, html, dcc
import plotly.express  as px
import pandas as pd

app = Dash(__name__)

data = pd.read_csv('C:/Users/eryas/Jupyter/Virtual_internship/formatted_data.csv')

df = pd.DataFrame(data)

fig = px.line(df, x="date", y="sales", title='Pink Morsel Sales')

app.layout = html.Div(children=[
    html.H1(children='Task-3'),
    html.Div(children='''
        Dash: Quantium Task-3.
    '''),
    dcc.Graph(
        id = 'Sales.',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)