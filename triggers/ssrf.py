import requests
from typing import Dict
from urllib.parse import urlparse
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL, PORT
from bottle import request

allowed_domains = ["portswigger.net", "owassp.org", f'localhost:{PORT}']

def trigger_ssrf(input: Dict):
    level = request.environ.get('beaker.session')['level']

    if level == MEDIUM_LEVEL:
        return medium_ssrf(input)
    
    elif level == STRONG_LEVEL:
        return strong_ssrf(input)
    
    else:
        return weak_ssrf(input)
    
def weak_ssrf(input: Dict):
    return _exec_ssrf(input)

def _is_valid_url(url, allowed_domains):
    parsed = urlparse(url)

    if parsed.scheme not in ["http", "https"]:
        return False

    domain = parsed.netloc
    return any(domain.endswith(allowed) for allowed in allowed_domains)

def _exec_ssrf(input: Dict):
    url = input['input']

    try:
        response = requests.get(url, timeout=5)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error occurred: {e}"

def medium_ssrf(input: dict):
    url = input.get("input")

    if not _is_valid_url(url, allowed_domains):
        return "Invalid URL"
    return _exec_ssrf(input)

def strong_ssrf(input: dict):
    url = input.get('input')

    if not _is_valid_url(url, allowed_domains[:-1]):
        return "Invalid URL"

    local_ips = ["127.0.0.1", "localhost", "::1"]
    for ip in local_ips:
        if url.startswith(f"http://{ip}"):
            return "Access to local resources is forbidden"

    return _exec_ssrf(input)