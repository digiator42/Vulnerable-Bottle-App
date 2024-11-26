from bottle import Bottle, run, redirect, request, template, response
from config.settings import HOST, PORT, DEBUG, RELOADER
from config.routes import add_routes
from triggers.sqli import create_admin_table
from bottle_session import SessionPlugin
from config.login import USERS
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'file',
    'session.data_dir': './data',
    'session.auto': True,
}

app = Bottle()

add_routes(app)
create_admin_table()

@app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.forms.get('username')
        password = request.forms.get('password')
        if username in USERS and USERS[username] == password:
            request.environ['beaker.session']['username'] = username
            return redirect('/')
        else:
            return "Invalid credentials. Please try again."
    return template("""<form action="/login" method="post">
                        Username: <input name="username" type="text" /><br>
                        Password: <input name="password" type="password" /><br>
                        <input value="Login" type="submit" />
                    </form>""")

@app.route('/logout')
def logout():
    session = request.environ['beaker.session']
    session.delete()  # Deletes the session from the server-side

    # Manually clear the session cookie
    response.set_cookie('session_id', '', expires=0)  # This clears the session cookie

    return redirect('/login')

app = SessionMiddleware(app, session_opts)

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)