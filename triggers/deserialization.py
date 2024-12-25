import pickle
import ast
from typing import Dict
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL
from bottle import request
import json

def trigger_deserialization(serialized_input: Dict):
    level = request.environ.get('beaker.session')['level']    
    
    if level == MEDIUM_LEVEL:
        return medium_deserialization(serialized_input)
    elif level == STRONG_LEVEL:
        return strong_deserialization(serialized_input)
    else:
        return weak_deserialization(serialized_input)

def weak_deserialization(serialized_input):
    byte_str = serialized_input['input']
    
    # convert string to into bytes
    try:
        byte_data = ast.literal_eval(byte_str)
    except (ValueError, SyntaxError) as e:
        return f"Invalid input format: {e}"

    # Now we have the actual bytes data to be serialized
    try:
        return pickle.loads(byte_data)
    except Exception as e:
        return f"Deserialization failed: {e}"
    
    
def medium_deserialization(serialized_input):
    byte_str = serialized_input['input']
    
    # convert string to into bytes
    try:
        byte_data = ast.literal_eval(byte_str)
    except (ValueError, SyntaxError) as e:
        return f"Invalid input format: {e}"

    try:
        obj = pickle.loads(byte_data)
        
        if not isinstance(obj, dict):
            return "Invalid data"
        return obj
    except Exception as e:
        return f"Deserialization failed: {e}"
    
def strong_deserialization(serialized_input):
    try:
        # Safely deserialize data with json
        obj = json.loads(serialized_input)
        if not isinstance(obj, dict):
            return "Invalid data"
        return obj
    except Exception as e:
        return f"Deserialization failed: {e}"