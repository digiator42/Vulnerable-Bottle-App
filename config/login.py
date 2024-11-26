from bottle import request, redirect, template, route

USERS = {
    'admin': 'password123',
    'user1': 'mypassword'
}

def login_required(func):
    def wrapper(*args, **kwargs):
        session = request.environ.get('beaker.session')
        print("----------> ", session)
        if not session:
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper