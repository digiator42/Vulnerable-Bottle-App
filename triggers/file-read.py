from typing import Dict
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL
from bottle import request
import os


def trigger_file_read(input: Dict):
    level = request.environ.get('beaker.session')['level']
    
    if level == MEDIUM_LEVEL:
        return medium_file_read(input)
    elif level == STRONG_LEVEL:
        return strong_file_read(input)
    else:
        return weak_file_read(input)

def weak_file_read(input: Dict):
    file_path = input.get('input')
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return str(e)

def medium_file_read(input: Dict):
   
    file_path = input.get('input')    

    try:
        with open('/var/www/' + file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return str(e)
    
def strong_file_read(input: Dict):
    base_dir = '/var/www/'
    requested_path = os.path.realpath(os.path.join(base_dir, input.get('input')))
    
    if not requested_path.startswith(base_dir):
        return "Access denied: Invalid file path"

    try:
        with open(requested_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return str(e)