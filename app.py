from bottle import Bottle, run, template, static_file
from config.settings import HOST, PORT, DEBUG, RELOADER
from config.routes import add_routes

app = Bottle()

add_routes(app)

@app.route('/static/<file:path>')
def serve_static(file):
    return static_file(file, root='./static')

@app.route('/')
def main():
    return template("main")

# for route in app.routes:
#     print(route)

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)