from flask import request
from models_users import SearchByEmail
from utils import check_password_hash, generate_jwt_token


def Login():
    email = request.get_json()['email']
    password = request.get_json()['password']

    curr_user = SearchByEmail(email)
    if curr_user:
        pw_hash = curr_user.password
        is_match = check_password_hash(pw_hash, password)

        if is_match:

            # generate jwt token
            user_id = curr_user.id
            token = generate_jwt_token(user_id)

            return token, 200
        else:
            return "user unauthorized", 401

    return "user unauthorized", 401
