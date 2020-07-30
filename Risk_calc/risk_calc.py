import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
import plotly.graph_objects as go
import time
import json
from pathlib import Path
import random
#import plotly.graph_objs as go

app = dash.Dash(__name__)

##some vars, dropdowns##
dd_age= [ {'value':x,'label':x} for x in range(0,100) ] 
dd_hour= [ {'value':x,'label':x} for x in range(0,25) ] 
##

def get_neigb():
    path = Path(__file__).parent / "ngb.json"
    with open(path, "r") as read_file:
        return json.load(read_file)

app.layout = html.Div(className= 'app-container', children=[
    html.Div(className='risk-container card', children=[

        html.H2(className='risk-title',children='RISK CALCULATOR'),

        html.Div(className='risk-selectors',children=[

            html.Div(className='risk-dropdowns',children=[

                dcc.Dropdown(id='selector1', 
                    options=get_neigb(),placeholder="Select a Neigborhood",
                    #style={'backgroundColor': "#1E1E1E"},
                    className='selector'),

                dcc.Dropdown(id='selector2', 
                    options=[{'label': 'Female', 'value': 'f'},{'label': 'Male', 'value': 'm'}],placeholder="Select a Gender",
                    #style={'backgroundColor': "#1E1E1E"},
                    className='selector'),
                    
                dcc.Dropdown(id='selector3', 
                    options=dd_age,placeholder="Select a Age",
                    #style={'backgroundColor': "#1E1E1E"},
                    className='selector'),

                dcc.Dropdown(id='selector4', 
                    options=dd_hour,placeholder="Select a Hour",
                    #style={'backgroundColor': "#1E1E1E"},
                    className='selector'),

                ##Cami, puse este botón porque creo que los eventos de los drop no deben ser los que actualizan
                # los gauge, sino despues de haver seleccionado las opciones, el boton debería llamar la funcion
                # de SAntiago enviándole los parametros y recibiendo los numeros para alimentar los gauges; sin 
                # embargo sipentase libre de vcabiar lo que quiera
                #   
                html.Button('Submit', id='submit-val', n_clicks=0)
        ]),
        
            html.Div(className='risk-gauges',children=[
                    daq.Gauge(
                        id='dom',
                        size=100,
                        color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
                        showCurrentValue=True,
                        units="%",
                        value=0,
                        label='Domestic Violence',
                        max=100,
                        min=0,
                        ) ,
                    daq.Gauge(
                        id='sex',
                        size=100,
                        color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
                        showCurrentValue=True,
                        units="%",
                        value=0,
                        label='Sexual Crimes',
                        max=100,
                        min=0,
                        ),
                    daq.Gauge(
                        id='per',
                        size=100,
                        color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
                        showCurrentValue=True,
                        units="%",
                        value=0,
                        label='Personal Injuries',
                        max=100,
                        min=0,
                        ),
                    daq.Gauge(
                        id='mur',
                        size=100,
                        color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
                        showCurrentValue=True,
                        units="%",
                        value=0,
                        label='Murders',
                        max=100,
                        min=0,
                        ),
                    daq.Gauge(
                        id='car',
                        size=100,
                        color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
                        showCurrentValue=True,
                        units="%",
                        value=0,
                        label='Car Theft',
                        max=100,
                        min=0,
                        ),
                    daq.Gauge(
                        id='mot',
                        size=100,
                        color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
                        showCurrentValue=True,
                        units="%",
                        value=0,
                        label='Motorcycle Theft',
                        max=100,
                        min=0,
                        ),
                    daq.Gauge(
                        id='thr',
                        size=100,
                        color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
                        showCurrentValue=True,
                        units="%",
                        value=0,
                        label='Threats',
                        max=100,
                        min=0,
                        ),
                    #dcc.Graph(id='crime4',figure=fig)   
            ]), 

        ])

    ])   
   
])

##esta funcioncita debería pasarle los parametros al modelo de santiago y traer los valores que necesitamos
def get_model_vals(neighb,gender,age,hour):
    #llamar modelo
    #valores = modelosant(neighb,gender,age,hour)
    # return 7 valores

    #mientras, valores aleatorios
    valores=[random.randint(0, 100) for x in range(0,10)]
    return valores


@app.callback([dash.dependencies.Output('dom', 'value'),
            dash.dependencies.Output('sex', 'value'),
            dash.dependencies.Output('per', 'value'),
            dash.dependencies.Output('mur', 'value'),
            dash.dependencies.Output('car', 'value'),
            dash.dependencies.Output('mot', 'value'),
            dash.dependencies.Output('thr', 'value')],
            [dash.dependencies.Input('submit-val', 'n_clicks')],
            [dash.dependencies.State('selector1', 'value'),
            dash.dependencies.State('selector2', 'value'),
            dash.dependencies.State('selector3', 'value'),
            dash.dependencies.State('selector4', 'value')])

def update_output(bot,sel1,sel2,sel3,sel4):
    print ("bot",bot)
    print ("sel1",sel1)
    print ("sel2",sel2)
    print ("sel3",sel3)
    print ("sel4",sel4)
    if bot != 0:
        vals=get_model_vals("a","b",0,0)
        return vals[0],vals[1],vals[2],vals[3],vals[4],vals[5],vals[6]
    else:
        return [0,0,0,0,0,0,0]


if __name__ == '__main__':
    app.run_server(debug=True)