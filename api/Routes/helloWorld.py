from flask import Blueprint
from api.Controllers.helloWorld import hello_world

hello_world_blueprint = Blueprint('helloWorld', __name__)


@hello_world_blueprint.route('/', methods=['GET'])
def hello_world_route():
    return hello_world()
