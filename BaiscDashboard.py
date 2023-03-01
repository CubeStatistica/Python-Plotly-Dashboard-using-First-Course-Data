import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

data = pd.read_csv("Data/Data - DS C1 Course.csv")

fig = px.bar(data, x="Age", y="Are you currently attending University / College?", color="Payment", barmode="group")
fig1 = px.bar(data, x='Payment', y='Age', color= "Which City are you currently residing in?")
fig2 = px.pie(data, values='Age', names='Gender')

app.layout = html.Div(children=[
    html.Div([
     dcc.Graph(id="graph1", figure=fig), 
     dcc.Graph(id="gra7", figure=fig2)
     ],className='six columns'),
    
    html.Div([
     dcc.Graph(id="graph2", figure=fig1), 
     ],className='six columns'),

    
    html.Div([
     dcc.Graph(id="graph3", figure=fig), 
     ],className='six columns'),

    html.Div([
     dcc.Graph(id="graph4", figure=fig1), 
     ],className='six columns'),

])

if __name__ == '__main__':
    app.run_server(host='localhost',port=8005)


