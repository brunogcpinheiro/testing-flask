from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, Flask"


@app.route("/<string:name>")
def greeting(name):
    name = name.capitalize()
    return f"Hello, {name}!"
