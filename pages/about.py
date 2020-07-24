import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from server import app
import pandas as pd
import plotly.express as px
from server import db
import plotly.graph_objects as go

layout = html.Div(children=[
    dbc.Row([
        dbc.Col(html.Img(
            src='./assets/images/team/carolina.png',
            width=150,
            height=150
        ), width=1, align='center'),
        dbc.Col(dcc.Markdown(
'''
## **Carolina Garzón**
Environmental engineer, GIS Specialist Uni. DistritalFrancisco José de Caldas.
Data Science Enthusiast, Professional bully.

*Selected interests:* Women’s empowerment, data for environmental management, geostatistics, poetry.
'''
        ), width=4, align='center')
    ],
    justify='center'),
    dbc.Row([
        dbc.Col(dcc.Markdown(
'''
## **Santiago Toledo**

Hombre, 1.75 cm
'''
        ), width=4, align='center', style={'text-align': 'right'}),
        dbc.Col(html.Img(
            src='./assets/images/team/santiago.png',
            width=150,
            height=150
        ), width=1, align='center')
    ],
    justify='center'),
    dbc.Row([
        dbc.Col(html.Img(
            src='./assets/images/team/cristian.png',
            width=150,
            height=150
        ), width=1, align='center'),
        dbc.Col(dcc.Markdown(
'''
## **Cristian Portela**

Missing
'''
        ), width=4, align='center')
    ],
    justify='center'),
])
