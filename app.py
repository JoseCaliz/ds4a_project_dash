import dash
import dash_core_components as dcc
import dash_html_components as html


header = open('templates/includes/header.html').read()
footer = open('templates/includes/footer.html').read()
sidenav = open('templates/includes/sidenav.html').read()
content = open('templates/includes/content.html').read()
 
app = dash.Dash(__name__)

app.index_string = header + sidenav + content + footer

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Plotly Dash', className="app-header--title")
        ]
    ),
    html.Div(
        children=html.Div([
            html.H5('Overview'),
            html.Div('''
                This is an example of a simple Dash app with
                local, customized CSS.
            ''')
        ])
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
