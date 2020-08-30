# We need session to interact with the db
# and Members to get users from this table
from app.mod_db import session, Members
# For interactive message
from flask import flash
# To set value for user_session
from flask import session as user_session


def check_user(login, password):
    # Check the user with such login and password exists
    # in the db
    return bool(
        session.query(Members).filter(
            Members.login == login,
            Members.password == password
        ).first()
    )


def signin(login, password):
    if check_user(login, password):
        # Setting value for user_session (dict).
        # Jinja2 will take care of giving functionality
        user_session["logged_in"] = True
        user_session["username"] = login
        flash("Log in succeeded!", "js")
    else:
        # Setting user_session["logged_in"] to False
        # does not change anything in terms of functionality
        user_session["logged_in"] = False
        flash("Wrong email or password.", "js")


def logout():
    # Logging out by changing value.
    # Jinja2 will take care of not giving functionality
    user_session["logged_in"] = False
