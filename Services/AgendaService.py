from Models.Agenda import Agenda
from Services.BaseService import CrudService


class AgendaService(CrudService):
    model = Agenda
