import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

data = pd.read_csv("Data/Data - DS C1 Course.csv")

fig = px.bar(data, x="Age", y="Are you currently attending University / College?", color="Payment", barmode="group")
fig1 = px.bar(data, x='Payment', y='Age', color= "Which City are you currently residing in?")
fig2 = px.pie(data, values='Age', names='Gender')
fig3 = px.histogram(data, x='Age', y='Age',
             hover_data=['Timestamp'], color='Do you understand that this is a paid course ?',
             labels={}, height=400)

# Define the sidebar content
sidebar = html.Div(
    [
        html.H2("Sidebar"),
        html.Hr(),
        html.P("Sidebar content goes here..."),
    ],
    id="sidebar",
    className="sidebar",
)

# Define the main content
content = html.Div(
    [
        html.Div(
            [
                dcc.Graph(id="graph1", figure=fig), 
                dcc.Graph(id="gra7", figure=fig2)
            ],
            className="column"
        ),
        html.Div(
            [
                dcc.Graph(id="graph2", figure=fig1)
            ],
            className="column"
        ),
        html.Div(
            [
                dcc.Graph(id="graph3", figure=fig3)
            ],
            className="column"
        ),
        html.Div(
            [
                dcc.Graph(id="graph4", figure=fig1)
            ],
            className="column"
        ),
    ],
    className="main-content",
)

# Define the layout
app.layout = html.Div([sidebar, content])

# Define the CSS styles
app.css.append_css(
    {
        "external_url": "https://raw.githubusercontent.com/saadmk11/dash-css-styles/main/styles.css"
    }
)

if __name__ == '__main__':
    app.run_server(host='localhost',port=8005)
