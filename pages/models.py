import pandas as pd
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from server import app
import pandas as pd
import plotly.express as px
from server import db, app
import plotly.graph_objects as go


df_mae_prophet = pd.read_csv('./models/mae_prophet.txt')
df_mae_xgboost = pd.read_csv('./models/mae_xgboost.txt')
df_mape_prophet = pd.read_csv('./models/mape_prophet.txt')
df_mape_xgboost = pd.read_csv('./models/mape_xgboost.txt')
df_mse_prophet = pd.read_csv('./models/mse_prophet.txt')
df_mse_xgboost = pd.read_csv('./models/mse_xgboost.txt')

prophet_conditions = [
    {
        'if': {
            'filter_query': '{D} > {Baseline}',
            'column_id': 'D'
        },
        'backgroundColor': 'lightgreen',
        'color': 'green'
    },
    {
        'if': {
            'filter_query': '{5D} > {Baseline.1}',
            'column_id': '5D'
        },
        'backgroundColor': 'lightgreen',
        'color': 'green'
    },
    {
        'if': {
            'filter_query': '{W} > {Baseline.2}',
            'column_id': 'W'
        },
        'backgroundColor': 'lightgreen',
        'color': 'green'
    },
    {
        'if': {
            'filter_query': '{2W} > {Baseline.3}',
            'column_id': '2W'
        },
        'backgroundColor': 'lightgreen',
        'color': 'green'
    }
]

table_mae_prophet = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df_mae_prophet.columns],
    data=df_mae_prophet.to_dict('records'),
    style_data_conditional=prophet_conditions
)

table_mae_xgboost = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df_mae_xgboost.columns],
    data=df_mae_xgboost.to_dict('records'),
)

table_mse_prophet = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df_mse_prophet.columns],
    data=df_mse_prophet.to_dict('records'),
    style_data_conditional=prophet_conditions
)

table_mse_xgboost = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df_mse_xgboost.columns],
    data=df_mse_xgboost.to_dict('records'),
)

table_mape_prophet = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df_mape_prophet.columns],
    data=df_mape_prophet.to_dict('records'),
    style_data_conditional=prophet_conditions
)

table_mape_xgboost = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df_mape_xgboost.columns],
    data=df_mape_xgboost.to_dict('records'),
)

all_layout = html.Div([
    dbc.Row([
        html.H1('MAE', style={
            'font-size':'2.5em',
            'font-weight':'bold'
        })
    ], justify='center'),
    dbc.Row([
        dbc.Col([table_mae_prophet], width=8)
    ], justify='center'),
    dbc.Row([
        dbc.Col([table_mae_xgboost], width=8)
    ], justify='center'),
    dbc.Row([
        html.H1('MSE', style={
            'font-size':'2.5em',
            'font-weight':'bold'
        })
    ], justify='center'),
    dbc.Row([
        dbc.Col([table_mse_prophet], width=8)
    ], justify='center'),
    dbc.Row([
        dbc.Col([table_mse_xgboost], width=8)
    ], justify='center'),
    dbc.Row([
        html.H1('MAPE', style={
            'font-size':'2.5em',
            'font-weight':'bold'
        })
    ], justify='center'),
    dbc.Row([
        dbc.Col([table_mape_prophet], width=8)
    ], justify='center'),
    dbc.Row([
        dbc.Col([table_mape_xgboost], width=8)
    ], justify='center')
], style={'padding-top':'2.5em'})

layout = all_layout
