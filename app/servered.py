from flask import Blueprint, render_template, request

import app.mod_db.signup as signup
from app.mod_db.signup import db

servered = Blueprint(
    "servered",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@servered.route("/contact")
def contact():
    return render_template("contact.html")


@servered.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        new_login = request.form.get("new_login")
        new_email = request.form.get("new_email")
        new_password = request.form.get("new_password")

        if signup.check_login(new_login):
            status_email = signup.signup(
                email=new_email,
                login=new_login,
                password=new_password
            )
            return render_template(
            "signup.html",
            message=status_email
            )
        return render_template(
            "signup.html",
            message=f"Login {new_login} already exists."
        )
    return render_template("signup.html", message=None)


@servered.route("/forgot")
def forgot():
    return render_template("forgot.html")
