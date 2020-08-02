import dash
#from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

import pandas as pd

df2 = pd.read_csv(r'./data/hurto_personas.csv')
df3 = pd.read_csv(r'./data/violencia_intrafamiliar.csv')
df4 = pd.read_csv(r'./data/del_sexuales.csv')
df5 = pd.read_csv(r'./data/lesiones_personales.csv')
df6 = pd.read_csv(r'./data/homicidios.csv')

layout=html.Div(children=[
    dbc.Row([
        dbc.Col(dcc.Markdown(
'''
## **DATASET**

**National Police of Colombia** provide a serie of datasets that covers *threats, sexual crimes, murders, murders in traffic accidents, theft, burglary and robbery, shoplifting, personal injuries and domestic violence.*
The data can be found [here](https://www.policia.gov.co/grupo-informaci%C3%B3n-criminalidad/estadistica-delictiva) 
'''
            ), width=6, align='center', style={'text-align': 'center'}),
    ], justify='center'),

    dbc.Row([
        dbc.Col(dcc.Markdown(
            '''
            ## **THEFT - JULY TO SEPTEMBER 2019**
            '''
            ), width=6, align='center', style={'text-align': 'center'})
    ], justify='center'),

    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
                        columns=[{"name": i, "id": i} for i in df2.columns],
                        data=df2.to_dict('records'),
                        filter_action='native',
                        page_size=10,
                    ), width=8
        ),
    ], justify='center'),

    dbc.Row([
        dbc.Col(dcc.Markdown(
            '''
            ## **DOMESTIC VIOLENCE - JULY TO SEPTEMBER 2019**
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
                    ), width=8
        ),
    ], justify='center'),

    dbc.Row([
        dbc.Col(dcc.Markdown(
            '''
            ## **SEXUAL CRIMES - JULY TO SEPTEMBER 2019**
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
                    ), width=8
        ),
    ], justify='center'),

    dbc.Row([
        dbc.Col(dcc.Markdown(
            '''
            ## **PERSONAL INJURIES - JULY TO SEPTEMBER 2019**
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
                    ), width=8
        ),
    ], justify='center'),

    dbc.Row([
        dbc.Col(dcc.Markdown(
            '''
            ## **MURDERS - JULY TO SEPTEMBER 2019**
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
                    ), width=8
        ),
    ], justify='center')

])

