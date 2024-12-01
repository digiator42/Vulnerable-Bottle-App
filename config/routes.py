from typing import Callable, Dict
from bottle import template, template, static_file, request, redirect
from utils.main import get_routes, get_trigger_functions, get_user_input, get_template, PY_EXT
from .login import login, logout
from .settings import DEFAULT_LEVEL


TRIGGER_ROUTES = get_routes(PY_EXT)
ROOT_ROUTES = get_routes()

def _render_template(view: str, func: Callable):
    """
    Renders a template with valid output of a trigger function.
    """
    user_input = get_user_input()
    if _valid_user_input(user_input):
        output = func(user_input)
    else:
        output = 'invalid input'
    return template(view[:PY_EXT], output=output)

def _valid_user_input(user_input: str):
    """
    Validates user input.
    """
    input = user_input.strip() if user_input else None
    if not input:
        return False
    return True

def serve_static(file: str):
    return static_file(file, root='./static')

def main_view():
    return template("_home", username=request.environ.get('beaker.session')['username'])

def xss_view(view, func):
    return lambda view=view, func=func: template(get_template(
        view[:PY_EXT], output=func(get_user_input())
    ))

def trigger_view(view, func):
    return lambda: _render_template(view, func)

def root_view(view):
    return lambda view=view: template(view, output='')

def session_middleware():
    session = request.environ.get('beaker.session')
    
    if not request.path.startswith('/login') and not request.path.startswith('/static'):
        user = 'logged_in' in session
        if not user:
            return redirect('/login')

    if selected_level := request.query.get('level'):
        session['level'] = selected_level
        session.save()
    if 'level' not in session:
        session['level'] = DEFAULT_LEVEL
        session.save()
    
def add_trigger_routes(app):
    """
    Adds trigger routes, imports trigger modules and their functions,
    then creates routes for each trigger function.
    """
    for trigger, view in TRIGGER_ROUTES.items():
        trigger_module = __import__(f'triggers.{trigger}', fromlist=['trigger'])

        trigger_functions: Dict[str, Callable] = get_trigger_functions(trigger_module)

        for func_name, func in trigger_functions.items():
            route_path = f"/trigger/{trigger}/{func_name.replace('trigger_', '')}"
            if func_name == 'trigger_xss':
                app.route(route_path, method=["GET", "POST"])(xss_view(view, func))
                continue
            app.route(route_path, method=["GET", "POST"])(trigger_view(view, func))
            
def add_root_routes(app):
    """
    Add routes for all views in the views directory.
    """
    for route, view in ROOT_ROUTES.items():
        app.route(f'/{route}', method=["GET", "POST"])(root_view(view))

def add_routes(app):
    """
    Adds all routes to the app.
    """
    app.route('/static/<file:path>', callback=serve_static)
    app.route('/', callback=main_view)
    app.route('/login', method=['GET', 'POST'], callback=login)
    app.route('/logout', callback=logout)
    
    app.hook('before_request')(session_middleware)
    
    add_root_routes(app)
    add_trigger_routes(app)
    # for route in app.routes:
    #     print(route.rule)