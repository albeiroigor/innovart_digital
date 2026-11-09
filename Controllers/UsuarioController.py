from flask import jsonify

from Controllers.BaseController import CrudController
from Services.BaseService import ConflictError
from Services.UsuarioService import UsuarioService


class UsuarioController(CrudController):
    service = UsuarioService()
    resource = "usuario"

    def create(self):
        data = self._payload()
        if data is None:
            return self._invalid_body()

        error = self._validate(data, self.service.model.required_fields)
        if error is not None:
            return error

        contrasena = data["contrasena"]
        if not isinstance(contrasena, str) or len(contrasena) < 8:
            return jsonify({
                "mensaje": "La contraseña debe tener mínimo 8 caracteres"
            }), 400

        try:
            usuario = self.service.create(data)
        except ConflictError as error:
            return jsonify({"mensaje": str(error)}), 409

        return jsonify({
            "mensaje": "Usuario registrado correctamente",
            "usuario": usuario,
        }), 201

    def login(self):
        data = self._payload()
        if data is None:
            return self._invalid_body()

        error = self._validate(data, ("correo", "contrasena"))
        if error is not None:
            return error

        usuario = self.service.validar_login(
            data["correo"],
            data["contrasena"],
        )
        if usuario is None:
            return jsonify({"mensaje": "Correo o contraseña incorrectos"}), 401

        return jsonify({
            "mensaje": "Inicio de sesión exitoso",
            "usuario": usuario.to_dict(),
        }), 200

    def update(self, id):
        data = self._payload()
        if data is None:
            return self._invalid_body()

        contrasena = data.get("contrasena")
        if contrasena is not None and (
            not isinstance(contrasena, str) or len(contrasena) < 8
        ):
            return jsonify({
                "mensaje": "La contraseña debe tener mínimo 8 caracteres"
            }), 400

        try:
            usuario = self.service.update(id, data)
        except ConflictError as error:
            return jsonify({"mensaje": str(error)}), 409

        if usuario is None:
            return self._not_found()
        return jsonify(usuario), 200
