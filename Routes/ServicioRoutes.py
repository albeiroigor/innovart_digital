from Controllers.ServicioController import ServicioController
from .crud_routes import crud_blueprint

ServicioRoutes = crud_blueprint("ServicioRoutes", ServicioController())
