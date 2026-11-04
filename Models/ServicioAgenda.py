class ServicioAgenda:
    def __init__(self, id, uuid, ser_id, age_id):
        self.ser_age_id = id
        self.ser_age_uuid = uuid
        self.ser_age_ser_id = ser_id
        self.ser_age_age_id = age_id

    def to_dict(self):
        return {
            "id": self.ser_age_id,
            "uuid": self.ser_age_uuid,
            "ser_id": self.ser_age_ser_id,
            "age_id": self.ser_age_age_id
        }
