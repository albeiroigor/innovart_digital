from Controllers.BaseController import CrudController
from Services.RolService import RolService


class RolController(CrudController):
    service = RolService()
    resource = "rol"
