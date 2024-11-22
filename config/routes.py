import re
import inspect
from pathlib import Path
from .settings import ROOT_DIR
from bottle import template, template, static_file, request

PY_EXT: int = -3
TPL_EXT: int = -4

def serve_static(file: str):
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
    views_dir = Path(ROOT_DIR, 'views')
    triggers_dir = Path(ROOT_DIR, 'triggers')
    
    files = views_dir.iterdir() if ext == TPL_EXT else triggers_dir.iterdir()
    view_files = [f.name for f in files if f.is_file()]
    routes = {file[:ext]: file for file in view_files if not file.startswith('_')}
    return routes

def get_trigger_functions(module):
    """
    Get all functions in a module that start with 'trigger_'.
    """
    trigger_pattern = re.compile(r"^trigger_")
    return {
        name: func
        for name, func in inspect.getmembers(module, inspect.isfunction)
        if trigger_pattern.match(name)
    }

def add_trigger_routes(app):
    """
    Adds trigger routes., imports trigger modules and their functions,
    then creates routes for each trigger function.
    """
    trigger_routes = _get_routes(PY_EXT)
    # use view as tpl to return trigger result afterwords
    for trigger, view in trigger_routes.items():
        trigger_module = __import__(f'triggers.{trigger}', fromlist=['trigger'])

        trigger_functions: dict[str, function] = get_trigger_functions(trigger_module)

        for func_name, func in trigger_functions.items():
            route_path = f"/trigger/{trigger}/{func_name.replace('trigger_', '')}"
            print(f"Adding route: {route_path}")
            app.route(route_path, method=["GET", "POST"])(
                lambda func=func: func(_get_user_input(request))
            )

def add_root_routes(app):
    """
    Add routes for all views in the views directory.
    """
    root_routes = _get_routes()
    for route, view in root_routes.items():
        app.route(f'/{route}', method=["GET", "POST"])(
            lambda view=view: template(view, output='output')
        )    

def add_routes(app):
    app.route('/static/<file:path>', callback=serve_static)
    app.route('/', callback=main_view)
    
    add_root_routes(app)
    add_trigger_routes(app)