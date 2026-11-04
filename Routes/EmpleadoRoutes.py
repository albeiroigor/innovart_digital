from flask import Blueprint
from Controllers.EmpleadoController import EmpleadoController


EmpleadoRoutes = Blueprint("EmpleadoRoutes", __name__)

controller = EmpleadoController()


@EmpleadoRoutes.route("/", methods=["GET"])
def list():
    return controller.list()


@EmpleadoRoutes.route("/<int:id>", methods=["GET"])
def get(id):
    return controller.get(id)


@EmpleadoRoutes.route("/", methods=["POST"])
def create():
    return controller.create()


@EmpleadoRoutes.route("/<int:id>", methods=["PUT"])
def update(id):
    return controller.update(id)


@EmpleadoRoutes.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return controller.delete(id)
