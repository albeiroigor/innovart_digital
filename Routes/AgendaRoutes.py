from Controllers.AgendaController import AgendaController
from .crud_routes import crud_blueprint

AgendaRoutes = crud_blueprint("AgendaRoutes", AgendaController())
