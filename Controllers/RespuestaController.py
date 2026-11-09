from Controllers.BaseController import CrudController
from Services.RespuestaService import RespuestaService


class RespuestaController(CrudController):
    service = RespuestaService()
    resource = "respuesta"
