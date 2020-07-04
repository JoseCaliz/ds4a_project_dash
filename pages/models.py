import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from server import app
from templates.includes.generate_template import full_template
import pandas as pd
import plotly.express as px
from server import db
import plotly.graph_objects as go


layout = html.Img(id='not_working_models', src='./assets/404.gif')
