class Consulta:
    def __init__(self, id, uuid, hora, fecha, mensaje, usu_id):
        self.con_id = id
        self.con_uuid = uuid
        self.con_hora = hora
        self.con_fecha = fecha
        self.con_mensaje = mensaje
        self.con_usu_id = usu_id

    def to_dict(self):
        return {
            "id": self.con_id,
            "uuid": self.con_uuid,
            "hora": self.con_hora,
            "fecha": self.con_fecha,
            "mensaje": self.con_mensaje,
            "usu_id": self.con_usu_id
        }
