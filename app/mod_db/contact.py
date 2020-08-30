# The backend for the contact form on contact.html

# For interactive message
from flask import flash
# For secure password typing
from getpass import getpass
# For sending emails
import smtplib, ssl

# By default, we want to decrypt password for kinomonsterbackend@gmail.com
from app.mod_db.signingup import decrypt_password, encrypted_pwd


def contact_mail(name, email, contents):
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
    # Interactive message which will be shown in bold in our template
    flash(f"If necessary, we may contact you on {email}", "contact")
