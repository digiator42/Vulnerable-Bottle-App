from typing import Callable, Dict
from bottle import (
    template, template, static_file, request,
    redirect, FileUpload
)
from utils.main import (
    get_routes, get_trigger_functions, get_user_input, 
    get_template, add_log, get_api_functions, PY_EXT
)
from utils.markdown_help import md
from bs4 import BeautifulSoup
from .login import login, logout
from .settings import DEFAULT_LEVEL, LEVELS
from importlib import import_module
import traceback

TRIGGER_ROUTES = get_routes(PY_EXT)
ROOT_ROUTES = get_routes()

def _render_template(view: str, func: Callable):
    """
    Renders a template with valid output of a trigger function.
    """
    level = request.environ.get('beaker.session')['level']
    user_input: Dict = get_user_input()

    if _valid_user_input(user_input):
        log_file = func.__name__.replace('trigger_', '')
        add_log(log_file, user_input)
        try:
            output = func(user_input)
        except Exception as e:
            traceback.print_exc()
            output = 'Error:' + str(e)
    else:
        output = ''
    
    return template(view[:PY_EXT], output=output, level=level)

def _valid_user_input(input: Dict):
    """
    Validates user input.
    """
    if input:
        for user_input in input.values():
            if isinstance(user_input, FileUpload):
                break
            valid_input = user_input.strip()
            if not valid_input:
                return False
        return True

    return False

def serve_static(file: str):
    return static_file(file, root='./static')

def serve_media(file):
    return static_file(file, root='./media')

def main_view():
    with open('./README.md', 'r') as f:
        html = md.render(f.read())
    
    temp = get_template('_home', instructions=html)
    # rm dashboard img
    soup = BeautifulSoup(temp, 'html.parser')
    img = soup.find('img')
    if img:
        img.decompose()
    return template(str(soup))

def routes_view():
    routes = [route.rule for route in request.app.routes]
    methods = [route.method for route in request.app.routes]

    return template("_routes", routes=zip(routes, methods))

def xss_ssti_view(view, func):
    """
    gets xss_ssti template and concatenate xss_ssti tag with user input,
    and trigger JS scripts
    """
    def get_xss_ssti_template():
        user_input = get_user_input()
        xss_ssti_output = ''
        if _valid_user_input(user_input):
            add_log(view[:PY_EXT], user_input)
            xss_ssti_output = func(user_input)
            
        xss_ssti_tag = f'<p>Hello <strong>{xss_ssti_output}</strong></p>'

        if view[:PY_EXT] == 'ssti':
            ssti_template = get_template(view[:PY_EXT])
            ssti_template += xss_ssti_tag
            return template(ssti_template)
        
        xss_ssti_output = BeautifulSoup(xss_ssti_tag, 'html.parser')
        xss_ssti_template = get_template(view[:PY_EXT])
        soup = BeautifulSoup(xss_ssti_template, 'html.parser')
        
        xss_ssti_form = soup.find('form')
        xss_ssti_form.insert_after(xss_ssti_output)
        return template(str(soup))
    
    return get_xss_ssti_template

def trigger_view(view, func):
    return lambda: _render_template(view, func)

def root_view(view):
    session = request.environ.get('beaker.session')
    if session:
        level = session.get('beaker.session')
    else:
        level = 'weak'
    return lambda view=view: template(view, output='', level=level)

def session_middleware():
    session = request.environ.get('beaker.session')

    if not request.path == '/login' and not request.path.startswith('/static'):
        user = 'logged_in' in session
        if not user:
            return redirect('/login')

    selected_level = request.query.get('level')
    if selected_level in LEVELS:
        session['level'] = selected_level
        session.save()

    if 'level' not in session:
        session['level'] = DEFAULT_LEVEL
        session.save()

def add_api_routes(app):
    api_module = import_module(f'config.api')
    api_functions: Dict[str, Callable] = get_api_functions(api_module)
    for name, func in api_functions.items():
        app.route(f'/api/{name}', callback=func)

def add_trigger_routes(app):
    """
    Adds trigger routes, imports trigger modules and their functions,
    then creates routes for each trigger function.
    """
    for trigger, view in TRIGGER_ROUTES.items():
        trigger_module = import_module(f'triggers.{trigger}')

        trigger_functions: Dict[str, Callable] = get_trigger_functions(trigger_module)

        for func_name, func in trigger_functions.items():
            route_path = f"/{trigger}/{func_name.replace('trigger_', '')}"
            if func_name == 'trigger_xss' or func_name == 'trigger_ssti':
                app.route(route_path, method=["GET", "POST"])(xss_ssti_view(view, func))
                continue
            app.route(route_path, method=["GET", "POST"])(trigger_view(view, func))
            
def add_root_routes(app):
    """
    Add routes for all views in the views directory.
    """
    for route, view in ROOT_ROUTES.items():
        app.route(f'/{route}', method=["GET"])(root_view(view))

def add_routes(app):
    """
    Adds all routes to the app.
    """
    app.route('/static/<file:path>', callback=serve_static)
    app.route('/media/<file:path>', callback=serve_media)
    app.route('/', callback=main_view)
    app.route('/routes', callback=routes_view)
    app.route('/login', method=['GET', 'POST'], callback=login)
    app.route('/logout', callback=logout)
    
    app.hook('before_request')(session_middleware)
    
    add_root_routes(app)
    add_trigger_routes(app)
    add_api_routes(app)