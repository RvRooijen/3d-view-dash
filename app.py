import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from flask import Flask
from flask_socketio import SocketIO, emit

# Initialize Flask and SocketIO
server = Flask(__name__)
socketio = SocketIO(server)

# Initialize Dash app
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout of the Dash app
app.layout = html.Div([
    dcc.Graph(id='3d-view'),
    html.Div(id='action-output')
])

# Callback to handle actions from the 3D view
@app.callback(
    Output('action-output', 'children'),
    [Input('3d-view', 'clickData')]
)
def display_click_data(clickData):
    if clickData is not None:
        return f'You clicked at: {clickData}'
    return 'Click on the 3D view to see data here.'

# SocketIO event to handle messages from the JavaScript application
@socketio.on('js_event')
def handle_js_event(data):
    print(f'Received event from JS: {data}')
    emit('dash_event', {'response': 'Event received'})

if __name__ == '__main__':
    socketio.run(server, debug=True)
