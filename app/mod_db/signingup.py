# For interactive message
from flask import flash

# For decrypting github-absent key.key to get credentials
# for kinomonsterbackend@gmaill.com
from cryptography.fernet import Fernet
# For secure password typing
from getpass import getpass

# For sending emails
import smtplib, ssl
# To make sure user has entered a valid email format
import re

# We need session to interact with the db
# and Members to add users to this table
from app.mod_db import session, Members

# Encrypted password for kinomonsterbackend@gmaill.com
encrypted_pwd = b"gAAAAABfQWlFS41yLCGyGuVax6vUKl" \
        b"hubQAlylQqSSGPdVGoEwIOnRBQf3NYUPunf9RW0W32ZO5" \
        b"KiA_jpyFX93H2StWZxJOfinJAOtqVKwF1Kq1KwTdOq3o="


def check_login(login):
    # Check the user is not in our database
    # Returns True - if not in the db
    #         False - if IN the db
    return not bool(session.query(Members).filter_by(login=login).first())


def sign_up(email, login, password):
    if check_email(email) and check_email_db(email) and check_login(login):
        # If the user input for email is of email format
        # and the user is not in db
        send_email(email=email, login=login, password=password)
        add_user(email=email, login=login, password=password)
        # The user will be sent the email with his/her credentials.
        flash(f"Email with your credentials is sent to {email}")
    elif not check_email(email):
        # If the user input for email is of wrong format.
        flash(f"{email} is not a correct email.")
    elif not check_email_db(email) or not check_login(login):
        # If the user is already in the db
        flash(f"{email} is already in our database, sign in.")


def decrypt_password(password):
    # The function trying to decrypt the password from key.key
    with open("app/mod_db/key.key", "rb") as file:
        key = file.read()
    cipher_suite = Fernet(key)
    sender_password = cipher_suite.decrypt(encrypted_pwd).decode()
    return sender_password


def send_email(email, login, password):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    try:
        # Trying to get key.key file (absent on GitHub for security reasons)
        sender_password = decrypt_password(encrypted_pwd)
    except FileNotFoundError:
        # If this app is used by other developer
        sender_email = input("Enter your gmail: ")
        # Because Gmail has to be given access to lesser-known apps
        print("Grant access to apps in your account!")
        # For security reasons, we type not seeing the password
        sender_password = getpass()
    else:
        # If the file was found, we can use the default Gmail
        sender_email = "kinomonsterbackend@gmail.com"
    finally:
        # Below is a standard form for sending plain emails
        receiver_email = email
        message = f"""\
        Subject: Your credentials

        Your credentials for Kinomonster:
            login: {login}
            password: {password}

        We are looking forward to seeing you!
        """

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            smtp_server,
            port,
            context=context
        ) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)


def check_email(email):
    # Check the user input for email has a valid email format
    expression = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-z]{2,}"
    match = re.search(expression, email)
    # Returns True - if the user has typed an email
    #         False - if the user has entered something else
    return bool(match)


def check_email_db(email):
    # Email is unique in the db so we will check the user is not in db
    return not bool(session.query(Members).filter_by(email=email).first())


def add_user(email, login, password):
    # Adding new user to the table with (email, login, password) columns
    new_user = Members(email=email, login=login, password=password)
    session.add(new_user)
    session.commit()
