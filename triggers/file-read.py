from typing import Dict
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL
from bottle import request

def trigger_file_read(input: Dict):
    level = request.environ.get('beaker.session')['level']
        
    file_path = input['input']
    
    if level == MEDIUM_LEVEL:
        return medium_file_read(input)
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return str(e)

def medium_file_read(input: Dict):
    
    file_path = input['input']    

    try:
        with open('./logs/' + file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return str(e)
    
def strong_file_read(input: Dict):
    pass