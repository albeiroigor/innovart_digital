from Controllers.BaseController import CrudController
from Services.PagoService import PagoService


class PagoController(CrudController):
    service = PagoService()
    resource = "pago"
