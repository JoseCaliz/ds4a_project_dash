#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

#Dash Bootstrap Components
import dash_bootstrap_components as dbc
from sqlalchemy import create_engine

#Data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json

#Recall app
from app import app



###########################################################
#
#           APP LAYOUT:
#
###########################################################

#LOAD THE DIFFERENT FILES
from lib import title, sidebar, us_map, stats

#PLACE THE COMPONENTS IN THE LAYOUT
app.layout =html.Div(
    [
      us_map.map,
      stats.stats,
      title.title,
      sidebar.sidebar,
    ],
    className="ds4a-app", #You can also add your own css files by locating them into the assets folder
)



###############################################
#
#           APP INTERACTIVITY:
#
###############################################

###############################################################
#Load and modify the data that will be used in the app.
#################################################################
#This connects to AWS DB where the files are stored.

driver = 'postgres'
username = 'ds4a'
password = 'ds4A-7eaM79'
host = 'ds4a.cm1dcdf7pnnv.us-east-2.rds.amazonaws.com'
port = 5432
database = 'team_79'

connection_string = f'{driver}://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_string, encoding='utf8')


mapa_query ='''
SELECT departamento, extract(year FROM fecha) AS year, 'robbery' AS crime, COUNT(dia) AS total
FROM hurto_personas
GROUP BY departamento, year

UNION ALL

SELECT departamento, extract(year FROM fecha) AS year, 'dom_viol' AS crime, COUNT(dia) AS total
FROM violencia_intrafamiliar
GROUP BY departamento, year

UNION ALL

SELECT departamento, extract(year FROM fecha) AS year, 'murder' AS crime, COUNT(dia) AS total
FROM homicidios
GROUP BY departamento, year

UNION ALL

SELECT departamento, extract(year FROM fecha) AS year, 'sex_off' AS crime, COUNT(dia) AS total
FROM homicidios
GROUP BY departamento, year

'''
with open('D:/Barrios_Bog/geojson_departamentos.json', encoding='utf8') as geo:
    geoj = json.loads(geo.read())

df = pd.read_sql_query(mapa_query, engine.connect()).reset_index(drop=True)
matcher = pd.read_csv(r'C:\Users\Admin\Desktop\matcherdpto.csv', encoding='UTF8')

mapper = matcher.set_index('dpto_orig').to_dict()['nom_match']
df['mapid']=df.departamento.map(mapper)
dff=df.groupby(['mapid','year','crime']).sum().reset_index()
#crimes=['robbery','dom_viol','sex_off']
year = 2012
#dfmap = dff[(dff['year']==year)&(dff['crime'].isin(crimes))]


@app.callback(
    Output('Crime_map', 'figure'),
    [
        Input("crime_dropdown","value"),
        Input("year_dropdown", "value")
    ],
)
def update_map_plot(crime_drop,year_drop):
    dfmap = dff[(dff['year']==year_drop)&(dff['crime'].isin(crime_drop))]
    dfmap = dfmap.groupby('mapid').sum().reset_index()
    Map_fig2 = px.choropleth_mapbox(dfmap,
            locations='mapid',
            color='total',
            #featureidkey="properties.NOMBRE_DPT",
            geojson=geoj,
            zoom=7,
            mapbox_style="stamen-toner",
            center={"lat": 4.655115, "lon": -74.055404}, #Center

            color_continuous_scale="matter",         #Color Scheme
            opacity=0.5,
            title='Total crimes in Colombia'
            )
    Map_fig2.update_layout(title='Total de Crímenes por Departamento',margin={"r":0,"t":0,"l":0,"b":0},paper_bgcolor="#F8F9F9")

    return Map_fig2

#asd
#############################################################
# LINE PLOT : Add sidebar interaction here
#############################################################
@app.callback(
    Output("Line", "figure"),
    [
        Input("depto_dropdown", "value"),
        Input("crime_dropdown","value")
    ],
)
def make_line_plot(depto,crimes):
    dptos=[]
    dptos.append(depto)
    dfall = dff[(dff['crime'].isin(crimes))&(dff['mapid'].isin(dptos))]


    Line_fig2=px.line(dfall,x="year",y="total", color="crime")
    graptitle='Evolution of crimes in time for {}'.format(dptos[0])
    Line_fig2.update_layout(title=graptitle,paper_bgcolor="#F8F9F9")


    # Scatter_fig=px.scatter(ddf, x="Sales", y="Profit", color="Category", hover_data=['State_abbr','Sub-Category','Order ID','Product Name'])
    # Scatter_fig.update_layout(title='Sales vs. Profit in selected states',paper_bgcolor="#F8F9F9")

    return Line_fig2


#############################################################
# PROFITS BY CATEGORY : Add sidebar interaction here
#############################################################



#############################################################
# TREEMAP PLOT : Add sidebar interaction here
#############################################################



#############################################################
# MAP : Add interactions here
#############################################################

#MAP date interaction



#MAP click interaction

@app.callback(
    Output('depto_dropdown','value'),
    [
        Input('Crime_map','clickData')
    ],
    [
        State('depto_dropdown','value')
    ]

)
def click_saver(clickData,state):
    if clickData is None:
        raise PreventUpdate

    # print(clickData)
    # print(state)
    newstate=clickData['points'][0]['location']
    #state.append(clickData['points'][0]['location'])


    return newstate













if __name__ == "__main__":
    app.run_server(debug=True)
