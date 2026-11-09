from Controllers.BaseController import CrudController
from Services.PersonaService import PersonaService


class PersonaController(CrudController):
    service = PersonaService()
    resource = "persona"
