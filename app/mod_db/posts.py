from app.mod_db import session, Posts


def get_posts():
    return session.query(Posts).all()


def get_posts_for_home():
    posts = get_posts()
    return posts[::-1][0:2]
