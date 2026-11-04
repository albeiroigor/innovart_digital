from .AgendaRoutes import AgendaRoutes
from .ConsultaRoutes import ConsultaRoutes
from .EmpleadoRoutes import EmpleadoRoutes
from .PagoRoutes import PagoRoutes
from .PersonaRoutes import PersonaRoutes
from .RespuestaRoutes import RespuestaRoutes
from .RolRoutes import RolRoutes
from .ServicioAgendaRoutes import ServicioAgendaRoutes
from .ServicioRoutes import ServicioRoutes
from .UsuarioRoutes import UsuarioRoutes
from .documentacion import documentacion_bp


def loadRoutes(app):

    app.register_blueprint(AgendaRoutes, url_prefix="/agendas")
    app.register_blueprint(ConsultaRoutes, url_prefix="/api/consultas")
    app.register_blueprint(EmpleadoRoutes, url_prefix="/api/empleados")
    app.register_blueprint(PagoRoutes, url_prefix="/api/pagos")
    app.register_blueprint(PersonaRoutes, url_prefix="/api/personas")
    app.register_blueprint(RespuestaRoutes, url_prefix="/api/respuestas")
    app.register_blueprint(RolRoutes, url_prefix="/api/roles")
    app.register_blueprint(ServicioAgendaRoutes, url_prefix="/api/servicios-agenda")
    app.register_blueprint(ServicioRoutes, url_prefix="/api/servicios")
    app.register_blueprint(UsuarioRoutes, url_prefix="/api/usuarios")
    app.register_blueprint(documentacion_bp, url_prefix="/api/documentacion")
