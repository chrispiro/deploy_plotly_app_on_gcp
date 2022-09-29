import plotly.express as px
import plotly.graph_objects as go

import plotly.express as px


def compute_figures(df):

    ##Chart 1: world population
    fig1 = px.choropleth(df, locations='CCA3', color='2022 Population',
                            color_continuous_scale="Blues",
                            range_color=(0, 500000000),
                            labels={'2022 Population':'2022 Population'}
                            )
    fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, dragmode=False)

    ##Chart 2:

    #Get population from 1970 to 2022
    df_population = df[df.columns[5:13]]

    #Invert order of columns
    df_population = df_population[df_population.columns[::-1]]
    df_population.insert(0, 'Country', df['Country'])

    fig2 = go.Figure()

    # set up ONE trace
    fig2.add_trace(go.Scatter(x=df_population.columns[1:],
                            y=df_population[df_population.Country=='Afghanistan'][df_population.columns[1:]].iloc[0],
                            fill='tozeroy',
                            visible=True)
                )


    updatemenu = []
    buttons = []

    # button with one option for each dataframe
    for country in df_population.Country:
        buttons.append(dict(method='restyle',
                            label=country,
                            visible=True,
                            args=[{'y': [df_population[df_population.Country==country][df_population.columns[1:]].iloc[0]],
                                'x': [df_population.columns[1:]],
                                'type':'line',
                                'fill' : 'tozeroy'}, [0]],
                            )
                    )

    # some adjustments to the updatemenus
    updatemenu = []
    your_menu = dict()
    updatemenu.append(your_menu)

    updatemenu[0]['buttons'] = buttons
    updatemenu[0]['direction'] = 'down'
    updatemenu[0]['showactive'] = True

    # add dropdown menus to the figure
    fig2.update_layout(showlegend=False, updatemenus=updatemenu)

    return fig1, fig2
