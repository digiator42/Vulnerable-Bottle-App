import re
import inspect
from pathlib import Path
from config.settings import ROOT_DIR
from bottle import request, response
from config.settings import KEY
import sqlite3
import json
import base64
import os
from cryptography.fernet import Fernet
from bcrypt import hashpw, gensalt

PY_EXT: int = -3
TPL_EXT: int = -4

csrf = ['amount', 'recipient', 'csrf_token']

input = [
    'username', 'password', 'input', 'role', 'jwt'
]

input.extend(csrf)

SECRET_KEY = """
eyJhZG1pbiI6eyJyb2xlIjoiYWRtaW4iLCJwYXNzd29yZCI6ImU4NWVlZTk2MjkwNzZiMTE4NDQ
5OTQ5ZjExNjJmYzdhIn0sImFsaWNlIjp7InJvbGUiOiJ1c2VyIiwicGFzc3dvcmQiOiIwNTcxNz
Q5ZTJhYzMzMGE3NDU1ODA5YzZiMGU3YWY5MCJ9LCJib2IiOnsicm9sZSI6InVzZXIiLCJwYXNzd
29yZCI6IjM4OTlkY2JhYjc5ZjkyYWY3MjdjMjE5MGJiZDhhYmM1In0sImNoYXJsaWUiOnsicm9s
ZSI6InVzZXIiLCJwYXNzd29yZCI6IjhhZmE4NDdmNTBhNzE2ZTY0OTMyZDk5NWM4ZTc0MzVhIn0
sImRhdmlkIjp7InJvbGUiOiJ1c2VyIiwicGFzc3dvcmQiOiIyNWY5ZTc5NDMyM2I0NTM4ODVmNT
E4MWYxYjYyNGQwYiJ9LCJldmUiOnsicm9sZSI6ImFkbWluIiwicGFzc3dvcmQiOiI1NGJmM2RjM
mM0Zjk4ZmFiZGY3OGI3MjE2YzBhZTg4ODQ1NWQwMDlhIn19============================
"""

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
        return template.format(**kwargs) or template
    except (FileExistsError, KeyError) as e:
        print(e)

def get_user_input():
    """
    Get user input from the request object.
    """
    input_dict = {}
    if request.json:
        input_dict = request.json
        return input_dict
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
    return {
        name: func
        for name, func in inspect.getmembers(module, inspect.isfunction)
        if name.startswith(f'{level}_') or name.startswith('_')
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
    os.makedirs('./logs', exist_ok=True)
    with open(f'./logs/{vuln}.log', 'a') as f:
        f.write(str(input) + '\n')

def get_data():
    decoded = base64.urlsafe_b64decode(SECRET_KEY.encode()).decode('utf-8')    
    return json.loads(decoded)

def create_database_tables():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
        )
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL,
                balance INTEGER DEFAULT 999999
            )
        ''')

        cursor.execute("SELECT * FROM users WHERE username = 'admin'")
        
        if cursor.fetchone() is None:
            for name, data in get_data().items():
                cursor.execute(
                    "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                    (name, data['password'], data['role'])
                )
        connection.commit()
    
def add_crypto_user():
    username = request.environ.get('beaker.session')['username']
    hex_pass = ('0x69', '0x63', '0x65', '0x63', '0x72', '0x65', '0x61', '0x6d')
    user_pass = ''.join(chr(int(x, 16)) for x in hex_pass)
    cipher_suite = Fernet(KEY)
    # Hash the user_pass
    bcrypt_hash = hashpw(user_pass.encode(), gensalt())
    # Encrypt the bcrypt hash with Fernet
    encrypted_hash = cipher_suite.encrypt(bcrypt_hash)
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users_hashed_pass (id INTEGER PRIMARY KEY, username TEXT, encrypted_password_hash TEXT)"
        )
        cursor.execute("SELECT * FROM users_hashed_pass WHERE username = ?", (username,))

        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO users_hashed_pass (username, encrypted_password_hash) VALUES (?, ?)",
                (username, encrypted_hash.decode())
            )
        connection.commit()