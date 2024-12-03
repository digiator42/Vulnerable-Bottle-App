from bottle import request
from config.settings import DEFAULT_LEVEL, MEDIUM_LEVEL

def trigger_xss(user_input):
    session = request.environ.get('beaker.session')
    
    if session.get('level') == DEFAULT_LEVEL:
        return user_input
    elif session.get('level') == MEDIUM_LEVEL:
        return medium_xss(user_input)

def medium_xss(input):
    return input['input'].replace('<script>', '')