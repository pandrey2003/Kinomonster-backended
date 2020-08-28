from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.mod_db import signingup
from app.mod_db.signingup import session, Members

from app.mod_db import signingin
from app.mod_db.signingin import user_session

from app.mod_db.reviews import gather_review

from app.mod_db.contact import contact_mail

servered = Blueprint(
    "servered",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@servered.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["review_name"]
        email = request.form["review_email"]
        contents = request.form["review_email"]
        contact_mail(name, email, contents)
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


@servered.route("/show/<name>", methods=["POST", "GET"])
def show(name):
    reviews = gather_review()
    return render_template(f"shows/{name}.html", user_session=user_session, reviews=reviews)
