# To save images on the filesystem instead of the db
# (filesystem space is cheaper, in db we store paths only)
import os
# To cache all & home posts to spend less time
# loading Posts and Home webpages
from cachetools import cached, TTLCache
# To save the image better
from werkzeug.utils import secure_filename

# We need session to interact with the db
# and Posts to get/add posts from/to this table
from app.mod_db import session, Posts
# Specifying the folder where all posted images
# will be saved
from config import UPLOAD_FOLDER
# To add user_session["username"] to the 'author' field
from app.mod_db.signingin import user_session

# Cache for all posts, using float("inf") as None is
# not implemented
cache = TTLCache(maxsize=float("inf"), ttl=900)
# Cache for 2 last posts in homepage
cache_home = TTLCache(maxsize=400, ttl=900)

# The list of extensions allowed for img src
ALLOWED_EXTENSIONS = {
    "apng",
    "bmp",
    "ico",
    "svg",
    "tif",
    "cur",
    "webp",
    "tiff",
    "png",
    "jpg",
    "jpeg",
    "gif"
}


@cached(cache)
def get_posts():
    # Returning all posts from the table in reversed order
    return session.query(Posts).all()[::-1]


@cached(cache_home)
def get_posts_for_home():
    posts = get_posts()
    # Returning 2 last posts
    return posts[0:2]


def release_cache():
    # We will clear cache when a user adds a post
    cache.clear()
    cache_home.clear()


def allowed_file(filename):
    # Checking the user image's name
    return "." in filename and \
        filename.split(".")[1].lower() in ALLOWED_EXTENSIONS


def upload(title, image, description, contents):
    # filename is not '' and allowed
    if image and allowed_file(image.filename):
        # Saving image to filesystem
        filename = save_image(image)
        # Adding appropriate information to the db
        upload_with_picture(title, filename, description, contents)
    else:
        # Adding information to the db with picture=None
        upload_without_picture(title, description, contents)
    release_cache()


def save_image(image):
    # Saving image to static/img/db_img/
    filename = secure_filename(image.filename)
    image.save(os.path.join(UPLOAD_FOLDER, filename))
    return filename


def upload_without_picture(title, description, contents):
    # Adding info to the db with picture=None
    new_post = Posts(
        title=title,
        description=description,
        picture=None,
        contents=contents,
        resource=None,
        author=user_session["username"]
    )
    session.add(new_post)
    session.commit()


def upload_with_picture(title, filename, description, contents):
    # Adding info to the db specifying the path to the image
    new_post = Posts(
        title=title,
        description=description,
        picture=filename,
        contents=contents,
        resource=None,
        author=user_session["username"]
    )
    session.add(new_post)
    session.commit()
