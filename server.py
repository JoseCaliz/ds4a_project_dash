# Dash app initialization
import dash
import dash_bootstrap_components as dbc

# global imports
import os
from flask_login import LoginManager, UserMixin
import random

# local imports
from utilities.auth import db, Users as base
from utilities.config import engine


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

server = app.server
app.config.suppress_callback_exceptions = True
#app.css.config.serve_locally = True
#app.scripts.config.serve_locally = True
app.title = 'Dash Auth Flow'

# TODO: Por favor debes remover esta linea
uri = 'postgresql://ds4a:L#Nhd4z!=uH@localhost:5432/alcaldia'

# config
server.config.update(
    SECRET_KEY=os.urandom(20),
    SQLALCHEMY_DATABASE_URI=uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db.init_app(server)

# Setup the LoginManager for the server
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'


# Create User class with UserMixin
class Users(UserMixin, base):
    pass

# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
