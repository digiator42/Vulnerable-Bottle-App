from bottle import Bottle, run, redirect, request, template, response
from config.settings import HOST, PORT, DEBUG, RELOADER
from config.routes import add_routes
from triggers.sqli import create_admin_table
from config.login import USERS
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'file',
    'session.data_dir': './data',
    'session.auto': True,
    'session.cookie_expires': True,
}

app = Bottle()

add_routes(app)
create_admin_table()

@app.route('/login', method=['GET', 'POST'])
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
    return template('_login', output="", login_url=LOGIN_URL)

@app.route('/logout')
def logout():
    session = request.environ['beaker.session']
    session.delete()

    response.set_cookie('session_id', '', expires=0)

    return redirect('/login')

app = SessionMiddleware(app, session_opts)

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)