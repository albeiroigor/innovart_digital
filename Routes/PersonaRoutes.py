from Controllers.PersonaController import PersonaController
from .crud_routes import crud_blueprint

PersonaRoutes = crud_blueprint("PersonaRoutes", PersonaController())
