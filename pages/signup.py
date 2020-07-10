import dash_html_components as html
import dash_bootstrap_components as dbc
from app.models import User
from server import server, db
from flask import request, redirect

prefix = 'signup'

name = dbc.FormGroup([
    dbc.Label('Name'),
    dbc.Input(
        name='name',
        id=f'{prefix}_Name',
        type='text',
        placeholder='Name'
)])

email = dbc.FormGroup([
    dbc.Input(
        name='email',
        id=f'{prefix}_email',
        type='email',
        placeholder='Email...'
)])

password = dbc.FormGroup([
    dbc.Input(
        name='password',
        id=f'{prefix}_password',
        type='password',
        placeholder='Password'
)])

register_button = dbc.FormGroup([
    html.Button(
        'Register',
        id=f'{prefix}_submit',
        className='btn btn-primary',
        type='submit'
)])

form = html.Form([
    name,
    email,
    password,
    register_button
], action='/signup', method='post')

layout = html.Div([form])

@server.route('/signup', methods=['POST'])
def signup_validation():
    form_data = request.form
    print(form_data)
    new_user = User()

    # TODO: cambiar eso para que el id se autoincremente
    new_user.id = 0
    new_user.name = form_data['name']
    new_user.email = form_data['email']
    new_user.password = form_data['password']

    db.session.add(new_user)
    db.session.commit()

    print(new_user.name)
    return redirect('/')
