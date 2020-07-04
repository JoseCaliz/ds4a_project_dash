import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from server import app
from templates.includes.generate_template import full_template
import pandas as pd
import plotly.express as px
from server import db
import plotly.graph_objects as go

engine = db.engine

queries_year ='''
SELECT extract(year FROM fecha) AS año,
    COUNT(departamento) AS cantidad,
    'hurto automotores' AS crimen
FROM hurto_automotores
GROUP BY año
---
SELECT extract(year FROM fecha) AS año,
    COUNT(departamento) AS cantidad,
    'hurto personas'AS crimen
FROM hurto_personas
GROUP BY año
---
SELECT extract(year FROM fecha) AS año,
    COUNT(departamento) AS cantidad,
    'violencia intrafamiliar'AS crimen
FROM violencia_intrafamiliar
GROUP BY año
---
SELECT extract(year FROM fecha) AS año,
    COUNT(departamento) AS cantidad,
    'delitos sexuales'AS crimen
FROM del_sexuales
GROUP BY año
---
SELECT extract(year FROM fecha) AS año,
    COUNT(departamento) AS cantidad,
    'lesiones personales'AS crimen
FROM lesiones_personales
GROUP BY año
---
SELECT extract(year FROM fecha) AS año,
    COUNT(departamento) AS cantidad,
    'homicidios'AS crimen
FROM homicidios
GROUP BY año
---
SELECT extract(year FROM fecha) AS año,
    COUNT(departamento) AS cantidad,
    'hurto motocicletas'AS crimen
FROM hurto_motocicletas
GROUP BY año
'''.split("---")

df = pd.concat([pd.read_sql_query(q, engine.connect()) for q in queries_year])\
    .reset_index(drop=True).sort_values('año')


fig = go.Figure()
fig.add_trace(
    go.Scatter(x=list(df[df.crimen=='hurto automotores'].año),
               y=list(df[df.crimen=='hurto automotores'].cantidad),
               name="Car theft",
               line=dict(color=px.colors.qualitative.Plotly[0])))

fig.add_trace(
    go.Scatter(x=list(df[df.crimen=='hurto personas'].año),
               y=list(df[df.crimen=='hurto personas'].cantidad),
               name="Shoplifting",
               line=dict(color=px.colors.qualitative.Plotly[1])))

fig.add_trace(
    go.Scatter(x=list(df[df.crimen=='violencia intrafamiliar'].año),
               y=list(df[df.crimen=='violencia intrafamiliar'].cantidad),
               name="Violencia intrafamiliar",
               line=dict(color=px.colors.qualitative.Plotly[2])))

fig.add_trace(
    go.Scatter(x=list(df[df.crimen=='delitos sexuales'].año),
               y=list(df[df.crimen=='delitos sexuales'].cantidad),
               name="Sexual crimes",
               line=dict(color=px.colors.qualitative.Plotly[3])))

fig.add_trace(
    go.Scatter(x=list(df[df.crimen=='lesiones personales'].año),
               y=list(df[df.crimen=='lesiones personales'].cantidad),
               name="Personal injuries",
               line=dict(color=px.colors.qualitative.Plotly[4])))

fig.add_trace(
    go.Scatter(x=list(df[df.crimen=='homicidios'].año),
               y=list(df[df.crimen=='homicidios'].cantidad),
               name="Murders",
               line=dict(color=px.colors.qualitative.Plotly[5])))

fig.add_trace(
    go.Scatter(x=list(df[df.crimen=='hurto motocicletas'].año),
               y=list(df[df.crimen=='hurto motocicletas'].cantidad),
               name="Theft of motorcycles",
               line=dict(color=px.colors.qualitative.Plotly[6])))

fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True, True, True, True, True, True, True]},
                           {"title": "Crimes in Colombia"}]),
                dict(label="Car theft",
                     method="update",
                     args=[{"visible": [True, False, False, False, False, False, False]},
                           {"title": "Car theft in Colombia"}]),
                dict(label="Shoplifting",
                     method="update",
                     args=[{"visible": [False, True, False, False, False, False, False]},
                           {"title": "Shoplifting in Colombia"}]),
                dict(label="Domestic violence",
                     method="update",
                     args=[{"visible": [False, False, True, False, False, False, False]},
                           {"title": "Domestic violence in Colombia"}]),
                dict(label="Sexual crimes",
                     method="update",
                     args=[{"visible": [False, False, False, True, False, False, False]},
                           {"title": "Delitos sexuales in Colombia"}]),
                dict(label="Personal injuries",
                     method="update",
                     args=[{"visible": [False, False, False, False, True, False, False]},
                           {"title": "Personal injuries in Colombia"}]),
                dict(label="Murders",
                     method="update",
                     args=[{"visible": [False, False, False, False, False, True, False]},
                           {"title": "Murders in Colombia"}]),
                dict(label="Theft of motorcycles",
                     method="update",
                     args=[{"visible": [False, False, False, False, False, False, True]},
                           {"title": "Theft of motorcycles in Colombia"}])
            ]),
        )
    ])

fig.update_layout(title_text="Crimes in Colombia")

app.index_string = full_template

graph = dcc.Graph(
    id='all_problems-graph',
    figure = fig
)

layout = html.Div([
    graph
])
