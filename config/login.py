from bottle import request, redirect, request, template, response
from .settings import DEFAULT_LEVEL

USERS = {
    'admin': 'password123',
    'user1': 'mypassword'
}

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
            
            return redirect('/')
        else:
            session = request.environ.get('beaker.session')
            level = session.get('level')
                            
            if level and level == DEFAULT_LEVEL:
                if username in USERS:
                    weak_msg = "invalid password, Please try again"
                else:
                    weak_msg = "invalid username, Please try again"
                msg = weak_msg
            else:
                good_msg = "Invalid credentials. Please try again."
                msg = good_msg
            
            return template("_login", output=msg)
    
    return template('_login', output="")

def logout():
    session = request.environ['beaker.session']
    session['logged_in'] = False
    session['username'] = ''
    
    # Since it's vulnerable, deleting session is not needed in order to 
    # display weak_msg and good_msg
    # session.delete()

    response.set_cookie('session_id', '', expires=0)

    return redirect('/login')