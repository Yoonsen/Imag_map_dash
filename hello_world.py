import dash
from dash import html

print("Starting app initialization...")

app = dash.Dash(
    __name__,  # Fixed syntax
    serve_locally=True,
    requests_pathname_prefix='/helloworld/',
    assets_folder='assets',
    assets_url_path='/helloworld/assets'
)
print("App initialized")

server = app.server

@server.before_request
def log_request():
    print("Request received!")

app.layout = html.Div([
    html.H1("Hello, Cloud Run!")
])