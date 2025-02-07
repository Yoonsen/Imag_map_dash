import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Detect if we are running on Cloud Run
IS_CLOUD_RUN = "K_SERVICE" in os.environ

# Set pathname prefix (important for Cloud Run)
REQUEST_PREFIX = "/helloworld/" if IS_CLOUD_RUN else "/"

# Initialize Dash app
app = dash.Dash(
    __name__,
    requests_pathname_prefix=REQUEST_PREFIX,  # Ensures Dash assets load correctly
    serve_locally=False  # Forces Dash to serve static files correctly
)

# Enable reverse proxy settings for Cloud Run
app.server.use_x_forwarded_for = True

# Define Layout
app.layout = html.Div([
    html.H1("Hello, Cloud Run!"),
    html.P("This Dash app runs on Cloud Run."),
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

# Expose Flask server for Gunicorn
server = app.server

# Run locally (not in Cloud Run)
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
