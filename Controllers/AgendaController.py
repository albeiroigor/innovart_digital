from Controllers.BaseController import CrudController
from Services.AgendaService import AgendaService


class AgendaController(CrudController):
    service = AgendaService()
    resource = "agenda"
