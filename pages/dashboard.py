import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_daq as daq
from server import app
import pandas as pd
import plotly.express as px
from server import db
import plotly.graph_objects as go
import json
import joblib

engine = db.engine

mapa_query ='''
SELECT barrio, extract(year FROM fecha) AS year, sexo, 'robbery' AS crime, COUNT(barrio) AS total
FROM hurto_personas
WHERE municipio LIKE 'BOGOTÁ D.C.'
GROUP BY barrio, year, sexo

UNION ALL

SELECT barrio, extract(year FROM fecha) AS year, sexo, 'dom_viol' AS crime, COUNT(barrio) AS total
FROM violencia_intrafamiliar
WHERE municipio LIKE 'BOGOTÁ D.C.'
GROUP BY barrio, year, sexo

UNION ALL

SELECT barrio, extract(year FROM fecha) AS year, sexo, 'murder' AS crime, COUNT(barrio) AS total
FROM homicidios
WHERE municipio LIKE 'BOGOTÁ D.C.'
GROUP BY barrio, year, sexo

UNION ALL

SELECT barrio, extract(year FROM fecha) AS year, sexo, 'sex_off' AS crime, COUNT(barrio) AS total
FROM del_sexuales
WHERE municipio LIKE 'BOGOTÁ D.C.'
GROUP BY barrio, year, sexo

'''
with open('D:/Barrios_Bog/loca.geojson', encoding='utf8') as geo:
    geojson = json.loads(geo.read())

with open('D:/Barrios_Bog/prueba1.txt', encoding='utf8') as test:
    testjson = json.loads(test.read())

testjson2 = testjson.copy()
query = ['COMPARTIR', '(20, 29]', 'MASCULINO', '20']
base = ['barrio_','edad_', 'sexo_', 'hora_']
keystest = [i + j for i, j in zip(base, query)]
for key in keystest:
    testjson2[key] = 1

test = pd.DataFrame(testjson2, index=[0])

clf = joblib.load('./data/naive_bayes.joblib.pkl')
#
# def predict_prob(barrio,edad,gender,hora):
#     que = [barrio,edad,gender,hora]
#     base = ['barrio_','edad_', 'sexo_', 'hora_']
#     keys = [i + j for i, j in zip(base, query)]
#     data = testjson.copy()
#     for key in keys:
#         data[key] = 1
#     test = pd.DataFrame(data, index=[0])
#     probabilities = clf.predict_proba(test)
#     return ['Murder:',probabilities[0,0],' Personal lesion:', probabilities[0,1]]
#

agedict = {}
for x in range(1,101):
    if x < 10:
        agedict[x] = '(0, 9]'
    elif x < 20:
        agedict[x] = '(10, 19]'
    elif x < 30:
        agedict[x] = '(20, 29]'
    elif x < 40:
        agedict[x] = '(30, 39]'
    elif x < 50:
        agedict[x] = '(40, 49]'
    elif x < 60:
        agedict[x] = '(50, 59]'
    elif x < 70:
        agedict[x] = '(60, 69]'
    elif x < 80:
        agedict[x] = '(70, 79]'
    elif x < 90:
        agedict[x] = '(80, 89]'
    elif x < 100:
        agedict[x] = '(90, 99]'


agerangedict = {
'0-9':'(0, 9]',
'10-19':'(10, 19]',
'20-29':'(20, 29]',
'30-39':'(30, 39]',
'40-49':'(40, 49]',
'50-59':'(50, 59]',
'60-69':'(60, 69]',
'70-79':'(70, 79]',
'80-89':'(80, 89]',
'90-99':'(90, 99]'
}


print(agedict[30])
print(type(agedict[30]))


df = pd.read_sql_query(mapa_query, engine.connect()).reset_index(drop=True)
matcher = pd.read_csv(r'C:\Users\Admin\Desktop\matcher.csv', encoding='UTF8')
matcher2 = pd.read_csv(r'C:/Users/Admin/Desktop/matcherloca.csv', encoding='UTF8')
mapper = matcher.set_index('barrio_original').to_dict()['nom_match']
mapper2 = matcher2.set_index('bar_orig').to_dict()['loc_match']
df['mapid'] = df.barrio.map(mapper)
df['locid'] = df.mapid.map(mapper2)

dff=df.groupby(['mapid','year','crime']).sum().reset_index()
dfloca=df.groupby(['locid','year','crime']).sum().reset_index()

crimes=['robbery','dom_viol','sex_off','murder']
year = 2012
loca_one=['SUBA']
barrio=['PASADENA']
#dfmap = dff[(dff['year']==year)&(dff['crime'].isin(crimes))]
dfgender = df.groupby(['mapid','year','crime','sexo']).sum().reset_index()
dfgender2 = df.groupby(['locid','year','crime','sexo']).sum().reset_index()


