from bottle import template, template, static_file
from utils.main import get_routes, get_trigger_functions, get_user_input, get_template, PY_EXT

def serve_static(file: str):
    return static_file(file, root='./static')

def main_view():
    return template("_home")

def xss_view(view, func):
    return lambda view=view, func=func: template(get_template(
        view[:PY_EXT], output=func(get_user_input())
    ))

def trigger_view(view, func):
    return lambda view=view, func=func: template(
        view[:PY_EXT], output=func(get_user_input())
    )
    
def add_trigger_routes(app):
    """
    Adds trigger routes., imports trigger modules and their functions,
    then creates routes for each trigger function.
    """
    trigger_routes = get_routes(PY_EXT)

    for trigger, view in trigger_routes.items():
        trigger_module = __import__(f'triggers.{trigger}', fromlist=['trigger'])

        trigger_functions: dict[str, function] = get_trigger_functions(trigger_module)

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
    root_routes = get_routes()
    for route, view in root_routes.items():
        app.route(f'/{route}', method=["GET", "POST"])(
            lambda view=view: template(view, output='')
        )    

def add_routes(app):
    app.route('/static/<file:path>', callback=serve_static)
    app.route('/', callback=main_view)
    
    add_root_routes(app)
    add_trigger_routes(app)
    # for route in app.routes:
    #     print(route.rule)