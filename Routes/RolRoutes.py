from flask import Blueprint
from Controllers.RolController import RolController


RolRoutes = Blueprint("RolRoutes", __name__)

controller = RolController()


@RolRoutes.route("/", methods=["GET"])
def list():
    return controller.list()


@RolRoutes.route("/<int:id>", methods=["GET"])
def get(id):
    return controller.get(id)


@RolRoutes.route("/", methods=["POST"])
def create():
    return controller.create()


@RolRoutes.route("/<int:id>", methods=["PUT"])
def update(id):
    return controller.update(id)


@RolRoutes.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return controller.delete(id)
