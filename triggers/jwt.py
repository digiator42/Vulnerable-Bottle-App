import base64
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL, KEY
from config.login import USERS
from typing import Dict
import json
from bottle import request
import jwt
from config.login import verify_user

def trigger_jwt(input: Dict):
    
    level = request.environ.get('beaker.session')['level']
    
    if level == STRONG_LEVEL:
        return strong_jwt(input)
    if level == MEDIUM_LEVEL:
        return medium_jwt(input)
    else:
        return weak_jwt(input)

def weak_jwt(input: Dict):
    password, jwt_token = [value for value in input.values()]
    
    if jwt_token:
        decoded_payload = weak_decode_jwt(jwt_token)
        
        if decoded_payload and 'username' in decoded_payload:
            jwt_username = decoded_payload['username']
            
            if verify_user(jwt_username, password):
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
    password = input.get('password')
    jwt_token = input.get('jwt')

    if jwt_token:
        decoded_payload = medium_decode_jwt(jwt_token)
        
        # Incase of exception
        if isinstance(decoded_payload, str) and decoded_payload.startswith('Error'):
            return decoded_payload
        # Is it valid payload
        if decoded_payload and 'username' in decoded_payload:
            jwt_username = decoded_payload.get('username')
        
            if verify_user(jwt_username, password):
                return f'Logged in as {jwt_username} (using JWT)'
            return 'Wrong credentials'
        
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
        return 'Error: Token has expired, login again'
    except jwt.InvalidTokenError as e:
        print(e)
        return 'Error: Invalid token'
    except jwt.InvalidAlgorithmError:
        print(e)
        return 'Error: Invalid algorithm'
    except Exception as e:
        print(e)
        return f'Invalid JWT'
    
def strong_jwt(input: Dict):
    password = input.get('password')
    jwt_token = input.get('jwt')

    try:
        if jwt_token:
            # can be enhance with iat
            decoded_payload = jwt.decode(jwt_token, KEY, algorithms=['HS256'], options={'require': ['exp']})

            if decoded_payload and 'username' in decoded_payload:
                jwt_username = decoded_payload.get('username')
        
            if verify_user(jwt_username, password):
                return f'Logged in as {jwt_username} (using JWT)'
            
            return 'Wrong credentials'
        return 'Invalid JWT'
        
    except jwt.ExpiredSignatureError as e:
        return 'Token has expired, login again'
    except Exception as e:
        return f'Invalid Jwt'
