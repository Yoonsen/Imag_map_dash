import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Read `SCRIPT_NAME` from environment
script_name = os.getenv("SCRIPT_NAME", "/")

# Ensure `SCRIPT_NAME` ends with `/`
if not script_name.endswith("/"):
    script_name += "/"

# Initialize Dash app
app = dash.Dash(
    __name__,
    requests_pathname_prefix=script_name,  # Ensures Dash assets load correctly
    routes_pathname_prefix=script_name,    # Ensures Dash routes internal API correctly
    serve_locally=False
)

# Define Layout
app.layout = html.Div([
    html.H1("Hello, Cloud Run!"),
    html.P(f"This Dash app runs on Cloud Run with prefix: {script_name}"),
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
        return f"Hello there! Who are you, {text}!"
    return "Waiting for input..."

server = app.server

# Run locally
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
