from flask import Blueprint
from Controllers.AgendaController import AgendaController


AgendaRoutes = Blueprint("AgendaRoutes", __name__)

controller = AgendaController()


@AgendaRoutes.route("/", methods=["GET"])
def list():
    return controller.list()


@AgendaRoutes.route("/<int:id>", methods=["GET"])
def get(id):
    return controller.get(id)


@AgendaRoutes.route("/", methods=["POST"])
def create():
    return controller.create()


@AgendaRoutes.route("/<int:id>", methods=["PUT"])
def update(id):
    return controller.update(id)


@AgendaRoutes.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return controller.delete(id)
