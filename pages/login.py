import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from server import app, server
from flask import redirect

prefix = 'Login'

hidden_div = html.Div(id="hidden_div_for_redirect_callback")

email_input = dbc.FormGroup(
    [
        dbc.Label('Email', html_for='example-email'),
        dbc.Input(
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
            type='password',
            id=f'{prefix}_password',
            placeholder='Password',
        ),
        dbc.FormText(
            'Shh...  Don\'t tell it to anyone', color='secondary'
        ),
    ]
)

submit_button = dbc.Button('Submit', id=f'{prefix}_submit', color='primary')
form = dbc.Form([email_input, password_input, submit_button])
layout = html.Div([
    hidden_div,
    form
])

@app.callback(
    [
        Output(f'{prefix}_email', 'valid'),
        Output(f'{prefix}_email', 'invalid')
    ],
    [Input(f'{prefix}_email', 'value')],
)
def check_validity(text):
    #TODO Agregar un sistema para la validación del email
    if text:
        is_gmail = text.endswith('@gmail.com')
        if is_gmail:
            return is_gmail, not is_gmail
    return False, False

@app.callback(
    Output("url_container", "children"),
    [Input(f'{prefix}_submit', 'n_clicks')],
    [State(f'{prefix}_email', 'value'),
     State(f'{prefix}_password', 'value')],
)
def redirect_to_home(n_clicks, email, password):
    if(n_clicks is not None):
        return dcc.Location(
            pathname="/home",
            refresh=False,
            id="url")
        # return '/home'

