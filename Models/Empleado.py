class Empleado:
    def __init__(self, id, uuid, rol_id, res_id, per_id, ser_id):
        self.emp_id = id
        self.emp_uuid = uuid
        self.emp_rol_id = rol_id
        self.emp_res_id = res_id
        self.emp_per_id = per_id
        self.emp_ser_id = ser_id

    def to_dict(self):
        return {
            "id": self.emp_id,
            "uuid": self.emp_uuid,
            "rol_id": self.emp_rol_id,
            "res_id": self.emp_res_id,
            "per_id": self.emp_per_id,
            "ser_id": self.emp_ser_id
        }
