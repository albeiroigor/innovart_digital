from Controllers.ConsultaController import ConsultaController
from .crud_routes import crud_blueprint

ConsultaRoutes = crud_blueprint("ConsultaRoutes", ConsultaController())
