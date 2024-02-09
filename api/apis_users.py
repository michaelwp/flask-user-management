import logging

from model.models_users import Create, Update as mUpdate
from flask import request, jsonify, json
from api.apis_common import Response, ERROR, SUCCESS
from middleware.middleware_authentication import Token_validation
from model.models_users import FindByID


def Get_current_user(req):
    # get user_id from token
    user_id, err = Token_validation(req)
    if err:
        return None, f'error get current user data: {err}'

    # get current user data by user_id
    current_user = FindByID(user_id)
    if current_user is None:
        return None, f'error get current user data: user not found'

    return current_user, None


def View():
    success_response = Response(
        status=SUCCESS
        , message="user data"
        , data=None
    )

    error_response = Response(
        status=ERROR
        , message="failed to get user data"
        , data=None
    )

    # get current user data
    curr_user, err = Get_current_user(request)
    if err:
        return jsonify(error_response), 400

    data = {
        "id": curr_user.id
        , "name": curr_user.name
        , "email": curr_user.email
    }

    success_response['data'] = data
    return jsonify(success_response), 200


def Register():
    success_response = Response(
        status=SUCCESS
        , message="user successfully registered"
        , data=None
    )

    error_response = Response(
        status=ERROR
        , message="all field required"
        , data=None
    )

    try:
        name = request.get_json()['name']
        email = request.get_json()['email']
        password = request.get_json()['password']

        err = Create(name, email, password)
        if err:
            err_msg = f'error register new user: {err}'
            logging.error(err_msg)
            error_response['message'] = err_msg
            return jsonify(error_response), 400

        return success_response, 200
    except KeyError as err:
        err_msg = f'error register new user: {err} required'
        logging.error(err_msg)
        error_response['message'] = err_msg
        return jsonify(error_response), 400


def Update():
    success_response = Response(
        status=SUCCESS
        , message="user data successfully updated"
        , data=None
    )

    error_response = Response(
        status=ERROR
        , message="failed to update user data"
        , data=None
    )

    try:
        # get current user data
        curr_user, err = Get_current_user(request)
        if err:
            return jsonify(error_response), 400

        name = request.get_json()['name']
        email = request.get_json()['email']

        user_data = {
            "id": curr_user.id
            , "name": name
            , "email": email
        }

        mUpdate(user_data)
        success_response['data'] = user_data
        return jsonify(success_response), 200
    except KeyError as err:
        err_msg = f'error update user data: {err} required'
        logging.error(err_msg)
        error_response['message'] = err_msg
        return jsonify(error_response), 400
