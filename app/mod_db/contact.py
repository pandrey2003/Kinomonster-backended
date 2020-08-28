from flask import flash
from cryptography.fernet import Fernet
from getpass import getpass

import smtplib, ssl
import re

from app.mod_db.signingup import decrypt_password, encrypted_pwd


def contact_mail(name, email, contents):
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
        receiver_email = sender_email
        message = f"""\
        Subject: {name} from {email}

        Name: {name}
        Email: {email}
        Contents: {contents}
        """
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            smtp_server,
            port,
            context=context
        ) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
    flash(f"If necessary, we may contact you on {email}", "contact")
