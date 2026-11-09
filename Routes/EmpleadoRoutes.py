from Controllers.EmpleadoController import EmpleadoController
from .crud_routes import crud_blueprint

EmpleadoRoutes = crud_blueprint("EmpleadoRoutes", EmpleadoController())
