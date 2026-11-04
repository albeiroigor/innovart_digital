class Rol:
    def __init__(self, id, uuid, tipo):
        self.rol_id = id
        self.rol_uuid = uuid
        self.rol_tipo = tipo

    def to_dict(self):
        return {
            "id": self.rol_id,
            "uuid": self.rol_uuid,
            "tipo": self.rol_tipo
        }
