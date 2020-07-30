import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
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
depto=['QUINDIO']
#dfmap = dff[(dff['year']==year)&(dff['crime'].isin(crimes))]
dfgender = df.groupby(['mapid','year','crime','sexo']).sum().reset_index()



df18 = dfgender[(dfgender['crime'].isin(crimes))&(dfgender['mapid'].isin(depto))]



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
Map_fig.update_layout(title='Total Crimes per Department',paper_bgcolor="#fffff0",margin={"r":0,"t":0,"l":20,"b":0})



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

values={'Robbery and theft':'robbery','Domestic violence':'dom_viol','Sex offenses':'sex_off','Manslaughter, Murder':'murder'}
revval = {value : key for (key, value) in values.items()}
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


ngbr=['EGIPTO', 'CHAPINERO', 'BELLA SUIZA']

dropdownngbr=dcc.Dropdown(
        id="ngbr_dropdown",
        options=[{"label":ngbr, "value":ngbr} for ngbr in ngbr],
        value='CHAPINERO',
        placeholder="Select a Neighborhood",
        multi=False
        )


gndr=['MASCULINO', 'FEMENINO']

dropdowngndr=dcc.Dropdown(
        id="gndr_dropdown",
        options=[{"label":gndr, "value":gndr} for gndr in gndr],
        value='FEMENINO',
        placeholder="Select Gender",
        multi=False
        )


dropdownage=dcc.Dropdown(
        id="age_dropdown",
        options=[{"label":age, "value":age} for age in range(1,100)],
        value=30,
        placeholder="Select Age",
        multi=False
        )


dropdownhour=dcc.Dropdown(
        id="hour_dropdown",
        options=[{"label":hour, "value":hour} for hour in range(24)],
        value=18,
        placeholder="Select Hour",
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

#Loading the logo
Logo_Img=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("logo.png"),
                    id="logo-image",
                    height=130


                )

            ], style={'textAlign': 'center'}
        )


#Dummy graph for dashboard design
#dummygraph.update_layout(paper_bgcolor="#fffff0")

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
gaugegraph.update_layout(paper_bgcolor="#fffff0",plot_bgcolor='#fffff0',margin={"r":10,"t":0,"l":10,"b":0})
#Yet another dummy.update_layout(paper_bgcolor="#fffff0")


fig4 = px.bar(df18, x="year", y="total",
             color='sexo',# barmode='group',
             facet_col='crime'
             )
fig4.update_layout(paper_bgcolor="#fffff0",plot_bgcolor='#fffff0',margin={"r":5,"t":0,"l":5,"b":0},legend={'x':0})

dfline = dff[(dff['crime'].isin(crimes))&(dff['mapid'].isin(depto))]
Line_fig=px.line(dfline,x="year",y="total", color="crime")
Line_fig.update_layout(title='Total Crimes in Colombia',paper_bgcolor="#fffff0")



dummybar = dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor':"#fffff0",
                'paper_bgcolor':"#fffff0",
                'margin':dict(l=40, r=20, t=00, b=00),

            }
        }
    )

# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

