from Models.Empleado import Empleado
from Services.BaseService import CrudService


class EmpleadoService(CrudService):
    model = Empleado
