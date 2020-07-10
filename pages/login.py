import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import re
from dash.dependencies import Input, Output, State
from server import app, server, db
from flask import request, redirect
from app.models import User
from flask_login import login_user

email_re = re.compile(
    r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
)

prefix = 'Login'

hidden_div = html.Div(id="hidden_div_for_redirect_callback")

email_input = dbc.FormGroup(
    [
        dbc.Label('Email', html_for='example-email'),
        dbc.Input(
            name='email',
            type='email',
            id=f'{prefix}_email',
            placeholder='Email'
        ),
        dbc.FormText(
            'Are you on email? You simply have to be these days',
            color='secondary',
        ),
    ]
)

password_input = dbc.FormGroup(
    [
        dbc.Label('Password', html_for='example-password'),
        dbc.Input(
            name='password',
            type='password',
            id=f'{prefix}_password',
            placeholder='Password',
        ),
        dbc.FormText(
            'Shh...  Don\'t tell it to anyone', color='secondary'
        ),
    ]
)

nav = dbc.Nav([
    dbc.NavLink("Create Account", href='/signup')
])

submit_button = html.Button(
    'Submit',
    id=f'{prefix}_submit',
    type='submit',
    className='btn btn-primary'
)

form = html.Form([
    email_input, password_input, nav, submit_button
], action='/post', method='post')

layout = html.Div([
    hidden_div,
    form,
])


def validate_user(email, password):
    print(email, password)
    saved_user = User.query.filter_by(email=email).first()
    if (saved_user is None or saved_user.password != password):
        return False

    return saved_user

@server.route('/post', methods=['POST'])
def on_post():
    data = request.form
    saved_user = validate_user(data['email'], data['password'])
    if(saved_user is not False):
        print('login succesful')
        login_user(saved_user)
        return redirect('/page1')

    return redirect('/')
