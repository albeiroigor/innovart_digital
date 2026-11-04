from flask import request, jsonify
from Services.EmpleadoService import EmpleadoService


class EmpleadoController:

    service = EmpleadoService()

    def list(self):
        return jsonify(self.service.list()), 200


    def get(self, id):
        data = self.service.getById(id)

        if data is None:
            return jsonify({"error": "empleado no encontrado"}), 404

        return jsonify(data), 200


    def create(self):
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "mensaje": "El cuerpo de la petición no debe estar vacío o mal formateado"
            }), 400

        camposR = ["uuid", "rol_id", "res_id", "per_id", "ser_id"]

        camposF = [x for x in camposR if x not in data]

        if len(camposF) > 0:
            return jsonify({
                "campos": f"Campos faltantes {camposF}"
            }), 400

        camposV = [
            x for x in camposR
            if data.get(x) is None or str(data.get(x)).strip() == ""
        ]

        if len(camposV) > 0:
            return jsonify({
                "campos": f"Campos vacíos {camposV}"
            }), 400

        result = self.service.create(data)
        return jsonify(result), 201


    def update(self, id):
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "mensaje": "El cuerpo de la petición no debe estar vacío o mal formateado"
            }), 400

        result = self.service.update(id, data)

        if result is None:
            return jsonify({"error": "empleado no encontrado"}), 404

        return jsonify(result), 200


    def delete(self, id):
        if not self.service.delete(id):
            return jsonify({"error": "empleado no encontrado"}), 404

        return jsonify({"message": "empleado eliminado correctamente"}), 200
