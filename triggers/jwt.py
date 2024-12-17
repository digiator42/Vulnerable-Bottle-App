import base64
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL, KEY
from config.login import USERS
from typing import Dict
import json
from bottle import request
import jwt

def trigger_jwt(input: Dict):
    
    level = request.environ.get('beaker.session')['level']
    
    if level == MEDIUM_LEVEL:
        return medium_jwt(input)
    else:
        return weak_jwt(input)

def weak_jwt(input: Dict):
    _, password, jwt_token = [value for value in input.values()]
    
    if jwt_token:
        decoded_payload = weak_decode_jwt(jwt_token)
        
        if decoded_payload and 'username' in decoded_payload:
            jwt_username = decoded_payload['username']
            
            if jwt_username in USERS and USERS[jwt_username] == password:
                return f'Logged in as {jwt_username} (using JWT)'
            return 'Invalid login', 401

    return 'Invalid jwt'

def weak_decode_jwt(jwt):
    try:
        _, payload, _ = jwt.split(".")
        
        # Decode the payload
        decoded_payload = base64.urlsafe_b64decode(payload + "==").decode("utf-8")
        
        return json.loads(decoded_payload)
    except Exception as _:
        return None
    
def medium_jwt(input: Dict):
    _, password, jwt_token = [value for value in input.values()]

    if jwt_token:
        decoded_payload = medium_decode_jwt(jwt_token)
        if decoded_payload == 'Token has expired':
            return 'Token has expired, login again'

        if decoded_payload and 'username' in decoded_payload:
            jwt_username = decoded_payload.get('username')
        
            if jwt_username in USERS and USERS[jwt_username] == password:
                return f'Logged in as {jwt_username} (using JWT)'
        return 'Invalid login', 401

    return 'Invalid jwt'
    
def medium_decode_jwt(jwt_token):
    try:
        unverified_header = jwt.get_unverified_header(jwt_token)
        
        if unverified_header.get('alg') == 'none':
            payload = jwt.decode(jwt_token, options={'verify_signature': False})
            return payload
        else:
            # Verify signature for algorithms
            payload = jwt.decode(jwt_token, KEY, algorithms=['HS256'])
            return payload
    except jwt.ExpiredSignatureError as e:
        print(e)
        return 'Token has expired'
    except jwt.InvalidTokenError as e:
        print(e)
        return 'Invalid token'