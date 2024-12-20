from bottle import request
from config.settings import DEFAULT_LEVEL, MEDIUM_LEVEL, STRONG_LEVEL
import re

def trigger_xss(input):
    session = request.environ.get('beaker.session')
    
    if session.get('level') == DEFAULT_LEVEL:
        return weak_xss(input)
    
    elif session.get('level') == MEDIUM_LEVEL:
        return medium_xss(input)
    
    elif session.get('level') == STRONG_LEVEL:
        return strong_xss(input)

def weak_xss(input):
    """
    This enables xss
    """
    
    return input.get('input')

def medium_xss(input):
    """
    This will disable script tag for medium level:
    """
    
    # match <script> tag | case insensitive
    return re.sub(r'(?i)<script.*?>', '', input.get('input'))

def strong_xss(input):
    """
    This will remove all possible XSS vectors by escaping special characters
    """
    substitutions = {
        # '<.*?>': '',
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#x27;',
        '/': '&#x2F;'
    }
    
    sanitized_input = input.get('input')
    for key, value in substitutions.items():
        sanitized_input = re.sub(key, value, sanitized_input)

    return sanitized_input
