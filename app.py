from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, Flask"


@app.route("/<string:name>")
def greeting(name):
    name = name.capitalize()
    return f"Hello, {name}!"


@app.route("/template")
def template():
    return render_template("index.html")
