import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from server import app
from templates.includes.generate_template import full_template
import pandas as pd
import plotly.express as px
from server import db

data = pd.read_sql(
    '''
    SELECT 
        Date_part('year', fecha) as year,
        count(*) as total_count
    FROM violencia_intrafamiliar 
    GROUP BY date_part('year', fecha)'''
    , db.engine)
fig = px.line(data_frame=data, x='year', y='total_count')
fig.update_layout(title='Total Count of Intrafamily Violence')

app.index_string = full_template

graph = dcc.Graph(
    id='violencia-graph',
    figure = fig
)

layout = html.Div([
    graph
])
