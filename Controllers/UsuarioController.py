from flask import current_app, jsonify, request
from Services.UsuarioService import UsuarioService



class UsuarioController:

    service = UsuarioService()

    def list(self):
        return jsonify(self.service.list()), 200

    

    def get(self, id):
        data = self.service.getById(id)

        if data is None:
            return jsonify({"mensaje": "Usuario no encontrado"}), 404

        return jsonify(data), 200



    def create(self):

        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "mensaje": "El cuerpo de la petición no debe estar vacío o mal formateado"
            }), 400

        correo = data.get("correo")
        contrasena = data.get("contrasena")
        per_id = data.get("per_id")

        # Validar campos
        if not correo or not contrasena or not per_id:

            return jsonify({
                "mensaje": "Correo, contraseña y rol son obligatorios"
            }), 400

        # Validación básica de contraseña
        if len(contrasena) < 8:

            return jsonify({
                "mensaje": "La contraseña debe tener mínimo 8 caracteres"
            }), 400

        usuario, error = self.service.create(
            current_app.mysql,
            correo,
            contrasena,
            per_id
        )

        if error:

            return jsonify({
                "mensaje": error
            }), 409

        return jsonify({
            "mensaje": "Usuario registrado correctamente",
            "usuario": usuario.to_dict()
        }), 201


    def login(self):

        data = request.get_json()

        if not data:

            return jsonify({
                "mensaje": "No se recibieron datos"
            }), 400

        correo = data.get("correo")
        contrasena = data.get("contrasena")

        if not correo or not contrasena:

            return jsonify({
                "mensaje": "Correo y contraseña son obligatorios"
            }), 400

        usuario = UsuarioService.validar_login(
            current_app.mysql,
            correo,
            contrasena
        )

        if usuario is None:

            return jsonify({
                "mensaje": "Correo o contraseña incorrectos"
            }), 401

        return jsonify({
            "mensaje": "Inicio de sesión exitoso",
            "usuario": usuario.to_dict()
        }), 200


    

    def update(self, id):
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "mensaje": "El cuerpo de la petición no debe estar vacío o mal formateado"
            }), 400

        usuario = UsuarioService().update(id, data)

        if usuario is None:
            return jsonify({"mensaje": "Usuario no encontrado"}), 404

        return jsonify(usuario), 200




    def delete(self, id):
        eliminado = UsuarioService().delete(id)

        if not eliminado:
            return jsonify({"mensaje": "Usuario no encontrado"}), 404

        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200