import plotly.express as px
import plotly.graph_objects as go

def create_figure_1(df):
    """ 
    Create choropleth chart (world map visualization)

    Args:
        df: input dataframe
    Returns:
        fig: Plotly figure 
    """

    ##Chart 1: world population
    fig1 = px.choropleth(df, locations='Country', locationmode='country names', color='2022 Population',
                            color_continuous_scale="Blues",
                            range_color=(0, 500000000),
                            labels={'2022 Population': '2022 Population'}
                            )
    fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, dragmode=False)

    return fig1

#TODO: Create new function: create_figure_2(df) with the code you wrote in the test_plotly_charts.ipynb
#Args: df
#Return: fig

def compute_figures(df):
    
    fig1 = create_figure_1(df)

    #TODO: Add the new figures in this code, and in the return List

    # fig2 = create_figure_2(df)

    return [fig1]