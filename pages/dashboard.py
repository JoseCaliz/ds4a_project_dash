import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from server import app
import pandas as pd
import plotly.express as px
from server import db
import plotly.graph_objects as go


engine = db.engine

hidden_div = html.Div(className='current_location',
                      children='home',
                      hidden=True)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

layout = html.Div(children=[

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
