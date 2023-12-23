from Utils.db import get_shoes
import flask


def hello_world():
    return flask.jsonify(get_shoes())
