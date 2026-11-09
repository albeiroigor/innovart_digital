from Controllers.UsuarioController import UsuarioController
from .crud_routes import crud_blueprint

controller = UsuarioController()
UsuarioRoutes = crud_blueprint("UsuarioRoutes", controller)
UsuarioRoutes.add_url_rule("/registro", "registro", controller.create, methods=["POST"])
UsuarioRoutes.add_url_rule("/login", "login", controller.login, methods=["POST"])
