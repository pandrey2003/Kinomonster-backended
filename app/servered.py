from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.mod_db import signingup
from app.mod_db.signingup import session, Members

from app.mod_db import signingin
from app.mod_db.signingin import user_session

from app.mod_db.reviews import gather_review

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


@servered.route("/show/interstellar", methods=["POST", "GET"])
def interstellar():
    reviews = gather_review()
    return render_template("shows/interstellar.html", user_session=user_session, reviews=reviews)


@servered.route("/show/breaking_bad", methods=["POST", "GET"])
def breaking_bad():
    reviews = gather_review()
    return render_template("shows/breaking_bad.html", user_session=user_session, reviews=reviews)


@servered.route("/show/cloud_atlas", methods=["POST", "GET"])
def cloud_atlas():
    reviews = gather_review()
    return render_template("shows/cloud_atlas.html", user_session=user_session, reviews=reviews)


@servered.route("/show/mad_max", methods=["POST", "GET"])
def mad_max():
    reviews = gather_review()
    return render_template("shows/mad_max.html", user_session=user_session, reviews=reviews)


@servered.route("/show/matrix", methods=["POST", "GET"])
def matrix():
    reviews = gather_review()
    return render_template("shows/matrix.html", user_session=user_session, reviews=reviews)


@servered.route("/show/silicon_valley", methods=["POST", "GET"])
def silicon_valley():
    reviews = gather_review()
    return render_template("shows/silicon_valley.html", user_session=user_session, reviews=reviews)


@servered.route("/show/the_x-files", methods=["POST", "GET"])
def the_x_files():
    reviews = gather_review()
    return render_template("shows/the_x-files.html", user_session=user_session, reviews=reviews)


@servered.route("/show/walking_dead", methods=["POST", "GET"])
def walking_dead():
    reviews = gather_review()
    return render_template("shows/walking_dead.html", user_session=user_session, reviews=reviews)
