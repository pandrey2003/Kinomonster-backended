from flask import Blueprint, render_template, url_for

frontended = Blueprint(
    "frontended",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@frontended.route("/films")
def films():
    return render_template("films.jinja2")


@frontended.route("/serial")
def serial():
    return render_template("serial.jinja2")


@frontended.route("/rating")
def rating():
    return render_template("rating.jinja2")


@frontended.route("/interstellar")
def interstellar():
    return render_template("interstellar.jinja2")
