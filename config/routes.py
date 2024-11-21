from pathlib import Path
from .settings import ROOT_DIR
from bottle import template, template, static_file

views_dir = Path(ROOT_DIR, 'views')

def serve_static(file):
    return static_file(file, root='./static')

def main_view():
    return template("_home")

def _get_root_routes():
    """
    Get all routes from the views directory
    `only` tpls which are not starting with underscore
    """
    view_files = [f.name for f in views_dir.iterdir() if f.is_file()]
    routes = {file[:-4]: file for file in view_files if not file.startswith('_')}
    return routes

def add_routes(app):
    app.route('/static/<file:path>', callback=serve_static)
    app.route('/', callback=main_view)
    
    root_routes = _get_root_routes()

    for route, view in root_routes.items():
        app.route(f'/{route}', method=["GET", "POST"])(
            lambda view=view: template(view, output='output')
        )
