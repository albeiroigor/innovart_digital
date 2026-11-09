from Controllers.PagoController import PagoController
from .crud_routes import crud_blueprint

PagoRoutes = crud_blueprint("PagoRoutes", PagoController())
