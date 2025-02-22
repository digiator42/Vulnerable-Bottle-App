from bottle import request
from config.settings import DEFAULT_LEVEL, MEDIUM_LEVEL, STRONG_LEVEL
import re

def trigger_ssti(input):
    session = request.environ.get('beaker.session')
    
    user_input = input.get('input')
    if session.get('level') == DEFAULT_LEVEL:
        return weak_ssti(user_input)
    
    elif session.get('level') == MEDIUM_LEVEL:
        return medium_ssti(user_input)
    
    elif session.get('level') == STRONG_LEVEL:
        return strong_ssti(user_input)
    
def weak_ssti(input: str):
    return input

def medium_ssti(input):
    
    substitutions = {
        '{': '&#123;',
        '}': '&#125;',
    }
    sanitized_input = input
    for key, value in substitutions.items():
        sanitized_input = re.sub(key, value, sanitized_input)
    return sanitized_input

def strong_ssti(input):
    # this is a built bottle function to escape html only
    # so by adding both it scaping the escape :)
    return '{{' + f'_escape("{input}")' + '}}'