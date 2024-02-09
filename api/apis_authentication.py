import logging

from flask import request, jsonify
from model.models_users import FindByEmail
from utils import utils_security
from api.apis_common import Response, SUCCESS, ERROR
from datetime import datetime, timedelta


def Login():
    success_response = Response(
        status=SUCCESS
        , message="user successfully login"
        , data=None
    )

    error_response = Response(
        status=ERROR
        , message="user unauthorized"
        , data=None
    )

    try:
        email = request.get_json()['email']
        password = request.get_json()['password']

        curr_user = FindByEmail(email)
        if curr_user:
            pw_hash = curr_user.password
            is_match, err = utils_security.check_hash(password, pw_hash)
            if err:
                logging.error('login error:', err)
                return jsonify(error_response), 401

            if is_match:
                # generate jwt token
                payload = {"id": curr_user.id, "exp": datetime.utcnow() + timedelta(minutes=15)}
                token, err = utils_security.generate_jwt_token(payload)
                if err:
                    logging.error('login error:', err)
                    return jsonify(error_response), 401

                success_response["data"] = {
                    "name": curr_user.name
                    , "token": token
                }

                return jsonify(success_response), 200

        return jsonify(error_response), 401
    except KeyError as err:
        err_msg = f'login error: {err} required'

        logging.error(err_msg)
        error_response['message'] = err_msg
        return jsonify(error_response), 401
    except:
        return jsonify(error_response), 401
