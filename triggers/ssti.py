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
    
def weak_ssti(input):
    return input

def medium_ssti(input):
    return "works"

def strong_ssti(input):
    return "works"