from bottle import Bottle, run, template, static_file
from config.settings import HOST, PORT, DEBUG, RELOADER
from config.routes import add_routes
from triggers.sqli import create_admin_table

app = Bottle()

add_routes(app)
create_admin_table()

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)