from Models.Persona import Persona
from Services.BaseService import CrudService


class PersonaService(CrudService):
    model = Persona
