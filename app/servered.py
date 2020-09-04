# We use Blueprint class to initialize a blueprint.
# render_template for loading templates from
# templates/ folder.
# request to work with forms
# redirect to redirect back on signin and coming-soon
# flash to interactively display messages
from flask import Blueprint, render_template, request, redirect, flash

# Importing signingup module to load functions in a modularized way
from app.mod_db import signingup

# Importing signingun module to load functions in a modularized way
from app.mod_db import signingin
# Importing user_session and passing it as parameters to render_template
from app.mod_db.signingin import user_session

# Importing functions from reviews module
from app.mod_db.reviews import get_reviews, post_review

# Importing contact_mail from contact module
from app.mod_db.contact import contact_mail

# Importing restore_password from forgot module
from app.mod_db.forgot import restore_password

# Importing functions from posts module
from app.mod_db.posts import get_posts_for_home, get_posts, upload

# Importing the last piece of news from news module
from app.mod_db.news import return_last_piece_of_news

# Initializing the blueprint
servered = Blueprint(
    "servered",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@servered.route("/")
def home():
    # Returning home page with 2 last posts
    home_posts = get_posts_for_home()
    # Returning home page with the last piece of news
    news = return_last_piece_of_news()
    return render_template(
        "index.html",
        user_session=user_session,
        posts=home_posts,
        news=news
    )


@servered.route("/posts/<int:post_id>")
def post(post_id):
    # Returning the post with the needed id
    all_posts, _ = get_posts()
    try:
        needed_post = all_posts[post_id]
        return render_template(
            "post.html",
            user_session=user_session,
            post=needed_post
        )
    except IndexError:
        return render_template("errors/404.html"), 404


@servered.route("/posts")
def posts():
    # Returning all posts, new ones go first
    _, reversed_posts = get_posts()
    return render_template(
        "posts.html",
        user_session=user_session,
        posts=reversed_posts
    )


@servered.route("/create/post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST" and "image" in request.files:
        # Getting all information from the form and passing it
        # to upload function
        image = request.files["image"]
        title = request.form["post_title"]
        description = request.form["post_description"]
        contents = request.form["post_contents"]
        upload(
            title=title,
            image=image,
            description=description,
            contents=contents
        )
    # Loads the write-post template after POST method and for GET
    return render_template("create.html", user_session=user_session)


@servered.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Getting all information from the form and passing it
        # to contact_mail function
        name = request.form["review_name"]
        email = request.form["review_email"]
        contents = request.form["review_text"]
        contact_mail(name, email, contents)
    # Loads the contact template after POST method and for GET
    return render_template("contact.html", user_session=user_session)


@servered.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Getting all information from the form and passing it
        # to signingup.sign_up function
        new_login = request.form.get("new_login")
        new_email = request.form.get("new_email")
        new_password = request.form.get("new_password")

        signingup.sign_up(
            email=new_email,
            login=new_login,
            password=new_password
        )
    # Loads the signup template after POST method and for GET
    return render_template("signup.html", user_session=user_session)


@servered.route("/server/signin", methods=["POST"])
def server_signin():
    # Getting all information from the form and passing it
    # to signingin.signin function
    login = request.form["login_field"]
    password = request.form["password_field"]
    signingin.signin(login, password)
    # Returning to the page from whence the route was called
    return redirect(request.referrer)


@servered.route("/server/logout", methods=["POST"])
def server_logout():
    # Logging out
    signingin.logout()
    # Returning to the page from whence the route was called
    return redirect(request.referrer)


@servered.route("/forgot", methods=["GET", "POST"])
def forgot():
    if request.method == "POST":
        # Getting all information from the form and passing it
        # to restore_password function
        email = request.form["forgot_email"]
        restore_password(email)
    # Loads the forgot template after POST method and for GET
    return render_template("forgot.html", user_session=user_session)


@servered.route("/show/<name>", methods=["GET", "POST"])
def show(name):
    # Takes request path and shortens to the name of the show
    path = request.path
    movie = path[6:].replace("_", " ").title()
    if request.method == "POST":
        # Getting all information from the form and passing it
        # to post_review function
        person_name = request.form["review_name"]
        contents = request.form["review_text"]
        post_review(movie, person_name, contents)
    # Reviews are taken in any case
    reviews = get_reviews(movie)

    # Returns a unique template for each show
    return render_template(
        f"shows/{name}.html",
        user_session=user_session,
        reviews=reviews
    )


@servered.route("/server/search", methods=["POST"])
def search():
    # This interactive message will be displayed as JS alert()
    flash("This feature is coming soon...", "implementation")
    # Returning to the page from whence the route was called
    return redirect(request.referrer)
