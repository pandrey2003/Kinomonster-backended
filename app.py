from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/films")
def films():
    return render_template("films.html")


@app.route("/serial")
def serial():
    return render_template("serial.html")


@app.route("/rating")
def rating():
    return render_template("rating.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/show")
def show():
    return render_template("show.html")


if __name__ == "__main__":
    app.run(debug=True)
