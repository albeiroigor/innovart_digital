class Persona:
    def __init__(
        self,
        id,
        uuid,
        cedula,
        documento,
        primer_nombre,
        segundo_nombre,
        primer_apellido,
        segundo_apellido,
        correo,
        direccion,
        telefono,
        fecha_nacimiento
    ):
        self.per_id = id
        self.per_uuid = uuid
        self.per_cedula = cedula
        self.per_documento = documento
        self.per_primer_nombre = primer_nombre
        self.per_segundo_nombre = segundo_nombre
        self.per_primer_apellido = primer_apellido
        self.per_segundo_apellido = segundo_apellido
        self.per_correo = correo
        self.per_direccion = direccion
        self.per_telefono = telefono
        self.per_fecha_nacimiento = fecha_nacimiento

    def to_dict(self):
        return {
            "id": self.per_id,
            "uuid": self.per_uuid,
            "cedula": self.per_cedula,
            "documento": self.per_documento,
            "primer_nombre": self.per_primer_nombre,
            "segundo_nombre": self.per_segundo_nombre,
            "primer_apellido": self.per_primer_apellido,
            "segundo_apellido": self.per_segundo_apellido,
            "correo": self.per_correo,
            "direccion": self.per_direccion,
            "telefono": self.per_telefono,
            "fecha_nacimiento": self.per_fecha_nacimiento
        }
