class Usuario:
    def __init__(self, id, uuid, correo, contrasena, per_id):
        self.usu_id = id
        self.usu_uuid = uuid
        self.usu_correo = correo
        self.usu_contrasena = contrasena
        self.usu_per_id = per_id

    def to_dict(self, incluir_contrasena=False):
        datos = {
            "id": self.usu_id,
            "uuid": self.usu_uuid,
            "correo": self.usu_correo,
            "per_id": self.usu_per_id
        }

        if incluir_contrasena:
            datos["contrasena"] = self.usu_contrasena

        return datos