df18 = dfgender2[(dfgender2['crime'].isin(crimes))&(dfgender2['locid'].isin(loca_one))]



dfmap = dfloca[(dfloca['year']==2018)]#&(dfloca['crime'].isin(crimes))]
dfmap = dfmap.groupby('locid').sum().reset_index()

#Create the map:
Map_fig = px.choropleth_mapbox(dfmap,
        locations='locid',
        color='total',
        featureidkey="properties.LocNombre",
        geojson=geojson,
        zoom=11,
        mapbox_style="stamen-toner",
        center={"lat": 4.655115, "lon": -74.055404}, #Center not too close to the actual center

        color_continuous_scale="portland",         #Color Scheme
        opacity=0.5,
        title='Total crimes in Bogotá by Neighborhood'
        )
Map_fig.update_layout(title='Total crimes in Bogotá by Neighborhood',paper_bgcolor="#fffff0",margin={"r":0,"t":0,"l":20,"b":0},mapbox=dict(bearing=95))

hidden_div = html.Div(className='current_location',
                      children='home',
                      hidden=True)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Creating dropdown

ys = dff.year.unique()

dropdown=dcc.Dropdown(
        id="year_dropdown",
        options=[{"label":year, "value":year} for year in ys],
        value=2018,
        placeholder="Select a Year",
        multi=False
        )

values={'Robbery and theft':'robbery','Domestic violence':'dom_viol','Sex offenses':'sex_off','Manslaughter, Murder':'murder'}
revval = {value : key for (key, value) in values.items()}
dropdowncrime=dcc.Dropdown(
        id="crime_dropdown",
        options=[{"label":key, "value":values[key]} for key in values.keys()],
        value=["sex_off",'murder'],
        placeholder="Select a Crime",
        multi=True
        )

localidades=dfloca.locid.unique()

dropdownloca=dcc.Dropdown(
        id="loca_dropdown",
        options=[{"label":loca, "value":loca} for loca in localidades],#+[{"label": 'ALL', "value":localidades}],
        value='SUBA',
        placeholder="Select a Locality",
        multi=False
        )


ngbr=dff.mapid.unique()

