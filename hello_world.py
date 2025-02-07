import dash
from dash import html

app = dash.Dash(
    __name__,
    serve_locally=True,
    requests_pathname_prefix='/helloworld/',
    assets_external_path='/helloworld/assets/'  # Add this
)

server = app.server

app.layout = html.Div([
    html.H1("Hello, Cloud Run!")
])