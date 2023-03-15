import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='graph1', figure={}),
        ], width=6),
        dbc.Col([
            dcc.Graph(id='graph2', figure={}),
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='graph3', figure={}),
        ], width=6),
        dbc.Col([
            dcc.Graph(id='graph4', figure={}),
        ], width=6),
    ]),
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