dropdownngbr=dcc.Dropdown(
        id="ngbr_dropdown",
        options=[{"label":ngbr, "value":ngbr} for ngbr in ngbr],
        value='COMPARTIR',
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
        options=[{"label":key, "value":agerangedict[key]} for key in agerangedict.keys()],
        value='(30, 39]',
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


#Now the gauge graph
# gaugegraph = go.Figure(go.Indicator(
#     domain = {'x': [0, 1], 'y': [0, 1]},
#     value = 76,
#     mode = "gauge+number+delta",
#     title = {'text': "Probability of being robbed"},
#     delta = {'reference': 90},
#     gauge = {'axis': {'range': [None, 100]},
#              'steps' : [
#                  {'range': [0, 30], 'color': "green"},
#                  {'range': [30, 60], 'color': "yellow"}],
#              'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 85}}))
# gaugegraph.update_layout(paper_bgcolor="#fffff0",plot_bgcolor='#fffff0',margin={"r":10,"t":0,"l":10,"b":0})

#daq Gauges
primarycrime = daq.Gauge(
    id='firstcrime',
    size=150,
    color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
    showCurrentValue=True,
    units="%",
    value=80,
    label='Most likely crime',
    labelPosition='top',
    max=100,
    min=0,
    )

secondcrime = daq.Gauge(
    id='secondcrime',
    size=120,
    color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
    showCurrentValue=True,
    units="%",
    value=40,
    label='Second crime',
    labelPosition='bottom',
    max=100,
    min=0,
    style={'margin':{"r":0,"t":0,"l":0,"b":0}}
    )
thirdcrime = daq.Gauge(
    id='thirdcrime',
    size=120,
    color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
    showCurrentValue=True,
    units="%",
    value=10,
    label='Third crime',
    labelPosition='bottom',
    max=100,
    min=0,
    )




fig4 = px.bar(df18, x="year", y="total",
             color='sexo',# barmode='group',
             facet_col='crime'
             )
fig4.update_layout(paper_bgcolor="#fffff0",plot_bgcolor='#fffff0',margin={"r":5,"t":10,"l":5,"b":0},legend={'x':0})

dfline = dfloca[(dfloca['crime'].isin(crimes))&(dfloca['locid'].isin(loca_one))]
Line_fig=px.line(dfline,x="year",y="total", color="crime")
Line_fig.update_layout(title='Total Crimes in Selected Locality',paper_bgcolor="#fffff0")



layout = dbc.Container(children=[


dbc.Row(
            [
                dbc.Col(dropdowncrime, width=6, lg=3),
                dbc.Col(dropdownloca, width=6, lg=3),
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
                                        html.H2("Risk Calculator"
                                        ),

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
                                        dropdownhour,
                                        html.Br(),
                                        html.Button('Submit', id='submit-val', n_clicks=0),]
                                , width=3, style={'height': '100%','paddingTop':'0'}),


                                dbc.Col([
                                    dbc.Row([
                                        dbc.Col([
                                        html.Div(className='risk-gauges',children=[
                                            #html.Div([
                                            secondcrime,
                                            primarycrime,
                                            thirdcrime

                                            ])
                                                ],style={'height': '100%'})

                                        ], style={'height': '45%'}),
                                    dbc.Row([
                                        dbc.Col([
                                                ],style={'height': '100%'})
                                        ], style={'height': '55%'})


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
                         style={'height': '100%', 'paddingTop':'0'}),
                    style={'height': '30%'},
                    #no_gutters=True
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
    dfmap = dfloca[(dfloca['year']==year_drop)&(dfloca['crime'].isin(crime_drop))]
    dfmap = dfmap.groupby('locid').sum().reset_index()
    Map_fig2 = px.choropleth_mapbox(dfmap,
            locations='locid',
            color='total',
            featureidkey="properties.LocNombre",
            geojson=geojson,
            zoom=11,
            mapbox_style="stamen-toner",
            center={"lat": 4.655115, "lon": -74.055404}, #Center

            color_continuous_scale="portland",         #Color Scheme
            opacity=0.5,
            #title='Total crimes in Colombia'
            )
    Map_fig2.update_layout(title='Total Crimes per Locality',margin={"r":0,"t":0,"l":5,"b":0},
                            paper_bgcolor="rgba(0,0,0,0)",mapbox=dict(bearing=95))

    return Map_fig2



@app.callback(
    Output('loca_dropdown','value'),
    [
        Input('Crime_map','clickData')
    ],
    [
        State('loca_dropdown','value')
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
        Input("loca_dropdown", "value")
    ],
)
def update_gender_and_line_plot(crime_drop,ngbr_drop):
    nghbrhd=[]
    nghbrhd.append(ngbr_drop)

    df18 = dfgender2[(dfgender2['crime'].isin(crime_drop))&(dfgender2['locid'].isin(nghbrhd))]
    fig5 = px.bar(df18, x="year", y="total",
                 color='sexo',# barmode='group',
                 facet_col='crime',labels={'sexo':'Sexo','crime':'Crime','total':'Total','year':'Year'}
                 )
    fig5.update_layout(paper_bgcolor="#fffff0",margin={"r":5,"t":5,"l":5,"b":0},legend={'x':0,'bgcolor':'rgba(0,0,0,0)'})#plot_bgcolor='#228822',

    dfline = dfloca[(dfloca['crime'].isin(crime_drop))&(dfloca['locid'].isin(nghbrhd))]
    Line_fig2=px.line(dfline,x="year",y="total", color="crime")
    Line_fig2.update_layout(title={ 'text': 'Total Crimes in {}'.format(nghbrhd[0]),
                            'y':0.5,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'},
                            paper_bgcolor="#fffff0",plot_bgcolor='#fffff0',
                            margin={"r":5,"t":10,"l":5,"b":0},legend={'x':0})



    return [fig5, Line_fig2]




@app.callback(
           [#Output('dom', 'value'),
            Output('firstcrime', 'value'),
            Output('secondcrime', 'value')],
            # Output('mur', 'value'),
            # Output('car', 'value'),
            # Output('mot', 'value'),
            # Output('thr', 'value')],
            [Input('submit-val', 'n_clicks')],
            [State('ngbr_dropdown', 'value'),
            State('age_dropdown', 'value'),
            State('gndr_dropdown', 'value'),
            State('hour_dropdown', 'value')]
)
def predict_prob(bot,barrio,edad,gender,hora):
    que = [barrio,edad,gender,str(hora)]
    base = ['barrio_','edad_', 'sexo_', 'hora_']
    keys = [i + j for i, j in zip(base, que)]
    data = testjson.copy()
    for key in keys:
        data[key] = 1
    test = pd.DataFrame(data, index=[0])
    probabilities = clf.predict_proba(test)
    probstring = ['Murder:',probabilities[0,0]],['Personal Injuries:', probabilities[0,1]]

    return [probabilities[0,0]*100,probabilities[0,1]*100]
