from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


def generate_hash(password):
    pw_hash = generate_password_hash(password, 12)
    return pw_hash


def check_hash(pw_hash, password):
    is_match = check_password_hash(pw_hash, password)
    return is_match


def generate_jwt_token(user_id):
    token = create_access_token(user_id)
    return token
