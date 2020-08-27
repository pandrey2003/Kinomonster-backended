from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.mod_db import signingup
from app.mod_db.signingup import session, Members

from app.mod_db import signingin
from app.mod_db.signingin import user_session

servered = Blueprint(
    "servered",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@servered.route("/contact")
def contact():
    return render_template("contact.html", user_session=user_session)


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
    return render_template("signup.html", user_session=user_session)


@servered.route("/server/signin", methods=["POST"])
def server_signin():
    login = request.form["login_field"]
    password = request.form["password_field"]
    signingin.signin(login, password)
    return redirect(url_for("home"))


@servered.route("/server/logout", methods=["POST"])
def server_logout():
    signingin.logout()
    return redirect(url_for("home"))


@servered.route("/forgot")
def forgot():
    return render_template("forgot.html", user_session=user_session)
