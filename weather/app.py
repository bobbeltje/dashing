# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State
from datetime import datetime as dt

import pandas as pd
import random

class Weather():
    def __init__(self):
        self.d = pd.DataFrame({
			'x': range(24), 
			'y': [10,9,8,7.5,6.6,7,8.8,9,10,12,15,16,
				18,21,22,22,21.5,20,20,19.6,18.4,17,17,12]
		})

    def set_data(self, d):
        self.d = d
        
    def get_data(self):
        return self.d
        
w = Weather()

app = dash.Dash(__name__)

app.layout = html.Div(children=[

    html.Button('Plot update', id='tst_button'),
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
    dcc.Graph(id='plot', style={'width': '800px'})
])

@app.callback(
    Output('plot', 'figure'),
    [Input('tst_button', 'n_clicks')]
)
def plot_weather(n_clicks):
    global w
    df = w.get_data()
    df.iat[0, 1] = df.iat[0, 1] + 1
    w.set_data(df)
    p = {
        'data': [
            {'x': df.x, 'y': df.y, 'type':'scatter', 'mode':'marker+lines'}
		],
        'layout': {
            'title': 'Temperature in Basel',
            'yaxis': {'title': 'Temperature'},
            'xaxis': {'title': 'Time'}
		}
	}
        
    return p

@app.callback(
    Output('typed_text', 'children'),
    [Input('location', 'value'), Input('get_data', 'n_clicks')])
def text_output(value, n_clicks):
    value = '' if value is None else value
    n_clicks = '' if n_clicks is None else str(n_clicks)
    return value + n_clicks

if __name__ == '__main__':
    app.run_server(debug=True)
