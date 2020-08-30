# We need session to interact with the db
# and Reviews to get/add reviews from/to this table
from app.mod_db import session, Reviews


def get_reviews(movie):
    # Returning all movies for the chosen movie
    return session.query(Reviews).filter_by(movie=movie).all()


def post_review(movie, name, contents):
    # Adding a new review to the db
    review = Reviews(movie=movie, fname=name, contents=contents)
    session.add(review)
    session.commit()
