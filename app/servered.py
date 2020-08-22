from flask import Blueprint, render_template, url_for

servered = Blueprint(
    "servered",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@servered.route("/contact")
def contact():
    return render_template("contact.jinja2")


@servered.route("/signup")
def signup():
    return render_template("signup.jinja2")


@servered.route("/forgot")
def forgot():
    return render_template("forgot.jinja2")
