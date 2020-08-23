from flask import Blueprint, render_template

servered = Blueprint(
    "servered",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@servered.route("/contact")
def contact():
    return render_template("contact.html")


@servered.route("/signup")
def signup():
    return render_template("signup.html")


@servered.route("/forgot")
def forgot():
    return render_template("forgot.html")
