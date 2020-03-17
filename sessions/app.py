from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = False

notes = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("index.html", notes=notes)


if __name__ == "__main__":
    app.run(debug=True)
