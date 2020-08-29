from flask import Blueprint, render_template

from .servered import user_session


frontended = Blueprint(
    "frontended",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@frontended.route("/films")
def films():
    return render_template("films.html", user_session=user_session)


@frontended.route("/serial")
def serial():
    return render_template("serial.html", user_session=user_session)


@frontended.route("/rating")
def rating():
    return render_template("rating.html", user_session=user_session)
