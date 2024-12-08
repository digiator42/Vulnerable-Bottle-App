import os
import subprocess
from config.settings import DEFAULT_LEVEL, MEDIUM_LEVEL, STRONG_LEVEL
from bottle import request
from typing import Dict

def trigger_cmd(user_input: Dict):
    os.system(user_input['input'])
    return user_input

def trigger_subprocess_cmd(user_input: Dict):
    session = request.environ.get('beaker.session')
    
    if session.get('level') == DEFAULT_LEVEL:
        return _exec_subprocess_cmd(user_input, show_result=True)
    
    elif session.get('level') == MEDIUM_LEVEL:
        return medium_subprocess_cmd(user_input)
    
    elif session.get('level') == STRONG_LEVEL:
        return strong_subprocess_cmd(user_input)
        
    
def medium_cmd():
    """
    test code api
    """
    pass

def medium_subprocess_cmd(user_input):
    """
    Medium level of cmd injection
    """
    bad_chars = [';', '&']
    cleared_input: str = user_input['input']

    if not cleared_input.startswith('ping'):
        return f'Invalid {cleared_input}'
    
    for char in bad_chars:
        cleared_input = cleared_input.replace(char, '')

    return _exec_subprocess_cmd({'input': cleared_input},  show_result=True)

def strong_subprocess_cmd(user_input):
    """
    High level of cmd injection
    """
    bad_chars = [';', '&', '|']
    cleared_input = user_input['input']

    if not cleared_input.startswith('ping'):
        return
        
    for char in bad_chars:
        cleared_input = cleared_input.replace(char, '')

    return _exec_subprocess_cmd({'input': cleared_input})

def _exec_subprocess_cmd(user_input, show_result=False):
    try:
        result = subprocess.run(user_input['input'], shell=True, check=True, \
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        return result.stdout or result.stderr
    except subprocess.CalledProcessError as e:
        if show_result:
            return e.stdout or e.stderr