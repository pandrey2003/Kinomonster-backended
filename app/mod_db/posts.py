import os
from flask import request
from cachetools import cached, TTLCache
from werkzeug.utils import secure_filename

from app.mod_db import session, Posts
from config import UPLOAD_FOLDER
from app.mod_db.signingin import user_session

cache = TTLCache(maxsize=float("inf"), ttl=900)
cache_home = TTLCache(maxsize=400, ttl=900)

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
    return session.query(Posts).all()[::-1]


@cached(cache_home)
def get_posts_for_home():
    posts = get_posts()
    return posts[0:2]


def release_cache():
    cache.clear()
    cache_home.clear()


def allowed_file(filename):
    return "." in filename and \
        filename.split(".")[1].lower() in ALLOWED_EXTENSIONS


def upload(title, image, description, contents):
    if image and allowed_file(image.filename):
        filename = save_image(image)
        upload_with_picture(title, filename, description, contents)
    else:
        upload_without_picture(title, description, contents)
    release_cache()


def save_image(image):
    filename = secure_filename(image.filename)
    image.save(os.path.join(UPLOAD_FOLDER, filename))
    return filename


def upload_without_picture(title, description, contents):
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
