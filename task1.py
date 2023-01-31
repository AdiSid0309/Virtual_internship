from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

data = pd.read_csv('C:/Users/eryas/Jupyter/Virtual_internship/daily_sales_data_0.csv')

df = pd.DataFrame(data)

'''def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
'''

fig = px.scatter(df, x="price", y="region",
                  color="quantity", hover_name="product",
                 log_x=True, size_max=800)


app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
  app.run_server(debug=True)