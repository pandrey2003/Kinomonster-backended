from app.mod_db import session, Reviews


def get_reviews(movie):
    return session.query(Reviews).filter_by(movie=movie).all()
