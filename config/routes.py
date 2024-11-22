from pathlib import Path
from .settings import ROOT_DIR
from bottle import template, template, static_file, request

views_dir = Path(ROOT_DIR, 'views')
triggers_dir = Path(ROOT_DIR, 'triggers')
PY_EXT = -3
TPL_EXT = -4

def serve_static(file):
    return static_file(file, root='./static')

def main_view():
    return template("_home")

def _get_user_input(request):
    if request.method == "GET":
        return request.GET.get("command", "")
    return request.POST.get("command", "")

def _get_routes(ext: int=TPL_EXT):
    """
    Get all routes from the views directory
    `only` tpls which are not starting with underscore
    """
    files = views_dir.iterdir() if ext == TPL_EXT else triggers_dir.iterdir()
    view_files = [f.name for f in files if f.is_file()]
    routes = {file[:ext]: file for file in view_files if not file.startswith('_')}
    return routes

def add_routes(app):
    app.route('/static/<file:path>', callback=serve_static)
    app.route('/', callback=main_view)
    
    root_routes = _get_routes()

    for route, view in root_routes.items():
        app.route(f'/{route}', method=["GET", "POST"])(
            lambda view=view: template(view, output='output')
        )
    trigger_routes = _get_routes(PY_EXT)
    for trigger, view in trigger_routes.items():
        trigger_module = __import__(f'triggers.{trigger}', fromlist=['trigger'])
        app.route(f'/trigger/{trigger}', method=["GET", "POST"])(
            lambda trigger_module=trigger_module: trigger_module.trigger(_get_user_input(request))
        )
    # for route in app.routes:
    #     print(route.rule)
