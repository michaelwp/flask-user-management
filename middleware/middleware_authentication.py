import logging
from functools import wraps
from flask import request, jsonify
from api.apis_common import Response, ERROR
from utils import utils_security as sec
from model import models_users as user


def Token_authentication():
    def _token_authentication(f):
        @wraps(f)
        def __token_authentication(*args, **kwargs):
            response_error = Response(
                status=ERROR
                , message="user unauthorized"
                , data=None
            )

            # token validation
            user_id, err = Token_validation(request)
            if err:
                err_msg = f'error token authentication: {err}'
                logging.error(err_msg)
                return jsonify(response_error), 401

            # validate user_id
            curr_user = user.FindByID(user_id)
            if curr_user is None:
                # if user not found then return error
                logging.error('error token authentication: user not found')
                return jsonify(response_error), 401

            result = f(*args, **kwargs)
            return result

        return __token_authentication

    return _token_authentication


def Token_validation(req):
    # get bearer token
    bearer_token = req.headers.get("Authorization")
    if bearer_token is None:
        return 0, "error token validation: token required"

    jwt_token = bearer_token.split(" ")[1]
    if jwt_token == "":
        # if bearer token is empty then return error
        return 0, "error token validation: token required"

    # decode & validate jwt token
    payload, err = sec.decode_jwt_token(jwt_token)
    if err:
        return 0, f"error token validation: {err}"

    user_id = payload['id']
    return user_id, None
