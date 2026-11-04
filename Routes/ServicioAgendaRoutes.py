from flask import Blueprint
from Controllers.ServicioAgendaController import ServicioAgendaController


ServicioAgendaRoutes = Blueprint("ServicioAgendaRoutes", __name__)

controller = ServicioAgendaController()


@ServicioAgendaRoutes.route("/", methods=["GET"])
def list():
    return controller.list()


@ServicioAgendaRoutes.route("/<int:id>", methods=["GET"])
def get(id):
    return controller.get(id)


@ServicioAgendaRoutes.route("/", methods=["POST"])
def create():
    return controller.create()


@ServicioAgendaRoutes.route("/<int:id>", methods=["PUT"])
def update(id):
    return controller.update(id)


@ServicioAgendaRoutes.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return controller.delete(id)
