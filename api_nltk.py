import nltk
from api_common import Response, ERROR, SUCCESS
from flask import jsonify, request


def FreqDist():
    words = request.get_json()['sentence']
    fd_result = WordFreqDist(words)

    response = Response(
        status=SUCCESS
        , message="freq dist"
        , data=fd_result
    )

    return jsonify(response), 200


def FreqDistUpload():
    f = request.files['file']
    f.save(f.filename)

    text = open(f.filename, "r")
    words = "".join(text.readlines())
    fd_result = WordFreqDist(words)
    text.close()

    response = Response(
        status=SUCCESS
        , message="freq dist upload"
        , data=fd_result
    )

    return jsonify(response), 200


def WordFreqDist(words):
    token = nltk.word_tokenize(words)
    return nltk.FreqDist(token)
