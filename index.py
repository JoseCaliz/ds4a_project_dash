import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app.models import User
from server import app, server, login_manager
from pages import login, signup, home, models
from flask_login import (
    LoginManager, current_user,
    logout_user, login_required
)

app.layout = html.Div([
    html.Div(id='url_container', children=[
        dcc.Location(id='url', refresh=False)
    ]),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    # elif (current_user.is_authenticated is False):
        # return login.layout
    # elif pathname == '/pages/app1':
        # return page1.layout
    # elif (current_user.is_authenticated is True):
        # return home.layout
    # else:
        # # TODO: Colocar alguna página para el 404
        # return '404'
    return models.layout

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@server.route("/logout")
@login_required
def logout():
    logout_user()

    # TODO: Esto creo que toca cambiarlo utilizando los callbacks de DASH
    return server.redirect('/login')

if __name__ == '__main__':
    app.run_server(debug=True)
