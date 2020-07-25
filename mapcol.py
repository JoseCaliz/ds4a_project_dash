import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from sqlalchemy import create_engine


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd

#Recall app
#from app import app

#This connects to AWS DB where the files are stored.

driver = 'postgres'
username = 'ds4a'
password = 'ds4A-7eaM79'
host = 'ds4a.cm1dcdf7pnnv.us-east-2.rds.amazonaws.com'
port = 5432
database = 'team_79'

connection_string = f'{driver}://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_string, encoding='utf8')


#############################
# First we need to load the data
#############################
#The data will be obtained via SQL query

mapa_query ='''
SELECT barrio, 'robbery' AS crime, extract(year FROM fecha) AS year
FROM hurto_personas
WHERE municipio LIKE 'BOGOTÁ D.C.'

UNION ALL

SELECT barrio, 'dom_viol' AS crime, extract(year FROM fecha) AS year
FROM violencia_intrafamiliar
WHERE municipio LIKE 'BOGOTÁ D.C.'

UNION ALL

SELECT barrio, 'murder' AS crime, extract(year FROM fecha) AS year
FROM homicidios
WHERE municipio LIKE 'BOGOTÁ D.C.'

UNION ALL

SELECT barrio, 'sex_off' AS crime, extract(year FROM fecha) AS year
FROM del_sexuales
WHERE municipio LIKE 'BOGOTÁ D.C.'

'''
# with open('D:/Barrios_Bog/BogotaNeighborhood.geojson') as geo:
#     geojson = json.loads(geo.read())
with open('D:/Barrios_Bog/SCat.geojson') as geo2:
    geoj = json.loads(geo2.read())

df = pd.read_sql_query(mapa_query, engine.connect()).reset_index(drop=True)
matcher = pd.read_csv(r'C:\Users\Admin\Desktop\matcher.csv', encoding='UTF8')

mapper = matcher.set_index('barrio_original').to_dict()['nom_match']
df['mapid']=df.barrio.map(mapper)
dff=df.groupby(['mapid','year','crime']).count().reset_index()
crimes=['robbery','dom_viol','sex_off']
year = 2012

dfmap = dff[dff['year']==year][dff['crime'].isin(crimes)].rename(columns={'mapid':'Barrio','barrio':'Total_crimen'}).groupby('Barrio').sum()['Total_crimen'].reset_index()
dfmap = dfmap.sort_values('Total_crimen', ascending=False)[1:]

Map_fig = px.choropleth_mapbox(dfmap.sort_values('Total_crimen', ascending=False)[1:],
        locations='Barrio',
        color='Total_crimen',
        featureidkey="properties.SCANOMBRE",
        geojson=geoj,
        zoom=8,
        mapbox_style="stamen-toner",
        center={"lat": 4.655115, "lon": -74.055404}, #Center

        color_continuous_scale="matter",         #Color Scheme
        opacity=0.4,
        title='Total crimes in Bogotá'
        )
#Now we create the map

Map_fig.update_layout(title='Total de Crímenes por Ciudad',paper_bgcolor="#F8F9F9")

values={'Robbery and theft':'robbery','Domestic violence':'dom_viol','Sex offenses':'sex_off'}

#Now we create the dropdown for crimes
dropdown=dcc.Dropdown(
        id="crime_dropdown",
        options=[{"label":key, "value":values[key]} for key in values.keys()],
        value=["sex_off",'robbery'],
        placeholder="Select a crime",
        multi=True
        )
#Now the dropdown for years
ys = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
dropdown2=dcc.Dropdown(
        id="year_dropdown",
        options=[{"label":year, "value":year} for year in ys],
        value=[2018],
        placeholder="Select a year",
        multi=False
        )



# date_picker=dcc.DatePickerSingle(
#                 id='date_picker',
#                 display_format='YYYY',
#                 min_date_allowed=dt(2010, 1, 1),
#                 max_date_allowed=dt(2019, 12, 31),
#                 start_date=dt(2016,1,1).date()
#             )
#
#
# @app.callback(
#     [Output("Line", "figure"),Output("Scatter","figure")],
#     [
#         Input("state_dropdown", "value"),
#         Input("date_picker", "start_date"),
#         Input("date_picker", "end_date")
#     ],
# )
# def make_line_plot(state_dropdown, start_date, end_date):
#     ddf=df[df['State_abbr'].isin(state_dropdown)]
#     ddf = ddf[(ddf['Order Date'] >= start_date) & (ddf['Order Date'] < end_date)]
#
#     ddf1=ddf.groupby(['Order_Month', 'State']).sum()
#     ddf1=ddf1.reset_index()
#
#     Line_fig=px.line(ddf1,x="Order_Month",y="Sales", color="State")
#     Line_fig.update_layout(title='Montly Sales in selected states',paper_bgcolor="#F8F9F9")
#
#     Scatter_fig=px.scatter(ddf, x="Sales", y="Profit", color="Category", hover_data=['State_abbr','Sub-Category','Order ID','Product Name'])
#     Scatter_fig.update_layout(title='Sales vs. Profit in selected states',paper_bgcolor="#F8F9F9")
#
#     return [Line_fig, Scatter_fig]




#Map Layout
##############################
#Create the app
app = dash.Dash(__name__)

#Create Layout
app.layout = html.Div([
 #Place the main graph component here:
dcc.Graph(figure=Map_fig, id='Crime_map'),

        html.H5("Select year"),
        dropdown2,
        html.Hr(),
        html.H5("Select crime"),
        dropdown



])



@app.callback(
    Output("Crime_map", "figure"),
    [
        Input("crime_dropdown","value"),
        Input("year_dropdown", "value")
    ],
)
def make_map_plot(crime_dropdown, date):
    dfmap = dff[dff['year'].isin(date)][dff['crime'].isin(crime_dropdown)].rename(columns={'mapid':'Barrio','barrio':'Total_crimen'}).groupby('Barrio').sum()['Total_crimen'].reset_index()
    dfmap = dfmap.sort_values('Total_crimen', ascending=False)[1:]

    Map_fig = px.choropleth_mapbox(dfmap.sort_values('Total_crimen', ascending=False)[1:],
            locations='Barrio',
            color='Total_crimen',
            featureidkey="properties.SCANOMBRE",
            geojson=geoj,
            zoom=13,
            mapbox_style="stamen-toner",
            center={"lat": 4.655115, "lon": -74.055404}, #Center

            color_continuous_scale="matter",         #Color Scheme
            opacity=0.4,
            title='Total crimes in Bogotá'
            )
    Map_fig.update_layout(title='Total de Crímenes por Departamento',paper_bgcolor="#F8F9F9")

    return Map_fig




    #Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(debug=True)
