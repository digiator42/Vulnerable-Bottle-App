import sqlite3
from typing import Dict
from config.settings import MEDIUM_LEVEL, STRONG_LEVEL
from bottle import request
import re


def trigger_sqli(input: Dict):
    
    session = request.environ.get('beaker.session')    
    security_level = session['level']
    
    if security_level == MEDIUM_LEVEL:
        return medium_sqli(input)
    elif security_level == STRONG_LEVEL:
        return strong_sqli(input)
    else:
        return weak_sqli(input)

def weak_sqli(input: Dict):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        
        query = f"SELECT * FROM users WHERE username = '{input['username']}';"

        try:
            cursor.execute(query)
        except sqlite3.OperationalError as e:
            return str(e)
        
        result = cursor.fetchall()
        
    return _exec_sqli(result)

def medium_sqli(input: Dict):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()

        query = f"SELECT * FROM users WHERE username = '{input['username']}' AND role = 'user';"

        try:
            cursor.execute(query)
        except Exception as e:
            return str(e)

        result = cursor.fetchall()

    return _exec_sqli(result)

def detect_sqli(input: Dict):
    # common SQL injections
    injection_patterns = [
        r"(--|\#)",
        r"('|\"|\bOR\b|\bAND\b)",
        r"(\bSELECT\b|\bUNION\b)",
    ]

    for pattern in injection_patterns:
        if re.search(pattern, input, re.IGNORECASE):
            return True
    return False

def strong_sqli(input: Dict):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()

        if detect_sqli(input['username']):
            return ""

        query = "SELECT * FROM users WHERE username = ? AND role = ?;"

        try:
            cursor.execute(query, (input['username'], input.get('role', 'user')))
        except sqlite3.OperationalError as e:
            return str(e)

        result = cursor.fetchall()

    return _exec_sqli(result)

def _exec_sqli(result):
    if result:
        if len(result) > 1:
            return result
        return f'username: {result[0][1]}'
    
    return ''