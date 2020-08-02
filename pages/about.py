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

layout = html.Div(children=[
    dbc.Row([
        dbc.Col(html.Img(
            src='./assets/images/team/carolina.png',
            style={'margin-left':'auto',
                   'display':'block','width':'170px','height':'170px'}
        ), width=2, align='center'),
        dbc.Col(dcc.Markdown(
'''
## **Carolina Garzón**
Experienced Freelance Consultant with a demonstrated history of working in the environmental services industry. Skilled in Research, Environmental Modeling, Data Analysis, Environmental Impact Assessment, and Environmental Management Systems. Strong engineering professional with a focused in Environmental Engineering from Universidad Distrital Francisco José de Caldas. Interested in software development for GIS.
'''
        ), width=4, align='center')
    ],
    justify='center'),
    dbc.Row([
        dbc.Col(dcc.Markdown(
'''
## **Santiago Toledo**

Mathematician, master in Applied Mathematics, and PhD candidate in Systems and Computer Engineering at the Universidad Nacional de Colombia. Machine Learning as main research topic. Member of the MindLab Reseach Group. High programming language skills, in Python, C ++, Matlab, and R.
'''
        ), width=4, align='center', style={'text-align': 'right'}),
        dbc.Col(html.Img(
            src='./assets/images/team/santiago.png',
            width=170,
            height=170,
            style={'margin-right':'auto',
                   'display':'block','width':'170px','height':'170px'}
        ), width=2, align='center')
    ],
    justify='center'),
    dbc.Row([
        dbc.Col(html.Img(
            src='./assets/images/team/cristian.png',
            width=170,
            height=170,
            style={'margin-left':'auto',
                   'display':'block','width':'170px','height':'170px'}
        ), width=2, align='center'),
        dbc.Col(dcc.Markdown(
'''
## **Cristian Portela**

Ingeniero en Mecatrónica y especialista en gerencia integral de proyectos con enfoque PMI. Experiencia en programación de distintos lenguajes como Python y JAVA; manejo de bases de datos como Oracle SQL, PostgreSQL entre otras y afinidad por la ciencia de datos; además de habilidades en IoT, dispositivos embebidos, Raspberry Pi, Arduino y Micro-Controladores.
'''
        ), width=4, align='center')
    ],
    justify='center'),
    dbc.Row([
        dbc.Col(dcc.Markdown(
'''
## **Jose Cáliz**

Engineer by profession, student of Master in Statistics, Senior Data Scientist.  Hater of the purple food, fan of Ramen. Proud owner of 25 dreads and a terrible humour sense. QWERTY keyboard should die, all hail Dvorak. Look mom!, I am becoming successful
'''
        ), width=4, align='center', style={'text-align': 'right'}),
        dbc.Col(html.Img(
            src='./assets/images/team/jose.png',
            width=170,
            height=170,
            style={'margin-right':'auto',
                   'display':'block','width':'170px','height':'170px'}
        ), width=2, align='center')
    ],
    justify='center'),
    dbc.Row([
        dbc.Col(html.Img(
            src='./assets/images/team/camilo.png',
            width=170,
            height=170,
            style={'margin-left':'auto',
                   'display':'block','width':'170px','height':'170px'}
        ), width=2, align='center'),
        dbc.Col(dcc.Markdown(
'''
## **Camilo De La Cruz Arboleda**

Experienced Research Professor with a demonstrated history of working in the higher education industry as well as in the private sector. Skilled in Python (Programming Language), Running, Cycling, Active Learning, and Research. Strong education professional with a Master of Laws - LLM focused in sustainability and technology from University of California, Berkeley - School of Law.
'''
        ), width=4, align='center')
    ],
    justify='center')
])
