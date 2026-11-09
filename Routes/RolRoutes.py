from Controllers.RolController import RolController
from .crud_routes import crud_blueprint

RolRoutes = crud_blueprint("RolRoutes", RolController())
