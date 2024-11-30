from bottle import request, redirect, request, template, response

USERS = {
    'admin': 'password123',
    'user1': 'mypassword'
}

def login_required(func):
    def wrapper(*args, **kwargs):
        session = request.environ.get('beaker.session')

        user = 'logged_in' in session
        if not user:
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper

def login():
    if request.environ.get('beaker.session').get('logged_in'):
        return redirect('/')
    if request.method == 'POST':
        username = request.forms.get('username')
        password = request.forms.get('password')
        if username in USERS and USERS[username] == password:
            request.environ['beaker.session']['logged_in'] = True
            response.set_cookie('session_id', request.environ['beaker.session'].id)
            request.environ['beaker.session']['username'] = username
            return redirect('/')
        else:
            return template("_login", output="Invalid credentials. Please try again.")
    return template('_login', output="")

def logout():
    session = request.environ['beaker.session']
    session.delete()

    response.set_cookie('session_id', '', expires=0)

    return redirect('/login')