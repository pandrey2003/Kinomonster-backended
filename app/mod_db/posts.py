from app.mod_db import session, Posts
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=float('inf'), ttl=900)
cache_home = TTLCache(maxsize=100, ttl=900)


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
