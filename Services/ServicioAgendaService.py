from Models.ServicioAgenda import ServicioAgenda
from Services.BaseService import CrudService


class ServicioAgendaService(CrudService):
    model = ServicioAgenda
