import dash
#from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

import pandas as pd

df2 = pd.read_csv(r'C:\Users\CAROL\Documents\Team79_git\ds4a_project_dash\data\hurto_personas.csv')
df3 = pd.read_csv(r'C:\Users\CAROL\Documents\Team79_git\ds4a_project_dash\data\violencia_intrafamiliar.csv')
df4 = pd.read_csv(r'C:\Users\CAROL\Documents\Team79_git\ds4a_project_dash\data\del_sexuales.csv')
df5 = pd.read_csv(r'C:\Users\CAROL\Documents\Team79_git\ds4a_project_dash\data\lesiones_personales.csv')
df6 = pd.read_csv(r'C:\Users\CAROL\Documents\Team79_git\ds4a_project_dash\data\homicidios.csv')

layout=html.Div(children=[
    dbc.Row([
        dbc.Col(dcc.Markdown(
            '''
            # **THEFT - AUGUST 2019**
            '''
            ), width=6, align='center', style={'text-align': 'left'})
    ], justify='center'),

    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
                        columns=[{"name": i, "id": i} for i in df2.columns],
                        data=df2.to_dict('records'),
                        filter_action='native',
                        page_size=10,
                        style_data={
                            'width': '150px', 'minWidth': '50px', 'maxWidth': '150px',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                        }
                    ), width={"offset": 1}
        ),
    ], justify='center'),

    dbc.Row([
        dbc.Col(dcc.Markdown(
            '''
            # **DOMESTIC VIOLENCE - AUGUST 2019**
            '''
            ), width=6, align='center', style={'text-align': 'left'})
    ], justify='center'),

    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
                        columns=[{"name": i, "id": i} for i in df3.columns],
                        data=df3.to_dict('records'),
                        filter_action='native',
                        page_size=10,
                        style_data={
                            'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                        }
                    ), width={"offset": 1}
        ),
    ], justify='center'),

    dbc.Row([
        dbc.Col(dcc.Markdown(
            '''
            # **SEXUAL CRIMES - AUGUST 2019**
            '''
            ), width=6, align='center', style={'text-align': 'left'})
    ], justify='center'),

    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
                        columns=[{"name": i, "id": i} for i in df4.columns],
                        data=df4.to_dict('records'),
                        filter_action='native',
                        page_size=10,
                        style_data={
                            'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                        }
                    ), width={"offset": 1}
        ),
    ], justify='center'),

    dbc.Row([
        dbc.Col(dcc.Markdown(
            '''
            # **PERSONAL INJURIES - AUGUST 2019**
            '''
            ), width=6, align='center', style={'text-align': 'left'})
    ], justify='center'),

    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
                        columns=[{"name": i, "id": i} for i in df5.columns],
                        data=df5.to_dict('records'),
                        filter_action='native',
                        page_size=10,
                        style_data={
                            'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                        }
                    ), width={"offset": 1}
        ),
    ], justify='center'),

    dbc.Row([
        dbc.Col(dcc.Markdown(
            '''
            # **MURDERS - AUGUST 2019**
            '''
            ), width=6, align='center', style={'text-align': 'left'})
    ], justify='center'),

    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
                        columns=[{"name": i, "id": i} for i in df6.columns],
                        data=df6.to_dict('records'),
                        filter_action='native',
                        page_size=10,
                        style_data={
                            'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                        }
                    ), width={"offset": 1}
        ),
    ], justify='center')

])

