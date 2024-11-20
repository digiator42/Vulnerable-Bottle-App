from bottle import Bottle, run, template

app = Bottle()

@app.route('/')
def hello():
    return template("<h1>Hello {{name}}!</h1>", name="World")

run(app, host='localhost', port=8080, reloader=True)