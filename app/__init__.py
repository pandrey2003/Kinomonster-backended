from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from .frontended import frontended
from .servered import servered

app = Flask(__name__)
app.config.from_object("config")

app.register_blueprint(frontended)
app.register_blueprint(servered)

db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template("index.jinja2")
