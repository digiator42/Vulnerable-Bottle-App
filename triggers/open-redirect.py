from bottle import redirect
from typing import Dict
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL
from bottle import request
from urllib.parse import urlparse

ALLOWED_DOMAIN = "portswigger.net"

def trigger_open_redirect(input: Dict):
    security_level = request.environ.get('beaker.session')['level']
    
    if security_level == MEDIUM_LEVEL:
        return medium_open_redirect(input)
    
    elif security_level == STRONG_LEVEL:
        return strong_open_redirect(input)
    
    else:
        return weak_open_redirect(input)
    
def weak_open_redirect(input: Dict):
    return redirect(input.get('input'))

def medium_open_redirect(input: Dict):
    url = input.get('input')
    
    parsed_url = urlparse(url)

    if ALLOWED_DOMAIN in parsed_url.netloc and parsed_url.scheme in ["http", "https"]:
        return redirect(url)

    return "Invalid redirect URL"

def strong_open_redirect(input: Dict):
    url = input.get('input')
    
    parsed_url = urlparse(url)

    if parsed_url.netloc == ALLOWED_DOMAIN and parsed_url.scheme in ["http", "https"]:
        if not parsed_url.path or parsed_url.path == "/":
            return redirect(url)

    return "Invalid redirect URL"
