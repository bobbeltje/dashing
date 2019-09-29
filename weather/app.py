# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State
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
    html.Button('Submit', id='get_data'),

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
    [Input('location', 'value'), Input('get_data', 'n_clicks')])
def text_output(value, n_clicks):
    value = '' if value is None else value
    n_clicks = '' if n_clicks is None else str(n_clicks)
    return value + n_clicks

if __name__ == '__main__':
    app.run_server(debug=True)
