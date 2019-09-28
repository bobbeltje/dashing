# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output
from datetime import datetime as dt

import pandas as pd
df = pd.DataFrame({'x': range(24), 
                   'y': [10,9,8,7.5,6.6,7,8.8,9,10,12,15,16,
                         18,21,22,22,21.5,20,20,19.6,18.4,17,17,12]})

app = dash.Dash(__name__)

app.layout = html.Div(children=[

    dcc.Input(id='location', type='text'),
    html.Div(id='typed_text'),
    html.Br(),
    dcc.DatePickerSingle(
        id='date_input', 
        min_date_allowed=dt(2010, 1, 1),
        max_date_allowed=dt(2020, 12, 31),
        initial_visible_month=dt.today(),
        date=str(dt.today())
        ),

    dcc.Graph(
        id='plot',
        style={'width': '800px'},
        figure={
            'data': [
                {'x': df.x, 'y': df.y, 'type':'scatter', 'mode':'marker+lines'}
            ],
            'layout': {
                'title': 'Temperature in Basel',
                'yaxis': {'title': 'Temperature'},
                'xaxis': {'title': 'Time'}
            }
        }
    )
])

@app.callback(
    Output('typed_text', 'children'),
    [Input('location', 'value')]
    )
def text_output(t):
    return t

if __name__ == '__main__':
    app.run_server(debug=True)
