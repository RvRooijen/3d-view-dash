import dash
from dash import html
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
    html.Button('Click Me', id='action-button'),
    html.Div(id='action-output')
])

# Callback to handle button click event
@app.callback(
    Output('action-output', 'children'),
    [Input('action-button', 'n_clicks')]
)
def handle_button_click(n_clicks):
    if n_clicks is not None:
        socketio.emit('dash_event', {'message': 'Button clicked!'})
        return f'Button clicked {n_clicks} times.'
    return 'Click the button to see data here.'

# SocketIO event to handle messages from the JavaScript application
@socketio.on('js_event')
def handle_js_event(data):
    print(f'Received event from JS: {data}')

if __name__ == '__main__':
    socketio.run(server, debug=True)
