from flask import Blueprint, render_template, request, flash

import app.mod_db.signingup as signingup
from app.mod_db.signingup import session, Members

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

        signingup.sign_up(
            email=new_email,
            login=new_login,
            password=new_password
        )
    return render_template("signup.html")


@servered.route("/forgot")
def forgot():
    return render_template("forgot.html")
