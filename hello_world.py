import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Hello, World!"),
    html.P("This is a simple Dash app."),
    dcc.Input(id="input-text", type="text", placeholder="Enter text..."),
    html.Button("Submit", id="submit-btn", n_clicks=0),
    html.H3("You entered:"),
    html.Div(id="output-text")
])

# Define the callback to update output
@app.callback(
    Output("output-text", "children"),
    Input("submit-btn", "n_clicks"),
    Input("input-text", "value")
)
def update_output(n_clicks, text):
    if n_clicks > 0 and text:
        return f"Hello there! Who are you {text}!"
    return "Waiting for input..."


server = app.server

# Run the app
if __name__ == "__main__":

    app.run_server(host="0.0.0.0", port=8050, debug=True)
