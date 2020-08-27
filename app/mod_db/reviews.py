from app.mod_db import session, Reviews
from flask import request

def get_reviews(movie):
    return session.query(Reviews).filter_by(movie=movie).all()


def post_review(movie, name, contents):
    review = Reviews(movie=movie, fname=name, contents=contents)
    session.add(review)
    session.commit()


def gather_review():
    path = request.path
    movie = path[6:].replace("_", " ").title()
    if request.method == "POST":
        name = request.form["review_name"]
        contents = request.form["review_text"]
        post_review(movie, name, contents)
    reviews = get_reviews(movie)
    return reviews
