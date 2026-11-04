class Servicio:
    def __init__(self, id, uuid, nombre, descripcion, precio, tipo, estado):
        self.ser_id = id
        self.ser_uuid = uuid
        self.ser_nombre = nombre
        self.ser_descripcion = descripcion
        self.ser_precio = precio
        self.ser_tipo = tipo
        self.ser_estado = estado

    def to_dict(self):
        return {
            "id": self.ser_id,
            "uuid": self.ser_uuid,
            "nombre": self.ser_nombre,
            "descripcion": self.ser_descripcion,
            "precio": self.ser_precio,
            "tipo": self.ser_tipo,
            "estado": self.ser_estado
        }
