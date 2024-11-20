from bottle import Bottle, run, template, static_file
from config.settings import HOST, PORT, DEBUG
from utils.main import get_template

app = Bottle()

@app.route('/static/<file:path>')
def serve_static(file):
    return static_file(file, root='./static')

@app.route('/')
def main():
    return template(get_template("base.html"))

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, reloader=DEBUG)