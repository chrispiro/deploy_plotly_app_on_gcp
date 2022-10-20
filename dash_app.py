from datetime import date
from dateutil.relativedelta import relativedelta
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output

from load_data import load_local_data
from create_charts import compute_figures

app = Dash(__name__)

local_path='world_population.csv'

##By defining the serve_layout function, we are ensuring that the data is refreshed everytime the page is reloaded
def serve_layout():

    df = load_local_data(local_path)

    figures = compute_figures(df)

    #Here we need to define the dash components
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

        ## TODO: Add your components here
        ## Hint: Use dcc.Graph to add the plotly charts
        ## Hint: Add separators and titles between charts (e.g. html elements like H1, H2 with a chart title as children attribute)

        ]

    )
            
    return dash_layout

## Dash App
app.layout = serve_layout

if __name__ == "__main__":

    ##TODO: Add command to run Dash server. (Tip: Specify 0.0.0.0 as host)