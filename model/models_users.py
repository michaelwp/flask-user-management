from app import db
from sqlalchemy.sql import func
from utils import utils_security


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


def Create(name, email, password):
    # find user by email
    curr_user = FindByEmail(email)

    if curr_user:  # if user exist then return err
        return "user already registered"

    # else insert to database
    pw_hash, err = utils_security.generate_hash(password)
    if err:
        return err

    new_user = Users(name=name, email=email, password=pw_hash)
    db.session.add(new_user)
    db.session.commit()

    return None


def Update(user_data):
    # find user by id
    curr_user = FindByID(user_data["id"])
    if curr_user is None:
        # if not found return error
        return "user not found"

    # if user found update user data
    curr_user.name = user_data["name"]
    curr_user.email = user_data["email"]
    db.session.commit()

    return None


def FindByEmail(email):
    curr_user = Users.query.filter_by(email=email).first()
    return curr_user


def FindByID(user_id):
    curr_user = Users.query.get(user_id)
    return curr_user
