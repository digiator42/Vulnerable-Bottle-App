from bottle import Bottle, run, template, static_file
from config.settings import HOST, PORT, DEBUG, RELOADER
from utils.main import get_template

app = Bottle()

@app.route('/static/<file:path>')
def serve_static(file):
    return static_file(file, root='./static')

@app.route('/')
def main():
    return template("main")

@app.get('/cmd')
def cmd():
    return template("cmd_injection")

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)