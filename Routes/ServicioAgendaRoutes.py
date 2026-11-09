from Controllers.ServicioAgendaController import ServicioAgendaController
from .crud_routes import crud_blueprint

ServicioAgendaRoutes = crud_blueprint(
    "ServicioAgendaRoutes",
    ServicioAgendaController(),
)
