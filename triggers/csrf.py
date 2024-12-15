from typing import Dict
import sqlite3
from bottle import request
from config.settings import DEFAULT_LEVEL, MEDIUM_LEVEL, STRONG_LEVEL
import hashlib


def trigger_csrf(input: Dict):
    session = request.environ.get('beaker.session')    
    level = session['level']
    
    if level == DEFAULT_LEVEL:
        return weak_csrf(input)
    
    elif level == MEDIUM_LEVEL:
        return medium_csrf(input)
    
    elif level == STRONG_LEVEL:
        return strong_csrf(input)
    
def weak_csrf(input):
    return _exec_csrf(input)

def medium_csrf(input: Dict):

    csrf_token = input['csrf_token']
    
    referer = request.headers.get('Referer')
    # e.g http://localhost:8080
    current_domain = "http://" + request.urlparts.netloc

    if not referer.startswith(current_domain):
        return "Invalid Rquest"
    
    session = request.environ.get('beaker.session')
    if csrf_token != generate_csrf_token(session['username']):
        return "CSRF token invalid"
    
    return _exec_csrf(input)
    
def strong_csrf(input: Dict):
    csrf_token = input['csrf_token']
    session = request.environ.get('beaker.session')
    
    if csrf_token != session['csrf_token']:
        return "CSRF token invalid"
    
    return _exec_csrf(input)

def _exec_csrf(input):
    amount = input['amount']
    recipient = input['recipient']
    session = request.environ.get('beaker.session')
    
    with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            
            cursor.execute("SELECT balance FROM users WHERE username = ? ", (session['username'],))
            
            balance = cursor.fetchone()
            new_balance = balance[0] - int(amount)
            
            cursor.execute("UPDATE users SET balance = ? WHERE username = ?", (new_balance, session['username']))
        
    return f'Transferred {amount} to {recipient}, balance {new_balance}'

def generate_csrf_token(username):
    return hashlib.md5(username.encode()).hexdigest()