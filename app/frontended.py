# We use Blueprint class to initialize a blueprint.
# render_template for loading templates from
# templates/ folder.
from flask import Blueprint, render_template

# We use user_session for servered blueprint
from .servered import user_session

# Initializing the blueprint
# specifying templates and static folders
frontended = Blueprint(
    "frontended",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@frontended.route("/films")
def films():
    # Loads movies webpage
    return render_template("films.html", user_session=user_session)


@frontended.route("/rating")
def rating():
    # Loads movie ratings webpage
    return render_template("rating.html", user_session=user_session)


@frontended.route("/about")
def about():
    # Loads about webpage (it is about this project and my work on it)
    return render_template("about.html", user_session=user_session)
