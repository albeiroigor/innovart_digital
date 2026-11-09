from Controllers.RespuestaController import RespuestaController
from .crud_routes import crud_blueprint

RespuestaRoutes = crud_blueprint("RespuestaRoutes", RespuestaController())
