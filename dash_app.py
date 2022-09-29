# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from datetime import date
from dateutil.relativedelta import relativedelta
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output

from load_data import load_local_data
from create_charts import compute_figures

app = Dash(__name__)


def serve_layout():

    local_path='world_population.csv'
    df = load_local_data(local_path)

    fig1, fig2 = compute_figures(df)
            
    return html.Div(
        children=[
            html.Nav(className='navbar', children=[
                html.Div(children=[html.Img(className='navbar__ing_logo', src='./assets/ing_white.png')]),
                html.H1(children="ARIA Topic models - Feedback dashboard"),
                html.Div(children=[html.Img(className='navbar__aria_logo', src='./assets/aria_logo.png')]),
            ]),
            
            html.Hr(className='solid'),
            
            dcc.Graph(id="fig1", figure=fig1),

            html.Hr(className='solid'),

            html.Div(className='div2', children=[
                html.H2(children="Evolution of population for each country")
            ]),

            dcc.Graph(id="fig2", figure=fig2),

        ]
    )

## Dash App
app.layout = serve_layout

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080, debug=True)