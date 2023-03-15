import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd 
import plotly_express as px 

app = dash.Dash(__name__)

data = pd.read_csv("Data/Data - DS C1 Course.csv")

fig = px.bar(data, x="Age", y="Are you currently attending University / College?", color="Payment", barmode="group")
fig1 = px.bar(data, x='Payment', y='Age', color= "Which City are you currently residing in?")
fig2 = px.pie(data, values='Age', names='Gender')
fig3 = px.histogram(data, x='Age', y='Age',
             hover_data=['Timestamp'], color='Do you understand that this is a paid course ?',
             labels={}, height=400)

app.layout = html.Div([
    html.Div([
            dcc.Graph(id='graph1', figure=fig),
            dcc.Graph(id='graph2', figure=fig1),
        ], className='row'),         
    html.Div([
        
            dcc.Graph(id='graph3', figure=fig2),
            dcc.Graph(id='graph4', figure=fig3),
        ], className='row')
    
], className='container')

if __name__ == '__main__':
    app.run_server(debug=True)
