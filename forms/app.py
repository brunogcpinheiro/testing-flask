from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user", methods=["GET", "POST"])
def created_user():
    if request.method == 'GET':
        return redirect(url_for('index'))
    else:
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        age = request.form.get("age")
        return render_template("created_user.html", first_name=first_name, last_name=last_name, age=age)
