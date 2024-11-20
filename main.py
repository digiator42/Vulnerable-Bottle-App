from bottle import Bottle, run, template
from config.settings import HOST, PORT, DEBUG

app = Bottle()

@app.route('/')
def hello():
    return template("<h1>Hello {{name}}!</h1>", name="World")

run(app, host=HOST, port=PORT, reloader=DEBUG)