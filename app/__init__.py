# Flask class for initializing the app.
# render_template for loading templates from
# templates/ folder.
from flask import Flask, render_template

# Importing blueprints
from .frontended import frontended
from .servered import servered

# Initializing the app
app = Flask(__name__)
# Configuring the app from config.py
app.config.from_object("config")

# Blueprints have to be registered, we do it
# for both of them
app.register_blueprint(frontended)
app.register_blueprint(servered)


# To handle 404 Not Found Error
@app.errorhandler(404)
def not_found(error):
    return render_template("errors/404.html"), 404


# To handle 405 Method Not Allowed Error
@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("errors/405.html"), 405
