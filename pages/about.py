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
            width=170,
            height=170,
            style={'margin-left':'auto', 'display':'block'}
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
            style={'margin-right':'auto', 'display':'block'}
        ), width=2, align='center')
    ],
    justify='center'),
    dbc.Row([
        dbc.Col(html.Img(
            src='./assets/images/team/cristian.png',
            width=170,
            height=170,
            style={'margin-left':'auto', 'display':'block'}
        ), width=2, align='center'),
        dbc.Col(dcc.Markdown(
'''
## **Cristian Portela**

Ingeniero Mecatrónico con conocimientos en: programación de lenguajes como C, C++, C#, JAVA, JAVASCRIPT, HTML, Sql Oracle, Unix, Visual Basic (Excel Avanzado), entre otros; programación de dispositivos electrónicos como PLC, FPGA y Micro-Controladores; manejo de Software para diseño (CAD) y fabricación (CAM) de dispositivos electrónicos y mecánicos. Con afinidad por el desarrollo de software, robótica e inteligencia artifical.

Serio y emprendedor, habituado al trabajo y desarrollo de proyectos en equipo; con facilidad para aprender y a la constante expectativa de adquisición de nuevos conocimientos y actualización profesional.
'''
        ), width=4, align='center')
    ],
    justify='center'),
    dbc.Row([
        dbc.Col(dcc.Markdown(
'''
## **Jose Cáliz**

Más tarde cambio esto porque no sé quién soy.
'''
        ), width=4, align='center', style={'text-align': 'right'}),
        dbc.Col(html.Img(
            src='./assets/images/team/jose.png',
            width=170,
            height=170,
            style={'margin-right':'auto', 'display':'block'}
        ), width=2, align='center')
    ],
    justify='center'),
    dbc.Row([
        dbc.Col(html.Img(
            src='./assets/images/team/camilo.png',
            width=170,
            height=170,
            style={'margin-left':'auto', 'display':'block'}
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
