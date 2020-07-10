import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from server import app
import pandas as pd
import plotly.express as px
from server import db, app
import plotly.graph_objects as go

layout = html.Img(id='not_working_models', src='./assets/404.gif')
