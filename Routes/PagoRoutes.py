from flask import Blueprint
from Controllers.PagoController import PagoController


PagoRoutes = Blueprint("PagoRoutes", __name__)

controller = PagoController()


@PagoRoutes.route("/", methods=["GET"])
def list():
    return controller.list()


@PagoRoutes.route("/<int:id>", methods=["GET"])
def get(id):
    return controller.get(id)


@PagoRoutes.route("/", methods=["POST"])
def create():
    return controller.create()


@PagoRoutes.route("/<int:id>", methods=["PUT"])
def update(id):
    return controller.update(id)


@PagoRoutes.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return controller.delete(id)
