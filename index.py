import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app.models import User
from server import app, server, login_manager
from pages import login, signup, dashboard, models, about
from flask_login import (
    LoginManager, current_user,
    logout_user, login_required
)
from flask import redirect
from utils.functions import highlight_current_page
from assets.generate_template import full_template_vanilla

full_template_dashboard = full_template_vanilla

app.index_string = full_template_dashboard
app.title='Dashboard'

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
    if pathname == '/' or pathname == '/dashboard':
        return dashboard.layout
    if pathname == '/tables':
        return dashboard.layout
    if pathname == '/models':
        return dashboard.layout
    if pathname == '/about':
        return about.layout

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@server.route("/logout")
@login_required
def logout():
    logout_user()

    # TODO: Esto creo que toca cambiarlo utilizando los callbacks de DASH
    return server.redirect('/login')

@server.route('/dashboard')
def update_index_dashboard():
    app.title = 'Dashboard'
    full_template_dashboard = full_template_vanilla
    full_template_dashboard = \
        full_template_dashboard.replace('{dashboard_div}', 'active')
    full_template_dashboard = full_template_dashboard.replace('{models_div}', '')
    full_template_dashboard = full_template_dashboard.replace('{tables_div}', '')
    full_template_dashboard = full_template_dashboard.replace('{about_div}', '')
    full_template_dashboard = full_template_dashboard.replace('{info_div}', '')
    app.index_string = full_template_dashboard
    return app.index()

@server.route('/models')
def update_index_model():
    app.title = 'Models'
    full_template_models = full_template_vanilla
    full_template_models = full_template_models.replace('{dashboard_div}', '')
    full_template_models = full_template_models.replace('{models_div}', 'active')
    full_template_models = full_template_models.replace('{tables_div}', '')
    full_template_models = full_template_models.replace('{about_div}', '')
    full_template_models = full_template_models.replace('{info_div}', '')
    app.index_string = full_template_models
    return app.index()

@server.route('/tables')
def update_index_tables():
    app.title = 'Tables'
    full_template_tables = full_template_vanilla
    full_template_tables = full_template_tables.replace('{dashboard_div}', '')
    full_template_tables = full_template_tables.replace('{models_div}', '')
    full_template_tables = full_template_tables.replace('{tables_div}', 'active')
    full_template_tables = full_template_tables.replace('{about_div}', '')
    full_template_tables = full_template_tables.replace('{info_div}', '')
    app.index_string = full_template_tables
    return app.index()

@server.route('/about')
def update_index_about():
    app.title = 'About'
    full_template_about = full_template_vanilla
    full_template_about = full_template_about.replace('{dashboard_div}', '')
    full_template_about = full_template_about.replace('{models_div}', '')
    full_template_about = full_template_about.replace('{tables_div}', '')
    full_template_about = full_template_about.replace('{about_div}', 'active')
    full_template_about = full_template_about.replace('{info_div}', '')
    app.index_string = full_template_about
    return app.index()

@server.route('/info')
def update_index_info():
    app.title = 'Info'
    full_template_info = full_template_vanilla
    full_template_info = full_template_info.replace('{dashboard_div}', '')
    full_template_info = full_template_info.replace('{models_div}', '')
    full_template_info = full_template_info.replace('{tables_div}', '')
    full_template_info = full_template_info.replace('{about_div}', '')
    full_template_info = full_template_info.replace('{info_div}', 'active')
    app.index_string = full_template_info
    return app.index()

if __name__ == '__main__':
    app.run_server(debug=True)

