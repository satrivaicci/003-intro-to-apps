######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go
import plotly.express as px


########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Beer Comparison'

label1='IBU'
label2='ABV'

########### Set up the chart

def make_that_cool_barchart(beers, ibu_values, abv_values, color1, color2, mytitle):
    bitterness = go.Bar(
        x=beers,
        y=ibu_values,
        name=label1,
        marker={'color':color1}
    )
    alcohol = go.Bar(
        x=beers,
        y=abv_values,
        name=label2,
        marker={'color':color2}
    )

    beer_data = [bitterness, alcohol]
    beer_layout = go.Layout(
        barmode='group',
        title = mytitle
    )

    beer_fig = go.Figure(data=beer_data, layout=beer_layout)
    return beer_fig

def make_bubble_chart():
    df = px.data.gapminder()
    return px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", log_x=True, size_max=60)


######### Run the function #######

if __name__ == '__main__':
    # fig = make_that_cool_barchart(beers, ibu_values, abv_values, color1, color2, mytitle)
    fig = make_bubble_chart()
    fig.write_html('docs/bubblechart.html')
    print('We successfully updated the bubblechart!')
