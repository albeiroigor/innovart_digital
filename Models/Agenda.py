class Agenda:
    def __init__(self, id, uuid, fecha, hora, ser_id, usu_id, age_pag_id):
        self.age_id = id
        self.age_uuid = uuid
        self.age_fecha = fecha
        self.age_hora = hora
        self.age_ser_id = ser_id
        self.age_usu_id = usu_id
        self.age_pag_id = age_pag_id

    def to_dict(self):
        return {
            "id": self.age_id,
            "uuid": self.age_uuid,
            "fecha": self.age_fecha,
            "hora": self.age_hora,
            "ser_id": self.age_ser_id,
            "usu_id": self.age_usu_id,
            "pag_id": self.age_pag_id
        }
