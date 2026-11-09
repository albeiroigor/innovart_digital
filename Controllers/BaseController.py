from flask import jsonify, request

from Services.BaseService import ConflictError


def _is_blank(value):
    return value is None or (isinstance(value, str) and not value.strip())


class CrudController:
    service = None
    resource = "recurso"

    def list(self):
        return jsonify(self.service.list()), 200

    def get(self, id):
        record = self.service.getById(id)
        if record is None:
            return self._not_found()
        return jsonify(record), 200

    def create(self):
        data = self._payload()
        if data is None:
            return self._invalid_body()

        error = self._validate(data, self.service.model.required_fields)
        if error is not None:
            return error

        try:
            result = self.service.create(data)
        except ConflictError as error:
            return jsonify({"mensaje": str(error)}), 409

        return jsonify(result), 201

    def update(self, id):
        data = self._payload()
        if data is None:
            return self._invalid_body()

        try:
            result = self.service.update(id, data)
        except ConflictError as error:
            return jsonify({"mensaje": str(error)}), 409

        if result is None:
            return self._not_found()
        return jsonify(result), 200

    def delete(self, id):
        try:
            deleted = self.service.delete(id)
        except ConflictError as error:
            return jsonify({"mensaje": str(error)}), 409

        if not deleted:
            return self._not_found()
        return jsonify({"mensaje": f"{self.resource} eliminado correctamente"}), 200

    def _payload(self):
        data = request.get_json(silent=True)
        return data if isinstance(data, dict) and data else None

    def _validate(self, data, required_fields):
        missing = [field for field in required_fields if field not in data]
        if missing:
            return jsonify({"campos": f"Campos faltantes {missing}"}), 400

        empty = [field for field in required_fields if _is_blank(data[field])]
        if empty:
            return jsonify({"campos": f"Campos vacíos {empty}"}), 400

        return None

    def _invalid_body(self):
        return jsonify({
            "mensaje": "El cuerpo de la petición no debe estar vacío o mal formateado"
        }), 400

    def _not_found(self):
        return jsonify({"error": f"{self.resource} no encontrado"}), 404
