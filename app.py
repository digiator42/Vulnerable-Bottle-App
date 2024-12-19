from bottle import Bottle, run
from config.settings import HOST, PORT, DEBUG, RELOADER
from config.routes import add_routes
from utils.main import create_database_tables
from beaker.middleware import SessionMiddleware
from config.settings import session_opts

app = Bottle()

add_routes(app)
create_database_tables()

app = SessionMiddleware(app, session_opts)

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)