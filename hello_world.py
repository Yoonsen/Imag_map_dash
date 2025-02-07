import dash
from dash import html

app = dash.Dash(
    __name__,
    serve_locally=True,
    requests_pathname_prefix='/helloworld/',
    assets_folder='assets',  # Add this
    assets_url_path='/helloworld/assets'  # And this
)

server = app.server

app.layout = html.Div([
    html.H1("Hello, Cloud Run!")
])