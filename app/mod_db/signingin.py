from app.mod_db import session, Members
from flask import flash
from flask import session as user_session


def check_user(login, password):
    return bool(
        session.query(Members).filter(Members.login==login, Members.password==password).first()
    )


def signin(login, password):
    if check_user(login, password):
        user_session["logged_in"] = True
        user_session["username"] = login
        flash("Log in succeeded!", "js")
    else:
        user_session["logged_in"] = False
        flash("Wrong email or password.", "js")


def logout():
    user_session["logged_in"] = False
