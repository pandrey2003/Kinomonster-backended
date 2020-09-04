# session is for interacting with the db
# News is the table of the db
from app.mod_db import session, News


def return_last_piece_of_news():
    # The function which returns the last piece of news
    all_pieces = session.query(News).all()
    last_piece = all_pieces[-1]
    return last_piece
