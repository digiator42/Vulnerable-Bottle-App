import base64
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL
from config.login import USERS
from typing import Dict
import json
from bottle import request

def trigger_jwt(input: Dict):
    
    level = request.environ.get('beaker.session')['level']
    
    if level == MEDIUM_LEVEL:
        pass
    else:
        return weak_jwt(input)

def weak_jwt(input: Dict):
    username, password, jwt_token = [value for value in input.values()]
    
    if jwt_token:
        decoded_payload = weak_decode_jwt(jwt_token)
        
        if decoded_payload and 'username' in decoded_payload:
            username = decoded_payload['username']
            if username in USERS and USERS[username] == password:
                return f'Logged in as {username} (using JWT)'
            return 'invalid login', 401

    return 'invalid jwt'

def weak_decode_jwt(jwt):
    try:
        _, payload, _ = jwt.split(".")
        
        # Decode the payload
        decoded_payload = base64.urlsafe_b64decode(payload + "==").decode("utf-8")
        
        return json.loads(decoded_payload)
    except Exception as _:
        return None