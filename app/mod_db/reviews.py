from app.mod_db import session, Reviews


def get_reviews(movie):
    return session.query(Reviews).filter_by(movie=movie).all()


def post_review(movie, name, contents):
    review = Reviews(movie=movie, fname=name, contents=contents)
    session.add(review)
    session.commit()
