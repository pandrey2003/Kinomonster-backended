from flask import flash

from cryptography.fernet import Fernet
from getpass import getpass

import smtplib, ssl
import re

from app.mod_db import session, Members

encrypted_pwd = b"gAAAAABfQWlFS41yLCGyGuVax6vUKl" \
        b"hubQAlylQqSSGPdVGoEwIOnRBQf3NYUPunf9RW0W32ZO5" \
        b"KiA_jpyFX93H2StWZxJOfinJAOtqVKwF1Kq1KwTdOq3o="


def check_login(login):
    return not bool(session.query(Members).filter_by(login=login).first())


def sign_up(email, login, password):
    if check_email(email) and check_email_db(email) and check_login(login):
        send_email(email=email, login=login, password=password)
        add_user(email=email, login=login, password=password)
        flash(f"Email with your credentials is sent to {email}")
    elif not check_email(email):
        flash(f"{email} is not a correct email.")
    elif not check_email_db(email):
        flash(f"{email} is already in our database, sign in.")
    elif not check_login(login):
        flash(f"{login} is already in our database, sign in.")


def decrypt_password(password):
    with open("app/mod_db/key.key", "rb") as file:
        key = file.read()
    cipher_suite = Fernet(key)
    sender_password = cipher_suite.decrypt(encrypted_pwd).decode()
    return sender_password


def send_email(email, login, password):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    try:
        sender_password = decrypt_password(encrypted_pwd)
    except FileNotFoundError:
        sender_email = input("Enter your gmail: ")
        print("Grant access to apps in your account!")
        sender_password = getpass()
    else:
        sender_email = "kinomonsterbackend@gmail.com"
    finally:
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
    expression = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-z]{2,}"
    match = re.search(expression, email)
    return bool(match)


def check_email_db(email):
    return not bool(session.query(Members).filter_by(email=email).first())


def add_user(email, login, password):
    new_user = Members(email=email, login=login, password=password)
    session.add(new_user)
    session.commit()
