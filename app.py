from bottle import Bottle, run, template, static_file
from config.settings import HOST, PORT, DEBUG, RELOADER
from config.routes import add_routes

app = Bottle()

add_routes(app)

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)