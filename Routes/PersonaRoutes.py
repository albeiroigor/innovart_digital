from flask import Blueprint
from Controllers.PersonaController import PersonaController


PersonaRoutes = Blueprint("PersonaRoutes", __name__)

controller = PersonaController()


@PersonaRoutes.route("/", methods=["GET"])
def list():
    return controller.list()


@PersonaRoutes.route("/<int:id>", methods=["GET"])
def get(id):
    return controller.get(id)


@PersonaRoutes.route("/", methods=["POST"])
def create():
    return controller.create()


@PersonaRoutes.route("/<int:id>", methods=["PUT"])
def update(id):
    return controller.update(id)


@PersonaRoutes.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return controller.delete(id)
