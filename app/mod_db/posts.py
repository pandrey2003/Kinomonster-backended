from app.mod_db import session, Posts
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=float('inf'), ttl=900)


@cached(cache)
def get_posts():
    return session.query(Posts).all()[::-1]


def get_posts_for_home():
    posts = get_posts()
    return posts[0:2]


def release_cache():
    cache.clear()
