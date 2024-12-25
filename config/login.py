from bottle import request, redirect, request, template, response
from .settings import DEFAULT_LEVEL, KEY
from utils.main import add_crypto_user
import jwt
from datetime import datetime, timedelta, timezone
import sqlite3
import hashlib


USERS = {
    'admin': 'password123',
    'user1': 'mypassword'
}

def generate_jwt_token():
    username = request.environ.get('beaker.session')['username']
    
    payload = {
        'username': username,
        'exp': datetime.now(timezone.utc) + timedelta(hours=1)
    }
    
    jwt_token = jwt.encode(payload, KEY, algorithm='HS256')
    request.environ['beaker.session']['jwt_token'] = jwt_token

def verify_user(username, password):
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        # Absense of username
        if not row:
            set_error_msg('username')
            return False
        # Pass
        stored_pass = row[2]
        
    if username == 'eve':
        if stored_pass and stored_pass == hashlib.sha1(password.encode()).hexdigest():
            return True
    else:
        if stored_pass and stored_pass == hashlib.md5(password.encode()).hexdigest():
            return True
        
    set_error_msg('password')
    return False
        
def set_error_msg(keyword: str):
    session = request.environ.get('beaker.session')
    level = session.get('level')
    global FAIL_LOGIN_MSG
    
    if level and level == DEFAULT_LEVEL:
        FAIL_LOGIN_MSG = f"Invalid {keyword}, Please try again"
    else:
        FAIL_LOGIN_MSG = "Invalid credentials. Please try again."
    
def login():
    if request.environ.get('beaker.session').get('logged_in'):
        return redirect('/')
    if request.method == 'POST':
        username = request.forms.get('username')
        password = request.forms.get('password')
        # Is is valid user
        if verify_user(username, password):
            request.environ['beaker.session']['logged_in'] = True
            request.environ['beaker.session']['username'] = username
            response.set_cookie('vbausername', username)
            # for crypto vulnerability
            add_crypto_user()
            # only for jwt vulnerabilty
            generate_jwt_token()
            return redirect('/')
        # Nope
        return template('_login', output=FAIL_LOGIN_MSG)
    
    # Display login page
    return template('_login', output='')

def logout():
    session = request.environ['beaker.session']

    del session['username']
    del session['logged_in']
    
    # Since it's vulnerable, deleting session is not needed in order to 
    # display weak_msg and good_msg
    # session.delete()

    response.set_cookie('session_id', '', expires=0)

    return redirect('/login')