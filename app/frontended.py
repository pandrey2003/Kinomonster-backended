from flask import Blueprint, render_template

frontended = Blueprint(
    "frontended",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@frontended.route("/films")
def films():
    return render_template("films.html")


@frontended.route("/serial")
def serial():
    return render_template("serial.html")


@frontended.route("/rating")
def rating():
    return render_template("rating.html")


@frontended.route("/interstellar")
def interstellar():
    return render_template("interstellar.html")
