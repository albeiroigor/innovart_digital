from flask import Blueprint
from Controllers.ServicioController import ServicioController


ServicioRoutes = Blueprint("ServicioRoutes", __name__)

controller = ServicioController()


@ServicioRoutes.route("/", methods=["GET"])
def list():
    return controller.list()


@ServicioRoutes.route("/<int:id>", methods=["GET"])
def get(id):
    return controller.get(id)


@ServicioRoutes.route("/", methods=["POST"])
def create():
    return controller.create()


@ServicioRoutes.route("/<int:id>", methods=["PUT"])
def update(id):
    return controller.update(id)


@ServicioRoutes.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return controller.delete(id)
