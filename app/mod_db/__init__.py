from app import db
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
Base.prepare(db.engine, reflect=True)

Members = Base.classes.members
Posts = Base.classes.posts
Reviews = Base.classes.reviews
