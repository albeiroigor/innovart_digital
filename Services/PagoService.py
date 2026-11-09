from Models.Pago import Pago
from Services.BaseService import CrudService


class PagoService(CrudService):
    model = Pago
