from flask import jsonify, request
from api.apis_common import Response,SUCCESS, ERROR
from middleware.middleware_authentication import Token_validation


def Home():
    success_response = Response(
        status=SUCCESS
        , message="welcome home"
        , data=None
    )

    return jsonify(success_response), 200
