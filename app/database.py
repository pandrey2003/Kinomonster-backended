# To intelligently join together BASE_DIR path
# and database.db
import os
# To create SQLAlchemy engine
from sqlalchemy import create_engine
# All interacting with databases are done using sessions,
# so we have to initialize one
from sqlalchemy.orm import Session
# I use the existing database, hence use automap_base
from sqlalchemy.ext.automap import automap_base

# Specifying BASE_DIR folder (./app/ per se)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# Specifying the path to the db not checking the same thread
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    os.path.join(BASE_DIR, 'database.db?check_same_thread=False')

# Creating the engine
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# Defining and preparing the Base object to work with tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Specify all in-db tables
Members = Base.classes.members
Posts = Base.classes.posts
Reviews = Base.classes.reviews
# Initializing session
session = Session(engine)
