from Controllers.BaseController import CrudController
from Services.ServicioAgendaService import ServicioAgendaService


class ServicioAgendaController(CrudController):
    service = ServicioAgendaService()
    resource = "servicioAgenda"
