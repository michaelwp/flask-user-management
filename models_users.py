from app import db
from sqlalchemy.sql import func
from utils import generate_hash


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


def Create(name, email, password):

    # search by email
    curr_user = SearchByEmail(email)

    if curr_user:  # if user exist then return err
        return "user already registered"

    # else insert to database
    pw_hash = generate_hash(password)

    new_user = Users(name=name, email=email, password=pw_hash)
    db.session.add(new_user)
    db.session.commit()

    return None


def Update():
    return


def SearchByEmail(email):
    curr_user = Users.query.filter_by(email=email).first()
    return curr_user
