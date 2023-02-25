import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__, suppress_callback_exceptions=True)

data = pd.read_csv("Data/Data - DS C1 Course.csv")

fig = px.bar(data, x="Age", y="Are you currently attending University / College?", color="Payment", barmode="group")
fig1 = px.bar(data, x='Payment', y='Age', color= "Which City are you currently residing in?")

app.layout = html.Div(children=[
    html.H1('Course Dashboard'),
    dcc.Graph(id="graph1", 
        figure=fig,
        style={'display': 'inline-block'}
        
    ), 
    dcc.Graph(id="graph1", 
        figure=fig1,
        style={'display': 'inline-block'}
    )

])

if __name__ == '__main__':
    app.run_server(host='localhost',port=8005)


