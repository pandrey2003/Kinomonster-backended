# For interactive message
from flask import flash

# To send email with user credentials
from app.mod_db.signingup import send_email
# To interact with the db and Members table
from app.mod_db import session, Members


def get_user(email):
    # The user is unique, so we take the first user from the db
    return session.query(Members).filter_by(email=email).first()


def restore_password(email):
    user = get_user(email)
    if user is not None:
        # Sending an email using the function from app.mod_db.signingup
        send_email(email=user.email, login=user.login, password=user.password)
        # Displaying flash message in a specific Jinja2-defined space
        flash(f"Email to {email} has been sent.", "forgot")
    else:
        # If the user is not found, SQLAlchemy returns None for get_user()
        flash(f"Sorry, user with email {email} is not found.", "forgot")
