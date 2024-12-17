from bottle import request, redirect, request, template, response
from .settings import DEFAULT_LEVEL, KEY
from utils.main import add_crypto_user
import jwt
from datetime import datetime, timedelta


USERS = {
    'admin': 'password123',
    'user1': 'mypassword'
}

def generate_jwt_token():
    username = request.environ.get('beaker.session')['username']
    
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    
    jwt_token = jwt.encode(payload, KEY, algorithm='HS256')
    request.environ['beaker.session']['jwt_token'] = jwt_token
    print('---------------> >>> ', jwt_token)
    
def login():
    if request.environ.get('beaker.session').get('logged_in'):
        return redirect('/')
    if request.method == 'POST':
        username = request.forms.get('username')
        password = request.forms.get('password')
        if username in USERS and USERS[username] == password:
            request.environ['beaker.session']['logged_in'] = True
            request.environ['beaker.session']['username'] = username
            response.set_cookie('session_id', request.environ['beaker.session'].id)
            # for crypto vulnerability
            add_crypto_user()
            # only for jwt vulnerabilty
            generate_jwt_token()
            
            return redirect('/')
        else:
            session = request.environ.get('beaker.session')
            level = session.get('level')
                            
            if level and level == DEFAULT_LEVEL:
                if username in USERS:
                    weak_msg = "Invalid password, Please try again"
                else:
                    weak_msg = "Invalid username, Please try again"
                msg = weak_msg
            else:
                good_msg = "Invalid credentials. Please try again."
                msg = good_msg
            
            return template("_login", output=msg)
    
    return template('_login', output="")

def logout():
    session = request.environ['beaker.session']

    del session['username']
    del session['logged_in']
    
    # Since it's vulnerable, deleting session is not needed in order to 
    # display weak_msg and good_msg
    # session.delete()

    response.set_cookie('session_id', '', expires=0)

    return redirect('/login')