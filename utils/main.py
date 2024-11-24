import re
import inspect
from pathlib import Path
from config.settings import ROOT_DIR
from bottle import request

PY_EXT: int = -3
TPL_EXT: int = -4

input = [
    'username', 'command', 'input', 'data', 'amount', 
    'path', 'requests', 'filepath', 'file', 'url'
]

def get_template(template_name, **kwargs):
    """
    Reads a template file and formats it with the provided keyword arguments.
    Args:
        template_name (str): The name of the template file to read.
        **kwargs: Arbitrary keyword arguments to format the template.
    Returns:
        str: The formatted template string.
    Raises:
        FileNotFoundError: If the template file does not exist.
        KeyError: If a placeholder in the template is not provided in kwargs.
    """
    
    with open(f"views/{template_name}.tpl") as f:
        template = f.read()
    return template.format(**kwargs)

def get_user_input():
    for usr_input in input:
        if request.GET.get(usr_input):
            return request.GET.get(usr_input)
        if request.POST.get(usr_input):
            return request.POST.get(usr_input)

def get_routes(ext: int=TPL_EXT):
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


print(get_template("xss", output='<script>alert(1)</script>')) # _home.tpl