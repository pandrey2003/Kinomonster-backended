from flask import flash

from app.mod_db.signingup import send_email
from app.mod_db import session, Members


def get_user(email):
    return session.query(Members).filter_by(email=email).first()


def restore_password(email):
    user = get_user(email)
    if user is not None:
        send_email(email=user.email, login=user.login, password=user.password)
        flash(f"Email to {email} has been sent.", "forgot")
    else:
        flash(f"Sorry, user with email {email} is not found.", "forgot")
