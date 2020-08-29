from flask import Blueprint, render_template, request, redirect

from app.mod_db import signingup

from app.mod_db import signingin
from app.mod_db.signingin import user_session

from app.mod_db.reviews import get_reviews, post_review

from app.mod_db.contact import contact_mail

from app.mod_db.forgot import restore_password

from app.mod_db.posts import get_posts_for_home, get_posts

servered = Blueprint(
    "servered",
    __name__,
    template_folder="templates",
    static_folder="static"
)


@servered.route("/")
def home():
    home_posts = get_posts_for_home()
    return render_template(
        "index.html",
        user_session=user_session,
        posts=home_posts
    )


@servered.route("/posts/<int:post_id>")
def post(post_id):
    all_posts = get_posts()
    needed_post = all_posts[post_id]
    return render_template("post.html", user_session=user_session, post=needed_post)


@servered.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["review_name"]
        email = request.form["review_email"]
        contents = request.form["review_text"]
        contact_mail(name, email, contents)
    return render_template("contact.html", user_session=user_session)


@servered.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        new_login = request.form.get("new_login")
        new_email = request.form.get("new_email")
        new_password = request.form.get("new_password")

        signingup.sign_up(
            email=new_email,
            login=new_login,
            password=new_password
        )
    return render_template("signup.html", user_session=user_session)


@servered.route("/server/signin", methods=["POST"])
def server_signin():
    login = request.form["login_field"]
    password = request.form["password_field"]
    signingin.signin(login, password)
    return redirect(request.referrer)


@servered.route("/server/logout", methods=["POST"])
def server_logout():
    signingin.logout()
    return redirect(request.referrer)


@servered.route("/forgot", methods=["GET", "POST"])
def forgot():
    if request.method == "POST":
        email = request.form["forgot_email"]
        restore_password(email)
    return render_template("forgot.html", user_session=user_session)


@servered.route("/show/<name>", methods=["POST", "GET"])
def show(name):
    path = request.path
    movie = path[6:].replace("_", " ").title()
    if request.method == "POST":
        name = request.form["review_name"]
        contents = request.form["review_text"]
        post_review(movie, name, contents)
    reviews = get_reviews(movie)

    return render_template(
        f"shows/{name}.html",
        user_session=user_session,
        reviews=reviews
    )
