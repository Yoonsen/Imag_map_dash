import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output




# Initialize Dash app with correct path prefixes
app = dash.Dash(
    __name__,
    serve_locally=True,
    requests_pathname_prefix='/helloworld/'
)
server = app.server

# Set up app layout
app.layout = html.Div([
    html.H1("Hello, Cloud Run!"),
    dcc.Input(id="input-text", type="text", placeholder="Enter text..."),
    html.Button("Submit", id="submit-btn", n_clicks=0),
    html.H3("You entered:"),
    html.Div(id="output-text")
])

# Define callback
@app.callback(
    Output("output-text", "children"),
    Input("submit-btn", "n_clicks"),
    Input("input-text", "value")
)
def update_output(n_clicks, text):
    if n_clicks > 0 and text:
        return f"Hello there! You are, {text}!"
    return "Waiting for input..."

# Run locally
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
