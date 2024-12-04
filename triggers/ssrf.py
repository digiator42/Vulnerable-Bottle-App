from bottle import request
import requests

def trigger_ssrf():
    url = request.query.url
    
    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)