layout = dbc.Container(children=[


dbc.Row(
            [
                dbc.Col(dropdowncrime, width=6, lg=3),
                dbc.Col(dropdowndepto, width=6, lg=3),
                dbc.Col(dropdown, width=6, lg=3),
                #dbc.Col(html.Div("I wonder what to put here"), width=6, lg=3),
            ],justify='center',style={"height": "5%"}
        ),
dbc.Row(
            [


                dbc.Col(
                    [
                    dbc.Row([

                        dbc.Col([

                            dbc.Row([

                                dbc.Col([
                                        html.Div(dcc.Markdown("## **Risk Calculator** "
                                        )),

                                ], style={'height': '100%'}),

                            ], style={'height': '5%'}),

                            dbc.Row([

                                dbc.Col([
                                        Logo_Img,
                                        html.Hr(),
                                        html.H5("Neighborhood:"),
                                        dropdownngbr,
                                        html.Hr(),
                                        html.H5("Gender:"),

                                        dropdowngndr,
                                        html.Hr(),
                                        html.H5("Age:"),

                                        dropdownage,
                                        html.Hr(),
                                        html.H5("Hour:"),

                                        dropdownhour,]
                                , width=3, style={'height': '100%'}),


                                dbc.Col([
                                        #html.Div([
                                        dcc.Graph(figure=gaugegraph, id='Gauge', className="h-100")#, style={'height': '400px','width':'200px'})
                                        #])
                                ], style={'height': '100%'}),
                            ], no_gutters=True,  style={'height': '95%'}
                            ),





                        ], style={'height': '100%'}),# md=12),
                    ], style={'height': '60%'}),
            #    ], width=12),

                    dbc.Row([
                        dbc.Col([


                        dcc.Graph(figure=fig4, id='Gender_bar', className="h-100"),#className="h-100")

                        ], style={'height': '100%'}),
                    ],justify='end',align='end', no_gutters=True, style={'height': '40%'}),
                ], width=5, style={"height": "100%"}),
                dbc.Col(
                [

                    dbc.Row(
                        dbc.Col([html.P(),dcc.Graph(figure=Map_fig, id='Crime_map',style={'height': '90%'})],
                        style={"height": "100%"}
                        ), style={'height': '70%'}
                    ),

                    dbc.Row(
                        #dbc.Col(width=2),
                        dbc.Col(dcc.Graph(figure=Line_fig, id='predict_bar',className="h-100"),
                         style={'height': '100%'}),
                    style={'height': '30%'}
                    )


                            ], width=6, style={"height": "100%"}),





            ],justify='center',style={"height": "95%"}
        )


],style={"height": "100vh"},fluid=True)



##################################################################
#Let's include here the callbacks                                #
##################################################################

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

            color_continuous_scale="rdYlGn",         #Color Scheme
            opacity=0.5,
            title='Total crimes in Colombia'
            )
    Map_fig2.update_layout(title='Total de Crímenes por Departamento',margin={"r":0,"t":0,"l":5,"b":0},paper_bgcolor="rgba(0,0,0,0)")

    return Map_fig2



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


#Update the gender chart

@app.callback(
    [

    Output('Gender_bar', 'figure'),
        Output('predict_bar', 'figure')


    ],
    [
        Input("crime_dropdown","value"),
        Input("depto_dropdown", "value")
    ],
)
def update_gender_and_line_plot(crime_drop,depto_drop):
    dptos=[]
    dptos.append(depto_drop)

    df18 = dfgender[(dfgender['crime'].isin(crime_drop))&(dfgender['mapid'].isin(dptos))]
    fig5 = px.bar(df18, x="year", y="total",
                 color='sexo',# barmode='group',
                 facet_col='crime'
                 )
    fig5.update_layout(paper_bgcolor="#fffff0",plot_bgcolor='#fffff0',margin={"r":5,"t":0,"l":5,"b":0},legend={'x':0})

    dfline = dff[(dff['crime'].isin(crime_drop))&(dff['mapid'].isin(dptos))]
    Line_fig2=px.line(dfline,x="year",y="total", color="crime")
    Line_fig2.update_layout(title='Total Crimes in {}'.format(dptos[0]),
                            paper_bgcolor="#fffff0",plot_bgcolor='#fffff0',
                            margin={"r":5,"t":0,"l":5,"b":0},legend={'x':0})

    return [fig5, Line_fig2]



    # @app.callback(
    #     Output('predict_bar', 'figure'),
    #     [
    #         Input("crime_dropdown","value"),
    #         Input("depto_dropdown", "value")
    #     ],
    # )
    # def update_line_plot(crime_drop,depto_drop):
    #     dptos=[]
    #     dptos.append(depto_drop)
    #     dfline = dff[(dff['crime'].isin(crime_drop))&(dff['mapid'].isin(dptos))]
    #     Line_fig2=px.line(dfline,x="year",y="total", color="crime")
    #     Line_fig2.update_layout(title='Total Crimes in Colombia',paper_bgcolor="#fffff0")
    #
    #     return Line_fig2
