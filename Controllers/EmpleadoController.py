from Controllers.BaseController import CrudController
from Services.EmpleadoService import EmpleadoService


class EmpleadoController(CrudController):
    service = EmpleadoService()
    resource = "empleado"
