from bottle import Bottle, run, template
from config.settings import HOST, PORT, DEBUG
from utils.main import get_template

app = Bottle()

@app.route('/')
def main():
    return template(get_template("cmd_injection.html"), name="World")

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, reloader=DEBUG)