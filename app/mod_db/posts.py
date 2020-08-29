from app.mod_db import session, Posts


def get_posts():
    return session.query(Posts).all()[::-1]


def get_posts_for_home():
    posts = get_posts()
    return posts[0:2]
