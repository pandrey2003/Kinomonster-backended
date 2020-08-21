from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config_from_object("config")
db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template("index.jinja2")


@app.route("/films")
def films():
    return render_template("films.jinja2")


@app.route("/serial")
def serial():
    return render_template("serial.jinja2")


@app.route("/rating")
def rating():
    return render_template("rating.jinja2")


@app.route("/contact")
def contact():
    return render_template("contact.jinja2")


@app.route("/interstellar")
def interstellar():
    return render_template("interstellar.jinja2")


@app.route("/signup")
def signup():
    return render_template("signup.jinja2")


@app.route("/forgot")
def forgot():
    return render_template("forgot.jinja2")


if __name__ == "__main__":
    app.run(debug=True)
