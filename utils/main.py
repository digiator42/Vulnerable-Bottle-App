import re
import inspect
from pathlib import Path
from config.settings import ROOT_DIR
from bottle import request, response
from config.settings import DEFAULT_LEVEL
import json

PY_EXT: int = -3
TPL_EXT: int = -4

email_injection = ['email', 'subject', 'message']

csrf = ['amount', 'recipient', 'csrf_token']

input = [
    'username', 'password', 'input', 'role',
]

input.extend(email_injection + csrf)

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
    try:
        with open(f"views/{template_name}.tpl") as f:
            template = f.read()
        return template.format(**kwargs)
    except (FileExistsError, KeyError) as e:
        print(e)

def get_user_input():
    """
    Get user input from the request object.
    """
    input_dict = {}
    for usr_input in input:
        if request.GET.get(usr_input):
            input_dict[usr_input] = request.GET.get(usr_input)
            
        if request.POST.get(usr_input):
            input_dict[usr_input] = request.POST.get(usr_input)
    
    return input_dict
def get_routes(ext: int=TPL_EXT):
    """
    Get all routes from the views, triggers directory
    `only` .tpl, .py which are not starting with underscore
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

def get_api_functions(module):
    """
    Get all functions in a api module.
    """
    return {
        name: func
        for name, func in inspect.getmembers(module, inspect.isfunction)
        if not name == 'template'
    }

def get_code_level_function(module, level):
    """
    Get requested code level source.
    """
    if level == DEFAULT_LEVEL:
        level = 'trigger'

    return {
        name: func
        for name, func in inspect.getmembers(module, inspect.isfunction)
        if name.startswith(f'{level}_')
    }

class JsonResponse:
    def __init__(self, data: dict, status: int = 200) -> None:
        """
        Initialize a JSON response using Bottle's response object.
        Args:
            data (dict): The data to be returned as JSON.
            status (int): The HTTP status code of the response.
        """
        self.data = data
        self.status = status

        response.content_type = 'application/json'
        response.status = self.status

    def render(self) -> str:
        """
        Converts the data to JSON format.
        Returns:
            str: JSON string.
        """
        return json.dumps(self.data)
    
    def __str__(self) -> str:
        """
        Representation of the HTTP response as a string.
        """
        return (
            f"HTTP/1.1 {self.status}\n"
            f"Content-Type: {response.content_type}\n\n"
            f"{self.render()}"
        )
        
def add_log(vuln, input):
    with open(f'./logs/{vuln}.log', 'a') as f:
        f.write(str(input) + '\n')