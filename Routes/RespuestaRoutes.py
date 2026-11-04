from flask import Blueprint
from Controllers.RespuestaController import RespuestaController


RespuestaRoutes = Blueprint("RespuestaRoutes", __name__)

controller = RespuestaController()


@RespuestaRoutes.route("/", methods=["GET"])
def list():
    return controller.list()


@RespuestaRoutes.route("/<int:id>", methods=["GET"])
def get(id):
    return controller.get(id)


@RespuestaRoutes.route("/", methods=["POST"])
def create():
    return controller.create()


@RespuestaRoutes.route("/<int:id>", methods=["PUT"])
def update(id):
    return controller.update(id)


@RespuestaRoutes.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return controller.delete(id)
