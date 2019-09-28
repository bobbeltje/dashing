# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output
from datetime import datetime as dt

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
        )
])

@app.callback(
    Output('typed_text', 'children'),
    [Input('location', 'value')]
    )
def text_output(t):
    return t

if __name__ == '__main__':
    app.run_server(debug=False)
