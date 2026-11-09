from Controllers.BaseController import CrudController
from Services.ConsultaService import ConsultaService


class ConsultaController(CrudController):
    service = ConsultaService()
    resource = "consulta"
