#!/usr/bin/env python3

import pickle

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from trace import TraceStep

trace = pickle.load(open('trace.pick', 'rb'))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash('introspector', external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.H1('Hello'),
    dcc.Input(id='filter-input', value='', type='text'),
    html.Ul(id='trace-list')
])


@app.callback(
    Output(component_id='trace-list', component_property='children'),
    [Input(component_id='filter-input', component_property='value')]
)
def update_list(filter):
    return [html.Li(step.msg) for step in trace if filter in step.msg]


def main():
    app.run_server(debug=True)


if __name__ == '__main__':
    main()
