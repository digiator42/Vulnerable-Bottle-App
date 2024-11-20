from pathlib import Path
from .settings import ROOT_DIR
from bottle import template, template, static_file

views_dir = Path(ROOT_DIR, 'views')

def _serve_static(file):
    return static_file(file, root='./static')

def _main_view():
    return template("main")

def _get_root_routes():
    view_files = [f.name for f in views_dir.iterdir() if f.is_file()]
    routes = {file[:-4]: file for file in view_files if file.endswith('.tpl')}
    return routes

def add_routes(app):
    app.route('/static/<file:path>', callback=_serve_static)
    app.route('/', callback=_main_view)
    root_routes = _get_root_routes()
    for route, view in root_routes.items():
        app.route(f'/{route}', method=["GET", "POST"])(lambda view=view: template(view, output='output'))
