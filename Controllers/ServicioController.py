from Controllers.BaseController import CrudController
from Services.ServicioService import ServicioService


class ServicioController(CrudController):
    service = ServicioService()
    resource = "servicio"
