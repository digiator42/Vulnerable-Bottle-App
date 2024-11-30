from bottle import Bottle, run, request
from config.settings import HOST, PORT, DEBUG, RELOADER
from config.routes import add_routes
from triggers.sqli import create_admin_table
from beaker.middleware import SessionMiddleware
from config.settings import session_opts

app = Bottle()

add_routes(app)
create_admin_table()

@app.hook('before_request')
def check_level():
    if request.path.startswith('/trigger'):
        session = request.environ.get('beaker.session')
        selected_level = request.query.get('level')
        if selected_level:
            session['level'] = selected_level
            session.save()

app = SessionMiddleware(app, session_opts)

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)