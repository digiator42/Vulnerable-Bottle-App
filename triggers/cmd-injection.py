import subprocess
from config.settings import DEFAULT_LEVEL, MEDIUM_LEVEL, STRONG_LEVEL
from bottle import request
from typing import Dict

def trigger_cmd_injection(user_input: Dict):
    session = request.environ.get('beaker.session')
    
    if session.get('level') == DEFAULT_LEVEL:
        return weak_cmd_injection(user_input)
    
    elif session.get('level') == MEDIUM_LEVEL:
        return medium_cmd_injection(user_input)
    
    elif session.get('level') == STRONG_LEVEL:
        return strong_cmd_injection(user_input)
    
def weak_cmd_injection(user_input):
    return _exec_cmd_injection(user_input, show_result=True)
    
def medium_cmd_injection(user_input):
    """
    Medium level of cmd injection
    """
    bad_chars = [';', '&', '|']
    cleared_input: str = user_input['input']

    if not cleared_input.startswith('ping'):
        return f'Invalid {cleared_input}'
    
    for char in bad_chars:
        cleared_input = cleared_input.replace(char, '')

    return _exec_cmd_injection({'input': cleared_input},  show_result=True)

def strong_cmd_injection(user_input):
    """
    Strong level of cmd injection
    """
    bad_chars = [
        ';', '&', '|', '&&', '||', '`', '$(', '<', '>', '>>', '<<', '*', '?', 
        '[', ']', '{', '}', '\\', '\n', '\r'
    ]
    
    input = user_input['input']

    if not input.startswith('ping'):
        return
    
    for char in bad_chars:
        if char in input:
            return 'Invalid cmd'

    return _exec_cmd_injection({'input': input})

def _exec_cmd_injection(user_input, show_result=False):
    try:
        result = subprocess.run(user_input['input'], shell=True, check=True, \
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        return result.stdout or result.stderr
    except subprocess.CalledProcessError as e:
        if show_result:
            return e.stdout or e.stderr