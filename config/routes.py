from pathlib import Path
from .settings import ROOT_DIR
from bottle import template

views_dir = Path(ROOT_DIR, 'views')

def get_root_routes():
    view_files = [f.name for f in views_dir.iterdir() if f.is_file()]
    routes = {file[:-4]: file for file in view_files if file.endswith('.tpl')}
    return routes

def add_routes(app):
    root_routes = get_root_routes()
    for route, view in root_routes.items():
        app.route(f'/{route}', method=["GET", "POST"])(lambda view=view: template(view, output='output'))
