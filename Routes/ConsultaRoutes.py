from flask import Blueprint
from Controllers.ConsultaController import ConsultaController


ConsultaRoutes = Blueprint("ConsultaRoutes", __name__)

controller = ConsultaController()


@ConsultaRoutes.route("/", methods=["GET"])
def list():
    return controller.list()


@ConsultaRoutes.route("/<int:id>", methods=["GET"])
def get(id):
    return controller.get(id)


@ConsultaRoutes.route("/", methods=["POST"])
def create():
    return controller.create()


@ConsultaRoutes.route("/<int:id>", methods=["PUT"])
def update(id):
    return controller.update(id)


@ConsultaRoutes.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return controller.delete(id)
