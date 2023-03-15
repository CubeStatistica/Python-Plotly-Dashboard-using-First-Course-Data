import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd 
import plotly_express as px 

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

data = pd.read_csv("Data/Data - DS C1 Course.csv")

fig = px.bar(data, x="Age", y="Are you currently attending University / College?", color="Payment", barmode="group")
fig1 = px.bar(data, x='Payment', y='Age', color= "Which City are you currently residing in?")
fig2 = px.pie(data, values='Age', names='Gender')
fig3 = px.histogram(data, x='Age', y='Age',
             hover_data=['Timestamp'], color='Do you understand that this is a paid course ?',
             labels={}, height=400)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='graph1', figure=fig),
        ], width=6),
        dbc.Col([
            dcc.Graph(id='graph2', figure=fig1),
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='graph3', figure=fig2),
        ], width=6),
        dbc.Col([
            dcc.Graph(id='graph4', figure=fig3),
        ], width=6),
    ]),
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
