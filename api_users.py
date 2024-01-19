from models_users import Create
from flask import request


def View():
    return "user_view", 200


def Register():
    name = request.get_json()['name']
    email = request.get_json()['email']
    password = request.get_json()['password']

    err = Create(name, email, password)
    if err:
        return err, 400

    return "user successfully registered", 200


def Update():
    return "update", 200
