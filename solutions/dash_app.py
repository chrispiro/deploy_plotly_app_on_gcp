from datetime import date
from dateutil.relativedelta import relativedelta
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output

from load_data import load_local_data
from create_charts import compute_figures

app = Dash(__name__)

local_path='../world_population.csv'

##By defining the serve_layout function, we are ensuring that the data is refreshed everytime the page is reloaded
def serve_layout():

    #Read data from local path
    df = load_local_data(local_path)

    #Here we are loading the plotly charts we created previously
    figures = compute_figures(df)

    #Here we are defining the dash components
    #The parent component is html.Div
    #For each component, we can define a list (children=[]) of components 

    dash_layout = html.Div(

        children=[

        #Navigation bar already defined
        html.Nav(className='navbar', children=[
            html.Div(children=[html.Img(className='navbar__gcp_logo', src='./assets/gcp_logo.png')]),
            html.H1(children="ING Code Breakfast - Dash App in GCP"),
            html.Div(children=[html.Img(className='navbar__dash_logo', src='./assets/dash_logo.png')]),
        ]),

        html.H1('World population map'),

        dcc.Graph(id='0', figure=figures[0]),

        ## TODO: Add your components here
        
        html.H1('Evolution of population for each country'),

        dcc.Graph(id='1', figure=figures[1]),

        html.H1('World Population Percentage'),

        dcc.Graph(id='2', figure=figures[2])
    ]

    )
            
    return dash_layout

## Dash App
app.layout = serve_layout

if __name__ == "__main__":

    app.run_server(host="0.0.0.0", port=8080, debug=True)

#Note: Run 'python dash_app.py' to run the application