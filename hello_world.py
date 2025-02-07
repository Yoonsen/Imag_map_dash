import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize Dash app **without manually setting pathname prefixes**
app = dash.Dash(__name__, serve_locally=False)

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

server = app.server

# Run locally
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
