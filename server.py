from flask import redirect
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask_sqlalchemy import SQLAlchemy
from config import Config
from dash_bootstrap_components import themes

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
                external_stylesheets=[themes.BOOTSTRAP],
                suppress_callback_exceptions=True)

server = app.server
server.config.from_object(Config)
db = SQLAlchemy(server)
