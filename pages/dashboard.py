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
import json

engine = db.engine

mapa_query ='''
SELECT departamento, extract(year FROM fecha) AS year, sexo, 'robbery' AS crime, COUNT(dia) AS total
FROM hurto_personas
GROUP BY departamento, year, sexo

UNION ALL

SELECT departamento, extract(year FROM fecha) AS year, sexo, 'dom_viol' AS crime, COUNT(dia) AS total
FROM violencia_intrafamiliar
GROUP BY departamento, year, sexo

UNION ALL

SELECT departamento, extract(year FROM fecha) AS year, sexo, 'murder' AS crime, COUNT(dia) AS total
FROM homicidios
GROUP BY departamento, year, sexo

UNION ALL

SELECT departamento, extract(year FROM fecha) AS year, sexo, 'sex_off' AS crime, COUNT(dia) AS total
FROM del_sexuales
GROUP BY departamento, year, sexo


'''
with open('D:/Barrios_Bog/geojson_departamentos.json', encoding='utf8') as geo:
    geoj = json.loads(geo.read())

df = pd.read_sql_query(mapa_query, engine.connect()).reset_index(drop=True)
matcher = pd.read_csv(r'C:\Users\Admin\Desktop\matcherdpto.csv', encoding='UTF8')

mapper = matcher.set_index('dpto_orig').to_dict()['nom_match']
df['mapid']=df.departamento.map(mapper)
dff=df.groupby(['mapid','year','crime']).sum().reset_index()
crimes=['robbery','dom_viol','sex_off','murder']
year = 2012
#dfmap = dff[(dff['year']==year)&(dff['crime'].isin(crimes))]
dfgender = df.groupby(['mapid','year','crime','sexo']).sum().reset_index()

dfmap = dff[(dff['year']==year)&(dff['crime'].isin(crimes))]
dfmap = dfmap.groupby('mapid').sum().reset_index()
#Create the map:
Map_fig = px.choropleth_mapbox(dfmap,
        locations='mapid',
        color='total',
        #featureidkey="properties.NOMBRE_DPT",
        geojson=geoj,
        zoom=7,
        mapbox_style="stamen-toner",
        center={"lat": 4.655115, "lon": -74.055404}, #Center

        color_continuous_scale="matter",         #Color Scheme
        opacity=0.5,
        title='Total crimes in Colombia by Department'
        )
Map_fig.update_layout(title='Total Crimes per Department',paper_bgcolor="#fffff0")



hidden_div = html.Div(className='current_location',
                      children='home',
                      hidden=True)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Creating dropdown

ys = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]

dropdown=dcc.Dropdown(
        id="year_dropdown",
        options=[{"label":year, "value":year} for year in ys],
        value=2018,
        placeholder="Select a year",
        multi=False
        )

values={'Robbery and theft':'robbery','Domestic violence':'dom_viol','Sex offenses':'sex_off'}

dropdowncrime=dcc.Dropdown(
        id="crime_dropdown",
        options=[{"label":key, "value":values[key]} for key in values.keys()],
        value=["sex_off",'robbery'],
        placeholder="Select a crime",
        multi=True
        )

deptos=['AMAZONAS', 'ANTIOQUIA', 'ARAUCA',
       'ATLANTICO', 'BOLIVAR', 'BOYACA', 'CALDAS', 'CAQUETA', 'CASANARE',
       'CAUCA', 'CESAR', 'CHOCO', 'CORDOBA', 'CUNDINAMARCA', 'GUAINIA',
       'GUAVIARE', 'HUILA', 'LA GUAJIRA', 'MAGDALENA', 'META', 'NARIÑO',
       'NORTE DE SANTANDER', 'PUTUMAYO', 'QUINDIO', 'RISARALDA',
       'SANTANDER', 'SUCRE', 'TOLIMA', 'VALLE DEL CAUCA', 'VAUPES',
       'VICHADA']

dropdowndepto=dcc.Dropdown(
        id="depto_dropdown",
        options=[{"label":dpto, "value":dpto} for dpto in deptos]+[{"label": 'SAN ANDRES', "value":'ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA'}],
        value='QUINDIO',
        placeholder="Select a Department",
        multi=False
        )

#Loading an image
Addict_Img=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("addict-img.png"),
                    id="addict-image",
                    width=200,
                    height=200,

                )

            ], style={'textAlign': 'center'}
        )


#Dummy graph for dashboard design

dummygraph = dcc.Graph(
    figure=dict(
        data=[
            dict(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                name='Rest of world',
                marker=dict(
                    color='rgb(55, 83, 109)'
                )
            ),
            dict(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='China',
                marker=dict(
                    color='rgb(26, 118, 255)'
                )
            )
        ],
        layout=dict(
            title='Crimes through the years',
            showlegend=True,
            legend=dict(
                x=0,
                y=1.0
            ),
            margin=dict(l=40, r=0, t=40, b=30)
        )
    ),
    style={'height': 300},
    id='dummy-graph'
)

#Now the gauge graph
gaugegraph = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 76,
    mode = "gauge+number+delta",
    title = {'text': "Probability of being robbed"},
    delta = {'reference': 90},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 30], 'color': "green"},
                 {'range': [30, 60], 'color': "yellow"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 85}}))

#Yet another dummy

dummybar = dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )

# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

layout = html.Div(children=[


dbc.Row(
            [
                dbc.Col(dropdowncrime, width=6, lg=3),
                dbc.Col(dropdowndepto, width=6, lg=3),
                dbc.Col(dropdown, width=6, lg=3),
                dbc.Col(html.Div("I wonder what to put here"), width=6, lg=3),
            ]
        ),
dbc.Row(
            [


                dbc.Col(
                    [
                    dbc.Row([


                        html.Div("Risk Calculator"),
                        html.Div([dcc.Graph(figure=gaugegraph, id='Gauge')]) #style={'height': '400px','width':'300px'},

                        ]),

                    dbc.Row([
                        html.Div([
                        dummybar
                        ])])

                    ], md=4),

                dbc.Col(
                [

                    dcc.Graph(figure=Map_fig,style={'height': '600px'}, id='Crime_map'),



                    dummygraph

                            ], md=6),





            ]
        )


])
